#!/bin/bash
# Deploy Quartz-built Beacon vault to GitHub Pages
# Run after: cd /root/beacon-quartz && npx quartz build
#
# Post-build steps handled by this script:
#   1. Rewrite index.html with SAR Compendium title (SPA redirect fix)
#   2. Remove index.xml if present (RSS conflict)
#   3. Push to gh-pages

set -e
cd /root/beacon-quartz/public

# Fix page titles: extract from vault frontmatter and patch HTML <title> tags
python3 /root/beacon-quartz/fix-titles.py

# Rewrite root index.html — Quartz SPA creates a redirect with slug-based title.
# Bookmark must read "SAR Compendium", not "home".
cat > index.html << 'EOF'
<!DOCTYPE html>
<html lang="en-us">
<head>
<title>SAR Compendium</title>
<link rel="canonical" href="./home">
<meta name="robots" content="noindex">
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=./home">
</head>
</html>
EOF

# Remove RSS index.xml — competes with index.html on gh-pages
rm -f index.xml

rm -rf .git
git init -q
git checkout -b gh-pages -q
touch .nojekyll
git add -A
git commit -q -m "deploy: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
git remote add origin https://github.com/Threeforks3/Beacon-vault.git
git push -f origin gh-pages

echo "Deployed: https://threeforks3.github.io/Beacon-vault/"
