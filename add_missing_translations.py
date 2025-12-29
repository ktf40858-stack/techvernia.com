#!/usr/bin/env python3
import sys, io, json, re

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

print("📝 AJOUT DES TRADUCTIONS MANQUANTES")
print("=" * 100)

tools = [
    'beamery', 'eightfold-ai', 'fetcher', 'findem', 'harver', 'hirevue',
    'humanly', 'paradox-olivia', 'phenom', 'pymetrics', 'seekout', 'sense',
    'textio', 'workable-ai'
]

# Traductions de référence pour les nouvelles clés
reference_translations = {
    'en': {
        'rating.features': 'Features',
        'rating.ease-of-use': 'Ease of Use',
        'rating.value': 'Value',
        'rating.support': 'Support',
        'rating.performance': 'Performance',
        'pricing.free-plan': 'Free Plan',
        'pricing.professional-plan': 'Professional',
        'pricing.enterprise-plan': 'Enterprise',
        'info.category': 'Category',
        'info.pricing': 'Pricing',
        'info.free-trial': 'Free Trial',
        'info.platform': 'Platform',
        'info.category-hr': 'HR & Recruiting',
        'info.pricing-from-free': 'From Free',
        'info.trial-14-days': '14 days',
        'info.platform-web-mobile': 'Web, Mobile',
        'sidebar.quick-info': 'ℹ️ Quick Info',
        'sidebar.table-of-contents': '📑 Table of Contents',
        'toc.overview': 'Overview',
        'toc.key-features': 'Key Features',
        'toc.pros-cons': 'Pros & Cons',
        'toc.pricing': 'Pricing',
        'toc.use-cases': 'Use Cases',
        'toc.comparison': 'Comparison',
        'toc.faq': 'FAQ',
        'toc.final-verdict': 'Final Verdict',
    },
    'de': {
        'rating.features': 'Funktionen',
        'rating.ease-of-use': 'Benutzerfreundlichkeit',
        'rating.value': 'Wert',
        'rating.support': 'Support',
        'rating.performance': 'Leistung',
        'pricing.free-plan': 'Kostenloser Plan',
        'pricing.professional-plan': 'Professionell',
        'pricing.enterprise-plan': 'Enterprise',
        'info.category': 'Kategorie',
        'info.pricing': 'Preise',
        'info.free-trial': 'Kostenlose Testversion',
        'info.platform': 'Plattform',
        'info.category-hr': 'HR & Recruiting',
        'info.pricing-from-free': 'Ab Kostenlos',
        'info.trial-14-days': '14 Tage',
        'info.platform-web-mobile': 'Web, Mobil',
        'sidebar.quick-info': 'ℹ️ Schnellinfo',
        'sidebar.table-of-contents': '📑 Inhaltsverzeichnis',
        'toc.overview': 'Überblick',
        'toc.key-features': 'Hauptfunktionen',
        'toc.pros-cons': 'Vor- & Nachteile',
        'toc.pricing': 'Preise',
        'toc.use-cases': 'Anwendungsfälle',
        'toc.comparison': 'Vergleich',
        'toc.faq': 'FAQ',
        'toc.final-verdict': 'Fazit',
    },
    'fr': {
        'rating.features': 'Fonctionnalités',
        'rating.ease-of-use': 'Facilité d\'utilisation',
        'rating.value': 'Valeur',
        'rating.support': 'Support',
        'rating.performance': 'Performance',
        'pricing.free-plan': 'Plan Gratuit',
        'pricing.professional-plan': 'Professionnel',
        'pricing.enterprise-plan': 'Entreprise',
        'info.category': 'Catégorie',
        'info.pricing': 'Tarification',
        'info.free-trial': 'Essai Gratuit',
        'info.platform': 'Plateforme',
        'info.category-hr': 'RH & Recrutement',
        'info.pricing-from-free': 'Dès Gratuit',
        'info.trial-14-days': '14 jours',
        'info.platform-web-mobile': 'Web, Mobile',
        'sidebar.quick-info': 'ℹ️ Infos Rapides',
        'sidebar.table-of-contents': '📑 Table des Matières',
        'toc.overview': 'Aperçu',
        'toc.key-features': 'Fonctionnalités Clés',
        'toc.pros-cons': 'Avantages & Inconvénients',
        'toc.pricing': 'Tarification',
        'toc.use-cases': 'Cas d\'Usage',
        'toc.comparison': 'Comparaison',
        'toc.faq': 'FAQ',
        'toc.final-verdict': 'Verdict Final',
    },
    'es': {
        'rating.features': 'Características',
        'rating.ease-of-use': 'Facilidad de Uso',
        'rating.value': 'Valor',
        'rating.support': 'Soporte',
        'rating.performance': 'Rendimiento',
        'pricing.free-plan': 'Plan Gratuito',
        'pricing.professional-plan': 'Profesional',
        'pricing.enterprise-plan': 'Empresa',
        'info.category': 'Categoría',
        'info.pricing': 'Precios',
        'info.free-trial': 'Prueba Gratuita',
        'info.platform': 'Plataforma',
        'info.category-hr': 'RRHH & Reclutamiento',
        'info.pricing-from-free': 'Desde Gratis',
        'info.trial-14-days': '14 días',
        'info.platform-web-mobile': 'Web, Móvil',
        'sidebar.quick-info': 'ℹ️ Información Rápida',
        'sidebar.table-of-contents': '📑 Tabla de Contenidos',
        'toc.overview': 'Resumen',
        'toc.key-features': 'Características Clave',
        'toc.pros-cons': 'Pros & Contras',
        'toc.pricing': 'Precios',
        'toc.use-cases': 'Casos de Uso',
        'toc.comparison': 'Comparación',
        'toc.faq': 'Preguntas Frecuentes',
        'toc.final-verdict': 'Veredicto Final',
    },
    'pt': {
        'rating.features': 'Recursos',
        'rating.ease-of-use': 'Facilidade de Uso',
        'rating.value': 'Valor',
        'rating.support': 'Suporte',
        'rating.performance': 'Desempenho',
        'pricing.free-plan': 'Plano Gratuito',
        'pricing.professional-plan': 'Profissional',
        'pricing.enterprise-plan': 'Enterprise',
        'info.category': 'Categoria',
        'info.pricing': 'Preços',
        'info.free-trial': 'Teste Gratuito',
        'info.platform': 'Plataforma',
        'info.category-hr': 'RH & Recrutamento',
        'info.pricing-from-free': 'A Partir de Grátis',
        'info.trial-14-days': '14 dias',
        'info.platform-web-mobile': 'Web, Mobile',
        'sidebar.quick-info': 'ℹ️ Informação Rápida',
        'sidebar.table-of-contents': '📑 Índice',
        'toc.overview': 'Visão Geral',
        'toc.key-features': 'Recursos Principais',
        'toc.pros-cons': 'Prós & Contras',
        'toc.pricing': 'Preços',
        'toc.use-cases': 'Casos de Uso',
        'toc.comparison': 'Comparação',
        'toc.faq': 'Perguntas Frequentes',
        'toc.final-verdict': 'Veredicto Final',
    },
    'zh': {
        'rating.features': '功能',
        'rating.ease-of-use': '易用性',
        'rating.value': '价值',
        'rating.support': '支持',
        'rating.performance': '性能',
        'pricing.free-plan': '免费计划',
        'pricing.professional-plan': '专业版',
        'pricing.enterprise-plan': '企业版',
        'info.category': '类别',
        'info.pricing': '定价',
        'info.free-trial': '免费试用',
        'info.platform': '平台',
        'info.category-hr': '人力资源与招聘',
        'info.pricing-from-free': '从免费起',
        'info.trial-14-days': '14天',
        'info.platform-web-mobile': '网页、移动',
        'sidebar.quick-info': 'ℹ️ 快速信息',
        'sidebar.table-of-contents': '📑 目录',
        'toc.overview': '概述',
        'toc.key-features': '主要功能',
        'toc.pros-cons': '优缺点',
        'toc.pricing': '定价',
        'toc.use-cases': '使用案例',
        'toc.comparison': '比较',
        'toc.faq': '常见问题',
        'toc.final-verdict': '最终结论',
    },
    'ja': {
        'rating.features': '機能',
        'rating.ease-of-use': '使いやすさ',
        'rating.value': '価値',
        'rating.support': 'サポート',
        'rating.performance': 'パフォーマンス',
        'pricing.free-plan': '無料プラン',
        'pricing.professional-plan': 'プロフェッショナル',
        'pricing.enterprise-plan': 'エンタープライズ',
        'info.category': 'カテゴリー',
        'info.pricing': '料金',
        'info.free-trial': '無料トライアル',
        'info.platform': 'プラットフォーム',
        'info.category-hr': '人事・採用',
        'info.pricing-from-free': '無料から',
        'info.trial-14-days': '14日間',
        'info.platform-web-mobile': 'ウェブ、モバイル',
        'sidebar.quick-info': 'ℹ️ クイック情報',
        'sidebar.table-of-contents': '📑 目次',
        'toc.overview': '概要',
        'toc.key-features': '主な機能',
        'toc.pros-cons': 'メリット・デメリット',
        'toc.pricing': '料金',
        'toc.use-cases': '活用事例',
        'toc.comparison': '比較',
        'toc.faq': 'よくある質問',
        'toc.final-verdict': '総合評価',
    },
    'ko': {
        'rating.features': '기능',
        'rating.ease-of-use': '사용 편의성',
        'rating.value': '가치',
        'rating.support': '지원',
        'rating.performance': '성능',
        'pricing.free-plan': '무료 플랜',
        'pricing.professional-plan': '프로페셔널',
        'pricing.enterprise-plan': '엔터프라이즈',
        'info.category': '카테고리',
        'info.pricing': '가격',
        'info.free-trial': '무료 체험',
        'info.platform': '플랫폼',
        'info.category-hr': '인사 & 채용',
        'info.pricing-from-free': '무료부터',
        'info.trial-14-days': '14일',
        'info.platform-web-mobile': '웹, 모바일',
        'sidebar.quick-info': 'ℹ️ 빠른 정보',
        'sidebar.table-of-contents': '📑 목차',
        'toc.overview': '개요',
        'toc.key-features': '주요 기능',
        'toc.pros-cons': '장단점',
        'toc.pricing': '가격',
        'toc.use-cases': '사용 사례',
        'toc.comparison': '비교',
        'toc.faq': '자주 묻는 질문',
        'toc.final-verdict': '최종 평가',
    },
    'ar': {
        'rating.features': 'الميزات',
        'rating.ease-of-use': 'سهولة الاستخدام',
        'rating.value': 'القيمة',
        'rating.support': 'الدعم',
        'rating.performance': 'الأداء',
        'pricing.free-plan': 'الخطة المجانية',
        'pricing.professional-plan': 'احترافي',
        'pricing.enterprise-plan': 'للمؤسسات',
        'info.category': 'الفئة',
        'info.pricing': 'التسعير',
        'info.free-trial': 'تجربة مجانية',
        'info.platform': 'المنصة',
        'info.category-hr': 'الموارد البشرية والتوظيف',
        'info.pricing-from-free': 'من مجاني',
        'info.trial-14-days': '14 يومًا',
        'info.platform-web-mobile': 'الويب، الجوال',
        'sidebar.quick-info': 'ℹ️ معلومات سريعة',
        'sidebar.table-of-contents': '📑 جدول المحتويات',
        'toc.overview': 'نظرة عامة',
        'toc.key-features': 'الميزات الرئيسية',
        'toc.pros-cons': 'الإيجابيات والسلبيات',
        'toc.pricing': 'التسعير',
        'toc.use-cases': 'حالات الاستخدام',
        'toc.comparison': 'المقارنة',
        'toc.faq': 'الأسئلة الشائعة',
        'toc.final-verdict': 'الحكم النهائي',
    },
    'hi': {
        'rating.features': 'विशेषताएं',
        'rating.ease-of-use': 'उपयोग में आसानी',
        'rating.value': 'मूल्य',
        'rating.support': 'सहायता',
        'rating.performance': 'प्रदर्शन',
        'pricing.free-plan': 'मुफ़्त योजना',
        'pricing.professional-plan': 'पेशेवर',
        'pricing.enterprise-plan': 'एंटरप्राइज़',
        'info.category': 'श्रेणी',
        'info.pricing': 'मूल्य निर्धारण',
        'info.free-trial': 'मुफ़्त परीक्षण',
        'info.platform': 'प्लेटफ़ॉर्म',
        'info.category-hr': 'मानव संसाधन और भर्ती',
        'info.pricing-from-free': 'मुफ़्त से',
        'info.trial-14-days': '14 दिन',
        'info.platform-web-mobile': 'वेब, मोबाइल',
        'sidebar.quick-info': 'ℹ️ त्वरित जानकारी',
        'sidebar.table-of-contents': '📑 विषय सूची',
        'toc.overview': 'अवलोकन',
        'toc.key-features': 'मुख्य विशेषताएं',
        'toc.pros-cons': 'फायदे और नुकसान',
        'toc.pricing': 'मूल्य निर्धारण',
        'toc.use-cases': 'उपयोग के मामले',
        'toc.comparison': 'तुलना',
        'toc.faq': 'अक्सर पूछे जाने वाले प्रश्न',
        'toc.final-verdict': 'अंतिम निर्णय',
    },
}

