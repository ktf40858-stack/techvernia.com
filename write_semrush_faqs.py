import json
import os

os.chdir('GenuisNet.ai/pages/reviews/seo')

# Semrush FAQs batch 1 (ES/FR/DE)
faqs_batch1 = {
  "en": {
    "review.semrush.faq.q1": "Is Semrush worth the price?",
    "review.semrush.faq.a1": "Yes, for anyone serious about SEO. Semrush provides the most accurate and comprehensive SEO data available, with fresh backlink data, reliable keyword metrics, and powerful competitive analysis. The insights you gain typically lead to significant improvements in rankings and traffic that justify the investment. For casual users or complete beginners, the free Semrush Webmaster Tools offer a good starting point.",
    "review.semrush.faq.q2": "How does Semrush compare to free alternatives?",
    "review.semrush.faq.a2": "While tools like Google Search Console and Ubersuggest offer basic SEO data for free, Semrush provides significantly more comprehensive and accurate information. The backlink database, competitor analysis, content explorer, and historical data are unmatched by free tools. For professional SEO work, the depth and reliability of Semrush data is essential and worth the investment.",
    "review.semrush.faq.q3": "What's included in the Lite plan?",
    "review.semrush.faq.a3": "The Lite plan ($99/month) includes 1 user, 5 projects, 500 credits per month, and access to all core tools: Site Explorer, Keywords Explorer, Site Audit, Rank Tracker, and Content Explorer. You get 6 months of historical data and can track up to 750 keywords. It's perfect for freelancers, consultants, and small business owners managing a few websites.",
    "review.semrush.faq.q4": "How accurate is Semrush keyword difficulty score?",
    "review.semrush.faq.a4": "Semrush Keyword Difficulty (KD) is highly accurate and based on the number of referring domains to top-ranking pages. It's measured on a scale of 0-100, with higher scores indicating more backlinks needed to rank. While no metric is perfect, Semrush KD is considered one of the most reliable difficulty scores in the industry, based on real backlink data rather than estimates.",
    "review.semrush.faq.q5": "Can I cancel my Semrush subscription anytime?",
    "review.semrush.faq.a5": "Yes, Semrush subscriptions are flexible and can be cancelled at any time. There are no long-term contracts or cancellation fees. You can also pause your subscription for up to 3 months if you need a temporary break. Monthly subscriptions renew automatically, but you maintain access until the end of your billing period if you cancel.",
    "review.semrush.faq.q6": "Does Semrush offer a free trial?",
    "review.semrush.faq.a6": "Semrush no longer offers a traditional free trial, but they provide Semrush Webmaster Tools completely free. This gives you access to Site Audit, Site Explorer (for your verified sites), and SERP checker. It's a great way to experience the platform's power before committing to a paid plan. They occasionally run $7 for 7 days trial promotions for new users."
  },
  "target_langs": ["es", "fr", "de"],
  "es": {
    "review.semrush.faq.q1": "¿Vale la pena el precio de Semrush?",
    "review.semrush.faq.a1": "Sí, para cualquiera que se tome en serio el SEO. Semrush proporciona los datos de SEO más precisos y completos disponibles, con datos de backlinks actualizados, métricas de palabras clave fiables y un potente análisis competitivo. Las perspectivas que obtienes normalmente conducen a mejoras significativas en rankings y tráfico que justifican la inversión. Para usuarios ocasionales o principiantes completos, las Semrush Webmaster Tools gratuitas ofrecen un buen punto de partida.",
    "review.semrush.faq.q2": "¿Cómo se compara Semrush con las alternativas gratuitas?",
    "review.semrush.faq.a2": "Aunque herramientas como Google Search Console y Ubersuggest ofrecen datos básicos de SEO de forma gratuita, Semrush proporciona información significativamente más completa y precisa. La base de datos de backlinks, el análisis de competidores, el explorador de contenido y los datos históricos no tienen comparación con las herramientas gratuitas. Para el trabajo de SEO profesional, la profundidad y fiabilidad de los datos de Semrush es esencial y vale la pena la inversión.",
    "review.semrush.faq.q3": "¿Qué incluye el plan Lite?",
    "review.semrush.faq.a3": "El plan Lite ($99/mes) incluye 1 usuario, 5 proyectos, 500 créditos por mes y acceso a todas las herramientas principales: Site Explorer, Keywords Explorer, Site Audit, Rank Tracker y Content Explorer. Obtienes 6 meses de datos históricos y puedes rastrear hasta 750 palabras clave. Es perfecto para freelancers, consultores y propietarios de pequeñas empresas que gestionan unos pocos sitios web.",
    "review.semrush.faq.q4": "¿Qué tan preciso es el puntaje de dificultad de palabras clave de Semrush?",
    "review.semrush.faq.a4": "Semrush Keyword Difficulty (KD) es muy preciso y se basa en el número de dominios de referencia a las páginas mejor posicionadas. Se mide en una escala de 0-100, con puntuaciones más altas que indican más backlinks necesarios para posicionarse. Aunque ninguna métrica es perfecta, Semrush KD se considera una de las puntuaciones de dificultad más fiables de la industria, basada en datos reales de backlinks en lugar de estimaciones.",
    "review.semrush.faq.q5": "¿Puedo cancelar mi suscripción a Semrush en cualquier momento?",
    "review.semrush.faq.a5": "Sí, las suscripciones de Semrush son flexibles y se pueden cancelar en cualquier momento. No hay contratos a largo plazo ni cargos por cancelación. También puedes pausar tu suscripción hasta 3 meses si necesitas un descanso temporal. Las suscripciones mensuales se renuevan automáticamente, pero mantienes el acceso hasta el final de tu período de facturación si cancelas.",
    "review.semrush.faq.q6": "¿Ofrece Semrush una prueba gratuita?",
    "review.semrush.faq.a6": "Semrush ya no ofrece una prueba gratuita tradicional, pero proporcionan Semrush Webmaster Tools completamente gratis. Esto te da acceso a Site Audit, Site Explorer (para tus sitios verificados) y el verificador de SERP. Es una excelente manera de experimentar el poder de la plataforma antes de comprometerte con un plan de pago. Ocasionalmente ofrecen promociones de prueba de $7 por 7 días para nuevos usuarios."
  },
  "fr": {
    "review.semrush.faq.q1": "Semrush vaut-il son prix ?",
    "review.semrush.faq.a1": "Oui, pour quiconque prend le SEO au sérieux. Semrush fournit les données SEO les plus précises et complètes disponibles, avec des données de backlinks actualisées, des métriques de mots-clés fiables et une analyse concurrentielle puissante. Les insights que vous obtenez conduisent généralement à des améliorations significatives du classement et du trafic qui justifient l'investissement. Pour les utilisateurs occasionnels ou les débutants complets, les Semrush Webmaster Tools gratuits offrent un bon point de départ.",
    "review.semrush.faq.q2": "Comment Semrush se compare-t-il aux alternatives gratuites ?",
    "review.semrush.faq.a2": "Bien que des outils comme Google Search Console et Ubersuggest offrent des données SEO de base gratuitement, Semrush fournit des informations nettement plus complètes et précises. La base de données de backlinks, l'analyse des concurrents, l'explorateur de contenu et les données historiques sont inégalés par les outils gratuits. Pour un travail SEO professionnel, la profondeur et la fiabilité des données de Semrush sont essentielles et valent l'investissement.",
    "review.semrush.faq.q3": "Qu'est-ce qui est inclus dans le plan Lite ?",
    "review.semrush.faq.a3": "Le plan Lite ($99/mois) comprend 1 utilisateur, 5 projets, 500 crédits par mois et l'accès à tous les outils principaux : Site Explorer, Keywords Explorer, Site Audit, Rank Tracker et Content Explorer. Vous obtenez 6 mois de données historiques et pouvez suivre jusqu'à 750 mots-clés. C'est parfait pour les freelances, les consultants et les propriétaires de petites entreprises gérant quelques sites web.",
    "review.semrush.faq.q4": "Quelle est la précision du score de difficulté des mots-clés de Semrush ?",
    "review.semrush.faq.a4": "Semrush Keyword Difficulty (KD) est très précis et basé sur le nombre de domaines référents vers les pages les mieux classées. Il est mesuré sur une échelle de 0-100, les scores plus élevés indiquant plus de backlinks nécessaires pour se classer. Bien qu'aucune métrique ne soit parfaite, Semrush KD est considéré comme l'un des scores de difficulté les plus fiables de l'industrie, basé sur des données réelles de backlinks plutôt que sur des estimations.",
    "review.semrush.faq.q5": "Puis-je annuler mon abonnement Semrush à tout moment ?",
    "review.semrush.faq.a5": "Oui, les abonnements Semrush sont flexibles et peuvent être annulés à tout moment. Il n'y a pas de contrats à long terme ni de frais d'annulation. Vous pouvez également mettre en pause votre abonnement jusqu'à 3 mois si vous avez besoin d'une pause temporaire. Les abonnements mensuels se renouvellent automatiquement, mais vous conservez l'accès jusqu'à la fin de votre période de facturation si vous annulez.",
    "review.semrush.faq.q6": "Semrush propose-t-il un essai gratuit ?",
    "review.semrush.faq.a6": "Semrush ne propose plus d'essai gratuit traditionnel, mais ils fournissent Semrush Webmaster Tools entièrement gratuit. Cela vous donne accès à Site Audit, Site Explorer (pour vos sites vérifiés) et au vérificateur SERP. C'est un excellent moyen de découvrir la puissance de la plateforme avant de vous engager dans un plan payant. Ils proposent occasionnellement des promotions d'essai à $7 pour 7 jours pour les nouveaux utilisateurs."
  },
  "de": {
    "review.semrush.faq.q1": "Ist Semrush den Preis wert?",
    "review.semrush.faq.a1": "Ja, für jeden, der SEO ernst nimmt. Semrush bietet die genauesten und umfassendsten verfügbaren SEO-Daten mit aktuellen Backlink-Daten, zuverlässigen Keyword-Metriken und leistungsstarker Wettbewerbsanalyse. Die Erkenntnisse, die Sie gewinnen, führen in der Regel zu erheblichen Verbesserungen bei Rankings und Traffic, die die Investition rechtfertigen. Für Gelegenheitsnutzer oder absolute Anfänger bieten die kostenlosen Semrush Webmaster Tools einen guten Einstiegspunkt.",
    "review.semrush.faq.q2": "Wie schneidet Semrush im Vergleich zu kostenlosen Alternativen ab?",
    "review.semrush.faq.a2": "Während Tools wie Google Search Console und Ubersuggest grundlegende SEO-Daten kostenlos anbieten, liefert Semrush deutlich umfassendere und genauere Informationen. Die Backlink-Datenbank, Wettbewerbsanalyse, Content Explorer und historische Daten sind von kostenlosen Tools unerreicht. Für professionelle SEO-Arbeit sind die Tiefe und Zuverlässigkeit der Semrush-Daten unerlässlich und die Investition wert.",
    "review.semrush.faq.q3": "Was ist im Lite-Plan enthalten?",
    "review.semrush.faq.a3": "Der Lite-Plan ($99/Monat) umfasst 1 Benutzer, 5 Projekte, 500 Credits pro Monat und Zugriff auf alle Haupttools: Site Explorer, Keywords Explorer, Site Audit, Rank Tracker und Content Explorer. Sie erhalten 6 Monate historische Daten und können bis zu 750 Keywords verfolgen. Es ist perfekt für Freelancer, Berater und Kleinunternehmer, die einige Websites verwalten.",
    "review.semrush.faq.q4": "Wie genau ist der Keyword-Schwierigkeitsgrad von Semrush?",
    "review.semrush.faq.a4": "Semrush Keyword Difficulty (KD) ist sehr genau und basiert auf der Anzahl der verweisenden Domains zu den am besten platzierten Seiten. Es wird auf einer Skala von 0-100 gemessen, wobei höhere Werte mehr Backlinks bedeuten, die zum Ranking benötigt werden. Obwohl keine Metrik perfekt ist, gilt Semrush KD als einer der zuverlässigsten Schwierigkeitswerte der Branche, basierend auf echten Backlink-Daten statt auf Schätzungen.",
    "review.semrush.faq.q5": "Kann ich mein Semrush-Abonnement jederzeit kündigen?",
    "review.semrush.faq.a5": "Ja, Semrush-Abonnements sind flexibel und können jederzeit gekündigt werden. Es gibt keine langfristigen Verträge oder Kündigungsgebühren. Sie können Ihr Abonnement auch bis zu 3 Monate pausieren, wenn Sie eine vorübergehende Pause benötigen. Monatsabonnements verlängern sich automatisch, aber Sie behalten den Zugang bis zum Ende Ihres Abrechnungszeitraums, wenn Sie kündigen.",
    "review.semrush.faq.q6": "Bietet Semrush eine kostenlose Testversion an?",
    "review.semrush.faq.a6": "Semrush bietet keine traditionelle kostenlose Testversion mehr an, aber sie stellen Semrush Webmaster Tools völlig kostenlos zur Verfügung. Dies gibt Ihnen Zugriff auf Site Audit, Site Explorer (für Ihre verifizierten Sites) und SERP-Checker. Es ist eine großartige Möglichkeit, die Leistungsfähigkeit der Plataforma zu erleben, bevor Sie sich für einen kostenpflichtigen Plan verpflichten. Gelegentlich bieten sie $7 für 7 Tage Testaktionen für neue Benutzer an."
  }
}

