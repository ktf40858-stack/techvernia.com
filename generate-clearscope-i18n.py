#!/usr/bin/env python3
"""
Script to generate clearscope-i18n.js from batch JSON files
Run this script from the project root directory
"""

import json
import os

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Read batch files
batch_dir = os.path.join(script_dir, 'GenuisNet.ai', 'pages', 'reviews', 'seo')
batch1_path = os.path.join(batch_dir, 'clearscope-batch1.json')
batch2_path = os.path.join(batch_dir, 'clearscope-batch2.json')
batch3_path = os.path.join(batch_dir, 'clearscope-batch3.json')

with open(batch1_path, 'r', encoding='utf-8') as f:
    batch1 = json.load(f)

with open(batch2_path, 'r', encoding='utf-8') as f:
    batch2 = json.load(f)

with open(batch3_path, 'r', encoding='utf-8') as f:
    batch3 = json.load(f)

# Merge translations by language
languages = ['en', 'es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']
merged = {}

for lang in languages:
    merged[lang] = {}
    for batch in [batch1, batch2, batch3]:
        if lang in batch:
            merged[lang].update(batch[lang])

# Build JavaScript file
js_content = f'const clearscopeTranslations = {json.dumps(merged, ensure_ascii=False, indent=2)};\n\n'

js_content += '''function getClearscopeTranslation(key, lang) {
  if (clearscopeTranslations[lang] && clearscopeTranslations[lang][key]) {
    return clearscopeTranslations[lang][key];
  }
  if (clearscopeTranslations.en && clearscopeTranslations.en[key]) {
    return clearscopeTranslations.en[key];
  }
  return null;
}

function applyClearscopeTranslations(lang) {
  console.log('Applying clearscope translations for:', lang);
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.getAttribute('data-i18n');
    if (key && key.startsWith('review.clearscope.')) {
      const translation = getClearscopeTranslation(key, lang);
      if (translation) {
        element.textContent = translation;
        count++;
      }
    }
  });
  console.log(`Applied ${count} clearscope translations`);
}

window.addEventListener('languageChanged', (e) => {
  const lang = e.detail.language;
  setTimeout(() => applyClearscopeTranslations(lang), 200);
});

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    applyClearscopeTranslations(currentLang);
  });
} else {
  const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
  applyClearscopeTranslations(currentLang);
}

console.log('clearscope i18n loaded');
'''

# Write the JavaScript file
output_path = os.path.join(script_dir, 'GenuisNet.ai', 'js', 'clearscope-i18n.js')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f'Created {output_path}')
print(f'Total keys: {len(merged["en"])}')
print(f'Languages: {", ".join(languages)}')
print(f'File size: {len(js_content)} bytes')
