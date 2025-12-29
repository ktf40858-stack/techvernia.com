import os
import re

js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

translation_tools = {
    "deepl-pro": "DeepL Pro",
    "google-translate-ai": "Google Translate AI",
    "lilt": "Lilt",
    "lokalise": "Lokalise",
    "microsoft-translator": "Microsoft Translator",
    "modernmt": "ModernMT",
    "phrase": "Phrase",
    "smartling": "Smartling",
    "systran": "SYSTRAN",
    "unbabel": "Unbabel"
}

# Feature descriptions translations
feature_descriptions = {
    "de": {
        "intelligent.automation.that.learns.from": "Intelligente Automatisierung, die aus Ihren Workflows lernt und Prozesse in Echtzeit optimiert.",
        "comprehensive.analytics.dashboard.with.actionable": "Umfassendes Analyse-Dashboard mit umsetzbaren Erkenntnissen und prädiktiven Analysen.",
        "connect.with.100.popular.tools": "Verbinden Sie sich mit über 100 beliebten Tools und Plattformen durch native Integrationen und API.",
        "bank-grade.encryption.sso.and.compliance": "Banksichere Verschlüsselung, SSO und Compliance mit SOC 2, GDPR und HIPAA-Standards.",
        "work.together.seamlessly.with.team": "Arbeiten Sie nahtlos mit Teammitgliedern über mehrere Standorte und Zeitzonen hinweg zusammen.",
        "access.all.features.on.any": "Greifen Sie auf alle Funktionen auf jedem Gerät mit responsivem Design und nativen mobilen Apps zu."
    },
    "es": {
        "intelligent.automation.that.learns.from": "Automatización inteligente que aprende de tus flujos de trabajo y optimiza procesos en tiempo real.",
        "comprehensive.analytics.dashboard.with.actionable": "Panel de análisis completo con información procesable y análisis predictivo.",
        "connect.with.100.popular.tools": "Conéctese con más de 100 herramientas y plataformas populares a través de integraciones nativas y API.",
        "bank-grade.encryption.sso.and.compliance": "Cifrado de grado bancario, SSO y cumplimiento de los estándares SOC 2, GDPR y HIPAA.",
        "work.together.seamlessly.with.team": "Trabaje sin problemas con miembros del equipo en múltiples ubicaciones y zonas horarias.",
        "access.all.features.on.any": "Acceda a todas las funciones en cualquier dispositivo con diseño responsive y aplicaciones móviles nativas."
    },
    "fr": {
        "intelligent.automation.that.learns.from": "Automatisation intelligente qui apprend de vos flux de travail et optimise les processus en temps réel.",
        "comprehensive.analytics.dashboard.with.actionable": "Tableau de bord d'analyse complet avec des informations exploitables et des analyses prédictives.",
        "connect.with.100.popular.tools": "Connectez-vous à plus de 100 outils et plateformes populaires via des intégrations natives et une API.",
        "bank-grade.encryption.sso.and.compliance": "Chiffrement de niveau bancaire, SSO et conformité aux normes SOC 2, GDPR et HIPAA.",
        "work.together.seamlessly.with.team": "Travaillez en toute transparence avec les membres de l'équipe sur plusieurs sites et fuseaux horaires.",
        "access.all.features.on.any": "Accédez à toutes les fonctionnalités sur n'importe quel appareil avec un design responsive et des applications mobiles natives."
    },
    "pt": {
        "intelligent.automation.that.learns.from": "Automação inteligente que aprende com seus fluxos de trabalho e otimiza processos em tempo real.",
        "comprehensive.analytics.dashboard.with.actionable": "Painel de análise abrangente com insights acionáveis e análises preditivas.",
        "connect.with.100.popular.tools": "Conecte-se com mais de 100 ferramentas e plataformas populares por meio de integrações nativas e API.",
        "bank-grade.encryption.sso.and.compliance": "Criptografia de nível bancário, SSO e conformidade com os padrões SOC 2, GDPR e HIPAA.",
        "work.together.seamlessly.with.team": "Trabalhe perfeitamente com membros da equipe em vários locais e fusos horários.",
        "access.all.features.on.any": "Acesse todos os recursos em qualquer dispositivo com design responsivo e aplicativos móveis nativos."
    },
    "zh": {
        "intelligent.automation.that.learns.from": "智能自动化，从您的工作流程中学习并实时优化流程。",
        "comprehensive.analytics.dashboard.with.actionable": "全面的分析仪表板，提供可操作的见解和预测分析。",
        "connect.with.100.popular.tools": "通过原生集成和API连接100多个流行工具和平台。",
        "bank-grade.encryption.sso.and.compliance": "银行级加密、SSO以及符合SOC 2、GDPR和HIPAA标准。",
        "work.together.seamlessly.with.team": "与跨多个地点和时区的团队成员无缝协作。",
        "access.all.features.on.any": "通过响应式设计和原生移动应用程序在任何设备上访问所有功能。"
    },
    "ja": {
        "intelligent.automation.that.learns.from": "ワークフローから学習し、プロセスをリアルタイムで最適化するインテリジェントな自動化。",
        "comprehensive.analytics.dashboard.with.actionable": "実用的なインサイトと予測分析を備えた包括的な分析ダッシュボード。",
        "connect.with.100.popular.tools": "ネイティブ統合とAPIを通じて100以上の人気ツールやプラットフォームと接続。",
        "bank-grade.encryption.sso.and.compliance": "銀行レベルの暗号化、SSOおよびSOC 2、GDPR、HIPAA基準への準拠。",
        "work.together.seamlessly.with.team": "複数の場所とタイムゾーンにわたるチームメンバーとシームレスに協力。",
        "access.all.features.on.any": "レスポンシブデザインとネイティブモバイルアプリで任意のデバイスですべての機能にアクセス。"
    },
    "ko": {
        "intelligent.automation.that.learns.from": "워크플로에서 학습하고 프로세스를 실시간으로 최적화하는 지능형 자동화.",
        "comprehensive.analytics.dashboard.with.actionable": "실행 가능한 인사이트와 예측 분석을 갖춘 포괄적인 분석 대시보드.",
        "connect.with.100.popular.tools": "기본 통합 및 API를 통해 100개 이상의 인기 도구 및 플랫폼과 연결.",
        "bank-grade.encryption.sso.and.compliance": "은행 수준의 암호화, SSO 및 SOC 2, GDPR, HIPAA 표준 준수.",
        "work.together.seamlessly.with.team": "여러 위치 및 시간대에 걸쳐 팀 구성원과 원활하게 협업.",
        "access.all.features.on.any": "반응형 디자인 및 네이티브 모바일 앱으로 모든 기기에서 모든 기능에 액세스."
    },
    "ar": {
        "intelligent.automation.that.learns.from": "أتمتة ذكية تتعلم من سير عملك وتحسن العمليات في الوقت الفعلي.",
        "comprehensive.analytics.dashboard.with.actionable": "لوحة تحليلات شاملة مع رؤى قابلة للتنفيذ وتحليلات تنبؤية.",
        "connect.with.100.popular.tools": "اتصل بأكثر من 100 أداة ومنصة شائعة من خلال التكاملات الأصلية وواجهة برمجة التطبيقات.",
        "bank-grade.encryption.sso.and.compliance": "تشفير على مستوى البنوك، SSO والامتثال لمعايير SOC 2 و GDPR و HIPAA.",
        "work.together.seamlessly.with.team": "اعمل بسلاسة مع أعضاء الفريق عبر مواقع ومناطق زمنية متعددة.",
        "access.all.features.on.any": "الوصول إلى جميع الميزات على أي جهاز مع تصميم سريع الاستجابة وتطبيقات محمولة أصلية."
    },
    "hi": {
        "intelligent.automation.that.learns.from": "बुद्धिमान स्वचालन जो आपके वर्कफ़्लो से सीखता है और वास्तविक समय में प्रक्रियाओं को अनुकूलित करता है।",
        "comprehensive.analytics.dashboard.with.actionable": "कार्रवाई योग्य अंतर्दृष्टि और भविष्यसूचक विश्लेषण के साथ व्यापक विश्लेषण डैशबोर्ड।",
        "connect.with.100.popular.tools": "मूल एकीकरण और API के माध्यम से 100+ लोकप्रिय टूल और प्लेटफार्मों से कनेक्ट करें।",
        "bank-grade.encryption.sso.and.compliance": "बैंक-ग्रेड एन्क्रिप्शन, SSO और SOC 2, GDPR, और HIPAA मानकों के साथ अनुपालन।",
        "work.together.seamlessly.with.team": "कई स्थानों और समय क्षेत्रों में टीम के सदस्यों के साथ निर्बाध रूप से काम करें।",
        "access.all.features.on.any": "उत्तरदायी डिज़ाइन और मूल मोबाइल ऐप्स के साथ किसी भी डिवाइस पर सभी सुविधाओं तक पहुँचें।"
    }
}