languages = ['en', 'de', 'fr', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

for tool in tools:
    tool_var = tool.replace('-', '')
    i18n_path = f'GenuisNet.ai/js/{tool}-i18n.js'

    print(f"\n🔧 {tool}...")

    # Lire le fichier i18n existant
    with open(i18n_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraire les traductions actuelles
    current_translations = {}

    for lang in languages:
        current_translations[lang] = {}

        # Trouver la section de langue
        lang_section_pattern = rf'  "{lang}": {{\n(.*?)\n  }}'
        match = re.search(lang_section_pattern, content, re.DOTALL)

        if match:
            section = match.group(1)

            # Extraire toutes les clés
            for line in section.split('\n'):
                key_match = re.match(r'\s+"([^"]+)":\s+"((?:[^"\\\\]|\\\\.)*)",?', line)
                if key_match:
                    key = key_match.group(1)
                    value = key_match.group(2)
                    current_translations[lang][key] = value

        # Ajouter les nouvelles traductions
        for short_key, translation in reference_translations[lang].items():
            full_key = f'review.{tool}.{short_key}'
            if full_key not in current_translations[lang]:
                current_translations[lang][full_key] = translation

    # Générer le nouveau fichier
    output_lines = []

    # Trouver où commence l'objet de traductions
    const_match = re.search(rf'const {tool_var}Translations = {{', content)
    if const_match:
        # Ajouter tout avant l'objet de traductions
        output_lines.append(content[:const_match.end()])
        output_lines.append('')

        # Ajouter les traductions
        for lang in languages:
            if current_translations[lang]:
                output_lines.append(f'  "{lang}": {{')
                for key in sorted(current_translations[lang].keys()):
                    value = current_translations[lang][key]
                    output_lines.append(f'      "{key}": "{value}",')

                if output_lines[-1].endswith(','):
                    output_lines[-1] = output_lines[-1][:-1]
                output_lines.append('  },')

        if output_lines[-1].endswith(','):
            output_lines[-1] = output_lines[-1][:-1]
        output_lines.append('};')

        # Ajouter le code d'application (après l'objet)
        function_match = re.search(r'\n\nfunction get', content, re.DOTALL)
        if function_match:
            output_lines.append(content[function_match.start():])
        else:
            # Générer le code d'application si manquant
            application_code = f'''

function get{tool_var.capitalize()}Translation(key, lang) {{
  if ({tool_var}Translations[lang] && {tool_var}Translations[lang][key]) {{
    return {tool_var}Translations[lang][key];
  }}
  if ({tool_var}Translations.en && {tool_var}Translations.en[key]) {{
    return {tool_var}Translations.en[key];
  }}
  return null;
}}

function apply{tool_var.capitalize()}Translations(lang) {{
  console.log(`🔥 Applying {tool} translations for: ${{lang}}`);
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {{
    const key = element.getAttribute('data-i18n');
    if (key && (key.startsWith('review.{tool}.') || key.startsWith('review.common.'))) {{
      const translation = get{tool_var.capitalize()}Translation(key, lang);
      if (translation) {{
        element.textContent = translation;
        count++;
      }}
    }}
  }});
  console.log(`✅ Applied ${{count}} {tool} translations`);
}}

window.addEventListener('languageChanged', (e) => {{
  const lang = e.detail.language;
  setTimeout(() => apply{tool_var.capitalize()}Translations(lang), 200);
}});

if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', () => {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{tool_var.capitalize()}Translations(currentLang);
  }});
}} else {{
  const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
  apply{tool_var.capitalize()}Translations(currentLang);
}}

console.log('✅ {tool} i18n loaded');
'''
            output_lines.append(application_code)

        # Sauvegarder
        with open(i18n_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output_lines))

        total = sum(len(current_translations[lang]) for lang in languages)
        print(f"  ✅ {total} traductions (incluant 260 nouvelles)")

print(f"\n{'='*100}")
print("✅ TOUTES LES TRADUCTIONS AJOUTÉES!")
print(f"{'='*100}")
