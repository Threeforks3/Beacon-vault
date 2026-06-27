#!/bin/bash
# Deploy Quartz-built Beacon vault to GitHub Pages
# Run after: cd /root/beacon-quartz && npx quartz build && cp public/home.html public/index.html

set -e
cd /root/beacon-quartz/public

# Verify index.html exists
if [ ! -f index.html ]; then
  echo "ERROR: index.html missing. Run: cp public/home.html public/index.html"
  exit 1
fi

# Verify no index.xml competing
if [ -f index.xml ]; then
  echo "ERROR: index.xml present — RSS should be disabled in quartz.config.yaml"
  exit 1
fi

rm -rf .git
git init -q
git checkout -b gh-pages -q
touch .nojekyll
git add -A
git commit -q -m "deploy: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
git remote add origin https://github.com/Threeforks3/Beacon-vault.git
git push -f origin gh-pages

echo "Deployed: https://threeforks3.github.io/Beacon-vault/"
