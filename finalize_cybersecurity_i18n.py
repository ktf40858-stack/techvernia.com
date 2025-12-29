#\!/usr/bin/env python3
import json
import os
from pathlib import Path

CYBERSECURITY_TOOLS = [
    ("cisco-securex", True), ("cortex-xdr", True), ("crowdstrike", True),
    ("cyberark", True), ("darktrace", True), ("fortinet", True),
    ("ibm-qradar", True), ("microsoft-sentinel", True), ("okta", True),
    ("palo-alto-ngfw", True), ("qualys", True), ("rapid7", True),
    ("sentinelone", True), ("sophos-interceptx", True), ("splunk-security", True),
    ("tenable", True), ("trend-micro-vision-one", True),
    ("abnormal-security", False), ("carbon-black", False), ("cybereason", False),
    ("cylance", False), ("exabeam", False), ("lacework", False),
    ("mcafee-mvision", False), ("recorded-future", False), ("snyk", False),
    ("symantec-endpoint", False), ("vectra-ai", False), ("wiz", False), ("zerofox", False),
]

BASE_DIR = Path("GenuisNet.ai/pages/reviews/cybersecurity")
JS_DIR = Path("GenuisNet.ai/js")

def load_json_safely(file_path):
    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        print(f"Warning: {file_path}: {e}")
    return {}

def merge_translations(tool_name, has_faqs):
    print(f"Merging {tool_name}...")
    merged = {"en": load_json_safely(BASE_DIR / f"{tool_name}-en.json")}
    
    batch1 = load_json_safely(BASE_DIR / f"{tool_name}-batch1.json")
    batch2 = load_json_safely(BASE_DIR / f"{tool_name}-batch2.json")
    batch3 = load_json_safely(BASE_DIR / f"{tool_name}-batch3.json")
    
    for lang in ["es", "fr", "de"]:
        if lang in batch1: merged[lang] = batch1[lang]
    for lang in ["pt", "zh", "ja"]:
        if lang in batch2: merged[lang] = batch2[lang]
    for lang in ["ko", "ar", "hi"]:
        if lang in batch3: merged[lang] = batch3[lang]
    
    if has_faqs:
        faq_en = load_json_safely(BASE_DIR / f"{tool_name}-faqs-en.json")
        if faq_en: merged["en"].update(faq_en)
        
        for i, langs in enumerate([["es","fr","de"], ["pt","zh","ja"], ["ko","ar","hi"]], 1):
            faq_batch = load_json_safely(BASE_DIR / f"{tool_name}-faqs-batch{i}.json")
            for lang in langs:
                if lang in faq_batch and lang in merged:
                    merged[lang].update(faq_batch[lang])
    
    return merged

def generate_i18n_js(tool_name, translations):
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

print("="*60)
print("CYBERSECURITY I18N FINALIZATION")
print("="*60)

stats = {"success": 0, "failed": []}

for tool, has_faqs in CYBERSECURITY_TOOLS:
    try:
        merged = merge_translations(tool, has_faqs)
        output = generate_i18n_js(tool, merged)
        size = output.stat().st_size / 1024
        print(f"[OK] {tool}: {size:.1f} KB")
        stats["success"] += 1
    except Exception as e:
        print(f"[FAIL] {tool}: {e}")
        stats["failed"].append(tool)

print("\n" + "="*60)
print(f"SUCCESS: {stats['success']}/{len(CYBERSECURITY_TOOLS)}")
if stats["failed"]: print(f"FAILED: {stats['failed']}")
print("="*60)
