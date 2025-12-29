#!/usr/bin/env python3
"""
Implement real screenshots for Quantum Computing category
Copy screenshots from source folder and update HTML files
"""

import os
import shutil
import re

# Screenshot mappings: source filename -> (destination filename, tool name)
SCREENSHOT_MAPPINGS = {
    "Amazon Braket.jpg": ("amazon-braket.jpg", "Amazon Braket"),
    "Azure Quantum": ("azure-quantum.jpg", "Azure Quantum"),
    "D-Wave Leap.jpg": ("d-wave-leap.jpg", "D-Wave Leap"),
    "Google Cirq.jpg": ("google-cirq.jpg", "Google Cirq"),
    "IBM Quantum": ("ibm-quantum.jpg", "IBM Quantum"),
    "IonQ.jpg": ("ionq.jpg", "IonQ"),
    "Rigetti QCS.png": ("rigetti-qcs.png", "Rigetti QCS"),
    "Xanadu PennyLane.png": ("xanadu-pennylane.png", "Xanadu PennyLane")
}

# HTML file mappings: html filename -> screenshot filename
HTML_SCREENSHOT_MAP = {
    "amazon-braket.html": "amazon-braket.jpg",
    "azure-quantum.html": "azure-quantum.jpg",
    "d-wave-leap.html": "d-wave-leap.jpg",
    "google-cirq.html": "google-cirq.jpg",
    "ibm-quantum.html": "ibm-quantum.jpg",
    "ionq.html": "ionq.jpg",
    "rigetti-qcs.html": "rigetti-qcs.png",
    "xanadu-pennylane.html": "xanadu-pennylane.png"
}

def copy_screenshots():
    """Copy screenshots from source to destination with correct names"""

    source_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\screenshot\AI Quantum Computing"
    dest_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\assets\screenshots\quantum"

    # Create dest dir if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)

    print("="*60)
    print("COPYING QUANTUM COMPUTING SCREENSHOTS")
    print("="*60)
    print()

    copied = 0

    for source_file, (dest_file, tool_name) in SCREENSHOT_MAPPINGS.items():
        source_path = os.path.join(source_dir, source_file)
        dest_path = os.path.join(dest_dir, dest_file)

        if not os.path.exists(source_path):
            print(f"[SKIP] Source not found: {source_file}")
            continue

        # Copy file
        shutil.copy2(source_path, dest_path)
        file_size = os.path.getsize(dest_path) / 1024  # Size in KB
        print(f"[OK] {tool_name}: {dest_file} ({file_size:.1f} KB)")
        copied += 1

    print()
    print(f"Total screenshots copied: {copied}")
    return copied

def update_html_screenshots():
    """Update HTML files to use the correct screenshot files"""

    html_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\quantum"

    print()
    print("="*60)
    print("UPDATING HTML FILES WITH SCREENSHOTS")
    print("="*60)
    print()

    updated = 0

    for html_file, screenshot_file in HTML_SCREENSHOT_MAP.items():
        html_path = os.path.join(html_dir, html_file)

        if not os.path.exists(html_path):
            print(f"[SKIP] HTML not found: {html_file}")
            continue

        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Pattern to match the screenshot img tag
        pattern = r'(src="../../../assets/screenshots/quantum/)([^"]+)(")'
        replacement = f'\\1{screenshot_file}\\3'

        content = re.sub(pattern, replacement, content)

        if content != original_content:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] {html_file} -> {screenshot_file}")
            updated += 1
        else:
            print(f"[NO CHANGE] {html_file}")

    print()
    print(f"Total HTML files updated: {updated}")
    return updated

def main():
    print("QUANTUM COMPUTING SCREENSHOTS IMPLEMENTATION")
    print()

    # Step 1: Copy screenshots
    copied = copy_screenshots()

    # Step 2: Update HTML files
    updated = update_html_screenshots()

    print()
    print("="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Screenshots copied: {copied}")
    print(f"HTML files updated: {updated}")
    print()
    print("Quantum Computing screenshots implementation complete!")

if __name__ == "__main__":
    main()
