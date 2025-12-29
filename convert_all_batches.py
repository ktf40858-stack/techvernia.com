import json
import os
import sys

# Force UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ANALYTICS_DIR = 'GenuisNet.ai/pages/reviews/analytics'
TOOLS = ['datarobot', 'domo-ai', 'h2oai', 'microstrategy-ai', 'power-bi-copilot', 'qlik-sense-ai', 'sisense-ai', 'yellowfin-ai']

def convert_batch_file(filepath):
    """Convert inverted format to normal format"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not data:
            return None, "Empty file"
        
        first_key = list(data.keys())[0]
        first_value = data[first_key]
        
        # Check if inverted format (key -> {lang: value})
        if isinstance(first_value, dict):
            result = {}
            for key, lang_dict in data.items():
                for lang, value in lang_dict.items():
                    if lang not in result:
                        result[lang] = {}
                    result[lang][key] = value
            
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            
            return result, f"Converted {len(data)} keys to {len(result)} languages"
        else:
            return data, "Already correct format"
    except Exception as e:
        return None, f"Error: {e}"

print("Converting All Batch Files to Normal Format")
print("=" * 70)

for tool in TOOLS:
    print(f"\n{tool}:")
    
    for batch_num in [1, 2, 3]:
        filepath = os.path.join(ANALYTICS_DIR, f"{tool}-batch{batch_num}.json")
        
        if not os.path.exists(filepath):
            print(f"  Batch {batch_num}: File not found")
            continue
        
        result, msg = convert_batch_file(filepath)
        print(f"  Batch {batch_num}: {msg}")

print("\n" + "=" * 70)
print("Conversion Complete!")
print("=" * 70)
