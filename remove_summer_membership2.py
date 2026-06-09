#!/usr/bin/env python3
import os
import re
import glob

BASE_DIR = "/root/.openclaw/workspace/heat-lagos"

# The exact JSON schema object to remove (with comma prefix since it's not the first element)
SCHEMA_OBJ = ',{"@type":"Offer","name":"Summer Membership","description":"3 months unlimited for the full Lagos summer.","price":"390","priceCurrency":"EUR","availability":"https://schema.org/InStock","url":"https://www.heatlagos.com/#memberships","seller":{"@id":"https://www.heatlagos.com/#studio"}}'

def find_matching_bracket(s, start):
    """Find the matching ] for [ at position start, handling nested brackets and strings."""
    count = 1
    in_string = False
    escape = False
    i = start + 1
    while i < len(s):
        c = s[i]
        if escape:
            escape = False
            i += 1
            continue
        if c == '\\':
            escape = True
            i += 1
            continue
        if c == '"':
            in_string = not in_string
            i += 1
            continue
        if in_string:
            i += 1
            continue
        if c in '[{':
            count += 1
        elif c in ']}':
            count -= 1
            if count == 0:
                return i
        i += 1
    return -1

files_changed = 0

for filepath in glob.glob(os.path.join(BASE_DIR, "**/*.html"), recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 1. Remove the JSON schema object from all files
    content = content.replace(SCHEMA_OBJ, "")

    # 2. In index.html, remove the RSC article node for Summer Membership
    if os.path.basename(filepath) == "index.html":
        rsc_start = content.find('["$","article","Summer Membership"')
        if rsc_start != -1:
            # Find the opening [ of this array
            start_bracket = rsc_start
            end_bracket = find_matching_bracket(content, start_bracket)
            if end_bracket != -1:
                # Determine boundaries: look for comma before or after
                before = content[start_bracket - 1:start_bracket]  # char before [
                after = content[end_bracket + 1:end_bracket + 2]   # char after ]

                # If preceded by comma (element in array), remove the comma too
                if before == ',':
                    removal_start = start_bracket - 1
                else:
                    removal_start = start_bracket

                # If followed by comma (not the last element), remove the comma too
                if after == ',':
                    removal_end = end_bracket + 2
                else:
                    removal_end = end_bracket + 1

                content = content[:removal_start] + content[removal_end:]
                print(f"  Removed RSC article node from {filepath}")

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        files_changed += 1
        print(f"Updated: {filepath}")

print(f"\nDone. {files_changed} files modified.")
