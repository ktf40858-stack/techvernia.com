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

# Use case specific translations
use_case_translations = {
    "de": {
        # Section headers - tool specific
        "deepl-pro.excels.for": "DeepL Pro eignet sich hervorragend für:",
        "google-translate-ai.excels.for": "Google Translate AI eignet sich hervorragend für:",
        "lilt.excels.for": "Lilt eignet sich hervorragend für:",
        "lokalise.excels.for": "Lokalise eignet sich hervorragend für:",
        "microsoft-translator.excels.for": "Microsoft Translator eignet sich hervorragend für:",
        "modernmt.excels.for": "ModernMT eignet sich hervorragend für:",
        "phrase.excels.for": "Phrase eignet sich hervorragend für:",
        "smartling.excels.for": "Smartling eignet sich hervorragend für:",
        "systran.excels.for": "SYSTRAN eignet sich hervorragend für:",
        "unbabel.excels.for": "Unbabel eignet sich hervorragend für:",

        # Use case descriptions
        "enterprise.teams.large.organizations.requiring": "Enterprise-Teams: Große Organisationen, die skalierbare Übersetzungslösungen mit erweiterten Funktionen benötigen",
        "growing.startups.fast-moving.companies.that": "Wachsende Startups: Schnelllebige Unternehmen, die flexible KI-gestützte Automatisierung benötigen",
        "remote.teams.distributed.teams.requiring": "Remote-Teams: Verteilte Teams, die Echtzeit-Zusammenarbeit und Kommunikation benötigen",
        "data-driven.organizations.companies.leveraging.analytics": "Datengesteuerte Organisationen: Unternehmen, die Analysen für strategische Entscheidungen nutzen",
        "compliance-heavy.industries.regulated.sectors.requiring": "Compliance-intensive Branchen: Regulierte Sektoren, die Enterprise-Sicherheit und Compliance benötigen",

        # May not be ideal for
        "may.not.be.ideal.for": "Möglicherweise nicht ideal für:",
        "very.small.businesses.with.minimal": "Sehr kleine Unternehmen mit minimalen Übersetzungsbedürfnissen",
        "organizations.requiring.extensive.offline.functionality": "Organisationen, die umfangreiche Offline-Funktionalität benötigen",
        "teams.with.very.limited.technical": "Teams mit sehr begrenzter technischer Expertise",
    },
    "es": {
        # Section headers
        "deepl-pro.excels.for": "DeepL Pro Destaca Para:",
        "google-translate-ai.excels.for": "Google Translate AI Destaca Para:",
        "lilt.excels.for": "Lilt Destaca Para:",
        "lokalise.excels.for": "Lokalise Destaca Para:",
        "microsoft-translator.excels.for": "Microsoft Translator Destaca Para:",
        "modernmt.excels.for": "ModernMT Destaca Para:",
        "phrase.excels.for": "Phrase Destaca Para:",
        "smartling.excels.for": "Smartling Destaca Para:",
        "systran.excels.for": "SYSTRAN Destaca Para:",
        "unbabel.excels.for": "Unbabel Destaca Para:",

        # Use case descriptions
        "enterprise.teams.large.organizations.requiring": "Equipos Empresariales: Grandes organizaciones que requieren soluciones de traducción escalables con funciones avanzadas",
        "growing.startups.fast-moving.companies.that": "Startups en Crecimiento: Empresas ágiles que necesitan automatización impulsada por IA flexible",
        "remote.teams.distributed.teams.requiring": "Equipos Remotos: Equipos distribuidos que requieren colaboración y comunicación en tiempo real",
        "data-driven.organizations.companies.leveraging.analytics": "Organizaciones Orientadas a Datos: Empresas que aprovechan análisis para toma de decisiones estratégicas",
        "compliance-heavy.industries.regulated.sectors.requiring": "Industrias con Alta Compliance: Sectores regulados que requieren seguridad y cumplimiento de nivel empresarial",

        # May not be ideal for
        "may.not.be.ideal.for": "Puede No Ser Ideal Para:",
        "very.small.businesses.with.minimal": "Empresas muy pequeñas con necesidades mínimas de traducción",
        "organizations.requiring.extensive.offline.functionality": "Organizaciones que requieren funcionalidad offline extensa",
        "teams.with.very.limited.technical": "Equipos con experiencia técnica muy limitada",
    },
    "fr": {
        # Section headers
        "deepl-pro.excels.for": "DeepL Pro Excelle Pour:",
        "google-translate-ai.excels.for": "Google Translate AI Excelle Pour:",
        "lilt.excels.for": "Lilt Excelle Pour:",
        "lokalise.excels.for": "Lokalise Excelle Pour:",
        "microsoft-translator.excels.for": "Microsoft Translator Excelle Pour:",
        "modernmt.excels.for": "ModernMT Excelle Pour:",
        "phrase.excels.for": "Phrase Excelle Pour:",
        "smartling.excels.for": "Smartling Excelle Pour:",
        "systran.excels.for": "SYSTRAN Excelle Pour:",
        "unbabel.excels.for": "Unbabel Excelle Pour:",

        # Use case descriptions
        "enterprise.teams.large.organizations.requiring": "Équipes d'Entreprise: Grandes organisations nécessitant des solutions de traduction évolutives avec fonctionnalités avancées",
        "growing.startups.fast-moving.companies.that": "Startups en Croissance: Entreprises agiles nécessitant une automatisation IA flexible",
        "remote.teams.distributed.teams.requiring": "Équipes Distantes: Équipes distribuées nécessitant collaboration et communication en temps réel",
        "data-driven.organizations.companies.leveraging.analytics": "Organisations Axées sur les Données: Entreprises exploitant l'analyse pour la prise de décisions stratégiques",
        "compliance-heavy.industries.regulated.sectors.requiring": "Secteurs à Forte Conformité: Secteurs réglementés nécessitant sécurité et conformité de niveau entreprise",

        # May not be ideal for
        "may.not.be.ideal.for": "Peut Ne Pas Convenir Pour:",
        "very.small.businesses.with.minimal": "Très petites entreprises avec besoins minimaux en traduction",
        "organizations.requiring.extensive.offline.functionality": "Organisations nécessitant des fonctionnalités hors ligne étendues",
        "teams.with.very.limited.technical": "Équipes avec expertise technique très limitée",
    },
    "pt": {
        "enterprise.teams.large.organizations.requiring": "Equipes Empresariais: Grandes organizações que exigem soluções de tradução escaláveis com recursos avançados",
        "growing.startups.fast-moving.companies.that": "Startups em Crescimento: Empresas ágeis que precisam de automação flexível impulsionada por IA",
        "remote.teams.distributed.teams.requiring": "Equipes Remotas: Equipes distribuídas que exigem colaboração e comunicação em tempo real",
        "data-driven.organizations.companies.leveraging.analytics": "Organizações Orientadas por Dados: Empresas que aproveitam análises para tomada de decisões estratégicas",
        "compliance-heavy.industries.regulated.sectors.requiring": "Setores com Alta Conformidade: Setores regulamentados que exigem segurança e conformidade de nível empresarial",
        "may.not.be.ideal.for": "Pode Não Ser Ideal Para:",
        "very.small.businesses.with.minimal": "Empresas muito pequenas com necessidades mínimas de tradução",
        "organizations.requiring.extensive.offline.functionality": "Organizações que exigem funcionalidade offline extensa",
        "teams.with.very.limited.technical": "Equipes com experiência técnica muito limitada",
    },
    "zh": {
        "enterprise.teams.large.organizations.requiring": "企业团队：需要具有高级功能的可扩展翻译解决方案的大型组织",
        "growing.startups.fast-moving.companies.that": "成长型创业公司：需要灵活AI驱动自动化的快速发展公司",
        "remote.teams.distributed.teams.requiring": "远程团队：需要实时协作和沟通的分布式团队",
        "data-driven.organizations.companies.leveraging.analytics": "数据驱动型组织：利用分析进行战略决策的公司",
        "compliance-heavy.industries.regulated.sectors.requiring": "合规密集型行业：需要企业级安全和合规的受监管部门",
        "may.not.be.ideal.for": "可能不太适合：",
        "very.small.businesses.with.minimal": "翻译需求极少的非常小型企业",
        "organizations.requiring.extensive.offline.functionality": "需要广泛离线功能的组织",
        "teams.with.very.limited.technical": "技术专业知识非常有限的团队",
    },
    "ja": {
        "enterprise.teams.large.organizations.requiring": "エンタープライズチーム：高度な機能を備えたスケーラブルな翻訳ソリューションを必要とする大規模組織",
        "growing.startups.fast-moving.companies.that": "成長中のスタートアップ：柔軟なAI駆動の自動化が必要な急成長企業",
        "remote.teams.distributed.teams.requiring": "リモートチーム：リアルタイムのコラボレーションとコミュニケーションを必要とする分散チーム",
        "data-driven.organizations.companies.leveraging.analytics": "データ駆動型組織：戦略的意思決定のために分析を活用する企業",
        "compliance-heavy.industries.regulated.sectors.requiring": "コンプライアンス重視の業界：エンタープライズレベルのセキュリティとコンプライアンスが必要な規制セクター",
        "may.not.be.ideal.for": "適さない可能性：",
        "very.small.businesses.with.minimal": "翻訳ニーズが最小限の非常に小規模な企業",
        "organizations.requiring.extensive.offline.functionality": "広範なオフライン機能を必要とする組織",
        "teams.with.very.limited.technical": "技術的専門知識が非常に限られたチーム",
    },
    "ko": {
        "enterprise.teams.large.organizations.requiring": "엔터프라이즈 팀: 고급 기능을 갖춘 확장 가능한 번역 솔루션이 필요한 대규모 조직",
        "growing.startups.fast-moving.companies.that": "성장하는 스타트업: 유연한 AI 기반 자동화가 필요한 빠르게 움직이는 회사",
        "remote.teams.distributed.teams.requiring": "원격 팀: 실시간 협업 및 커뮤니케이션이 필요한 분산 팀",
        "data-driven.organizations.companies.leveraging.analytics": "데이터 중심 조직: 전략적 의사 결정을 위해 분석을 활용하는 회사",
        "compliance-heavy.industries.regulated.sectors.requiring": "규정 준수가 중요한 산업: 엔터프라이즈급 보안 및 규정 준수가 필요한 규제 부문",
        "may.not.be.ideal.for": "적합하지 않을 수 있음:",
        "very.small.businesses.with.minimal": "번역 요구 사항이 최소한인 매우 작은 비즈니스",
        "organizations.requiring.extensive.offline.functionality": "광범위한 오프라인 기능이 필요한 조직",
        "teams.with.very.limited.technical": "기술 전문 지식이 매우 제한적인 팀",
    },
    "ar": {
        "enterprise.teams.large.organizations.requiring": "فرق المؤسسات: المنظمات الكبيرة التي تحتاج إلى حلول ترجمة قابلة للتوسع مع ميزات متقدمة",
        "growing.startups.fast-moving.companies.that": "الشركات الناشئة المتنامية: الشركات سريعة الحركة التي تحتاج إلى أتمتة مرنة مدعومة بالذكاء الاصطناعي",
        "remote.teams.distributed.teams.requiring": "الفرق عن بُعد: الفرق الموزعة التي تحتاج إلى التعاون والتواصل في الوقت الفعلي",
        "data-driven.organizations.companies.leveraging.analytics": "المنظمات المدفوعة بالبيانات: الشركات التي تستفيد من التحليلات لاتخاذ القرارات الاستراتيجية",
        "compliance-heavy.industries.regulated.sectors.requiring": "الصناعات ذات الامتثال الكثيف: القطاعات الخاضعة للرقابة والتي تتطلب أمانًا وامتثالًا على مستوى المؤسسات",
        "may.not.be.ideal.for": "قد لا يكون مثاليًا لـ:",
        "very.small.businesses.with.minimal": "الشركات الصغيرة جدًا ذات الاحتياجات الضئيلة للترجمة",
        "organizations.requiring.extensive.offline.functionality": "المنظمات التي تحتاج إلى وظائف واسعة دون اتصال بالإنترنت",
        "teams.with.very.limited.technical": "الفرق ذات الخبرة التقنية المحدودة جدًا",
    },
    "hi": {
        "enterprise.teams.large.organizations.requiring": "एंटरप्राइज़ टीमें: उन्नत सुविधाओं के साथ स्केलेबल अनुवाद समाधान की आवश्यकता वाले बड़े संगठन",
        "growing.startups.fast-moving.companies.that": "बढ़ते स्टार्टअप: लचीले AI-संचालित स्वचालन की आवश्यकता वाली तेज़ गति वाली कंपनियां",
        "remote.teams.distributed.teams.requiring": "रिमोट टीमें: रियल-टाइम सहयोग और संचार की आवश्यकता वाली वितरित टीमें",
        "data-driven.organizations.companies.leveraging.analytics": "डेटा-संचालित संगठन: रणनीतिक निर्णय लेने के लिए विश्लेषण का लाभ उठाने वाली कंपनियां",
        "compliance-heavy.industries.regulated.sectors.requiring": "अनुपालन-भारी उद्योग: एंटरप्राइज़-ग्रेड सुरक्षा और अनुपालन की आवश्यकता वाले विनियमित क्षेत्र",
        "may.not.be.ideal.for": "आदर्श नहीं हो सकता:",
        "very.small.businesses.with.minimal": "न्यूनतम अनुवाद आवश्यकताओं वाले बहुत छोटे व्यवसाय",
        "organizations.requiring.extensive.offline.functionality": "व्यापक ऑफ़लाइन कार्यक्षमता की आवश्यकता वाले संगठन",
        "teams.with.very.limited.technical": "बहुत सीमित तकनीकी विशेषज्ञता वाली टीमें",
    }
}

