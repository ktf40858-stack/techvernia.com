#!/usr/bin/env python3
"""
Complete ALL missing Clearscope translations for batches 2 and 3
"""

import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
batch_dir = os.path.join(script_dir, 'GenuisNet.ai', 'pages', 'reviews', 'seo')

# Load English source
with open(os.path.join(batch_dir, 'clearscope-en.json'), 'r', encoding='utf-8') as f:
    en_source = json.load(f)

# Load existing batch1 (already completed)
with open(os.path.join(batch_dir, 'clearscope-batch1.json'), 'r', encoding='utf-8') as f:
    batch1 = json.load(f)

# Load batch2
with open(os.path.join(batch_dir, 'clearscope-batch2.json'), 'r', encoding='utf-8') as f:
    batch2 = json.load(f)

# Load batch3
with open(os.path.join(batch_dir, 'clearscope-batch3.json'), 'r', encoding='utf-8') as f:
    batch3 = json.load(f)

# Get the keys we need to add from batch1's ES translations
batch1_keys = set(batch1['es'].keys())
batch2_keys = set(batch2['pt'].keys())
batch3_keys = set(batch3['ko'].keys())

missing_in_batch2 = batch1_keys - batch2_keys
missing_in_batch3 = batch1_keys - batch3_keys

print(f'Missing keys in Batch 2: {len(missing_in_batch2)}')
print(f'Missing keys in Batch 3: {len(missing_in_batch3)}')

