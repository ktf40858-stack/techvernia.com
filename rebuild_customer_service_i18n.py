import json
import os

# Base paths
base_path = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
customer_service_path = os.path.join(base_path, "pages", "reviews", "customer-service")
js_path = os.path.join(base_path, "js")

# List of all customer service tools
tools = [
    "ada",
    "certainly",
    "cognigy",
    "drift",
    "forethought",
    "freshdesk-ai",
    "helpshift",
    "intercom-fin",
    "kustomer",
    "liveperson",
    "netomi",
    "polyai",
    "ultimateai",
    "yellowai",
    "zendesk-ai"
]

def camel_case(tool_name):
    """Convert tool-name to ToolName"""
    parts = tool_name.split('-')
    return ''.join(word.capitalize() for word in parts)

def get_function_name(tool_name):
    """Convert tool-name to toolName for function names"""
    if tool_name == "intercom-fin":
        return "intercomFin"
    elif tool_name == "freshdesk-ai":
        return "freshdeskAi"
    elif tool_name == "ultimateai":
        return "ultimateai"
    elif tool_name == "yellowai":
        return "yellowai"
    elif tool_name == "zendesk-ai":
        return "zendeskAi"
    else:
        parts = tool_name.split('-')
        if len(parts) == 1:
            return parts[0]
        return parts[0] + ''.join(word.capitalize() for word in parts[1:])

def merge_batch_files(tool_name):
    """Merge batch1, batch2, batch3, and -en.json files for a tool"""
    merged = {}

    # First, load English translations from -en.json
    en_file = os.path.join(customer_service_path, f"{tool_name}-en.json")
    if os.path.exists(en_file):
        try:
            with open(en_file, 'r', encoding='utf-8') as f:
                en_data = json.load(f)
            merged["en"] = en_data
            print(f"  [OK] Loaded {tool_name}-en.json ({len(en_data)} translations)")
        except Exception as e:
            print(f"  [ERROR] Error reading {en_file}: {e}")
    else:
        print(f"  [WARNING] Missing: {en_file}")

    # Then load batch files for other languages
    for batch_num in [1, 2, 3]:
        batch_file = os.path.join(customer_service_path, f"{tool_name}-batch{batch_num}.json")

        if not os.path.exists(batch_file):
            print(f"  [WARNING] Missing: {batch_file}")
            continue

        try:
            with open(batch_file, 'r', encoding='utf-8') as f:
                batch_data = json.load(f)

            # Check if this is a valid translation batch (not API request data)
            if "custom_id" in batch_data or "method" in batch_data:
                print(f"  [WARNING] Skipping {tool_name}-batch{batch_num}.json (API request format)")
                continue

            # Merge all language translations
            for lang, translations in batch_data.items():
                if lang not in merged:
                    merged[lang] = {}
                merged[lang].update(translations)

            print(f"  [OK] Merged {tool_name}-batch{batch_num}.json")
        except Exception as e:
            print(f"  [ERROR] Error reading {batch_file}: {e}")

    return merged

def generate_i18n_js(tool_name, translations):
    """Generate the i18n.js file content"""
    func_name = get_function_name(tool_name)
    var_name = func_name
    func_name_cap = func_name[0].upper() + func_name[1:]

    # Start with the comment and variable declaration
    js_content = f"// {tool_name.upper().replace('-', ' ')} I18N\n"
    js_content += f"const {var_name}Translations = {{\n"

    # Add all languages in order: en, de, es, fr, pt, zh, ja, ko, ar, hi
    language_order = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in language_order:
        if lang in translations:
            js_content += f'  "{lang}": {{\n'

            # Sort keys for consistency
            sorted_keys = sorted(translations[lang].keys())

            for i, key in enumerate(sorted_keys):
                value = translations[lang][key]
                # Escape quotes and backslashes in the value
                escaped_value = value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

                if i < len(sorted_keys) - 1:
                    js_content += f'      "{key}": "{escaped_value}",\n'
                else:
                    js_content += f'      "{key}": "{escaped_value}"\n'

            if lang == "hi":  # Last language
                js_content += "  }\n"
            else:
                js_content += "  },\n"

    js_content += "};\n\n"

    # Add the helper functions
    js_content += f"""function get{func_name_cap}Translation(key, lang) {{
  if ({var_name}Translations[lang] && {var_name}Translations[lang][key]) {{
    return {var_name}Translations[lang][key];
  }}
  if ({var_name}Translations.en && {var_name}Translations.en[key]) {{
    return {var_name}Translations.en[key];
  }}
  return null;
}}

function apply{func_name_cap}Translations(lang) {{
  console.log(`🔥 Applying {tool_name} translations for: ${{lang}}`);
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {{
    const key = element.getAttribute('data-i18n');
    if (key && (key.startsWith('review.{tool_name}.') || key.startsWith('review.common.'))) {{
      const translation = get{func_name_cap}Translation(key, lang);
      if (translation) {{
        element.textContent = translation;
        count++;
      }}
    }}
  }});
  console.log(`✅ Applied ${{count}} {tool_name} translations`);
}}

window.addEventListener('languageChanged', (e) => {{
  const lang = e.detail.language;
  setTimeout(() => apply{func_name_cap}Translations(lang), 200);
}});

if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', () => {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{func_name_cap}Translations(currentLang);
  }});
}} else {{
  const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
  apply{func_name_cap}Translations(currentLang);
}}

console.log('✅ {tool_name} i18n loaded');
"""

    return js_content

def process_tool(tool_name):
    """Process a single tool: merge batches and generate i18n.js"""
    print(f"\n[PROCESSING] {tool_name}...")

    # Merge batch files
    translations = merge_batch_files(tool_name)

    if not translations:
        print(f"  [ERROR] No translations found for {tool_name}")
        return False

    # Check we have all 10 languages
    expected_langs = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]
    missing_langs = [lang for lang in expected_langs if lang not in translations]

    if missing_langs:
        print(f"  [WARNING] Missing languages: {', '.join(missing_langs)}")

    print(f"  [INFO] Found {len(translations)} languages: {', '.join(sorted(translations.keys()))}")

    # Count translations per language
    for lang in expected_langs:
        if lang in translations:
            print(f"     {lang}: {len(translations[lang])} translations")

    # Generate i18n.js content
    js_content = generate_i18n_js(tool_name, translations)

    # Write to file
    output_file = os.path.join(js_path, f"{tool_name}-i18n.js")
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(js_content)
        print(f"  [OK] Written: {output_file}")
        return True
    except Exception as e:
        print(f"  [ERROR] Error writing {output_file}: {e}")
        return False

# Main execution
print("=" * 80)
print("REBUILDING CUSTOMER SERVICE I18N FILES")
print("=" * 80)

success_count = 0
failed_tools = []

for tool in tools:
    if process_tool(tool):
        success_count += 1
    else:
        failed_tools.append(tool)

print("\n" + "=" * 80)
print(f"COMPLETED: {success_count}/{len(tools)} tools processed successfully")
if failed_tools:
    print(f"FAILED: {', '.join(failed_tools)}")
print("=" * 80)
