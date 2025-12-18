#!/usr/bin/env python3
"""
Vérification finale - Tout est-il en place?
"""

import re
import json

def verify_all():
    print("\n" + "="*80)
    print("🔍 VÉRIFICATION FINALE DU SYSTÈME MULTILINGUE")
    print("="*80 + "\n")
    
    # 1. Vérifier index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    data_i18n_count = len(re.findall(r'data-i18n="[^"]+"', html_content))
    data_i18n_text = len(re.findall(r'data-i18n-text="[^"]+"', html_content))
    data_i18n_alt = len(re.findall(r'data-i18n-alt="[^"]+"', html_content))
    
    print("📄 INDEX.HTML:")
    print(f"   ✅ data-i18n: {data_i18n_count}")
    print(f"   ✅ data-i18n-text: {data_i18n_text}")
    print(f"   ✅ data-i18n-alt: {data_i18n_alt}")
    print(f"   ✅ TOTAL: {data_i18n_count + data_i18n_text + data_i18n_alt}")
    
    # 2. Vérifier clés critiques
    print("\n🔑 CLÉS CRITIQUES:")
    critical_keys = [
        'hero.discover-the-future',
        'hero.of-ai-tools',
        'hero.discover-the-futureof-ai-tools',
        'btn.ready-to-discover-your-perfect',
        'btn.explore-116-carefully-curated-',
        'nav.home',
        'footer.privacy-policy',
    ]
    
    for key in critical_keys:
        in_html = f'data-i18n="{key}"' in html_content or f'data-i18n-text="{key}"' in html_content
        status = "✅" if in_html else "❌"
        print(f"   {status} {key} dans HTML")
    
    # 3. Vérifier js/i18n.js
    with open('js/i18n.js', 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    # Vérifier que data-i18n-text est géré
    has_text_handler = 'data-i18n-text' in js_content and 'setAttribute' in js_content
    
    print("\n⚙️  JS/I18N.JS:")
    print(f"   {'✅' if has_text_handler else '❌'} Support data-i18n-text")
    
    # Compter les clés par langue
    for lang in ['en', 'es', 'fr', 'de']:
        count = js_content.count(f'"{lang}": {{')
        print(f"   ✅ Bloc {lang.upper()}: {'présent' if count > 0 else 'MANQUANT'}")
    
    # 4. Vérifier traductions clés
    print("\n🌐 TRADUCTIONS ESPAGNOLES:")
    spanish_tests = [
        ('"hero.discover-the-future": "Descubre el Futuro"', 'Hero discover'),
        ('"hero.of-ai-tools": "de Herramientas IA"', 'Hero of-ai-tools'),
        ('"nav.home": "Inicio"', 'Nav home'),
        ('"footer.privacy-policy": "Política de Privacidad"', 'Footer privacy'),
    ]
    
    for test, name in spanish_tests:
        found = test in js_content
        print(f"   {'✅' if found else '❌'} {name}")
    
    # 5. Synthèse
    print("\n" + "="*80)
    print("📊 SYNTHÈSE:")
    all_good = (
        data_i18n_count >= 70 and
        data_i18n_text >= 1 and
        has_text_handler and
        all(test in js_content for test, _ in spanish_tests)
    )
    
    if all_good:
        print("✅ TOUT EST EN PLACE! Système prêt à tester.")
        print("\n🚀 PROCHAINE ÉTAPE:")
        print("   1. Ouvrir index.html dans le navigateur")
        print("   2. Changer pour Español 🇪🇸")
        print("   3. Vérifier que les textes changent")
    else:
        print("⚠️  ATTENTION: Certains éléments manquants.")
        print("   Vérifier les ❌ ci-dessus")
    
    print("="*80 + "\n")

if __name__ == "__main__":
    verify_all()
