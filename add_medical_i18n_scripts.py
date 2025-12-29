#!/usr/bin/env python3
"""Add i18n script tags to Medical HTML files."""
import re
from pathlib import Path

MEDICAL_TOOLS = [
    'aidoc', 'butterfly-iq', 'nuance-dragon', 'paige-ai',
    'pathai', 'tempus', 'viz-ai', 'zebra-medical'
]

HTML_DIR = Path("GenuisNet.ai/pages/reviews/medical")

def add_i18n_script(html_path, tool_name):
    """Add i18n script tag if not already present."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if script already exists
    script_tag = f'<script src="../../../js/{tool_name}-i18n.js"></script>'
    if script_tag in content:
        print(f"[SKIP] {tool_name}: Script already exists")
        return False

    # Find the closing </body> tag and insert before it
    if '</body>' in content:
        content = content.replace('</body>', f'    {script_tag}\n</body>')
    else:
        print(f"[WARN] {tool_name}: No </body> tag found")
        return False

    # Write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"[OK] {tool_name}: Added i18n script")
    return True

def main():
    print("="*60)
    print("ADDING I18N SCRIPTS TO MEDICAL HTML FILES")
    print("="*60)

    stats = {"added": 0, "skipped": 0, "failed": 0}

    for tool in MEDICAL_TOOLS:
        html_file = HTML_DIR / f"{tool}.html"
        if not html_file.exists():
            print(f"[FAIL] {tool}: HTML file not found")
            stats["failed"] += 1
            continue

        try:
            if add_i18n_script(html_file, tool):
                stats["added"] += 1
            else:
                stats["skipped"] += 1
        except Exception as e:
            print(f"[FAIL] {tool}: {e}")
            stats["failed"] += 1

    print("\n" + "="*60)
    print(f"ADDED: {stats['added']}")
    print(f"SKIPPED: {stats['skipped']}")
    print(f"FAILED: {stats['failed']}")
    print("="*60)

if __name__ == "__main__":
    main()