# Translations for Batch 2 (PT, ZH, JA) - from Batch 1 keys
batch2_translations = {}
for key in missing_in_batch2:
    if key == "review.common.try.it.now":
        batch2_translations[key] = {"pt": "Experimente Agora", "zh": "立即试用", "ja": "今すぐ試す"}
    elif key == "review.clearscope.request.demo":
        batch2_translations[key] = {"pt": "Solicitar Demo →", "zh": "申请演示 →", "ja": "デモをリクエスト →"}
    elif key == "review.clearscope.view.pricing":
        batch2_translations[key] = {"pt": "Ver Preços", "zh": "查看定价", "ja": "料金を見る"}
    elif key == "review.common.overview":
        batch2_translations[key] = {"pt": "Visão Geral", "zh": "概述", "ja": "概要"}
    elif key == "review.clearscope.clearscope.is.a.premium.ai-powered":
        batch2_translations[key] = {
            "pt": "Clearscope é uma plataforma premium de otimização de conteúdo impulsionada por IA projetada para ajudar criadores de conteúdo e profissionais de SEO a escrever artigos de alto ranking. Confiável por mais de 10.000 profissionais de marketing em empresas como Shopify, Deloitte e Condé Nast, o Clearscope simplifica o processo de criação de conteúdo otimizado para SEO, fornecendo recomendações baseadas em dados e classificação de conteúdo em tempo real.",
            "zh": "Clearscope是一个高级AI驱动的内容优化平台，旨在帮助内容创作者和SEO专业人士撰写高排名文章。受到Shopify、Deloitte和Condé Nast等公司超过10,000名营销人员的信任，Clearscope通过提供数据驱动的建议和实时内容评分，简化了创建SEO优化内容的过程。",
            "ja": "Clearscopeは、コンテンツクリエイターとSEO専門家が高ランキングの記事を書くのを支援するために設計されたプレミアムAI駆動のコンテンツ最適化プラットフォームです。Shopify、Deloitte、Condé Nastなどの企業の10,000人以上のマーケターから信頼されているClearscopeは、データ駆動の推奨事項とリアルタイムのコンテンツ評価を提供することで、SEO最適化されたコンテンツの作成プロセスを簡素化します。"
        }
    elif key == "review.clearscope.what.makes.clearscope.stand.out":
        batch2_translations[key] = {
            "pt": "O que faz o Clearscope se destacar é seu foco na simplicidade e na ação. Ao contrário de suítes SEO complexas com dezenas de recursos, o Clearscope faz uma coisa excepcionalmente bem: ajuda você a otimizar conteúdo para mecanismos de busca. A plataforma analisa as páginas com melhor classificação para suas palavras-chave alvo e fornece recomendações claras sobre termos a incluir, perguntas a responder e melhorias de legibilidade a fazer. A classificação de conteúdo proprietária fornece feedback instantâneo sobre quão bem seu conteúdo está otimizado.",
            "zh": "Clearscope的突出之处在于其对简单性和可操作性的关注。与具有数十种功能的复杂SEO套件不同，Clearscope在一件事上做得特别好：它帮助您优化搜索引擎的内容。该平台分析您目标关键词的顶级排名页面，并提供关于要包含的术语、要回答的问题和要进行的可读性改进的明确建议。专有的内容评分为您提供关于内容优化程度的即时反馈。",
            "ja": "Clearscopeを際立たせているのは、シンプルさと実行可能性への焦点です。何十もの機能を持つ複雑なSEOスイートとは異なり、Clearscopeは1つのことを非常にうまく行います：検索エンジン向けにコンテンツを最適化することです。このプラットフォームは、ターゲットキーワードの上位ランキングページを分析し、含めるべき用語、答えるべき質問、行うべき読みやすさの改善について明確な推奨事項を提供します。独自のコンテンツグレードは、コンテンツがどの程度最適化されているかについて即座にフィードバックを提供します。"
        }
    elif key == "review.clearscope.with.seamless.integrations.for.google":
        batch2_translations[key] = {
            "pt": "Com integrações perfeitas para Google Docs e WordPress, o Clearscope se encaixa naturalmente nos fluxos de trabalho de conteúdo existentes. A interface limpa da plataforma e as recomendações diretas a tornam acessível para escritores que não são especialistas em SEO, enquanto ainda fornece a profundidade que os profissionais experientes precisam. Para equipes de conteúdo sérias sobre crescimento orgânico, o Clearscope é uma ferramenta essencial.",
            "zh": "凭借与Google Docs和WordPress的无缝集成，Clearscope自然地融入现有的内容工作流程。该平台简洁的界面和直接的建议使其对非SEO专家的作者也易于使用，同时仍提供经验丰富的专业人士所需的深度。对于认真对待有机增长的内容团队来说，Clearscope是一个必不可少的工具。",
            "ja": "Google DocsとWordPressのシームレスな統合により、Clearscopeは既存のコンテンツワークフローに自然に適合します。プラットフォームのクリーンなインターフェースと分かりやすい推奨事項により、SEOの専門家でないライターにもアクセスしやすく、経験豊富な専門家が必要とする深さも提供します。オーガニック成長を真剣に考えているコンテンツチームにとって、Clearscopeは不可欠なツールです。"
        }
    elif key == "review.common.key.features":
        batch2_translations[key] = {"pt": "Recursos Principais", "zh": "主要功能", "ja": "主な機能"}
    elif key == "review.clearscope.get.a.real-time.content.grade":
        batch2_translations[key] = {
            "pt": "Obtenha uma classificação de conteúdo em tempo real (0-100) enquanto você escreve. Veja exatamente como seu conteúdo se compara às páginas com melhor classificação para sua palavra-chave alvo.",
            "zh": "在您写作时获得实时内容评分（0-100）。准确了解您的内容与目标关键词的顶级排名页面相比如何。",
            "ja": "執筆中にリアルタイムでコンテンツグレード（0-100）を取得します。ターゲットキーワードの上位ランキングページと比較して、コンテンツがどの程度かを正確に確認できます。"
        }
    elif key == "review.clearscope.discover.relevant.keywords.and.topics":
        batch2_translations[key] = {
            "pt": "Descubra palavras-chave e tópicos relevantes para incluir em seu conteúdo. Recomendações baseadas em dados sobre o que está classificando.",
            "zh": "发现要包含在您的内容中的相关关键词和主题。基于排名数据的数据驱动建议。",
            "ja": "コンテンツに含めるべき関連キーワードとトピックを発見します。ランキングに基づくデータ駆動の推奨事項。"
        }
    elif key == "review.clearscope.detailed.optimization.reports.showing.recommended":
        batch2_translations[key] = {
            "pt": "Relatórios de otimização detalhados mostrando termos, perguntas e tópicos recomendados. Orientação clara sobre o que incluir em seu conteúdo.",
            "zh": "详细的优化报告显示推荐的术语、问题和主题。关于在您的内容中包含什么的明确指导。",
            "ja": "推奨される用語、質問、トピックを示す詳細な最適化レポート。コンテンツに含めるべきものに関する明確なガイダンス。"
        }
    elif key == "review.clearscope.optimize.content.directly.in.google":
        batch2_translations[key] = {
            "pt": "Otimize conteúdo diretamente no Google Docs com a barra lateral do Clearscope. Escreva e otimize em um fluxo de trabalho perfeito.",
            "zh": "直接在Google Docs中使用Clearscope侧边栏优化内容。在一个无缝工作流程中写作和优化。",
            "ja": "Clearscopeサイドバーを使用してGoogle Docsで直接コンテンツを最適化します。シームレスなワークフローで執筆と最適化を行います。"
        }
    elif key == "review.clearscope.analyze.content.readability.with.flesch-kincaid":
        batch2_translations[key] = {
            "pt": "Analise a legibilidade do conteúdo com pontuações Flesch-Kincaid. Certifique-se de que seu conteúdo seja acessível ao seu público-alvo.",
            "zh": "使用Flesch-Kincaid分数分析内容可读性。确保您的内容对目标受众易于访问。",
            "ja": "Flesch-Kincaidスコアでコンテンツの読みやすさを分析します。ターゲットオーディエンスがアクセスしやすいコンテンツであることを確認します。"
        }
    elif key == "review.clearscope.see.what.top-ranking.pages.are":
        batch2_translations[key] = {
            "pt": "Veja o que as páginas com melhor classificação estão cobrindo. Identifique lacunas de conteúdo e oportunidades para criar conteúdo melhor.",
            "zh": "查看顶级排名页面正在涵盖的内容。识别内容空白和创建更好内容的机会。",
            "ja": "上位ランキングページがカバーしている内容を確認します。コンテンツのギャップとより良いコンテンツを作成する機会を特定します。"
        }
    elif key == "review.clearscope.track.how.your.content.performs":
        batch2_translations[key] = {
            "pt": "Acompanhe o desempenho do seu conteúdo ao longo do tempo. Receba alertas quando surgirem oportunidades de otimização ou as classificações mudarem.",
            "zh": "跟踪您的内容随时间的表现。当出现优化机会或排名变化时获得警报。",
            "ja": "時間の経過とともにコンテンツのパフォーマンスを追跡します。最適化の機会が生じたりランキングが変化したときにアラートを受け取ります。"
        }
    elif key == "review.clearscope.share.reports.with.team.members":
        batch2_translations[key] = {
            "pt": "Compartilhe relatórios com membros da equipe e clientes. Colabore na otimização de conteúdo com permissões e fluxos de trabalho integrados.",
            "zh": "与团队成员和客户共享报告。通过内置权限和工作流程在内容优化方面进行协作。",
            "ja": "チームメンバーやクライアントとレポートを共有します。組み込みの権限とワークフローでコンテンツ最適化について協力します。"
        }
    elif key == "review.clearscope.pros.cons":
        batch2_translations[key] = {"pt": "Prós e Contras", "zh": "优点和缺点", "ja": "長所と短所"}
    elif key == "review.clearscope.simple.intuitive.interface":
        batch2_translations[key] = {"pt": "Interface simples e intuitiva", "zh": "简单直观的界面", "ja": "シンプルで直感的なインターフェース"}
    elif key == "review.clearscope.highly.accurate.content.grading":
        batch2_translations[key] = {"pt": "Classificação de conteúdo altamente precisa", "zh": "高度准确的内容评分", "ja": "非常に正確なコンテンツグレーディング"}
    elif key == "review.clearscope.excellent.google.docs.integration":
        batch2_translations[key] = {"pt": "Excelente integração com Google Docs", "zh": "出色的Google Docs集成", "ja": "優れたGoogle Docs統合"}
    elif key == "review.clearscope.clear.actionable.recommendations":
        batch2_translations[key] = {"pt": "Recomendações claras e acionáveis", "zh": "清晰可操作的建议", "ja": "明確で実行可能な推奨事項"}
    elif key == "review.clearscope.fast.report.generation":
        batch2_translations[key] = {"pt": "Geração rápida de relatórios", "zh": "快速生成报告", "ja": "高速なレポート生成"}
    elif key == "review.clearscope.great.for.content.teams":
        batch2_translations[key] = {"pt": "Ótimo para equipes de conteúdo", "zh": "非常适合内容团队", "ja": "コンテンツチームに最適"}
    elif key == "review.clearscope.readability.analysis.included":
        batch2_translations[key] = {"pt": "Análise de legibilidade incluída", "zh": "包含可读性分析", "ja": "読みやすさ分析が含まれています"}
    elif key == "review.clearscope.regular.algorithm.updates":
        batch2_translations[key] = {"pt": "Atualizações regulares do algoritmo", "zh": "定期算法更新", "ja": "定期的なアルゴリズム更新"}
    elif key == "review.clearscope.outstanding.customer.support":
        batch2_translations[key] = {"pt": "Suporte ao cliente excepcional", "zh": "卓越的客户支持", "ja": "優れたカスタマーサポート"}

