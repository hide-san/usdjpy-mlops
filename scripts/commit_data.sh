#!/bin/bash
set -e
git config --local user.email "actions@github.com"
git config --local user.name "GitHub Actions"
git add data/usdjpy.csv
git commit -m "Update data" || echo "No changes"
git push
