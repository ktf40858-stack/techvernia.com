#!/usr/bin/env python3
"""
Add tool-specific i18n script references to Quantum Computing HTML files
"""

import re
import os

QUANTUM_SCRIPTS = {
    "amazon-braket.html": "amazon-braket-i18n.js",
    "azure-quantum.html": "azure-quantum-i18n.js",
    "d-wave-leap.html": "d-wave-leap-i18n.js",
    "google-cirq.html": "google-cirq-i18n.js",
    "ibm-quantum.html": "ibm-quantum-i18n.js",
    "ionq.html": "ionq-i18n.js",
    "rigetti-qcs.html": "rigetti-qcs-i18n.js",
    "xanadu-pennylane.html": "xanadu-pennylane-i18n.js"
}

def add_i18n_script(html_path, script_name):
    """Add tool-specific i18n script before the closing body tag"""

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Check if script already exists
    if script_name in content:
        return False

    # Pattern to match before </body>
    pattern = r'(</body>)'

    # Script tag to add
    script_tag = f'<script src="../../../js/{script_name}"></script>\n<script src="../../../js/i18n.js"></script>\n'

    # Replace
    content = re.sub(pattern, script_tag + r'\1', content)

    if content != original_content:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    html_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\quantum"

    print("="*60)
    print("ADDING I18N SCRIPTS TO QUANTUM COMPUTING CATEGORY")
    print("="*60)
    print()

    updated = 0

    for html_file, script_name in QUANTUM_SCRIPTS.items():
        html_path = os.path.join(html_dir, html_file)

        if not os.path.exists(html_path):
            print(f"[SKIP] File not found: {html_file}")
            continue

        if add_i18n_script(html_path, script_name):
            print(f"[OK] {html_file}: {script_name} added")
            updated += 1
        else:
            print(f"[ALREADY EXISTS] {html_file}")

    print()
    print("="*60)
    print(f"TOTAL SCRIPTS ADDED: {updated}/{len(QUANTUM_SCRIPTS)}")
    print("="*60)

if __name__ == "__main__":
    main()
