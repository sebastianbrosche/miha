#!/usr/bin/env python3
import os
import re
import glob

BASE_DIR = "/root/.openclaw/workspace/heat-lagos"

# 1. Remove Summer Membership from JSON schema in all HTML files
schema_pattern = re.compile(
    r',\{"@type":"Offer","name":"Summer Membership","description":"3 months unlimited for the full Lagos summer\.","price":"390","priceCurrency":"EUR","availability":"https://schema\.org/InStock","url":"https://www\.heatlagos\.com/#memberships","seller":\{"@id":"https://www\.heatlagos\.com/#studio"\}\}'
)

# 2. Remove the Summer Membership pricing card from index.html
# This pattern matches the entire <article> block that contains "Summer Membership"
article_pattern = re.compile(
    r'<article class="[^"]*?bg-stone-dark/60[^"]*?">'
    r'.*?'
    r'<h3 class="[^"]*?">Summer Membership</h3>'
    r'.*?'
    r'</article>'
)

files_changed = 0
for filepath in glob.glob(os.path.join(BASE_DIR, "**/*.html"), recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Remove schema object
    content = schema_pattern.sub("", content)

    # Remove visible article from index.html
    if os.path.basename(filepath) == "index.html":
        content = article_pattern.sub("", content)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        files_changed += 1
        print(f"Updated: {filepath}")

print(f"\nDone. {files_changed} files modified.")
