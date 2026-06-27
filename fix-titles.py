#!/usr/bin/env python3
"""Post-build: patch <title> tags in Quartz HTML output using frontmatter titles from the SAR vault.

Quartz strips frontmatter before build, so content pages inherit their slug as <title>.
This script walks the SAR vault source (which still has frontmatter), extracts `title:`,
maps to the corresponding public/ HTML file, and patches the <title> tag.
"""

import os, re, sys

PUBLIC_DIR = "/root/beacon-quartz/public"
VAULT_DIR = "/root/Beacon/sar-knowledge"
SUFFIX = " — SAR Compendium"

patched = 0
skipped = 0
errors = []

for root, dirs, files in os.walk(VAULT_DIR):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for fname in files:
        if not fname.endswith('.md'):
            continue

        md_path = os.path.join(root, fname)
        rel = os.path.relpath(md_path, VAULT_DIR)

        # Read frontmatter
        with open(md_path, 'r') as f:
            content = f.read()

        m = re.search(r'^title:\s*"([^"]+)"', content, re.MULTILINE)
        if not m:
            # Try to extract from first # heading if no frontmatter title
            hm = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if hm:
                title = hm.group(1).strip()
            else:
                skipped += 1
                continue
        else:
            title = m.group(1)

        # Map to HTML: spaces → dashes, .md → .html
        html_rel = rel.replace('.md', '.html')
        # Split path components and replace spaces in each
        parts = html_rel.split('/')
        parts = [p.replace(' ', '-') for p in parts]
        html_rel = '/'.join(parts)

        html_path = os.path.join(PUBLIC_DIR, html_rel)
        if not os.path.exists(html_path):
            # Try lowercase (Quartz lowercases some paths)
            html_rel_lower = '/'.join([p.lower() for p in parts])
            html_path = os.path.join(PUBLIC_DIR, html_rel_lower)
            if not os.path.exists(html_path):
                skipped += 1
                continue

        # Read HTML
        with open(html_path, 'r') as f:
            html = f.read()

        new_title = f"<title>{title}{SUFFIX}</title>"
        if title == "SAR Compendium":
            new_title = f"<title>{title}</title>"
        old_title_pattern = r'<title>[^<]*</title>'

        if not re.search(old_title_pattern, html):
            errors.append(f"No <title> in {html_rel}")
            skipped += 1
            continue

        html = re.sub(old_title_pattern, new_title, html, count=1)

        with open(html_path, 'w') as f:
            f.write(html)

        patched += 1

print(f"Title fix: {patched} patched, {skipped} skipped, {len(errors)} errors")
if errors:
    for e in errors[:5]:
        print(f"  ⚠ {e}")

sys.exit(0 if not errors else 0)  # non-fatal