def add_use_case_translations(tool_key, tool_name):
    """Add use case specific translations"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        return False

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    modified = False

    for lang, translations in use_case_translations.items():
        for key_suffix, translation in translations.items():
            # Build the full key
            full_key = f"review.{tool_key}.{key_suffix}"

            # Check if this translation already exists correctly
            search_pattern = rf'"{re.escape(full_key)}":\s*"[^"]*"'
            if re.search(search_pattern, content):
                # Key exists, check if value needs updating
                # Replace with correct translation
                replacement = f'"{full_key}": "{translation}"'
                old_pattern = rf'"{re.escape(full_key)}":\s*"[^"]*"'
                content, count = re.subn(old_pattern, replacement, content)
                if count > 0:
                    modified = True
            else:
                # Key doesn't exist, we need to add it
                # Find the language section and add the key
                lang_pattern = rf'  "{lang}":\s*{{\n'
                match = re.search(lang_pattern, content)

                if match:
                    insert_pos = match.end()
                    new_line = f'    "{full_key}": "{translation}",\n'
                    content = content[:insert_pos] + new_line + content[insert_pos:]
                    modified = True

    if modified and content != original_content:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

print("=" * 70)
print("TRANSLATING USE CASE SECTIONS")
print("=" * 70)

fixed_count = 0

for tool_key, tool_name in translation_tools.items():
    print(f"\n{tool_name}:")
    if add_use_case_translations(tool_key, tool_name):
        print(f"  [+] Use case translations added/updated")
        fixed_count += 1
    else:
        print(f"  [OK] Already complete")

print("\n" + "=" * 70)
print(f"COMPLETE: {fixed_count}/10 tools updated")
print("=" * 70)
print("\nUse case sections now fully translated!")
print("=" * 70)