# Write FAQs batch 1
with open('semrush-faqs-batch1.json', 'w', encoding='utf-8') as f:
    json.dump(faqs_batch1, f, ensure_ascii=False, indent=2)

print('Written semrush-faqs-batch1.json')

# FAQs batch 2 (PT/ZH/JA)
faqs_batch2 = {
  "en": {
    "review.semrush.faq.q1": "Is Semrush worth the price?",
    "review.semrush.faq.a1": "Yes, for anyone serious about SEO. Semrush provides the most accurate and comprehensive SEO data available, with fresh backlink data, reliable keyword metrics, and powerful competitive analysis. The insights you gain typically lead to significant improvements in rankings and traffic that justify the investment. For casual users or complete beginners, the free Semrush Webmaster Tools offer a good starting point.",
    "review.semrush.faq.q2": "How does Semrush compare to free alternatives?",
    "review.semrush.faq.a2": "While tools like Google Search Console and Ubersuggest offer basic SEO data for free, Semrush provides significantly more comprehensive and accurate information. The backlink database, competitor analysis, content explorer, and historical data are unmatched by free tools. For professional SEO work, the depth and reliability of Semrush data is essential and worth the investment.",
    "review.semrush.faq.q3": "What's included in the Lite plan?",
    "review.semrush.faq.a3": "The Lite plan ($99/month) includes 1 user, 5 projects, 500 credits per month, and access to all core tools: Site Explorer, Keywords Explorer, Site Audit, Rank Tracker, and Content Explorer. You get 6 months of historical data and can track up to 750 keywords. It's perfect for freelancers, consultants, and small business owners managing a few websites.",
    "review.semrush.faq.q4": "How accurate is Semrush keyword difficulty score?",
    "review.semrush.faq.a4": "Semrush Keyword Difficulty (KD) is highly accurate and based on the number of referring domains to top-ranking pages. It's measured on a scale of 0-100, with higher scores indicating more backlinks needed to rank. While no metric is perfect, Semrush KD is considered one of the most reliable difficulty scores in the industry, based on real backlink data rather than estimates.",
    "review.semrush.faq.q5": "Can I cancel my Semrush subscription anytime?",
    "review.semrush.faq.a5": "Yes, Semrush subscriptions are flexible and can be cancelled at any time. There are no long-term contracts or cancellation fees. You can also pause your subscription for up to 3 months if you need a temporary break. Monthly subscriptions renew automatically, but you maintain access until the end of your billing period if you cancel.",
    "review.semrush.faq.q6": "Does Semrush offer a free trial?",
    "review.semrush.faq.a6": "Semrush no longer offers a traditional free trial, but they provide Semrush Webmaster Tools completely free. This gives you access to Site Audit, Site Explorer (for your verified sites), and SERP checker. It's a great way to experience the platform's power before committing to a paid plan. They occasionally run $7 for 7 days trial promotions for new users."
  },
  "target_langs": ["pt", "zh", "ja"],
  "pt": {
    "review.semrush.faq.q1": "O Semrush vale o preço?",
    "review.semrush.faq.a1": "Sim, para quem leva SEO a sério. O Semrush fornece os dados de SEO mais precisos e abrangentes disponíveis, com dados de backlink atualizados, métricas de palavras-chave confiáveis e análise competitiva poderosa. Os insights que você obtém normalmente levam a melhorias significativas em rankings e tráfego que justificam o investimento. Para usuários casuais ou iniciantes completos, as Semrush Webmaster Tools gratuitas oferecem um bom ponto de partida.",
    "review.semrush.faq.q2": "Como o Semrush se compara às alternativas gratuitas?",
    "review.semrush.faq.a2": "Embora ferramentas como Google Search Console e Ubersuggest ofereçam dados básicos de SEO gratuitamente, o Semrush fornece informações significativamente mais abrangentes e precisas. O banco de dados de backlinks, análise de concorrentes, explorador de conteúdo e dados históricos são incomparáveis pelas ferramentas gratuitas. Para trabalho profissional de SEO, a profundidade e confiabilidade dos dados do Semrush são essenciais e valem o investimento.",
    "review.semrush.faq.q3": "O que está incluído no plano Lite?",
    "review.semrush.faq.a3": "O plano Lite ($99/mês) inclui 1 usuário, 5 projetos, 500 créditos por mês e acesso a todas as ferramentas principais: Site Explorer, Keywords Explorer, Site Audit, Rank Tracker e Content Explorer. Você obtém 6 meses de dados históricos e pode rastrear até 750 palavras-chave. É perfeito para freelancers, consultores e proprietários de pequenas empresas que gerenciam alguns sites.",
    "review.semrush.faq.q4": "Quão preciso é o score de dificuldade de palavras-chave do Semrush?",
    "review.semrush.faq.a4": "O Keyword Difficulty (KD) do Semrush é altamente preciso e baseado no número de domínios de referência para páginas com melhor classificação. É medido em uma escala de 0-100, com pontuações mais altas indicando mais backlinks necessários para classificar. Embora nenhuma métrica seja perfeita, o KD do Semrush é considerado um dos scores de dificuldade mais confiáveis do setor, baseado em dados reais de backlink em vez de estimativas.",
    "review.semrush.faq.q5": "Posso cancelar minha assinatura do Semrush a qualquer momento?",
    "review.semrush.faq.a5": "Sim, as assinaturas do Semrush são flexíveis e podem ser canceladas a qualquer momento. Não há contratos de longo prazo ou taxas de cancelamento. Você também pode pausar sua assinatura por até 3 meses se precisar de uma pausa temporária. As assinaturas mensais são renovadas automaticamente, mas você mantém o acesso até o final do seu período de faturamento se cancelar.",
    "review.semrush.faq.q6": "O Semrush oferece um teste gratuito?",
    "review.semrush.faq.a6": "O Semrush não oferece mais um teste gratuito tradicional, mas fornece o Semrush Webmaster Tools completamente gratuito. Isso lhe dá acesso ao Site Audit, Site Explorer (para seus sites verificados) e verificador SERP. É uma ótima maneira de experimentar o poder da plataforma antes de se comprometer com um plano pago. Eles ocasionalmente executam promoções de teste de $7 por 7 dias para novos usuários."
  },
  "zh": {
    "review.semrush.faq.q1": "Semrush值这个价格吗？",
    "review.semrush.faq.a1": "对于认真做SEO的人来说，是的。Semrush提供最准确和最全面的SEO数据，包括新鲜的反向链接数据、可靠的关键词指标和强大的竞争分析。您获得的见解通常会显著改善排名和流量，从而证明投资是值得的。对于休闲用户或完全的初学者，免费的Semrush Webmaster Tools提供了一个很好的起点。",
    "review.semrush.faq.q2": "Semrush与免费替代工具相比如何？",
    "review.semrush.faq.a2": "虽然Google Search Console和Ubersuggest等工具免费提供基本的SEO数据，但Semrush提供的信息要全面和准确得多。反向链接数据库、竞争对手分析、内容浏览器和历史数据是免费工具无法比拟的。对于专业的SEO工作，Semrush数据的深度和可靠性至关重要，值得投资。",
    "review.semrush.faq.q3": "Lite计划包含什么？",
    "review.semrush.faq.a3": "Lite计划（$99/月）包括1个用户、5个项目、每月500个积分，以及访问所有核心工具的权限：Site Explorer、Keywords Explorer、Site Audit、Rank Tracker和Content Explorer。您可以获得6个月的历史数据，并可以跟踪多达750个关键词。它非常适合管理几个网站的自由职业者、顾问和小企业主。",
    "review.semrush.faq.q4": "Semrush关键词难度分数有多准确？",
    "review.semrush.faq.a4": "Semrush Keyword Difficulty（KD）非常准确，基于排名靠前页面的引用域数量。它以0-100的范围进行测量，分数越高表示需要更多反向链接才能排名。虽然没有指标是完美的，但Semrush KD被认为是行业中最可靠的难度分数之一，基于真实的反向链接数据而不是估计值。",
    "review.semrush.faq.q5": "我可以随时取消Semrush订阅吗？",
    "review.semrush.faq.a5": "是的，Semrush订阅是灵活的，可以随时取消。没有长期合同或取消费用。如果您需要临时休息，还可以暂停订阅长达3个月。月度订阅会自动续订，但如果您取消，您将保持访问权限直到计费周期结束。",
    "review.semrush.faq.q6": "Semrush提供免费试用吗？",
    "review.semrush.faq.a6": "Semrush不再提供传统的免费试用，但他们完全免费提供Semrush Webmaster Tools。这使您可以访问Site Audit、Site Explorer（用于您已验证的网站）和SERP检查器。这是在承诺付费计划之前体验平台强大功能的好方法。他们偶尔会为新用户提供$7试用7天的促销活动。"
  },
  "ja": {
    "review.semrush.faq.q1": "Semrushは価格に見合う価値がありますか？",
    "review.semrush.faq.a1": "はい、SEOに真剣に取り組む人にとっては価値があります。Semrushは、最新のバックリンクデータ、信頼できるキーワード指標、強力な競合分析を備えた、最も正確で包括的なSEOデータを提供します。得られるインサイトは通常、投資を正当化するランキングとトラフィックの大幅な改善につながります。カジュアルユーザーや完全な初心者には、無料のSemrush Webmaster Toolsが良い出発点となります。",
    "review.semrush.faq.q2": "Semrushは無料の代替ツールと比較してどうですか？",
    "review.semrush.faq.a2": "Google Search ConsoleやUbersuggestなどのツールは基本的なSEOデータを無料で提供していますが、Semrushははるかに包括的で正確な情報を提供します。バックリンクデータベース、競合分析、コンテンツエクスプローラー、履歴データは、無料ツールでは比類のないものです。プロフェッショナルなSEO作業には、Semrushデータの深さと信頼性が不可欠であり、投資する価値があります。",
    "review.semrush.faq.q3": "Liteプランには何が含まれていますか？",
    "review.semrush.faq.a3": "Liteプラン（$99/月）には、1ユーザー、5プロジェクト、月間500クレジット、およびすべてのコアツールへのアクセスが含まれます：Site Explorer、Keywords Explorer、Site Audit、Rank Tracker、Content Explorer。6か月の履歴データが取得でき、最大750のキーワードを追跡できます。いくつかのWebサイトを管理するフリーランサー、コンサルタント、中小企業オーナーに最適です。",
    "review.semrush.faq.q4": "Semrushのキーワード難易度スコアはどのくらい正確ですか？",
    "review.semrush.faq.a4": "Semrush Keyword Difficulty（KD）は非常に正確で、上位ランキングページへの参照ドメイン数に基づいています。0-100のスケールで測定され、スコアが高いほどランク付けに必要なバックリンクが多いことを示します。完璧な指標はありませんが、Semrush KDは、推定値ではなく実際のバックリンクデータに基づいた、業界で最も信頼できる難易度スコアの1つと考えられています。",
    "review.semrush.faq.q5": "Semrushのサブスクリプションはいつでもキャンセルできますか？",
    "review.semrush.faq.a5": "はい、Semrushのサブスクリプションは柔軟で、いつでもキャンセルできます。長期契約やキャンセル料はありません。一時的な休憩が必要な場合は、最大3か月間サブスクリプションを一時停止することもできます。月額サブスクリプションは自動的に更新されますが、キャンセルした場合は請求期間の終了までアクセスを維持できます。",
    "review.semrush.faq.q6": "Semrushは無料トライアルを提供していますか?",
    "review.semrush.faq.a6": "Semrushは従来の無料トライアルを提供していませんが、Semrush Webmaster Toolsを完全に無料で提供しています。これにより、Site Audit、Site Explorer（確認済みサイト用）、SERPチェッカーにアクセスできます。有料プランにコミットする前に、プラットフォームのパワーを体験する素晴らしい方法です。新規ユーザー向けに$7で7日間のトライアルプロモーションを時々実施しています。"
  }
}

# Write FAQs batch 2
with open('semrush-faqs-batch2.json', 'w', encoding='utf-8') as f:
    json.dump(faqs_batch2, f, ensure_ascii=False, indent=2)

print('Written semrush-faqs-batch2.json')
print('All FAQ files written successfully!')
