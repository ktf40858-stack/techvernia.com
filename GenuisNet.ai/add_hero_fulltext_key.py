#!/usr/bin/env python3
"""
Ajouter la clé hero.discover-the-future-of-ai-tools dans toutes les langues
"""

import re

def add_hero_fulltext():
    print("\n" + "="*80)
    print("🔧 AJOUT DE LA CLÉ hero.discover-the-future-of-ai-tools")
    print("="*80 + "\n")
    
    with open('js/i18n.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Traductions complètes pour "Discover the Future of AI Tools"
    translations = {
        'en': 'Discover the Future of AI Tools',
        'es': 'Descubre el Futuro de las Herramientas IA',
        'fr': "Découvrez l'Avenir des Outils IA",
        'de': 'Entdecken Sie die Zukunft der KI-Tools',
        'pt': 'Descubra o Futuro das Ferramentas IA',
        'zh': '发现AI工具的未来',
        'ja': 'AIツールの未来を発見',
        'ko': 'AI 도구의 미래를 발견하세요',
        'ar': 'اكتشف مستقبل أدوات الذكاء الاصطناعي',
        'hi': 'AI टूल्स के भविष्य की खोज करें',
    }
    
    modifications = 0
    
    # Ajouter après hero.of-ai-tools dans chaque langue
    for lang, translation in translations.items():
        # Pattern: trouver "hero.of-ai-tools": "...",
        pattern = rf'("hero\.of-ai-tools": "[^"]+",)'
        replacement = rf'\1\n        "hero.discover-the-future-of-ai-tools": "{translation}",'
        
        # Chercher dans le bloc de cette langue
        # On utilise un marqueur pour savoir où on est
        lang_pattern = rf'({lang}: {{[^}}]*?{pattern})'
        
        # Approche plus simple: chercher juste après hero.of-ai-tools
        simple_pattern = rf'("hero\.of-ai-tools": "([^"]+)",)(\s+)("hero\.discover-the-futureof-ai-tools")'
        
        # Si la clé suivante est hero.discover-the-futureof-ai-tools, insérer avant
        if re.search(simple_pattern, content):
            content = re.sub(
                simple_pattern,
                rf'\1\3"hero.discover-the-future-of-ai-tools": "{translation}",\3\4',
                content,
                count=1
            )
            print(f"✅ Ajouté pour {lang}: {translation[:40]}...")
            modifications += 1
    
    if modifications == 0:
        # Méthode alternative: insertion après "hero.of-ai-tools" de manière brute
        print("⚠️  Méthode simple échouée, utilisation méthode alternative...")
        
        # Pour chaque langue, trouver le bon endroit
        for lang in ['en', 'es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']:
            translation = translations[lang]
            
            # Chercher "hero.of-ai-tools": "...", dans cette langue
            # puis ajouter juste après
            pattern = rf'("{lang}": {{.*?)"hero\.of-ai-tools": "([^"]+)",(.*?)}}'
            
            def replacer(match):
                before = match.group(1)
                of_ai_tools_value = match.group(2)
                after = match.group(3)
                
                # Ajouter la nouvelle clé juste après hero.of-ai-tools
                new_line = f'\n        "hero.discover-the-future-of-ai-tools": "{translation}",'
                
                return f'{before}"hero.of-ai-tools": "{of_ai_tools_value}",{new_line}{after}}}'
            
            content_before = content
            content = re.sub(pattern, replacer, content, flags=re.DOTALL, count=1)
            
            if content != content_before:
                print(f"✅ Ajouté pour {lang}: {translation[:40]}...")
                modifications += 1
    
    # Sauvegarder
    with open('js/i18n.js', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n{'='*80}")
    print(f"✅ TOTAL: {modifications} traductions ajoutées")
    print(f"✅ js/i18n.js mis à jour")
    print(f"{'='*80}\n")
    
    return modifications

if __name__ == "__main__":
    add_hero_fulltext()
