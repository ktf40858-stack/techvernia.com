#!/usr/bin/env python3
"""
Script pour ajouter les descriptions .full pour les 7 langues restantes
"""

def add_full_reviews_remaining():
    """Ajoute les descriptions complètes (.full) pour DE, PT, ZH, JA, KO, AR, HI"""

    file_path = "GenuisNet.ai/js/i18n.js"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # === SECTION ALLEMANDE (DE) ===
    de_marker = '"cat.cybersecurity.full": "Darktrace, CrowdStrike, SentinelOne und weitere KI-gestützte Sicherheits-Tools.",'

    if de_marker in content:
        de_full_additions = '''
        "cat.architecture.full": "ArchiCAD AI, Hypar, Spacemaker und weitere Architekturdesign-Tools.",
        "cat.medical.full": "IBM Watson Health, PathAI, Tempus und weitere KI-Lösungen für das Gesundheitswesen.",
        "cat.analytics.full": "Tableau AI, Power BI Copilot, ThoughtSpot und weitere Business Intelligence Tools.",
        "cat.legal.full": "LexisNexis AI, Casetext, Harvey AI und weitere juristische Recherche-Tools.",
        "cat.customer-service.full": "Zendesk AI, Intercom, Ada und weitere Kundensupport-Automatisierungstools.",
        "cat.education.full": "Khan Academy AI, Duolingo Max, Coursera Coach und weitere Lernplattformen.",
        "cat.sales.full": "Gong, Clari, Salesforce Einstein und weitere Vertriebs-Tools.",
        "cat.research.full": "Elicit, Consensus, Scholarcy und weitere akademische Forschungstools.",
        "cat.hr.full": "HireVue, Pymetrics, Eightfold AI und weitere HR-Automatisierungstools.",
        "cat.translation.full": "DeepL, Google Translate AI, Unbabel und weitere Übersetzungstools.",
        "cat.gaming.full": "Inworld AI, Scenario, Charisma AI und weitere Spieleentwicklungstools.",
        "cat.quantum.full": "Zapata Computing, Xanadu, IBM Quantum und weitere Quantum-ML-Plattformen.",'''

        content = content.replace(de_marker, de_marker + de_full_additions)
        print("✅ Ajouté: 12 descriptions .full (DE)")

    # === SECTION PORTUGAISE (PT) ===
    pt_marker = '"cat.cybersecurity.full": "Darktrace, CrowdStrike, SentinelOne e mais ferramentas de segurança alimentadas por IA.",'

    if pt_marker in content:
        pt_full_additions = '''
        "cat.architecture.full": "ArchiCAD AI, Hypar, Spacemaker e mais ferramentas de design arquitetônico.",
        "cat.medical.full": "IBM Watson Health, PathAI, Tempus e mais soluções de IA para saúde.",
        "cat.analytics.full": "Tableau AI, Power BI Copilot, ThoughtSpot e mais ferramentas de inteligência empresarial.",
        "cat.legal.full": "LexisNexis AI, Casetext, Harvey AI e mais ferramentas de pesquisa jurídica.",
        "cat.customer-service.full": "Zendesk AI, Intercom, Ada e mais ferramentas de automação de suporte.",
        "cat.education.full": "Khan Academy AI, Duolingo Max, Coursera Coach e mais plataformas de aprendizagem.",
        "cat.sales.full": "Gong, Clari, Salesforce Einstein e mais ferramentas de vendas.",
        "cat.research.full": "Elicit, Consensus, Scholarcy e mais ferramentas de pesquisa acadêmica.",
        "cat.hr.full": "HireVue, Pymetrics, Eightfold AI e mais ferramentas de automação de RH.",
        "cat.translation.full": "DeepL, Google Translate AI, Unbabel e mais ferramentas de tradução.",
        "cat.gaming.full": "Inworld AI, Scenario, Charisma AI e mais ferramentas de desenvolvimento de jogos.",
        "cat.quantum.full": "Zapata Computing, Xanadu, IBM Quantum e mais plataformas de ML quântico.",'''

        content = content.replace(pt_marker, pt_marker + pt_full_additions)
        print("✅ Ajouté: 12 descriptions .full (PT)")

    # === SECTION CHINOISE (ZH) ===
    zh_marker = '"cat.cybersecurity.full": "Darktrace、CrowdStrike、SentinelOne等AI驱动的安全工具。",'

    if zh_marker in content:
        zh_full_additions = '''
        "cat.architecture.full": "ArchiCAD AI、Hypar、Spacemaker 等建筑设计工具。",
        "cat.medical.full": "IBM Watson Health、PathAI、Tempus 等医疗 AI 解决方案。",
        "cat.analytics.full": "Tableau AI、Power BI Copilot、ThoughtSpot 等商业智能工具。",
        "cat.legal.full": "LexisNexis AI、Casetext、Harvey AI 等法律研究工具。",
        "cat.customer-service.full": "Zendesk AI、Intercom、Ada 等客户支持自动化工具。",
        "cat.education.full": "Khan Academy AI、Duolingo Max、Coursera Coach 等学习平台。",
        "cat.sales.full": "Gong、Clari、Salesforce Einstein 等销售工具。",
        "cat.research.full": "Elicit、Consensus、Scholarcy 等学术研究工具。",
        "cat.hr.full": "HireVue、Pymetrics、Eightfold AI 等人力资源自动化工具。",
        "cat.translation.full": "DeepL、Google Translate AI、Unbabel 等翻译工具。",
        "cat.gaming.full": "Inworld AI、Scenario、Charisma AI 等游戏开发工具。",
        "cat.quantum.full": "Zapata Computing、Xanadu、IBM Quantum 等量子机器学习平台。",'''

        content = content.replace(zh_marker, zh_marker + zh_full_additions)
        print("✅ Ajouté: 12 descriptions .full (ZH)")

    # === SECTION JAPONAISE (JA) ===
    ja_marker = '"cat.cybersecurity.full": "Darktrace、CrowdStrike、SentinelOneなどのAI搭載セキュリティツール。",'

    if ja_marker in content:
        ja_full_additions = '''
        "cat.architecture.full": "ArchiCAD AI、Hypar、Spacemaker などの建築設計ツール。",
        "cat.medical.full": "IBM Watson Health、PathAI、Tempus などの医療 AI ソリューション。",
        "cat.analytics.full": "Tableau AI、Power BI Copilot、ThoughtSpot などのビジネスインテリジェンスツール。",
        "cat.legal.full": "LexisNexis AI、Casetext、Harvey AI などの法律調査ツール。",
        "cat.customer-service.full": "Zendesk AI、Intercom、Ada などのカスタマーサポート自動化ツール。",
        "cat.education.full": "Khan Academy AI、Duolingo Max、Coursera Coach などの学習プラットフォーム。",
        "cat.sales.full": "Gong、Clari、Salesforce Einstein などの営業ツール。",
        "cat.research.full": "Elicit、Consensus、Scholarcy などの学術研究ツール。",
        "cat.hr.full": "HireVue、Pymetrics、Eightfold AI などの人事自動化ツール。",
        "cat.translation.full": "DeepL、Google Translate AI、Unbabel などの翻訳ツール。",
        "cat.gaming.full": "Inworld AI、Scenario、Charisma AI などのゲーム開発ツール。",
        "cat.quantum.full": "Zapata Computing、Xanadu、IBM Quantum などの量子機械学習プラットフォーム。",'''

        content = content.replace(ja_marker, ja_marker + ja_full_additions)
        print("✅ Ajouté: 12 descriptions .full (JA)")

    # === SECTION CORÉENNE (KO) ===
    ko_marker = '"cat.cybersecurity.full": "Darktrace, CrowdStrike, SentinelOne 등 AI 기반 보안 도구.",'

    if ko_marker in content:
        ko_full_additions = '''
        "cat.architecture.full": "ArchiCAD AI, Hypar, Spacemaker 등의 건축 설계 도구.",
        "cat.medical.full": "IBM Watson Health, PathAI, Tempus 등의 의료 AI 솔루션.",
        "cat.analytics.full": "Tableau AI, Power BI Copilot, ThoughtSpot 등의 비즈니스 인텔리전스 도구.",
        "cat.legal.full": "LexisNexis AI, Casetext, Harvey AI 등의 법률 조사 도구.",
        "cat.customer-service.full": "Zendesk AI, Intercom, Ada 등의 고객 지원 자동화 도구.",
        "cat.education.full": "Khan Academy AI, Duolingo Max, Coursera Coach 등의 학습 플랫폼.",
        "cat.sales.full": "Gong, Clari, Salesforce Einstein 등의 영업 도구.",
        "cat.research.full": "Elicit, Consensus, Scholarcy 등의 학술 연구 도구.",
        "cat.hr.full": "HireVue, Pymetrics, Eightfold AI 등의 인사 자동화 도구.",
        "cat.translation.full": "DeepL, Google Translate AI, Unbabel 등의 번역 도구.",
        "cat.gaming.full": "Inworld AI, Scenario, Charisma AI 등의 게임 개발 도구.",
        "cat.quantum.full": "Zapata Computing, Xanadu, IBM Quantum 등의 양자 머신러닝 플랫폼.",'''

        content = content.replace(ko_marker, ko_marker + ko_full_additions)
        print("✅ Ajouté: 12 descriptions .full (KO)")

    # === SECTION ARABE (AR) ===
    ar_marker = '"cat.cybersecurity.full": "Darktrace وCrowdStrike وSentinelOne وأدوات الأمان المدعومة بالذكاء الاصطناعي.",'

    if ar_marker in content:
        ar_full_additions = '''
        "cat.architecture.full": "ArchiCAD AI وHypar وSpacemaker والمزيد من أدوات التصميم المعماري.",
        "cat.medical.full": "IBM Watson Health وPathAI وTempus والمزيد من حلول الذكاء الاصطناعي الطبية.",
        "cat.analytics.full": "Tableau AI وPower BI Copilot وThoughtSpot والمزيد من أدوات ذكاء الأعمال.",
        "cat.legal.full": "LexisNexis AI وCasetext وHarvey AI والمزيد من أدوات البحث القانوني.",
        "cat.customer-service.full": "Zendesk AI وIntercom وAda والمزيد من أدوات أتمتة دعم العملاء.",
        "cat.education.full": "Khan Academy AI وDuolingo Max وCoursera Coach والمزيد من منصات التعلم.",
        "cat.sales.full": "Gong وClari وSalesforce Einstein والمزيد من أدوات المبيعات.",
        "cat.research.full": "Elicit وConsensus وScholarcy والمزيد من أدوات البحث الأكاديمي.",
        "cat.hr.full": "HireVue وPymetrics وEightfold AI والمزيد من أدوات أتمتة الموارد البشرية.",
        "cat.translation.full": "DeepL وGoogle Translate AI وUnbabel والمزيد من أدوات الترجمة.",
        "cat.gaming.full": "Inworld AI وScenario وCharisma AI والمزيد من أدوات تطوير الألعاب.",
        "cat.quantum.full": "Zapata Computing وXanadu وIBM Quantum والمزيد من منصات التعلم الآلي الكمي.",'''

        content = content.replace(ar_marker, ar_marker + ar_full_additions)
        print("✅ Ajouté: 12 descriptions .full (AR)")

    # === SECTION HINDI (HI) ===
    hi_marker = '"cat.cybersecurity.full": "Darktrace, CrowdStrike, SentinelOne और अन्य AI-संचालित सुरक्षा टूल्स।",'

    if hi_marker in content:
        hi_full_additions = '''
        "cat.architecture.full": "ArchiCAD AI, Hypar, Spacemaker और अधिक वास्तुकला डिज़ाइन उपकरण।",
        "cat.medical.full": "IBM Watson Health, PathAI, Tempus और अधिक स्वास्थ्य देखभाल AI समाधान।",
        "cat.analytics.full": "Tableau AI, Power BI Copilot, ThoughtSpot और अधिक व्यावसायिक खुफिया उपकरण।",
        "cat.legal.full": "LexisNexis AI, Casetext, Harvey AI और अधिक कानूनी अनुसंधान उपकरण।",
        "cat.customer-service.full": "Zendesk AI, Intercom, Ada और अधिक ग्राहक सहायता स्वचालन उपकरण।",
        "cat.education.full": "Khan Academy AI, Duolingo Max, Coursera Coach और अधिक शिक्षण प्लेटफॉर्म।",
        "cat.sales.full": "Gong, Clari, Salesforce Einstein और अधिक बिक्री उपकरण।",
        "cat.research.full": "Elicit, Consensus, Scholarcy और अधिक शैक्षणिक अनुसंधान उपकरण।",
        "cat.hr.full": "HireVue, Pymetrics, Eightfold AI और अधिक HR स्वचालन उपकरण।",
        "cat.translation.full": "DeepL, Google Translate AI, Unbabel और अधिक अनुवाद उपकरण।",
        "cat.gaming.full": "Inworld AI, Scenario, Charisma AI और अधिक गेम विकास उपकरण।",
        "cat.quantum.full": "Zapata Computing, Xanadu, IBM Quantum और अधिक क्वांटम ML प्लेटफॉर्म।",'''

        content = content.replace(hi_marker, hi_marker + hi_full_additions)
        print("✅ Ajouté: 12 descriptions .full (HI)")

    # Écrire les modifications
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print("\n✅ Toutes les descriptions complètes pour les 7 langues restantes ont été ajoutées!")
        print("📊 Total: 12 catégories × 7 langues = 84 nouvelles traductions")
        print("📊 Grand total: 12 catégories × 10 langues = 120 traductions .full ajoutées")
    else:
        print("\nℹ️  Aucune modification nécessaire")

if __name__ == "__main__":
    add_full_reviews_remaining()
