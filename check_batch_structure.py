import json
import os

ANALYTICS_DIR = 'GenuisNet.ai/pages/reviews/analytics'

tools = ['datarobot', 'domo-ai', 'h2oai', 'microstrategy-ai', 'power-bi-copilot', 'qlik-sense-ai', 'sisense-ai', 'yellowfin-ai']

print("Batch File Structure Analysis")
print("=" * 70)

for tool in tools:
    print(f"\n{tool}:")

    for batch_num in [1, 2, 3]:
        filepath = os.path.join(ANALYTICS_DIR, f"{tool}-batch{batch_num}.json")

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if not data:
                print(f"  Batch {batch_num}: EMPTY")
                continue

            first_key = list(data.keys())[0]
            first_value = data[first_key]

            if isinstance(first_value, dict):
                # Inverted format: key -> {lang: value}
                num_keys = len(data)
                langs_in_first = list(first_value.keys()) if first_value else []
                print(f"  Batch {batch_num}: INVERTED - {num_keys} keys x {langs_in_first}")
            elif isinstance(first_value, str):
                # Normal format: lang -> {key: value}
                langs = list(data.keys())
                num_keys_per_lang = {lang: len(data[lang]) for lang in langs if data[lang]}
                print(f"  Batch {batch_num}: NORMAL - {langs} with {num_keys_per_lang} keys each")
            else:
                print(f"  Batch {batch_num}: UNKNOWN FORMAT")

        except Exception as e:
            print(f"  Batch {batch_num}: ERROR - {e}")
