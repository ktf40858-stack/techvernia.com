import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
hr_dir = os.path.join(base_dir, "pages", "reviews", "hr")
research_reference = os.path.join(base_dir, "pages", "reviews", "research", "consensus.html")

hr_tools = [
    "beamery", "eightfold-ai", "fetcher", "findem", "harver",
    "hirevue", "humanly", "paradox-olivia", "phenom", "pymetrics",
    "seekout", "sense", "textio", "workable-ai"
]

print("=" * 70)
print("REPLACING BASIC NAVBAR WITH FULL NAVBAR + LANGUAGE SELECTOR")
print("=" * 70)

# Extract full navbar from Research reference
print("\n[1] Extracting full navbar from Research...")

with open(research_reference, 'r', encoding='utf-8') as f:
    research_content = f.read()

navbar_pattern = r'<nav class="navbar" id="navbar">.*?</nav>'
navbar_match = re.search(navbar_pattern, research_content, re.DOTALL)

if not navbar_match:
    print("ERROR: Could not extract navbar")
    exit(1)

navbar_template = navbar_match.group(0)

# Adapt for HR category
navbar_hr = navbar_template.replace(
    'href="../../categories/ai-research.html"',
    'href="../../categories/ai-hr.html"'
)

print("  [+] Full navbar extracted and adapted for HR category")

# Replace navbar in all HR tools
print("\n[2] Replacing navbar in all HR tools...")

replaced = 0

for tool_key in hr_tools:
    html_file = os.path.join(hr_dir, f"{tool_key}.html")

    if not os.path.exists(html_file):
        print(f"  [!] {tool_key}: File not found")
        continue

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and remove old navbar
    old_navbar_pattern = r'<nav class="navbar"[^>]*>.*?</nav>'

    if not re.search(old_navbar_pattern, content, re.DOTALL):
        print(f"  [!] {tool_key}: No navbar found")
        continue

    # Remove old navbar
    content = re.sub(old_navbar_pattern, '{{NAVBAR_PLACEHOLDER}}', content, count=1, flags=re.DOTALL)

    # Insert new navbar
    content = content.replace('{{NAVBAR_PLACEHOLDER}}', navbar_hr)

    # Write back
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  [+] {tool_key}: Navbar replaced with full version")
    replaced += 1

print("\n" + "=" * 70)
print(f"COMPLETE: Replaced navbar in {replaced}/{len(hr_tools)} tools")
print("=" * 70)
print("\nAll HR tools now have:")
print("  - Full navigation menu (Home, Categories, Guides, etc.)")
print("  - Language selector with 10 languages")
print("  - Mobile-responsive hamburger menu")
print("=" * 70)
