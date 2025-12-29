"""
Quick script to check which translation batches have been completed
"""
import json
import os

TOOLS = ['ansible', 'cisco-ai', 'datadog', 'juniper-mist', 'prtg', 'splunk', 'terraform', 'zabbix']
LANGUAGES = ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

print("\n" + "="*60)
print("NETWORKING TRANSLATION BATCH STATUS CHECK")
print("="*60)

total_batches = 0
completed_batches = 0
incomplete_batches = []

for tool in TOOLS:
    print(f"\n{tool.upper()}:")

    # Check content batches
    for batch_num in range(1, 4):
        batch_file = f"GenuisNet.ai/pages/reviews/networking/{tool}-batch{batch_num}.json"
        total_batches += 1

        if os.path.exists(batch_file):
            try:
                with open(batch_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Check if all 3 languages have translations (not just English structure)
                langs_complete = []
                for lang in ['es', 'fr', 'de'] if batch_num == 1 else ['pt', 'zh', 'ja'] if batch_num == 2 else ['ko', 'ar', 'hi']:
                    if lang in data and len(data[lang]) > 0:
                        # Check if first value looks translated (not English)
                        first_value = list(data[lang].values())[0] if data[lang] else ""
                        if first_value and len(first_value) > 5:
                            langs_complete.append(lang)

                if len(langs_complete) == 3:
                    print(f"  ✅ batch{batch_num}: {'/'.join(langs_complete).upper()}")
                    completed_batches += 1
                else:
                    print(f"  ⏳ batch{batch_num}: {len(langs_complete)}/3 languages")
                    incomplete_batches.append(f"{tool}-batch{batch_num}")
            except Exception as e:
                print(f"  ❌ batch{batch_num}: ERROR - {str(e)}")
                incomplete_batches.append(f"{tool}-batch{batch_num}")

    # Check FAQ batches (only for tools with FAQs)
    for batch_num in range(1, 4):
        faq_batch_file = f"GenuisNet.ai/pages/reviews/networking/{tool}-faqs-batch{batch_num}.json"

        if os.path.exists(faq_batch_file):
            total_batches += 1
            try:
                with open(faq_batch_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                langs_complete = []
                for lang in ['es', 'fr', 'de'] if batch_num == 1 else ['pt', 'zh', 'ja'] if batch_num == 2 else ['ko', 'ar', 'hi']:
                    if lang in data and len(data[lang]) > 0:
                        first_value = list(data[lang].values())[0] if data[lang] else ""
                        if first_value and len(first_value) > 5:
                            langs_complete.append(lang)

                if len(langs_complete) == 3:
                    print(f"  ✅ FAQs batch{batch_num}: {'/'.join(langs_complete).upper()}")
                    completed_batches += 1
                else:
                    print(f"  ⏳ FAQs batch{batch_num}: {len(langs_complete)}/3 languages")
                    incomplete_batches.append(f"{tool}-faqs-batch{batch_num}")
            except Exception as e:
                print(f"  ❌ FAQs batch{batch_num}: ERROR - {str(e)}")
                incomplete_batches.append(f"{tool}-faqs-batch{batch_num}")

print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print(f"Total batches: {total_batches}")
print(f"Completed: {completed_batches}/{total_batches} ({(completed_batches/total_batches)*100:.1f}%)")
print(f"Remaining: {total_batches - completed_batches}")

if incomplete_batches:
    print(f"\nIncomplete batches ({len(incomplete_batches)}):")
    for batch in incomplete_batches[:10]:
        print(f"  - {batch}")
    if len(incomplete_batches) > 10:
        print(f"  ... and {len(incomplete_batches) - 10} more")

if completed_batches == total_batches:
    print("\n🎉 ALL TRANSLATIONS COMPLETE! Ready to generate i18n files.")
else:
    print(f"\n⏳ Waiting for {total_batches - completed_batches} batches to complete...")
