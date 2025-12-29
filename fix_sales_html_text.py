import os

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
sales_dir = os.path.join(base_dir, "pages", "reviews", "sales")

tools = [
    "6sense",
    "apolloio",
    "attention",
    "chorusai",
    "clari",
    "conversica",
    "exceedai",
    "gong",
    "hubspot-ai",
    "insidesales",
    "lavender",
    "outreach",
    "peopleai",
    "regieai",
    "salesforce-einstein-gpt",
    "troopsai"
]

def fix_html_text(html_file):
    """Remplace les textes pour les adapter aux Sales"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = [
        ("modern businesses", "modern sales teams"),
        ("organizations worldwide", "sales organizations worldwide"),
        ("customer service", "sales"),
        ("customer-service", "sales"),
        # Variantes possibles
        ("Modern businesses", "Modern sales teams"),
        ("Organizations worldwide", "Sales organizations worldwide"),
        ("Customer service", "Sales"),
        ("Customer-service", "Sales")
    ]

    fixed_count = 0
    for old_text, new_text in replacements:
        if old_text in content:
            content = content.replace(old_text, new_text)
            fixed_count += 1

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return fixed_count

# MAIN
print("=" * 70)
print("FIXING ENGLISH TEXT IN SALES HTML FILES")
print("=" * 70)

total_fixed = 0
for tool in tools:
    html_file = os.path.join(sales_dir, f"{tool}.html")

    if os.path.exists(html_file):
        count = fix_html_text(html_file)
        if count > 0:
            print(f"  [FIXED] {tool}.html ({count} replacements)")
            total_fixed += count
        else:
            print(f"  [OK] {tool}.html")
    else:
        print(f"  [SKIP] {tool}.html not found")

print("\n" + "=" * 70)
print(f"[COMPLETE] {total_fixed} total replacements across all files")
print("=" * 70)