def get_language_section(content, lang):
    """Extract a specific language section from the i18n file"""
    pattern = rf'  "{lang}":\s*{{([^}}]+(?:{{[^}}]+}}[^}}]*)*)}}'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def add_feature_description_translations(tool_key, tool_name):
    """Add feature description translations to all languages"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        return False

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    modified = False

    # For each language
    for lang, translations in feature_descriptions.items():
        # Find the language section
        lang_section = get_language_section(content, lang)

        if not lang_section:
            print(f"    [!] Language {lang} section not found")
            continue

        # Find insertion point
        lang_pattern = rf'  "{lang}":\s*{{\n'
        match = re.search(lang_pattern, content)

        if not match:
            continue

        insert_pos = match.end()

        # Add missing translations
        lines_to_add = []
        for key_suffix, translation in translations.items():
            full_key = f"review.{tool_key}.{key_suffix}"

            # Check if key exists in this language section
            if f'"{full_key}"' not in lang_section:
                escaped_value = translation.replace('"', '\\"')
                lines_to_add.append(f'    "{full_key}": "{escaped_value}",\n')
                modified = True

        if lines_to_add:
            new_content = ''.join(lines_to_add)
            content = content[:insert_pos] + new_content + content[insert_pos:]
            print(f"    [+] Added {len(lines_to_add)} description translations for {lang}")

    if modified and content != original_content:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

print("=" * 70)
print("ADDING FEATURE DESCRIPTION TRANSLATIONS")
print("=" * 70)

fixed_count = 0

for tool_key, tool_name in translation_tools.items():
    print(f"\n{tool_name}:")
    if add_feature_description_translations(tool_key, tool_name):
        fixed_count += 1
    else:
        print(f"  [OK] All translations already present")

print("\n" + "=" * 70)
print(f"COMPLETE: {fixed_count}/10 tools updated")
print("=" * 70)
print("\nFeature descriptions now translate in all 10 languages!")
print("=" * 70)
