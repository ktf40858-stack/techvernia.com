#!/usr/bin/env python3
"""Final verification script - check all translations are complete"""

import json
import os
import re

ANALYTICS_DIR = 'GenuisNet.ai/pages/reviews/analytics'
JS_DIR = 'GenuisNet.ai/js'
ALL_LANGUAGES = ['en', 'es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']
TOOLS = ['datarobot', 'domo-ai', 'h2oai', 'microstrategy-ai', 'power-bi-copilot', 'qlik-sense-ai', 'sisense-ai', 'yellowfin-ai']

def check_i18n_file(tool):
    """Check language coverage in i18n file"""
    filepath = os.path.join(JS_DIR, f"{tool}-i18n.js")
    
    if not os.path.exists(filepath):
        return None, "File not found"
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all language declarations
        pattern = r'"([a-z]{2})":\s*\{'
        languages = sorted(set(re.findall(pattern, content)))
        
        missing = [lang for lang in ALL_LANGUAGES if lang not in languages]
        
        return languages, missing
    except Exception as e:
        return None, f"Error: {e}"

def check_batch_files(tool):
    """Check which batch files exist and their content"""
    batches = {}
    
    for batch_num in [1, 2, 3]:
        filepath = os.path.join(ANALYTICS_DIR, f"{tool}-batch{batch_num}.json")
        
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                if data:
                    langs = list(data.keys())
                    batches[batch_num] = langs
            except:
                pass
    
    return batches

print("=" * 80)
print("FINAL ANALYTICS TRANSLATION VERIFICATION")
print("=" * 80)

complete_count = 0
incomplete_count = 0
total_missing_langs = 0

for tool in TOOLS:
    print(f"\n{tool}:")
    
    # Check i18n file
    languages, missing = check_i18n_file(tool)
    
    if languages is None:
        print(f"  [ERROR] {missing}")
        incomplete_count += 1
        continue
    
    # Check batch files
    batches = check_batch_files(tool)
    
    print(f"  Languages in i18n: {len(languages)}/10 - {', '.join(languages)}")
    
    if missing:
        print(f"  Missing ({len(missing)}): {', '.join(missing)}")
        incomplete_count += 1
        total_missing_langs += len(missing)
        
        # Show batch file status
        if batches:
            print(f"  Batch files: {batches}")
    else:
        print(f"  [COMPLETE] All 10 languages present!")
        complete_count += 1

print("\n" + "=" * 80)
print(f"SUMMARY:")
print(f"  Complete: {complete_count}/8 tools")
print(f"  Incomplete: {incomplete_count}/8 tools")
print(f"  Total missing languages: {total_missing_langs}")

if complete_count == 8:
    print(f"\n  SUCCESS! All 8 Analytics tools have complete translations!")
else:
    print(f"\n  {incomplete_count} tools still need work")

print("=" * 80)
