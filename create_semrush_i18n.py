import json
import os

# Change to SEO directory
os.chdir('GenuisNet.ai/pages/reviews/seo')

# Load all translations
merged = {}

# Load content batches
for i in range(1, 4):
    with open(f'semrush-batch{i}.json', 'r', encoding='utf-8') as f:
        batch = json.load(f)
        for lang in batch.keys():
            if lang not in ['en', 'target_langs']:
                if lang not in merged:
                    merged[lang] = {}
                merged[lang].update(batch[lang])

# Load EN content
with open('semrush-en.json', 'r', encoding='utf-8') as f:
    merged['en'] = json.load(f)

# Load FAQ batches
for i in range(1, 4):
    with open(f'semrush-faqs-batch{i}.json', 'r', encoding='utf-8') as f:
        batch = json.load(f)
        for lang in batch.keys():
            if lang not in ['en', 'target_langs']:
                if lang not in merged:
                    merged[lang] = {}
                merged[lang].update(batch[lang])

# Load EN FAQs
with open('semrush-faqs-en.json', 'r', encoding='utf-8') as f:
    merged['en'].update(json.load(f))

# Create JavaScript content
js_content = 'const semrushTranslations = ' + json.dumps(merged, ensure_ascii=False, indent=2) + ''';

function getSemrushTranslation(key, lang) {
    if (semrushTranslations[lang] && semrushTranslations[lang][key]) {
        return semrushTranslations[lang][key];
    }
    if (semrushTranslations.en && semrushTranslations.en[key]) {
        return semrushTranslations.en[key];
    }
    return null;
}

function applySemrushTranslations(lang) {
    console.log('Applying semrush translations for:', lang);
    let count = 0;
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (key && key.startsWith('review.semrush.')) {
            const translation = getSemrushTranslation(key, lang);
            if (translation) {
                element.textContent = translation;
                count++;
            }
        }
    });
    console.log(`Applied ${count} semrush translations`);
}

window.addEventListener('languageChanged', (e) => {
    const lang = e.detail.language;
    setTimeout(() => applySemrushTranslations(lang), 200);
});

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
        applySemrushTranslations(currentLang);
    });
} else {
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    applySemrushTranslations(currentLang);
}

console.log('semrush i18n loaded');
'''

# Write to js file
os.chdir('../../..')
with open('js/semrush-i18n.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print('Created semrush-i18n.js successfully')
print(f'Total languages: {len(merged)}')
print(f'Keys per language: {len(merged["en"])}')