# Add translations to batch2
for key, translations in batch2_translations.items():
    for lang in ['pt', 'zh', 'ja']:
        if lang not in batch2:
            batch2[lang] = {}
        if key in translations:
            batch2[lang][key] = translations[lang]

# Now handle batch2 specific keys (from Batch 2 source) that need to be added to Batch 3
batch2_only_keys = batch2_keys - batch3_keys

# Translations for Batch 3 (KO, AR, HI) - ALL keys from source
all_translations_ko_ar_hi = {
    "review.common.try.it.now": {"ko": "지금 시도하기", "ar": "جربها الآن", "hi": "अभी आजमाएं"},
    "review.clearscope.request.demo": {"ko": "데모 요청 →", "ar": "طلب عرض توضيحي →", "hi": "डेमो का अनुरोध करें →"},
    "review.clearscope.view.pricing": {"ko": "가격 보기", "ar": "عرض الأسعار", "hi": "मूल्य निर्धारण देखें"},
    "review.common.overview": {"ko": "개요", "ar": "نظرة عامة", "hi": "अवलोकन"},
    "review.clearscope.clearscope.is.a.premium.ai-powered": {
        "ko": "Clearscope는 콘텐츠 크리에이터와 SEO 전문가가 높은 순위의 기사를 작성할 수 있도록 설계된 프리미엄 AI 기반 콘텐츠 최적화 플랫폼입니다. Shopify, Deloitte, Condé Nast와 같은 회사의 10,000명 이상의 마케터로부터 신뢰를 받고 있는 Clearscope는 데이터 기반 권장 사항과 실시간 콘텐츠 평가를 제공하여 SEO 최적화된 콘텐츠 생성 프로세스를 단순화합니다.",
        "ar": "Clearscope هي منصة تحسين محتوى متميزة مدعومة بالذكاء الاصطناعي مصممة لمساعدة منشئي المحتوى ومحترفي SEO على كتابة مقالات عالية التصنيف. موثوق بها من قبل أكثر من 10,000 مسوق في شركات مثل Shopify وDeloitte وCondé Nast، تعمل Clearscope على تبسيط عملية إنشاء محتوى محسّن لتحسين محركات البحث من خلال توفير توصيات مستندة إلى البيانات وتصنيف المحتوى في الوقت الفعلي.",
        "hi": "Clearscope एक प्रीमियम AI-संचालित सामग्री अनुकूलन प्लेटफ़ॉर्म है जो सामग्री निर्माताओं और SEO पेशेवरों को उच्च रैंकिंग वाले लेख लिखने में मदद करने के लिए डिज़ाइन किया गया है। Shopify, Deloitte और Condé Nast जैसी कंपनियों में 10,000 से अधिक विपणक द्वारा विश्वसनीय, Clearscope डेटा-संचालित सिफारिशें और वास्तविक समय सामग्री ग्रेडिंग प्रदान करके SEO-अनुकूलित सामग्री बनाने की प्रक्रिया को सरल बनाता है।"
    },
    "review.clearscope.what.makes.clearscope.stand.out": {
        "ko": "Clearscope를 돋보이게 하는 것은 단순성과 실행 가능성에 대한 초점입니다. 수십 가지 기능을 가진 복잡한 SEO 제품군과 달리, Clearscope는 한 가지를 특별히 잘합니다: 검색 엔진을 위한 콘텐츠 최적화를 돕습니다. 이 플랫폼은 대상 키워드에 대한 상위 순위 페이지를 분석하고 포함할 용어, 답변할 질문 및 수행할 가독성 개선에 대한 명확한 권장 사항을 제공합니다. 독점 콘텐츠 등급은 콘텐츠가 얼마나 잘 최적화되어 있는지에 대한 즉각적인 피드백을 제공합니다.",
        "ar": "ما يميز Clearscope هو تركيزه على البساطة والقابلية للتنفيذ. على عكس مجموعات SEO المعقدة التي تحتوي على عشرات الميزات، فإن Clearscope يقوم بشيء واحد بشكل استثنائي: يساعدك على تحسين المحتوى لمحركات البحث. تقوم المنصة بتحليل الصفحات الأعلى تصنيفًا لكلماتك الرئيسية المستهدفة وتوفر توصيات واضحة حول المصطلحات التي يجب تضمينها والأسئلة التي يجب الإجابة عليها وتحسينات القراءة التي يجب إجراؤها. تمنحك درجة المحتوى الخاصة ملاحظات فورية حول مدى جودة تحسين المحتوى الخاص بك.",
        "hi": "Clearscope को अलग बनाता है इसकी सरलता और कार्रवाई योग्यता पर ध्यान केंद्रित करना। दर्जनों सुविधाओं वाले जटिल SEO सूट के विपरीत, Clearscope एक चीज़ असाधारण रूप से अच्छी तरह से करता है: यह आपको खोज इंजनों के लिए सामग्री को अनुकूलित करने में मदद करता है। प्लेटफ़ॉर्म आपके लक्षित कीवर्ड के लिए शीर्ष-रैंकिंग पृष्ठों का विश्लेषण करता है और शामिल करने के लिए शब्द, उत्तर देने के लिए प्रश्न और करने के लिए पठनीयता सुधार पर स्पष्ट सिफारिशें प्रदान करता है। मालिकाना सामग्री ग्रेड आपको तुरंत प्रतिक्रिया देता है कि आपकी सामग्री कितनी अच्छी तरह अनुकूलित है।"
    },
    "review.clearscope.with.seamless.integrations.for.google": {
        "ko": "Google Docs 및 WordPress에 대한 원활한 통합으로 Clearscope는 기존 콘텐츠 워크플로에 자연스럽게 적합합니다. 플랫폼의 깨끗한 인터페이스와 간단한 권장 사항은 SEO 전문가가 아닌 작가도 액세스할 수 있게 하면서 경험 많은 전문가가 필요로 하는 깊이를 제공합니다. 유기적 성장을 진지하게 생각하는 콘텐츠 팀에게 Clearscope는 필수 도구입니다.",
        "ar": "مع التكاملات السلسة لـ Google Docs وWordPress، يتناسب Clearscope بشكل طبيعي مع سير عمل المحتوى الحالي. تجعل واجهة المنصة النظيفة والتوصيات المباشرة من السهل الوصول إليها للكتاب الذين ليسوا خبراء SEO، مع توفير العمق الذي يحتاجه المحترفون ذوو الخبرة. بالنسبة لفرق المحتوى الجادة في النمو العضوي، فإن Clearscope أداة أساسية.",
        "hi": "Google Docs और WordPress के लिए निर्बाध एकीकरण के साथ, Clearscope स्वाभाविक रूप से मौजूदा सामग्री वर्कफ़्लो में फिट बैठता है। प्लेटफ़ॉर्म का स्वच्छ इंटरफ़ेस और सीधी सिफारिशें इसे उन लेखकों के लिए सुलभ बनाती हैं जो SEO विशेषज्ञ नहीं हैं, जबकि अनुभवी पेशेवरों को आवश्यक गहराई प्रदान करते हैं। जैविक विकास के बारे में गंभीर सामग्री टीमों के लिए, Clearscope एक आवश्यक उपकरण है।"
    },
    "review.common.key.features": {"ko": "주요 기능", "ar": "الميزات الرئيسية", "hi": "मुख्य विशेषताएं"},
    "review.clearscope.get.a.real-time.content.grade": {
        "ko": "작성하는 동안 실시간 콘텐츠 등급(0-100)을 받으세요. 대상 키워드의 상위 순위 페이지와 비교하여 콘텐츠가 어떻게 비교되는지 정확히 확인하세요.",
        "ar": "احصل على درجة محتوى في الوقت الفعلي (0-100) أثناء الكتابة. اطلع على كيفية مقارنة المحتوى الخاص بك بالصفحات الأعلى تصنيفًا لكلمتك الرئيسية المستهدفة.",
        "hi": "जब आप लिखते हैं तो वास्तविक समय सामग्री ग्रेड (0-100) प्राप्त करें। अपने लक्षित कीवर्ड के लिए शीर्ष-रैंकिंग पृष्ठों की तुलना में आपकी सामग्री कैसी है, यह बिल्कुल देखें।"
    },
    "review.clearscope.discover.relevant.keywords.and.topics": {
        "ko": "콘텐츠에 포함할 관련 키워드 및 주제를 발견하세요. 순위에 기반한 데이터 기반 권장 사항.",
        "ar": "اكتشف الكلمات الرئيسية والموضوعات ذات الصلة لتضمينها في المحتوى الخاص بك. توصيات مستندة إلى البيانات بناءً على ما يتم تصنيفه.",
        "hi": "अपनी सामग्री में शामिल करने के लिए प्रासंगिक कीवर्ड और विषयों की खोज करें। रैंकिंग के आधार पर डेटा-संचालित सिफारिशें।"
    },
    "review.clearscope.detailed.optimization.reports.showing.recommended": {
        "ko": "권장 용어, 질문 및 주제를 보여주는 상세한 최적화 보고서. 콘텐츠에 포함할 내용에 대한 명확한 안내.",
        "ar": "تقارير تحسين مفصلة تظهر المصطلحات والأسئلة والموضوعات الموصى بها. إرشادات واضحة حول ما يجب تضمينه في المحتوى الخاص بك.",
        "hi": "अनुशंसित शब्द, प्रश्न और विषय दिखाने वाली विस्तृत अनुकूलन रिपोर्ट। आपकी सामग्री में क्या शामिल करना है इस पर स्पष्ट मार्गदर्शन।"
    },
    "review.clearscope.optimize.content.directly.in.google": {
        "ko": "Clearscope 사이드바를 사용하여 Google Docs에서 직접 콘텐츠를 최적화하세요. 하나의 원활한 워크플로에서 작성하고 최적화하세요.",
        "ar": "قم بتحسين المحتوى مباشرة في Google Docs باستخدام الشريط الجانبي Clearscope. اكتب وحسّن في سير عمل سلس واحد.",
        "hi": "Clearscope साइडबार के साथ सीधे Google Docs में सामग्री को अनुकूलित करें। एक निर्बाध वर्कफ़्लो में लिखें और अनुकूलित करें।"
    },
    "review.clearscope.analyze.content.readability.with.flesch-kincaid": {
        "ko": "Flesch-Kincaid 점수로 콘텐츠 가독성을 분석하세요. 콘텐츠가 대상 청중에게 접근 가능한지 확인하세요.",
        "ar": "حلل قابلية قراءة المحتوى باستخدام درجات Flesch-Kincaid. تأكد من أن المحتوى الخاص بك يمكن الوصول إليه لجمهورك المستهدف.",
        "hi": "Flesch-Kincaid स्कोर के साथ सामग्री पठनीयता का विश्लेषण करें। सुनिश्चित करें कि आपकी सामग्री आपके लक्षित दर्शकों के लिए सुलभ है।"
    },
    "review.clearscope.see.what.top-ranking.pages.are": {
        "ko": "상위 순위 페이지가 다루는 내용을 확인하세요. 콘텐츠 격차와 더 나은 콘텐츠를 만들 기회를 식별하세요.",
        "ar": "اطلع على ما تغطيه الصفحات الأعلى تصنيفًا. حدد فجوات المحتوى والفرص لإنشاء محتوى أفضل.",
        "hi": "देखें कि शीर्ष-रैंकिंग पृष्ठ क्या कवर कर रहे हैं। सामग्री अंतराल और बेहतर सामग्री बनाने के अवसरों की पहचान करें।"
    },
    "review.clearscope.track.how.your.content.performs": {
        "ko": "시간이 지남에 따라 콘텐츠의 성능을 추적하세요. 최적화 기회가 발생하거나 순위가 변경될 때 알림을 받으세요.",
        "ar": "تتبع أداء المحتوى الخاص بك مع مرور الوقت. احصل على تنبيهات عندما تنشأ فرص التحسين أو تتغير التصنيفات.",
        "hi": "समय के साथ अपनी सामग्री का प्रदर्शन ट्रैक करें। जब अनुकूलन के अवसर उत्पन्न होते हैं या रैंकिंग बदलती है तो अलर्ट प्राप्त करें।"
    },
    "review.clearscope.share.reports.with.team.members": {
        "ko": "팀 구성원 및 클라이언트와 보고서를 공유하세요. 내장된 권한 및 워크플로로 콘텐츠 최적화에 협력하세요.",
        "ar": "شارك التقارير مع أعضاء الفريق والعملاء. تعاون في تحسين المحتوى باستخدام الأذونات وسير العمل المدمجة.",
        "hi": "टीम के सदस्यों और क्लाइंट के साथ रिपोर्ट साझा करें। अंतर्निहित अनुमतियों और वर्कफ़्लो के साथ सामग्री अनुकूलन पर सहयोग करें।"
    },
    "review.clearscope.pros.cons": {"ko": "장점 및 단점", "ar": "الإيجابيات والسلبيات", "hi": "फायदे और नुकसान"},
    "review.clearscope.simple.intuitive.interface": {"ko": "단순하고 직관적인 인터페이스", "ar": "واجهة بسيطة وبديهية", "hi": "सरल, सहज इंटरफ़ेस"},
    "review.clearscope.highly.accurate.content.grading": {"ko": "매우 정확한 콘텐츠 평가", "ar": "تصنيف محتوى دقيق للغاية", "hi": "अत्यधिक सटीक सामग्री ग्रेडिंग"},
    "review.clearscope.excellent.google.docs.integration": {"ko": "우수한 Google Docs 통합", "ar": "تكامل ممتاز مع Google Docs", "hi": "उत्कृष्ट Google Docs एकीकरण"},
    "review.clearscope.clear.actionable.recommendations": {"ko": "명확하고 실행 가능한 권장 사항", "ar": "توصيات واضحة وقابلة للتنفيذ", "hi": "स्पष्ट, कार्रवाई योग्य सिफारिशें"},
    "review.clearscope.fast.report.generation": {"ko": "빠른 보고서 생성", "ar": "إنشاء تقارير سريع", "hi": "तेज़ रिपोर्ट निर्माण"},
    "review.clearscope.great.for.content.teams": {"ko": "콘텐츠 팀에 적합", "ar": "رائع لفرق المحتوى", "hi": "सामग्री टीमों के लिए बढ़िया"},
    "review.clearscope.readability.analysis.included": {"ko": "가독성 분석 포함", "ar": "تحليل القراءة مدرج", "hi": "पठनीयता विश्लेषण शामिल"},
    "review.clearscope.regular.algorithm.updates": {"ko": "정기적인 알고리즘 업데이트", "ar": "تحديثات الخوارزمية المنتظمة", "hi": "नियमित एल्गोरिदम अपडेट"},
    "review.clearscope.outstanding.customer.support": {"ko": "뛰어난 고객 지원", "ar": "دعم عملاء متميز", "hi": "उत्कृष्ट ग्राहक सहायता"},
    "review.clearscope.clean.distraction-free.workflow": {"ko": "깨끗하고 방해 없는 워크플로", "ar": "سير عمل نظيف وخالي من التشتيت", "hi": "स्वच्छ, व्यवधान-मुक्त वर्कफ़्लो"},
    "review.clearscope.premium.pricing.starts.at.170month": {"ko": "프리미엄 가격($170/월부터)", "ar": "تسعير متميز (يبدأ من $170/شهر)", "hi": "प्रीमियम मूल्य निर्धारण ($170/माह से शुरू)"},
    "review.clearscope.no.free.plan.or.trial": {"ko": "무료 플랜 또는 체험판 없음", "ar": "لا خطة مجانية أو تجربة", "hi": "कोई निःशुल्क योजना या परीक्षण नहीं"},
    "review.clearscope.limited.to.content.optimization": {"ko": "콘텐츠 최적화로 제한됨", "ar": "مقتصر على تحسين المحتوى", "hi": "सामग्री अनुकूलन तक सीमित"},
    "review.clearscope.no.backlink.or.technical.seo": {"ko": "백링크 또는 기술 SEO 기능 없음", "ar": "لا ميزات backlink أو SEO التقني", "hi": "कोई बैकलिंक या तकनीकी SEO सुविधाएं नहीं"},
    "review.clearscope.report.credits.can.run.out": {"ko": "보고서 크레딧이 빨리 소진될 수 있음", "ar": "يمكن أن تنفد أرصدة التقرير بسرعة", "hi": "रिपोर्ट क्रेडिट जल्दी खत्म हो सकते हैं"},
    "review.clearscope.learning.curve.for.interpreting.data": {"ko": "데이터 해석을 위한 학습 곡선", "ar": "منحنى تعلم لتفسير البيانات", "hi": "डेटा की व्याख्या के लिए सीखने की अवस्था"},
    "review.clearscope.limited.keyword.research.capabilities": {"ko": "제한된 키워드 조사 기능", "ar": "قدرات بحث محدودة عن الكلمات الرئيسية", "hi": "सीमित कीवर्ड अनुसंधान क्षमताएं"},
    "review.clearscope.no.built-in.content.writing": {"ko": "내장 콘텐츠 작성 기능 없음", "ar": "لا كتابة محتوى مدمجة", "hi": "कोई अंतर्निहित सामग्री लेखन नहीं"},
    "review.common.pricing.plans": {"ko": "가격 플랜", "ar": "خطط الأسعار", "hi": "मूल्य निर्धारण योजनाएं"},
    "review.clearscope.plan": {"ko": "플랜", "ar": "الخطة", "hi": "योजना"},
    "review.clearscope.price": {"ko": "가격", "ar": "السعر", "hi": "मूल्य"},
    "review.clearscope.credits": {"ko": "크레딧", "ar": "الأرصدة", "hi": "क्रेडिट"},
    "review.clearscope.key.features": {"ko": "주요 기능", "ar": "الميزات الرئيسية", "hi": "मुख्य विशेषताएं"},
    "review.clearscope.essentials": {"ko": "Essentials", "ar": "Essentials", "hi": "Essentials"},
    "review.clearscope.170month": {"ko": "$170/월", "ar": "$170/شهر", "hi": "$170/माह"},
    "review.clearscope.10.reports": {"ko": "약 10개 보고서", "ar": "~10 تقارير", "hi": "~10 रिपोर्ट"},
    "review.clearscope.1-3.users.google.docs.integration": {
        "ko": "1-3명 사용자, Google Docs 통합, 콘텐츠 모니터링, 무제한 최적화",
        "ar": "1-3 مستخدمين، تكامل Google Docs، مراقبة المحتوى، تحسينات غير محدودة",
        "hi": "1-3 उपयोगकर्ता, Google Docs एकीकरण, सामग्री निगरानी, असीमित अनुकूलन"
    },
    "review.clearscope.business": {"ko": "Business", "ar": "Business", "hi": "Business"},
    "review.clearscope.custom": {"ko": "맞춤형", "ar": "مخصص", "hi": "कस्टम"},
    "review.clearscope.3.users.api.access.bulk": {
        "ko": "3+ 사용자, API 액세스, 대량 업로드, 우선 지원, 맞춤형 교육",
        "ar": "3+ مستخدمين، الوصول إلى API، التحميلات الجماعية، الدعم ذو الأولوية، التدريب المخصص",
        "hi": "3+ उपयोगकर्ता, API एक्सेस, बल्क अपलोड, प्राथमिकता समर्थन, कस्टम प्रशिक्षण"
    },
    "review.clearscope.enterprise": {"ko": "Enterprise", "ar": "Enterprise", "hi": "Enterprise"},
    "review.clearscope.unlimited.users.dedicated.account.manager": {
        "ko": "무제한 사용자, 전담 계정 관리자, 맞춤형 통합, SLA",
        "ar": "مستخدمون غير محدودين، مدير حساب مخصص، تكاملات مخصصة، SLA",
        "hi": "असीमित उपयोगकर्ता, समर्पित खाता प्रबंधक, कस्टम एकीकरण, SLA"
    },
    "review.common.best.use.cases": {"ko": "최적 사용 사례", "ar": "أفضل حالات الاستخدام", "hi": "सर्वोत्तम उपयोग के मामले"},
    "review.clearscope.clearscope.excels.at": {"ko": "Clearscope가 뛰어난 분야:", "ar": "Clearscope يتفوق في:", "hi": "Clearscope में उत्कृष्टता:"},
    "review.clearscope.blog.content.optimization.perfect.for": {
        "ko": "블로그 콘텐츠 최적화: 검색 순위를 위한 블로그 게시물 및 기사 최적화에 완벽",
        "ar": "تحسين محتوى المدونة: مثالي لتحسين منشورات المدونة والمقالات لتصنيفات البحث",
        "hi": "ब्लॉग सामग्री अनुकूलन: खोज रैंकिंग के लिए ब्लॉग पोस्ट और लेख को अनुकूलित करने के लिए बिल्कुल सही"
    }
}

# Add all necessary translations to batch3
for key in en_source.keys():
    if key in all_translations_ko_ar_hi:
        for lang in ['ko', 'ar', 'hi']:
            if lang not in batch3:
                batch3[lang] = {}
            if key in all_translations_ko_ar_hi:
                batch3[lang][key] = all_translations_ko_ar_hi[key][lang]

# Save batch2
with open(os.path.join(batch_dir, 'clearscope-batch2.json'), 'w', encoding='utf-8') as f:
    json.dump(batch2, f, ensure_ascii=False, indent=2)

# Save batch3
with open(os.path.join(batch_dir, 'clearscope-batch3.json'), 'w', encoding='utf-8') as f:
    json.dump(batch3, f, ensure_ascii=False, indent=2)

print('Updated clearscope-batch2.json (PT, ZH, JA)')
print('Updated clearscope-batch3.json (KO, AR, HI)')
print('All batches completed!')
