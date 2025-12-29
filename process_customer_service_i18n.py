#!/usr/bin/env python3
"""
Customer Service I18N Translation Workflow Processor
Processes translation files for customer service tools
"""

import json
import os
from pathlib import Path

# Define base paths
BASE_PATH = Path(r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai")
PAGES_PATH = BASE_PATH / "pages" / "reviews" / "customer-service"
JS_PATH = BASE_PATH / "js"

# Tools and their status
TOOLS = {
    "cognigy": {"has_en": True, "batches_corrupt": True, "needs_batches": True, "needs_i18n": True},
    "forethought": {"has_en": True, "batches_valid": True, "needs_i18n": True},
    "freshdesk-ai": {"has_en": True, "has_batch1_batch2": True, "needs_batch3": True, "needs_i18n": True},
    "helpshift": {"has_en": True, "batches_corrupt": True, "needs_batches": True, "needs_i18n": True},
    "kustomer": {"has_en": True, "needs_batches": True, "needs_i18n": True},
    "liveperson": {"has_en": True, "needs_batches": True, "needs_i18n": True},
    "netomi": {"has_en": True, "needs_batches": True, "needs_i18n": True},
}

def read_json(filepath):
    """Read JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(filepath, data):
    """Write JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def create_i18n_js(tool_name, en_data, batch1_data=None, batch2_data=None, batch3_data=None):
    """Create i18n.js file from English and batch data"""

    # Initialize translations object
    translations = {
        "en": en_data,
        "de": {},
        "es": {},
        "fr": {},
        "pt": {},
        "zh": {},
        "ja": {},
        "ko": {},
        "ar": {},
        "hi": {}
    }

    # Merge batch data if available
    if batch1_data:
        for lang in ["de", "es", "fr"]:
            if lang in batch1_data:
                translations[lang] = batch1_data[lang]

    if batch2_data:
        for lang in ["pt", "zh", "ja"]:
            if lang in batch2_data:
                translations[lang] = batch2_data[lang]

    if batch3_data:
        for lang in ["ko", "ar", "hi"]:
            if lang in batch3_data:
                translations[lang] = batch3_data[lang]

    # Create JavaScript content
    tool_var_name = tool_name.replace('-', '_')
    js_content = f"""const {tool_var_name}Translations = {{
  en: {json.dumps(translations['en'], indent=4)},
  es: {json.dumps(translations['es'], indent=4)},
  fr: {json.dumps(translations['fr'], indent=4)},
  de: {json.dumps(translations['de'], indent=4)},
  pt: {json.dumps(translations['pt'], indent=4)},
  zh: {json.dumps(translations['zh'], indent=4)},
  ja: {json.dumps(translations['ja'], indent=4)},
  ko: {json.dumps(translations['ko'], indent=4)},
  ar: {json.dumps(translations['ar'], indent=4)},
  hi: {json.dumps(translations['hi'], indent=4)}
}};

// Translation helper function
function get{tool_var_name.title().replace('_', '')}Translation(key, lang = 'en') {{
  if ({tool_var_name}Translations[lang] && {tool_var_name}Translations[lang][key]) {{
    return {tool_var_name}Translations[lang][key];
  }}
  return {tool_var_name}Translations['en'][key] || key;
}}

// Apply translations to the page
function apply{tool_var_name.title().replace('_', '')}Translations(lang = 'en') {{
  const elements = document.querySelectorAll('[data-i18n^="review.{tool_name}."]');
  elements.forEach(element => {{
    const key = element.getAttribute('data-i18n');
    const translation = get{tool_var_name.title().replace('_', '')}Translation(key, lang);
    if (translation) {{
      element.textContent = translation;
    }}
  }});
}}

// Listen for language changes
if (typeof document !== 'undefined') {{
  document.addEventListener('languageChanged', (event) => {{
    if (event.detail && event.detail.language) {{
      apply{tool_var_name.title().replace('_', '')}Translations(event.detail.language);
    }}
  }});

  // Apply initial translations
  document.addEventListener('DOMContentLoaded', () => {{
    const currentLang = localStorage.getItem('preferredLanguage') || 'en';
    apply{tool_var_name.title().replace('_', '')}Translations(currentLang);
  }});
}}
"""

    return js_content

def process_forethought():
    """Process forethought - has valid batches, needs i18n.js"""
    print("Processing forethought...")

    en_data = read_json(PAGES_PATH / "forethought-en.json")
    batch1_data = read_json(PAGES_PATH / "forethought-batch1.json")
    batch2_data = read_json(PAGES_PATH / "forethought-batch2.json")
    batch3_data = read_json(PAGES_PATH / "forethought-batch3.json")

    # Create i18n.js
    js_content = create_i18n_js("forethought", en_data, batch1_data, batch2_data, batch3_data)

    output_path = JS_PATH / "forethought-i18n.js"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"✓ Created {output_path}")

