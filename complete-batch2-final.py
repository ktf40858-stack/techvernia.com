#!/usr/bin/env python3
"""
Complete Batch 2 translations (PT, ZH, JA) with ALL missing keys
"""

import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
batch_dir = os.path.join(script_dir, 'GenuisNet.ai', 'pages', 'reviews', 'seo')

# Load batch2
with open(os.path.join(batch_dir, 'clearscope-batch2.json'), 'r', encoding='utf-8') as f:
    batch2 = json.load(f)

# All missing translations for batch2 (the ones from batch1 and batch3 that are missing)
missing_batch2 = {
    "review.common.try.it.now": {
        "pt": "Experimente Agora",
        "zh": "立即试用",
        "ja": "今すぐ試す"
    },
    "review.clearscope.request.demo": {
        "pt": "Solicitar Demo →",
        "zh": "申请演示 →",
        "ja": "デモをリクエスト →"
    },
    "review.clearscope.view.pricing": {
        "pt": "Ver Preços",
        "zh": "查看定价",
        "ja": "料金を見る"
    },
    "review.common.overview": {
        "pt": "Visão Geral",
        "zh": "概述",
        "ja": "概要"
    },
    "review.clearscope.clearscope.is.a.premium.ai-powered": {
        "pt": "Clearscope é uma plataforma premium de otimização de conteúdo impulsionada por IA projetada para ajudar criadores de conteúdo e profissionais de SEO a escrever artigos de alto ranking. Confiável por mais de 10.000 profissionais de marketing em empresas como Shopify, Deloitte e Condé Nast, o Clearscope simplifica o processo de criação de conteúdo otimizado para SEO, fornecendo recomendações baseadas em dados e classificação de conteúdo em tempo real.",
        "zh": "Clearscope是一个高级AI驱动的内容优化平台，旨在帮助内容创作者和SEO专业人士撰写高排名文章。受到Shopify、Deloitte和Condé Nast等公司超过10,000名营销人员的信任，Clearscope通过提供数据驱动的建议和实时内容评分，简化了创建SEO优化内容的过程。",
        "ja": "Clearscopeは、コンテンツクリエイターとSEO専門家が高ランキングの記事を書くのを支援するために設計されたプレミアムAI駆動のコンテンツ最適化プラットフォームです。Shopify、Deloitte、Condé Nastなどの企業の10,000人以上のマーケターから信頼されているClearscopeは、データ駆動の推奨事項とリアルタイムのコンテンツ評価を提供することで、SEO最適化されたコンテンツの作成プロセスを簡素化します。"
    },
    "review.clearscope.what.makes.clearscope.stand.out": {
        "pt": "O que faz o Clearscope se destacar é seu foco na simplicidade e na ação. Ao contrário de suítes SEO complexas com dezenas de recursos, o Clearscope faz uma coisa excepcionalmente bem: ajuda você a otimizar conteúdo para mecanismos de busca. A plataforma analisa as páginas com melhor classificação para suas palavras-chave alvo e fornece recomendações claras sobre termos a incluir, perguntas a responder e melhorias de legibilidade a fazer. A classificação de conteúdo proprietária fornece feedback instantâneo sobre quão bem seu conteúdo está otimizado.",
        "zh": "Clearscope的突出之处在于其对简单性和可操作性的关注。与具有数十种功能的复杂SEO套件不同，Clearscope在一件事上做得特别好：它帮助您优化搜索引擎的内容。该平台分析您目标关键词的顶级排名页面，并提供关于要包含的术语、要回答的问题和要进行的可读性改进的明确建议。专有的内容评分为您提供关于内容优化程度的即时反馈。",
        "ja": "Clearscopeを際立たせているのは、シンプルさと実行可能性への焦点です。何十もの機能を持つ複雑なSEOスイートとは異なり、Clearscopeは1つのことを非常にうまく行います：検索エンジン向けにコンテンツを最適化することです。このプラットフォームは、ターゲットキーワードの上位ランキングページを分析し、含めるべき用語、答えるべき質問、行うべき読みやすさの改善について明確な推奨事項を提供します。独自のコンテンツグレードは、コンテンツがどの程度最適化されているかについて即座にフィードバックを提供します。"
    },
    "review.clearscope.with.seamless.integrations.for.google": {
        "pt": "Com integrações perfeitas para Google Docs e WordPress, o Clearscope se encaixa naturalmente nos fluxos de trabalho de conteúdo existentes. A interface limpa da plataforma e as recomendações diretas a tornam acessível para escritores que não são especialistas em SEO, enquanto ainda fornece a profundidade que os profissionais experientes precisam. Para equipes de conteúdo sérias sobre crescimento orgânico, o Clearscope é uma ferramenta essencial.",
        "zh": "凭借与Google Docs和WordPress的无缝集成，Clearscope自然地融入现有的内容工作流程。该平台简洁的界面和直接的建议使其对非SEO专家的作者也易于使用，同时仍提供经验丰富的专业人士所需的深度。对于认真对待有机增长的内容团队来说，Clearscope是一个必不可少的工具。",
        "ja": "Google DocsとWordPressのシームレスな統合により、Clearscopeは既存のコンテンツワークフローに自然に適合します。プラットフォームのクリーンなインターフェースと分かりやすい推奨事項により、SEOの専門家でないライターにもアクセスしやすく、経験豊富な専門家が必要とする深さも提供します。オーガニック成長を真剣に考えているコンテンツチームにとって、Clearscopeは不可欠なツールです。"
    },
    "review.common.key.features": {
        "pt": "Recursos Principais",
        "zh": "主要功能",
        "ja": "主な機能"
    },
    "review.clearscope.get.a.real-time.content.grade": {
        "pt": "Obtenha uma classificação de conteúdo em tempo real (0-100) enquanto você escreve. Veja exatamente como seu conteúdo se compara às páginas com melhor classificação para sua palavra-chave alvo.",
        "zh": "在您写作时获得实时内容评分（0-100）。准确了解您的内容与目标关键词的顶级排名页面相比如何。",
        "ja": "執筆中にリアルタイムでコンテンツグレード（0-100）を取得します。ターゲットキーワードの上位ランキングページと比較して、コンテンツがどの程度かを正確に確認できます。"
    },
    "review.clearscope.discover.relevant.keywords.and.topics": {
        "pt": "Descubra palavras-chave e tópicos relevantes para incluir em seu conteúdo. Recomendações baseadas em dados sobre o que está classificando.",
        "zh": "发现要包含在您的内容中的相关关键词和主题。基于排名数据的数据驱动建议。",
        "ja": "コンテンツに含めるべき関連キーワードとトピックを発見します。ランキングに基づくデータ駆動の推奨事項。"
    },
    "review.clearscope.detailed.optimization.reports.showing.recommended": {
        "pt": "Relatórios de otimização detalhados mostrando termos, perguntas e tópicos recomendados. Orientação clara sobre o que incluir em seu conteúdo.",
        "zh": "详细的优化报告显示推荐的术语、问题和主题。关于在您的内容中包含什么的明确指导。",
        "ja": "推奨される用語、質問、トピックを示す詳細な最適化レポート。コンテンツに含めるべきものに関する明確なガイダンス。"
    },
    "review.clearscope.optimize.content.directly.in.google": {
        "pt": "Otimize conteúdo diretamente no Google Docs com a barra lateral do Clearscope. Escreva e otimize em um fluxo de trabalho perfeito.",
        "zh": "直接在Google Docs中使用Clearscope侧边栏优化内容。在一个无缝工作流程中写作和优化。",
        "ja": "Clearscopeサイドバーを使用してGoogle Docsで直接コンテンツを最適化します。シームレスなワークフローで執筆と最適化を行います。"
    },
    "review.clearscope.analyze.content.readability.with.flesch-kincaid": {
        "pt": "Analise a legibilidade do conteúdo com pontuações Flesch-Kincaid. Certifique-se de que seu conteúdo seja acessível ao seu público-alvo.",
        "zh": "使用Flesch-Kincaid分数分析内容可读性。确保您的内容对目标受众易于访问。",
        "ja": "Flesch-Kincaidスコアでコンテンツの読みやすさを分析します。ターゲットオーディエンスがアクセスしやすいコンテンツであることを確認します。"
    },
    "review.clearscope.see.what.top-ranking.pages.are": {
        "pt": "Veja o que as páginas com melhor classificação estão cobrindo. Identifique lacunas de conteúdo e oportunidades para criar conteúdo melhor.",
        "zh": "查看顶级排名页面正在涵盖的内容。识别内容空白和创建更好内容的机会。",
        "ja": "上位ランキングページがカバーしている内容を確認します。コンテンツのギャップとより良いコンテンツを作成する機会を特定します。"
    },
    "review.clearscope.track.how.your.content.performs": {
        "pt": "Acompanhe o desempenho do seu conteúdo ao longo do tempo. Receba alertas quando surgirem oportunidades de otimização ou as classificações mudarem.",
        "zh": "跟踪您的内容随时间的表现。当出现优化机会或排名变化时获得警报。",
        "ja": "時間の経過とともにコンテンツのパフォーマンスを追跡します。最適化の機会が生じたりランキングが変化したときにアラートを受け取ります。"
    },
    "review.clearscope.share.reports.with.team.members": {
        "pt": "Compartilhe relatórios com membros da equipe e clientes. Colabore na otimização de conteúdo com permissões e fluxos de trabalho integrados.",
        "zh": "与团队成员和客户共享报告。通过内置权限和工作流程在内容优化方面进行协作。",
        "ja": "チームメンバーやクライアントとレポートを共有します。組み込みの権限とワークフローでコンテンツ最適化について協力します。"
    },
    "review.clearscope.pros.cons": {
        "pt": "Prós e Contras",
        "zh": "优点和缺点",
        "ja": "長所と短所"
    },
    "review.clearscope.simple.intuitive.interface": {
        "pt": "Interface simples e intuitiva",
        "zh": "简单直观的界面",
        "ja": "シンプルで直感的なインターフェース"
    },
    "review.clearscope.highly.accurate.content.grading": {
        "pt": "Classificação de conteúdo altamente precisa",
        "zh": "高度准确的内容评分",
        "ja": "非常に正確なコンテンツグレーディング"
    },
    "review.clearscope.excellent.google.docs.integration": {
        "pt": "Excelente integração com Google Docs",
        "zh": "出色的Google Docs集成",
        "ja": "優れたGoogle Docs統合"
    },
    "review.clearscope.clear.actionable.recommendations": {
        "pt": "Recomendações claras e acionáveis",
        "zh": "清晰可操作的建议",
        "ja": "明確で実行可能な推奨事項"
    },
    "review.clearscope.fast.report.generation": {
        "pt": "Geração rápida de relatórios",
        "zh": "快速生成报告",
        "ja": "高速なレポート生成"
    },
    "review.clearscope.great.for.content.teams": {
        "pt": "Ótimo para equipes de conteúdo",
        "zh": "非常适合内容团队",
        "ja": "コンテンツチームに最適"
    },
    "review.clearscope.readability.analysis.included": {
        "pt": "Análise de legibilidade incluída",
        "zh": "包含可读性分析",
        "ja": "読みやすさ分析が含まれています"
    },
    "review.clearscope.regular.algorithm.updates": {
        "pt": "Atualizações regulares do algoritmo",
        "zh": "定期算法更新",
        "ja": "定期的なアルゴリズム更新"
    },
    "review.clearscope.outstanding.customer.support": {
        "pt": "Suporte ao cliente excepcional",
        "zh": "卓越的客户支持",
        "ja": "優れたカスタマーサポート"
    },
    "review.clearscope.content.marketing.ensure.every.piece": {
        "pt": "Marketing de Conteúdo: Certifique-se de que cada peça de conteúdo esteja totalmente otimizada antes da publicação",
        "zh": "内容营销：确保每一篇内容在发布前都经过完全优化",
        "ja": "コンテンツマーケティング：公開前にすべてのコンテンツが完全に最適化されていることを確認します"
    },
    "review.clearscope.seo.writing.help.writers.create": {
        "pt": "Redação SEO: Ajude escritores a criar conteúdo amigável para SEO sem precisar de profunda experiência em SEO",
        "zh": "SEO写作：帮助作家在不需要深厚SEO专业知识的情况下创建SEO友好的内容",
        "ja": "SEOライティング：深いSEO専門知識を必要とせずに、ライターがSEOフレンドリーなコンテンツを作成するのを支援します"
    },
    "review.clearscope.content.audits.identify.optimization.opportunities": {
        "pt": "Auditorias de Conteúdo: Identifique oportunidades de otimização em conteúdo existente",
        "zh": "内容审计：识别现有内容中的优化机会",
        "ja": "コンテンツ監査：既存のコンテンツの最適化機会を特定します"
    },
    "review.clearscope.agency.work.generate.client.reports": {
        "pt": "Trabalho de Agência: Gere relatórios de clientes mostrando recomendações de otimização",
        "zh": "代理工作：生成显示优化建议的客户报告",
        "ja": "エージェンシー業務：最適化の推奨事項を示すクライアントレポートを生成します"
    },
    "review.clearscope.team.workflows.standardize.content.optimization": {
        "pt": "Fluxos de Trabalho em Equipe: Padronize a otimização de conteúdo entre as equipes de conteúdo",
        "zh": "团队工作流程：在内容团队中标准化内容优化",
        "ja": "チームワークフロー：コンテンツチーム全体でコンテンツ最適化を標準化します"
    },
    "review.clearscope.competitive.research.understand.what.top": {
        "pt": "Pesquisa Competitiva: Entenda o que os principais concorrentes estão cobrindo em seu conteúdo",
        "zh": "竞争研究：了解顶级竞争对手在其内容中涵盖的内容",
        "ja": "競合調査：トップ競合他社がコンテンツで何をカバーしているかを理解します"
    },
    "review.clearscope.content.strategy.identify.content.gaps": {
        "pt": "Estratégia de Conteúdo: Identifique lacunas de conteúdo e tópicos a cobrir com base em dados de pesquisa",
        "zh": "内容策略：根据搜索数据识别内容空白和要涵盖的主题",
        "ja": "コンテンツ戦略：検索データに基づいてコンテンツのギャップとカバーすべきトピックを特定します"
    },
    "review.clearscope.may.not.be.ideal.for": {
        "pt": "Pode Não Ser Ideal Para:",
        "zh": "可能不适合：",
        "ja": "理想的でない場合があります："
    },
    "review.clearscope.businesses.needing.full.seo.suite": {
        "pt": "Empresas que precisam de suíte SEO completa (backlinks, SEO técnico, etc.)",
        "zh": "需要完整SEO套件的企业（反向链接、技术SEO等）",
        "ja": "完全なSEOスイートが必要な企業（バックリンク、テクニカルSEOなど）"
    },
    "review.clearscope.small.blogs.with.limited.budgets": {
        "pt": "Blogs pequenos com orçamentos limitados",
        "zh": "预算有限的小型博客",
        "ja": "予算が限られている小規模ブログ"
    },
    "review.clearscope.those.wanting.ai.content.generation": {
        "pt": "Aqueles que desejam geração de conteúdo com IA",
        "zh": "想要AI内容生成的用户",
        "ja": "AIコンテンツ生成を希望する人"
    },
    "review.clearscope.users.needing.extensive.keyword.research": {
        "pt": "Usuários que precisam de ferramentas extensas de pesquisa de palavras-chave",
        "zh": "需要广泛关键词研究工具的用户",
        "ja": "広範なキーワード調査ツールが必要なユーザー"
    },
    "review.clearscope.how.it.compares": {
        "pt": "Como Se Compara",
        "zh": "如何比较",
        "ja": "比較"
    },
    "review.clearscope.clearscope.vs.surfer.seo": {
        "pt": "Clearscope vs Surfer SEO",
        "zh": "Clearscope vs Surfer SEO",
        "ja": "Clearscope vs Surfer SEO"
    },
    "review.clearscope.clearscope.offers.a.cleaner.more": {
        "pt": "O Clearscope oferece uma interface mais limpa e focada com integração superior ao Google Docs, tornando-o ideal para equipes de conteúdo. O Surfer SEO fornece mais recursos, incluindo pesquisa de palavras-chave, análise SERP e escrita com IA a um preço mais baixo. A classificação de conteúdo do Clearscope é mais refinada e intuitiva. O Surfer oferece melhor valor para criadores individuais, enquanto o Clearscope é preferido por equipes de conteúdo maiores e agências que priorizam a integração do fluxo de trabalho.",
        "zh": "Clearscope提供更简洁、更专注的界面，具有优越的Google Docs集成，使其成为内容团队的理想选择。Surfer SEO以更低的价格提供更多功能，包括关键词研究、SERP分析和AI写作。Clearscope的内容评分更加精细和直观。Surfer为个人创作者提供更好的价值，而Clearscope则受到优先考虑工作流程集成的大型内容团队和代理机构的青睐。",
        "ja": "Clearscopeは、優れたGoogle Docs統合を備えたよりクリーンで焦点を絞ったインターフェースを提供し、コンテンツチームに最適です。Surfer SEOは、キーワード調査、SERP分析、AIライティングを含むより多くの機能をより低い価格で提供します。Clearscopeのコンテンツグレーディングはより洗練され直感的です。Surferは個人クリエイターに優れた価値を提供しますが、Clearscopeはワークフロー統合を優先する大規模なコンテンツチームやエージェンシーに好まれています。"
    },
    "review.clearscope.clearscope.vs.frase": {
        "pt": "Clearscope vs Frase",
        "zh": "Clearscope vs Frase",
        "ja": "Clearscope vs Frase"
    },
    "review.clearscope.clearscope.focuses.purely.on.content": {
        "pt": "O Clearscope se concentra puramente na otimização de conteúdo com precisão premium e recursos de equipe. O Frase combina otimização com escrita com IA, resumos de conteúdo e ferramentas de pesquisa a um preço mais acessível. As recomendações do Clearscope são mais precisas e acionáveis. O Frase fornece mais recursos pelo preço, mas com uma curva de aprendizado mais acentuada. Escolha Clearscope para excelência em otimização pura, Frase para uma solução de conteúdo completa.",
        "zh": "Clearscope纯粹专注于内容优化，具有高级准确性和团队功能。Frase以更实惠的价格将优化与AI写作、内容简报和研究工具相结合。Clearscope的建议更加精确和可操作。Frase以更高的价格提供更多功能，但学习曲线更陡峭。选择Clearscope以获得纯粹的优化卓越性，选择Frase以获得全方位的内容解决方案。",
        "ja": "Clearscopeは、プレミアムな精度とチーム機能を備えたコンテンツ最適化に純粋に焦点を当てています。Fraseは、よりアクセスしやすい価格でAIライティング、コンテンツブリーフ、リサーチツールと最適化を組み合わせています。Clearscopeの推奨事項はより正確で実行可能です。Fraseは価格に対してより多くの機能を提供しますが、学習曲線が急です。純粋な最適化の卓越性を求めるならClearscope、オールインワンのコンテンツソリューションを求めるならFraseを選択してください。"
    },
    "review.common.final.verdict": {
        "pt": "Veredicto Final",
        "zh": "最终裁决",
        "ja": "最終評価"
    },
    "review.clearscope.our.recommendation": {
        "pt": "Nossa Recomendação",
        "zh": "我们的推荐",
        "ja": "私たちの推奨"
    },
    "review.clearscope.clearscope.is.the.premium.choice": {
        "pt": "O Clearscope é a escolha premium para equipes de conteúdo e agências que precisam da plataforma de otimização de conteúdo mais precisa e acionável disponível. Embora o preço a partir de $170/mês seja alto, a qualidade das recomendações, a integração perfeita do fluxo de trabalho e o impacto no desempenho do conteúdo justificam o investimento para profissionais de marketing de conteúdo sérios. Somente a integração com o Google Docs economiza inúmeras horas e torna o processo de otimização natural em vez de forçado. O sistema de classificação de conteúdo é o melhor do setor, fornecendo feedback instantâneo e confiável em que escritores e especialistas em SEO podem confiar. Para blogueiros individuais ou pequenas empresas com orçamentos limitados, o preço pode ser proibitivo - alternativas como Surfer SEO ou Frase oferecem mais recursos a custos menores. No entanto, se você é uma equipe de conteúdo em crescimento, agência ou empresa que publica conteúdo de alta qualidade regularmente e precisa garantir que cada peça seja bem classificada, o Clearscope vale cada centavo. O ROI de rankings melhorados e tráfego orgânico normalmente excede em muito o custo da assinatura. Solicite uma demonstração para ver se é adequado para sua equipe.",
        "zh": "Clearscope是内容团队和代理机构的高级选择，他们需要最准确、最可操作的内容优化平台。虽然从$170/月起的价格很高，但建议的质量、无缝的工作流程集成以及对内容性能的影响为认真的内容营销人员证明了投资的合理性。仅Google Docs集成就节省了无数小时，并使优化过程感觉自然而不是强制。内容评分系统是业界最好的，提供作家和SEO专家可以信赖的即时可靠反馈。对于预算有限的个人博主或小型企业，价格可能令人望而却步——Surfer SEO或Frase等替代方案以更低的成本提供更多功能。然而，如果您是一个不断发展的内容团队、代理机构或定期发布高质量内容并需要确保每一篇内容都能很好地排名的企业，Clearscope物有所值。改进排名和自然流量的投资回报率通常远远超过订阅成本。请求演示以查看是否适合您的团队。",
        "ja": "Clearscopeは、最も正確で実行可能なコンテンツ最適化プラットフォームを必要とするコンテンツチームやエージェンシーにとってのプレミアム選択肢です。$170/月から始まる価格は高いですが、推奨事項の品質、シームレスなワークフロー統合、コンテンツパフォーマンスへの影響は、真剣なコンテンツマーケターにとって投資を正当化します。Google Docs統合だけでも無数の時間を節約し、最適化プロセスを強制的ではなく自然に感じさせます。コンテンツグレーディングシステムは業界最高で、ライターとSEOスペシャリストの両方が信頼できる即座で信頼性の高いフィードバックを提供します。予算が限られている個人ブロガーや中小企業にとって、価格は禁止的かもしれません - Surfer SEOやFraseなどの代替案は、より低コストでより多くの機能を提供します。ただし、定期的に高品質なコンテンツを公開し、すべてのコンテンツが適切にランク付けされることを確保する必要がある成長中のコンテンツチーム、エージェンシー、または企業である場合、Clearscopeは一銭も惜しくありません。改善されたランキングとオーガニックトラフィックからのROIは、通常、サブスクリプションコストをはるかに上回ります。チームに適しているかどうかを確認するためにデモをリクエストしてください。"
    },
    "review.common.screenshots.interface": {
        "pt": "Capturas de Tela e Interface",
        "zh": "截图和界面",
        "ja": "スクリーンショットとインターフェース"
    },
    "review.clearscope.explore.clearscopes.interface": {
        "pt": "Explore a interface do Clearscope:",
        "zh": "探索Clearscope的界面：",
        "ja": "Clearscopeのインターフェースを探索："
    },
    "review.clearscope.main.interface.-.overview.of": {
        "pt": "Interface Principal - Visão geral da plataforma",
        "zh": "主界面 - 平台概述",
        "ja": "メインインターフェース - プラットフォームの概要"
    },
    "review.common.frequently.asked.questions": {
        "pt": "Perguntas Frequentes",
        "zh": "常见问题",
        "ja": "よくある質問"
    }
}

# Add all translations to batch2
for key, translations in missing_batch2.items():
    for lang in ['pt', 'zh', 'ja']:
        if lang not in batch2:
            batch2[lang] = {}
        batch2[lang][key] = translations[lang]

# Save updated batch2
with open(os.path.join(batch_dir, 'clearscope-batch2.json'), 'w', encoding='utf-8') as f:
    json.dump(batch2, f, ensure_ascii=False, indent=2)

print('Updated clearscope-batch2.json with ALL missing translations')
print('Batch 2 (PT, ZH, JA) is now COMPLETE!')
