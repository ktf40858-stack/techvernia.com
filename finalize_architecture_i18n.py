#!/usr/bin/env python3
"""Finalize Architecture i18n by merging batches and generating JS files."""
import json
import os
from pathlib import Path

ARCHITECTURE_TOOLS = [
    'architechtures', 'arko-ai', 'finch3d', 'hypar', 'maket-ai',
    'spacemaker-ai', 'testfit', 'veras-ai'
]

BASE_DIR = Path("GenuisNet.ai/pages/reviews/architecture")
JS_DIR = Path("GenuisNet.ai/js")

def load_json_safely(file_path):
    """Load JSON file safely."""
    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        print(f"Warning: {file_path}: {e}")
    return {}

def merge_translations(tool_name):
    """Merge EN and all batch translations for a tool."""
    print(f"Merging {tool_name}...")

    # Load EN
    merged = {"en": load_json_safely(BASE_DIR / f"{tool_name}-en.json")}

    # Load batches
    batch1 = load_json_safely(BASE_DIR / f"{tool_name}-batch1.json")
    batch2 = load_json_safely(BASE_DIR / f"{tool_name}-batch2.json")
    batch3 = load_json_safely(BASE_DIR / f"{tool_name}-batch3.json")

    # Load common section titles
    common_en = load_json_safely(BASE_DIR / "common-section-titles-en.json")
    common_batch1 = load_json_safely(BASE_DIR / "common-section-titles-batch1.json")
    common_batch2 = load_json_safely(BASE_DIR / "common-section-titles-batch2.json")
    common_batch3 = load_json_safely(BASE_DIR / "common-section-titles-batch3.json")

    # Add common titles to EN
    if common_en:
        merged["en"].update(common_en)

    # Merge batch 1 (ES, FR, DE)
    for lang in ["es", "fr", "de"]:
        if lang in batch1:
            merged[lang] = batch1[lang]
            # Add common titles
            if lang in common_batch1:
                merged[lang].update(common_batch1[lang])

    # Merge batch 2 (PT, ZH, JA)
    for lang in ["pt", "zh", "ja"]:
        if lang in batch2:
            merged[lang] = batch2[lang]
            # Add common titles
            if lang in common_batch2:
                merged[lang].update(common_batch2[lang])

    # Merge batch 3 (KO, AR, HI)
    for lang in ["ko", "ar", "hi"]:
        if lang in batch3:
            merged[lang] = batch3[lang]
            # Add common titles
            if lang in common_batch3:
                merged[lang].update(common_batch3[lang])

    return merged

def generate_i18n_js(tool_name, translations):
    """Generate i18n.js file for a tool."""
    # Convert tool-name to camelCase for variable names
    camel = "".join(w.capitalize() for w in tool_name.split("-"))

    js = f"""// {tool_name.upper()} I18N
const {camel.lower()}Translations = {json.dumps(translations, ensure_ascii=False, indent=2)};

function get{camel}Translation(key, lang) {{
    return ({camel.lower()}Translations[lang] && {camel.lower()}Translations[lang][key]) ||
           ({camel.lower()}Translations.en && {camel.lower()}Translations.en[key]) || null;
}}

function apply{camel}Translations(lang) {{
    let count = 0;
    document.querySelectorAll("[data-i18n]").forEach(el => {{
        const key = el.getAttribute("data-i18n");
        if (key && (key.startsWith("review.{tool_name}.") || key.startsWith("review.common."))) {{
            const translation = get{camel}Translation(key, lang);
            if (translation) {{ el.textContent = translation; count++; }}
        }}
    }});
    console.log(`Applied ${{count}} {tool_name} translations`);
}}

window.addEventListener("languageChanged", e => setTimeout(() => apply{camel}Translations(e.detail.language), 200));

if (document.readyState === "loading") {{
    document.addEventListener("DOMContentLoaded", () => apply{camel}Translations(window.i18n?.getCurrentLanguage() || "en"));
}} else {{
    apply{camel}Translations(window.i18n?.getCurrentLanguage() || "en");
}}
"""

    output = JS_DIR / f"{tool_name}-i18n.js"
    output.write_text(js, encoding="utf-8")
    return output

def main():
    print("="*60)
    print("ARCHITECTURE I18N FINALIZATION")
    print("="*60)

    stats = {"success": 0, "failed": []}

    for tool in ARCHITECTURE_TOOLS:
        try:
            merged = merge_translations(tool)
            output = generate_i18n_js(tool, merged)
            size = output.stat().st_size / 1024
            print(f"[OK] {tool}: {size:.1f} KB")
            stats["success"] += 1
        except Exception as e:
            print(f"[FAIL] {tool}: {e}")
            stats["failed"].append(tool)

    print("\n" + "="*60)
    print(f"SUCCESS: {stats['success']}/{len(ARCHITECTURE_TOOLS)}")
    if stats["failed"]:
        print(f"FAILED: {stats['failed']}")
    print("="*60)

if __name__ == "__main__":
    main()
