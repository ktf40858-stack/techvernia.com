#!/usr/bin/env python3
import sys, io, re

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# Lire le fichier
with open('GenuisNet.ai/js/paradox-olivia-i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

languages = ['en', 'de', 'fr', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']
test_keys = [
    'review.paradox-olivia.overview',
    'review.paradox-olivia.paradox-olivia.is.a',
    'review.paradox-olivia.the.platform.leverages.advanced.machine',
    'review.paradox-olivia.whether.youre.a.small.startup'
]

print("🔍 VÉRIFICATION TRADUCTION COMPLÈTE\n")
print("=" * 80)

for lang in languages:
    print(f"\n{lang.upper()}:")
    print("-" * 80)

    # Extraire la section de cette langue
    lang_pattern = rf'  "{lang}": {{\n(.*?)\n  }}'
    match = re.search(lang_pattern, content, re.DOTALL)

    if match:
        section = match.group(1)

        # Compter total de clés
        total_keys = len(re.findall(r'"review\.paradox-olivia\.[^"]+": ', section))

        # Vérifier les clés de test
        for key in test_keys:
            key_match = re.search(rf'"{key}":\s+"([^"]+)"', section)
            if key_match:
                value = key_match.group(1)
                # Tronquer si trop long
                if len(value) > 70:
                    value = value[:70] + "..."
                print(f"  ✓ {key.split('.')[-1]}: {value}")
            else:
                print(f"  ❌ {key.split('.')[-1]}: MANQUANT")

        print(f"\n  📊 Total: {total_keys} clés")
    else:
        print(f"  ❌ Section non trouvée")

print("\n" + "=" * 80)
print("✅ Vérification terminée!")
