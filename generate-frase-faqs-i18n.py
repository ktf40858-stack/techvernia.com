#!/usr/bin/env python3
"""
Script to generate frase-faqs-i18n.js from batch JSON files
Run this script from the project root directory
"""

import json
import os

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Read batch files
batch_dir = os.path.join(script_dir, 'GenuisNet.ai', 'pages', 'reviews', 'seo')
batch1_path = os.path.join(batch_dir, 'frase-faqs-batch1.json')
batch2_path = os.path.join(batch_dir, 'frase-faqs-batch2.json')
batch3_path = os.path.join(batch_dir, 'frase-faqs-batch3.json')

with open(batch1_path, 'r', encoding='utf-8') as f:
    batch1 = json.load(f)

with open(batch2_path, 'r', encoding='utf-8') as f:
    batch2 = json.load(f)

with open(batch3_path, 'r', encoding='utf-8') as f:
    batch3 = json.load(f)

# Read English source file
en_path = os.path.join(batch_dir, 'frase-faqs-en.json')
with open(en_path, 'r', encoding='utf-8') as f:
    en_data = json.load(f)

# Merge translations by language
languages = ['en', 'es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']
merged = {}

# Add English first
merged['en'] = en_data

# Add other languages from batches
for lang in languages[1:]:  # Skip 'en' since we already added it
    merged[lang] = {}
    for batch in [batch1, batch2, batch3]:
        if lang in batch:
            merged[lang].update(batch[lang])

# Build JavaScript file
js_content = f'const fraseFaqTranslations = {json.dumps(merged, ensure_ascii=False, indent=2)};\n\n'

js_content += '''function getFraseFaqTranslation(key, lang) {
  if (fraseFaqTranslations[lang] && fraseFaqTranslations[lang][key]) {
    return fraseFaqTranslations[lang][key];
  }
  if (fraseFaqTranslations.en && fraseFaqTranslations.en[key]) {
    return fraseFaqTranslations.en[key];
  }
  return null;
}

function applyFraseFaqTranslations(lang) {
  console.log('Applying frase FAQ translations for:', lang);
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.getAttribute('data-i18n');
    if (key && key.startsWith('review.frase.faq.')) {
      const translation = getFraseFaqTranslation(key, lang);
      if (translation) {
        element.textContent = translation;
        count++;
      }
    }
  });
  console.log(`Applied ${count} frase FAQ translations`);
}

window.addEventListener('languageChanged', (e) => {
  const lang = e.detail.language;
  setTimeout(() => applyFraseFaqTranslations(lang), 200);
});

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    applyFraseFaqTranslations(currentLang);
  });
} else {
  const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
  applyFraseFaqTranslations(currentLang);
}

console.log('frase FAQ i18n loaded');
'''

# Write the JavaScript file
output_path = os.path.join(script_dir, 'GenuisNet.ai', 'js', 'frase-faqs-i18n.js')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f'Created {output_path}')
print(f'Total FAQ keys: {len(merged["en"])}')
print(f'Languages: {", ".join(languages)}')
print(f'File size: {len(js_content)} bytes')