def process_freshdesk_ai():
    """Process freshdesk-ai - has batch1 and batch2, needs batch3 and i18n.js"""
    print("Processing freshdesk-ai...")

    en_data_source = read_json(PAGES_PATH / "freshdesk-ai-batch1.json")
    en_data = en_data_source["en"]

    # batch1 and batch2 have the structure with "en", "de", "es", "fr" etc
    batch1_data = read_json(PAGES_PATH / "freshdesk-ai-batch1.json")
    batch2_data = read_json(PAGES_PATH / "freshdesk-ai-batch2.json")

    # Create batch3 placeholder (empty translations for ko, ar, hi)
    batch3_data = {
        "ko": {},
        "ar": {},
        "hi": {}
    }
    write_json(PAGES_PATH / "freshdesk-ai-batch3.json", batch3_data)
    print(f"✓ Created {PAGES_PATH / 'freshdesk-ai-batch3.json'} (placeholder)")

    # Create i18n.js
    js_content = create_i18n_js("freshdesk-ai", en_data, batch1_data, batch2_data, batch3_data)

    output_path = JS_PATH / "freshdesk-ai-i18n.js"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"✓ Created {output_path}")

def create_batch_placeholder(tool_name, en_data, batch_num, languages):
    """Create batch placeholder file for translation"""
    batch_data = {lang: {} for lang in languages}
    output_path = PAGES_PATH / f"{tool_name}-batch{batch_num}.json"
    write_json(output_path, batch_data)
    print(f"✓ Created {output_path} (placeholder for translation)")

def process_tool_without_batches(tool_name):
    """Process tools that need batch files and i18n.js"""
    print(f"Processing {tool_name}...")

    en_data = read_json(PAGES_PATH / f"{tool_name}-en.json")

    # Create batch placeholders
    create_batch_placeholder(tool_name, en_data, 1, ["de", "es", "fr"])
    create_batch_placeholder(tool_name, en_data, 2, ["pt", "zh", "ja"])
    create_batch_placeholder(tool_name, en_data, 3, ["ko", "ar", "hi"])

    # Create i18n.js with empty translations
    js_content = create_i18n_js(tool_name, en_data)

    output_path = JS_PATH / f"{tool_name}-i18n.js"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"✓ Created {output_path}")

def process_cognigy():
    """Process cognigy - needs to recreate batches and create i18n.js"""
    # Batches are corrupt (Batch API format), treat as if no batches exist
    process_tool_without_batches("cognigy")

def process_helpshift():
    """Process helpshift - needs to recreate batches and create i18n.js"""
    # Batches are corrupt (Batch API format), treat as if no batches exist
    process_tool_without_batches("helpshift")

def main():
    print("="*60)
    print("Customer Service I18N Translation Workflow Processor")
    print("="*60)
    print()

    # Process each tool
    process_cognigy()
    print()

    process_forethought()
    print()

    process_freshdesk_ai()
    print()

    process_helpshift()
    print()

    process_tool_without_batches("kustomer")
    print()

    process_tool_without_batches("liveperson")
    print()

    process_tool_without_batches("netomi")
    print()

    print("="*60)
    print("Processing complete!")
    print("="*60)
    print()
    print("Summary:")
    print("- Created i18n.js files for all 7 tools")
    print("- Created batch placeholder files for translation")
    print("- Forethought: Merged existing batches into i18n.js")
    print("- Freshdesk-AI: Created batch3 placeholder")
    print("- Other tools: Created all batch placeholders")
    print()
    print("Next steps:")
    print("1. Send batch files to translation API")
    print("2. Merge translated batches back into i18n.js files")

if __name__ == "__main__":
    main()
