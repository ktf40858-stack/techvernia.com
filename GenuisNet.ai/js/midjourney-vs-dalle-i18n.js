// Midjourney vs DALL-E 3 Article - Multilingual Translations
// 10 Languages: EN, ES, FR, DE, PT, ZH, JA, KO, AR, HI

console.log('📦 midjourney-vs-dalle-i18n.js loaded');

const articleTranslations = {
    en: {
        // Meta & Page Title
        pageTitle: "Midjourney V6 vs DALL-E 3: The Ultimate Image Generation Showdown | GenuisNet.ai",
        metaDescription: "Midjourney V6 vs DALL-E 3 comparison 2026. Detailed analysis with sample images, pricing breakdown, and recommendations for choosing the best AI image generator.",
        metaKeywords: "Midjourney vs DALL-E 3, AI image generation, Midjourney V6, DALL-E 3, AI art",

        // Hero Section
        heroTitle: "Midjourney V6 vs DALL-E 3: The Ultimate Image Generation Showdown",
        heroExcerpt: "Detailed comparison with sample images, pricing analysis, and recommendations to help you choose the best AI image generator for your needs.",

        // Main Headings
        heading1: "Executive Summary",
        heading2: "Quick Comparison",
        heading3: "Image Quality & Aesthetic",
        heading4: "Prompt Accuracy",
        heading5: "Pricing Breakdown",
        heading6: "Interface & Workflow",
        heading7: "Use Case Recommendations",
        heading8: "Strengths & Weaknesses",
        heading9: "Final Verdict",

        // Subheadings
        subheading3_1: "Midjourney V6: Artistic Excellence",
        subheading3_2: "DALL-E 3: Photorealistic Precision",
        subheading5_1: "Midjourney",
        subheading5_2: "DALL-E 3",
        subheading6_1: "Midjourney (Discord)",
        subheading6_2: "DALL-E 3 (ChatGPT)",
        subheading7_1: "Choose Midjourney if you need:",
        subheading7_2: "Choose DALL-E 3 if you need:",
        subheading8_1: "Midjourney V6",
        subheading8_2: "DALL-E 3",

        // Executive Summary
        para1_1: "Midjourney V6 excels at creating stunning, artistic images with exceptional detail and aesthetic quality. It's perfect for creative professionals, artists, and anyone who values beauty and artistry.",
        para1_2: "DALL-E 3 focuses on prompt accuracy and photorealism. It's ideal for precise visualizations, marketing materials, and users who need reliable, consistent results integrated with ChatGPT.",

        // Comparison Table
        tableFeature: "Feature",
        tableMidjourney: "Midjourney V6",
        tableDallE: "DALL-E 3",
        tablePricing: "Pricing",
        tablePricingMJ: "$10-60/month",
        tablePricingDE: "$20/month (ChatGPT Plus)",
        tableInterface: "Interface",
        tableInterfaceMJ: "Discord",
        tableInterfaceDE: "ChatGPT",
        tableImageQuality: "Image Quality",
        tableImageQualityMJ: "10/10 - Stunning",
        tableImageQualityDE: "8/10 - Excellent",
        tablePromptAccuracy: "Prompt Accuracy",
        tablePromptAccuracyMJ: "7/10 - Creative interpretation",
        tablePromptAccuracyDE: "9/10 - Very precise",
        tableTextInImages: "Text in Images",
        tableTextMJ: "Limited",
        tableTextDE: "Very good",
        tableStyleOptions: "Style Options",
        tableStyleMJ: "Extensive",
        tableStyleDE: "Moderate",
        tableSpeed: "Speed",
        tableSpeedMJ: "~60 seconds",
        tableSpeedDE: "~30 seconds",
        tableEditing: "Editing",
        tableEditingMJ: "Vary, Zoom, Pan",
        tableEditingDE: "Limited variations",
        tableCommercial: "Commercial Use",
        tableCommercialMJ: "Allowed (paid plans)",
        tableCommercialDE: "Allowed",

        // Image Quality Section
        para3_1: "Midjourney has built its reputation on producing breathtakingly beautiful images. Version 6 delivers:",
        list3_1_1: "Exceptional detail:",
        list3_1_1_desc: " Incredible texture, lighting, and depth",
        list3_1_2: "Artistic coherence:",
        list3_1_2_desc: " Images that feel professionally composed",
        list3_1_3: "Style versatility:",
        list3_1_3_desc: " From photorealism to abstract art",
        list3_1_4: "Cinematic quality:",
        list3_1_4_desc: " Perfect for concept art and storytelling",

        para3_2: "DALL-E 3 focuses on accuracy and photorealism:",
        list3_2_1: "Consistent photorealism:",
        list3_2_1_desc: " Reliable realistic images",
        list3_2_2: "Accurate representations:",
        list3_2_2_desc: " Objects and scenes match descriptions precisely",
        list3_2_3: "Text rendering:",
        list3_2_3_desc: " Can generate readable text in images (logos, signs)",
        list3_2_4: "Natural compositions:",
        list3_2_4_desc: " Less \"AI-generated\" look",

        // Prompt Accuracy
        para4_1: "DALL-E 3 wins here. It follows prompts more literally and includes specific details you request. ChatGPT also helps refine your prompt before generation.",
        para4_2: "Midjourney takes creative liberties, which can produce stunning results but may not match your exact vision. You'll often need multiple iterations.",

        // Pricing Breakdown
        list5_1_1: "Basic Plan:",
        list5_1_1_desc: " $10/month (~200 images)",
        list5_1_2: "Standard Plan:",
        list5_1_2_desc: " $30/month (~900 images, Fast mode)",
        list5_1_3: "Pro Plan:",
        list5_1_3_desc: " $60/month (~1800 images, Stealth mode)",

        list5_2_1: "ChatGPT Plus:",
        list5_2_1_desc: " $20/month (includes all ChatGPT features)",
        list5_2_2: "Rate limit: ~40 images/3 hours",
        list5_2_3: "No standalone pricing—must subscribe to ChatGPT Plus",

        para5_1: "Value Winner: DALL-E 3 if you already want ChatGPT Plus. Midjourney Basic ($10) if you only need image generation.",

        // Interface & Workflow
        list6_1_1: "Requires Discord account",
        list6_1_2: "Type \"/imagine\" + prompt in Discord",
        list6_1_3: "Images appear in public channels (unless Pro with Stealth)",
        list6_1_4: "Powerful editing tools (Vary, Zoom Out, Pan)",
        list6_1_5: "Steeper learning curve",

        list6_2_1: "Integrated into ChatGPT interface",
        list6_2_2: "Natural language conversation",
        list6_2_3: "ChatGPT refines your prompt automatically",
        list6_2_4: "Private generation",
        list6_2_5: "More intuitive for beginners",

        // Use Case Recommendations
        list7_1_1: "Stunning artwork for creative projects",
        list7_1_2: "Concept art, character design, world-building",
        list7_1_3: "Fine art prints or portfolio pieces",
        list7_1_4: "Fantasy, sci-fi, or stylized imagery",
        list7_1_5: "Maximum aesthetic quality",

        list7_2_1: "Precise visualizations for presentations",
        list7_2_2: "Marketing materials with specific branding",
        list7_2_3: "Images with readable text (logos, infographics)",
        list7_2_4: "Photorealistic product mockups",
        list7_2_5: "Integration with ChatGPT for content creation",
        list7_2_6: "Simple, beginner-friendly interface",

        // Strengths & Weaknesses
        strengthsLabel: "Strengths:",
        weaknessesLabel: "Weaknesses:",

        list8_1_s1: "Best-in-class image quality and aesthetics",
        list8_1_s2: "Powerful editing and variation tools",
        list8_1_s3: "Large creative community for inspiration",
        list8_1_s4: "Flexible pricing tiers",

        list8_1_w1: "Discord-based workflow can be confusing",
        list8_1_w2: "Less accurate prompt following",
        list8_1_w3: "Poor text rendering in images",
        list8_1_w4: "Public generation (unless Pro plan)",

        list8_2_s1: "Excellent prompt accuracy",
        list8_2_s2: "Integrated with ChatGPT",
        list8_2_s3: "Good text rendering",
        list8_2_s4: "User-friendly interface",
        list8_2_s5: "Private generation",

        list8_2_w1: "Requires ChatGPT Plus subscription",
        list8_2_w2: "Limited editing capabilities",
        list8_2_w3: "Fewer style options",
        list8_2_w4: "Rate limits can be restrictive",

        // Final Verdict
        para9_1: "For Artists & Creatives:",
        para9_1_desc: " Midjourney V6. The image quality is unmatched, and the creative possibilities are endless.",
        para9_2: "For Business & Marketing:",
        para9_2_desc: " DALL-E 3. Prompt accuracy, text rendering, and ChatGPT integration make it more practical for commercial applications.",
        para9_3: "For Beginners:",
        para9_3_desc: " DALL-E 3. The ChatGPT interface is more intuitive, and you get AI writing tools included.",
        para9_4: "Best Value:",
        para9_4_desc: " If you need both image generation and an AI assistant, DALL-E 3 via ChatGPT Plus ($20/month) is excellent value. If you only need images, Midjourney Basic ($10/month) is cheaper.",
        para9_5: "The Ultimate Setup:",
        para9_5_desc: " Subscribe to both! Many power users use Midjourney for artistic work and DALL-E 3 for precise, practical visualizations. Combined cost: $30-50/month.",

        // Footer
        footerDesc: "Your trusted source for AI tool reviews, comparisons, and guides.",
        footerCategories: "Categories",
        footerResources: "Resources",
        footerCopyright: "© 2026 GenuisNet.ai. All rights reserved."
    },

    es: {
        pageTitle: "Midjourney V6 vs DALL-E 3: El Enfrentamiento Definitivo de Generación de Imágenes | GenuisNet.ai",
        metaDescription: "Comparación Midjourney V6 vs DALL-E 3 2026. Análisis detallado con imágenes de muestra, desglose de precios y recomendaciones para elegir el mejor generador de imágenes IA.",
        metaKeywords: "Midjourney vs DALL-E 3, generación de imágenes IA, Midjourney V6, DALL-E 3, arte IA",

        heroTitle: "Midjourney V6 vs DALL-E 3: El Enfrentamiento Definitivo de Generación de Imágenes",
        heroExcerpt: "Comparación detallada con imágenes de muestra, análisis de precios y recomendaciones para ayudarte a elegir el mejor generador de imágenes IA para tus necesidades.",

        heading1: "Resumen Ejecutivo",
        heading2: "Comparación Rápida",
        heading3: "Calidad de Imagen y Estética",
        heading4: "Precisión del Prompt",
        heading5: "Desglose de Precios",
        heading6: "Interfaz y Flujo de Trabajo",
        heading7: "Recomendaciones de Casos de Uso",
        heading8: "Fortalezas y Debilidades",
        heading9: "Veredicto Final",

        subheading3_1: "Midjourney V6: Excelencia Artística",
        subheading3_2: "DALL-E 3: Precisión Fotorrealista",
        subheading5_1: "Midjourney",
        subheading5_2: "DALL-E 3",
        subheading6_1: "Midjourney (Discord)",
        subheading6_2: "DALL-E 3 (ChatGPT)",
        subheading7_1: "Elige Midjourney si necesitas:",
        subheading7_2: "Elige DALL-E 3 si necesitas:",
        subheading8_1: "Midjourney V6",
        subheading8_2: "DALL-E 3",

        para1_1: "Midjourney V6 sobresale en crear imágenes artísticas impresionantes con detalle excepcional y calidad estética. Es perfecto para profesionales creativos, artistas y cualquiera que valore la belleza y el arte.",
        para1_2: "DALL-E 3 se enfoca en la precisión del prompt y el fotorrealismo. Es ideal para visualizaciones precisas, materiales de marketing y usuarios que necesitan resultados confiables y consistentes integrados con ChatGPT.",

        tableFeature: "Característica",
        tableMidjourney: "Midjourney V6",
        tableDallE: "DALL-E 3",
        tablePricing: "Precio",
        tablePricingMJ: "$10-60/mes",
        tablePricingDE: "$20/mes (ChatGPT Plus)",
        tableInterface: "Interfaz",
        tableInterfaceMJ: "Discord",
        tableInterfaceDE: "ChatGPT",
        tableImageQuality: "Calidad de Imagen",
        tableImageQualityMJ: "10/10 - Impresionante",
        tableImageQualityDE: "8/10 - Excelente",
        tablePromptAccuracy: "Precisión del Prompt",
        tablePromptAccuracyMJ: "7/10 - Interpretación creativa",
        tablePromptAccuracyDE: "9/10 - Muy preciso",
        tableTextInImages: "Texto en Imágenes",
        tableTextMJ: "Limitado",
        tableTextDE: "Muy bueno",
        tableStyleOptions: "Opciones de Estilo",
        tableStyleMJ: "Extenso",
        tableStyleDE: "Moderado",
        tableSpeed: "Velocidad",
        tableSpeedMJ: "~60 segundos",
        tableSpeedDE: "~30 segundos",
        tableEditing: "Edición",
        tableEditingMJ: "Variar, Zoom, Panorámica",
        tableEditingDE: "Variaciones limitadas",
        tableCommercial: "Uso Comercial",
        tableCommercialMJ: "Permitido (planes pagos)",
        tableCommercialDE: "Permitido",

        para3_1: "Midjourney ha construido su reputación produciendo imágenes increíblemente hermosas. La versión 6 ofrece:",
        list3_1_1: "Detalle excepcional:",
        list3_1_1_desc: " Textura, iluminación y profundidad increíbles",
        list3_1_2: "Coherencia artística:",
        list3_1_2_desc: " Imágenes que se sienten profesionalmente compuestas",
        list3_1_3: "Versatilidad de estilo:",
        list3_1_3_desc: " Desde fotorrealismo hasta arte abstracto",
        list3_1_4: "Calidad cinematográfica:",
        list3_1_4_desc: " Perfecto para arte conceptual y narrativa",

        para3_2: "DALL-E 3 se enfoca en precisión y fotorrealismo:",
        list3_2_1: "Fotorrealismo consistente:",
        list3_2_1_desc: " Imágenes realistas confiables",
        list3_2_2: "Representaciones precisas:",
        list3_2_2_desc: " Objetos y escenas coinciden con las descripciones precisamente",
        list3_2_3: "Renderizado de texto:",
        list3_2_3_desc: " Puede generar texto legible en imágenes (logos, letreros)",
        list3_2_4: "Composiciones naturales:",
        list3_2_4_desc: " Menos aspecto \"generado por IA\"",

        para4_1: "DALL-E 3 gana aquí. Sigue los prompts más literalmente e incluye detalles específicos que solicitas. ChatGPT también ayuda a refinar tu prompt antes de la generación.",
        para4_2: "Midjourney toma libertades creativas, lo que puede producir resultados impresionantes pero puede no coincidir con tu visión exacta. A menudo necesitarás múltiples iteraciones.",

        list5_1_1: "Plan Básico:",
        list5_1_1_desc: " $10/mes (~200 imágenes)",
        list5_1_2: "Plan Estándar:",
        list5_1_2_desc: " $30/mes (~900 imágenes, modo Rápido)",
        list5_1_3: "Plan Pro:",
        list5_1_3_desc: " $60/mes (~1800 imágenes, modo Stealth)",

        list5_2_1: "ChatGPT Plus:",
        list5_2_1_desc: " $20/mes (incluye todas las funciones de ChatGPT)",
        list5_2_2: "Límite de velocidad: ~40 imágenes/3 horas",
        list5_2_3: "Sin precio independiente—debe suscribirse a ChatGPT Plus",

        para5_1: "Ganador en Valor: DALL-E 3 si ya quieres ChatGPT Plus. Midjourney Basic ($10) si solo necesitas generación de imágenes.",

        list6_1_1: "Requiere cuenta de Discord",
        list6_1_2: "Escribe \"/imagine\" + prompt en Discord",
        list6_1_3: "Las imágenes aparecen en canales públicos (a menos que sea Pro con Stealth)",
        list6_1_4: "Herramientas de edición potentes (Variar, Zoom Out, Pan)",
        list6_1_5: "Curva de aprendizaje más pronunciada",

        list6_2_1: "Integrado en la interfaz de ChatGPT",
        list6_2_2: "Conversación en lenguaje natural",
        list6_2_3: "ChatGPT refina tu prompt automáticamente",
        list6_2_4: "Generación privada",
        list6_2_5: "Más intuitivo para principiantes",

        list7_1_1: "Arte impresionante para proyectos creativos",
        list7_1_2: "Arte conceptual, diseño de personajes, construcción de mundos",
        list7_1_3: "Impresiones de arte fino o piezas de portafolio",
        list7_1_4: "Imágenes de fantasía, ciencia ficción o estilizadas",
        list7_1_5: "Máxima calidad estética",

        list7_2_1: "Visualizaciones precisas para presentaciones",
        list7_2_2: "Materiales de marketing con marca específica",
        list7_2_3: "Imágenes con texto legible (logos, infografías)",
        list7_2_4: "Maquetas de productos fotorrealistas",
        list7_2_5: "Integración con ChatGPT para creación de contenido",
        list7_2_6: "Interfaz simple y amigable para principiantes",

        strengthsLabel: "Fortalezas:",
        weaknessesLabel: "Debilidades:",

        list8_1_s1: "Calidad de imagen y estética de mejor clase",
        list8_1_s2: "Herramientas de edición y variación potentes",
        list8_1_s3: "Gran comunidad creativa para inspiración",
        list8_1_s4: "Niveles de precios flexibles",

        list8_1_w1: "El flujo de trabajo basado en Discord puede ser confuso",
        list8_1_w2: "Menos precisión al seguir prompts",
        list8_1_w3: "Pobre renderizado de texto en imágenes",
        list8_1_w4: "Generación pública (a menos que sea plan Pro)",

        list8_2_s1: "Excelente precisión de prompt",
        list8_2_s2: "Integrado con ChatGPT",
        list8_2_s3: "Buen renderizado de texto",
        list8_2_s4: "Interfaz amigable para el usuario",
        list8_2_s5: "Generación privada",

        list8_2_w1: "Requiere suscripción a ChatGPT Plus",
        list8_2_w2: "Capacidades de edición limitadas",
        list8_2_w3: "Menos opciones de estilo",
        list8_2_w4: "Los límites de velocidad pueden ser restrictivos",

        para9_1: "Para Artistas y Creativos:",
        para9_1_desc: " Midjourney V6. La calidad de imagen es inigualable y las posibilidades creativas son infinitas.",
        para9_2: "Para Negocios y Marketing:",
        para9_2_desc: " DALL-E 3. La precisión del prompt, renderizado de texto e integración con ChatGPT lo hacen más práctico para aplicaciones comerciales.",
        para9_3: "Para Principiantes:",
        para9_3_desc: " DALL-E 3. La interfaz de ChatGPT es más intuitiva y obtienes herramientas de escritura IA incluidas.",
        para9_4: "Mejor Valor:",
        para9_4_desc: " Si necesitas tanto generación de imágenes como un asistente IA, DALL-E 3 vía ChatGPT Plus ($20/mes) es excelente valor. Si solo necesitas imágenes, Midjourney Basic ($10/mes) es más barato.",
        para9_5: "La Configuración Definitiva:",
        para9_5_desc: " ¡Suscríbete a ambos! Muchos usuarios avanzados usan Midjourney para trabajo artístico y DALL-E 3 para visualizaciones precisas y prácticas. Costo combinado: $30-50/mes.",

        footerDesc: "Tu fuente confiable de reseñas, comparaciones y guías de herramientas IA.",
        footerCategories: "Categorías",
        footerResources: "Recursos",
        footerCopyright: "© 2026 GenuisNet.ai. Todos los derechos reservados."
    },

    fr: {
        pageTitle: "Midjourney V6 vs DALL-E 3 : L'Affrontement Ultime de Génération d'Images | GenuisNet.ai",
        metaDescription: "Comparaison Midjourney V6 vs DALL-E 3 2026. Analyse détaillée avec exemples d'images, répartition des prix et recommandations pour choisir le meilleur générateur d'images IA.",
        metaKeywords: "Midjourney vs DALL-E 3, génération d'images IA, Midjourney V6, DALL-E 3, art IA",

        heroTitle: "Midjourney V6 vs DALL-E 3 : L'Affrontement Ultime de Génération d'Images",
        heroExcerpt: "Comparaison détaillée avec exemples d'images, analyse des prix et recommandations pour vous aider à choisir le meilleur générateur d'images IA pour vos besoins.",

        heading1: "Résumé Exécutif",
        heading2: "Comparaison Rapide",
        heading3: "Qualité d'Image et Esthétique",
        heading4: "Précision du Prompt",
        heading5: "Répartition des Prix",
        heading6: "Interface et Flux de Travail",
        heading7: "Recommandations de Cas d'Usage",
        heading8: "Forces et Faiblesses",
        heading9: "Verdict Final",

        subheading3_1: "Midjourney V6 : Excellence Artistique",
        subheading3_2: "DALL-E 3 : Précision Photoréaliste",
        subheading5_1: "Midjourney",
        subheading5_2: "DALL-E 3",
        subheading6_1: "Midjourney (Discord)",
        subheading6_2: "DALL-E 3 (ChatGPT)",
        subheading7_1: "Choisissez Midjourney si vous avez besoin :",
        subheading7_2: "Choisissez DALL-E 3 si vous avez besoin :",
        subheading8_1: "Midjourney V6",
        subheading8_2: "DALL-E 3",

        para1_1: "Midjourney V6 excelle dans la création d'images artistiques époustouflantes avec un détail exceptionnel et une qualité esthétique. C'est parfait pour les professionnels créatifs, les artistes et tous ceux qui apprécient la beauté et l'art.",
        para1_2: "DALL-E 3 se concentre sur la précision du prompt et le photoréalisme. Il est idéal pour les visualisations précises, les supports marketing et les utilisateurs qui ont besoin de résultats fiables et cohérents intégrés à ChatGPT.",

        tableFeature: "Fonctionnalité",
        tableMidjourney: "Midjourney V6",
        tableDallE: "DALL-E 3",
        tablePricing: "Tarification",
        tablePricingMJ: "10-60$/mois",
        tablePricingDE: "20$/mois (ChatGPT Plus)",
        tableInterface: "Interface",
        tableInterfaceMJ: "Discord",
        tableInterfaceDE: "ChatGPT",
        tableImageQuality: "Qualité d'Image",
        tableImageQualityMJ: "10/10 - Époustouflant",
        tableImageQualityDE: "8/10 - Excellent",
        tablePromptAccuracy: "Précision du Prompt",
        tablePromptAccuracyMJ: "7/10 - Interprétation créative",
        tablePromptAccuracyDE: "9/10 - Très précis",
        tableTextInImages: "Texte dans les Images",
        tableTextMJ: "Limité",
        tableTextDE: "Très bon",
        tableStyleOptions: "Options de Style",
        tableStyleMJ: "Extensif",
        tableStyleDE: "Modéré",
        tableSpeed: "Vitesse",
        tableSpeedMJ: "~60 secondes",
        tableSpeedDE: "~30 secondes",
        tableEditing: "Édition",
        tableEditingMJ: "Varier, Zoom, Panoramique",
        tableEditingDE: "Variations limitées",
        tableCommercial: "Usage Commercial",
        tableCommercialMJ: "Autorisé (plans payants)",
        tableCommercialDE: "Autorisé",

        para3_1: "Midjourney a bâti sa réputation en produisant des images d'une beauté à couper le souffle. La version 6 offre :",
        list3_1_1: "Détail exceptionnel :",
        list3_1_1_desc: " Texture, éclairage et profondeur incroyables",
        list3_1_2: "Cohérence artistique :",
        list3_1_2_desc: " Images qui semblent composées professionnellement",
        list3_1_3: "Polyvalence de style :",
        list3_1_3_desc: " Du photoréalisme à l'art abstrait",
        list3_1_4: "Qualité cinématographique :",
        list3_1_4_desc: " Parfait pour l'art conceptuel et la narration",

        para3_2: "DALL-E 3 se concentre sur la précision et le photoréalisme :",
        list3_2_1: "Photoréalisme cohérent :",
        list3_2_1_desc: " Images réalistes fiables",
        list3_2_2: "Représentations précises :",
        list3_2_2_desc: " Les objets et scènes correspondent précisément aux descriptions",
        list3_2_3: "Rendu de texte :",
        list3_2_3_desc: " Peut générer du texte lisible dans les images (logos, panneaux)",
        list3_2_4: "Compositions naturelles :",
        list3_2_4_desc: " Moins d'aspect \"généré par IA\"",

        para4_1: "DALL-E 3 gagne ici. Il suit les prompts plus littéralement et inclut des détails spécifiques que vous demandez. ChatGPT aide également à affiner votre prompt avant la génération.",
        para4_2: "Midjourney prend des libertés créatives, ce qui peut produire des résultats époustouflants mais peut ne pas correspondre à votre vision exacte. Vous aurez souvent besoin de plusieurs itérations.",

        list5_1_1: "Plan Basique :",
        list5_1_1_desc: " 10$/mois (~200 images)",
        list5_1_2: "Plan Standard :",
        list5_1_2_desc: " 30$/mois (~900 images, mode Rapide)",
        list5_1_3: "Plan Pro :",
        list5_1_3_desc: " 60$/mois (~1800 images, mode Stealth)",

        list5_2_1: "ChatGPT Plus :",
        list5_2_1_desc: " 20$/mois (inclut toutes les fonctionnalités ChatGPT)",
        list5_2_2: "Limite de taux : ~40 images/3 heures",
        list5_2_3: "Pas de tarification autonome—doit s'abonner à ChatGPT Plus",

        para5_1: "Meilleur Rapport Qualité-Prix : DALL-E 3 si vous voulez déjà ChatGPT Plus. Midjourney Basic (10$) si vous avez besoin uniquement de génération d'images.",

        list6_1_1: "Nécessite un compte Discord",
        list6_1_2: "Tapez \"/imagine\" + prompt dans Discord",
        list6_1_3: "Les images apparaissent dans les canaux publics (sauf si Pro avec Stealth)",
        list6_1_4: "Outils d'édition puissants (Varier, Zoom Out, Pan)",
        list6_1_5: "Courbe d'apprentissage plus raide",

        list6_2_1: "Intégré dans l'interface ChatGPT",
        list6_2_2: "Conversation en langage naturel",
        list6_2_3: "ChatGPT affine votre prompt automatiquement",
        list6_2_4: "Génération privée",
        list6_2_5: "Plus intuitif pour les débutants",

        list7_1_1: "Œuvres d'art époustouflantes pour projets créatifs",
        list7_1_2: "Art conceptuel, design de personnages, construction de monde",
        list7_1_3: "Impressions d'art ou pièces de portfolio",
        list7_1_4: "Imagerie fantastique, science-fiction ou stylisée",
        list7_1_5: "Qualité esthétique maximale",

        list7_2_1: "Visualisations précises pour présentations",
        list7_2_2: "Supports marketing avec image de marque spécifique",
        list7_2_3: "Images avec texte lisible (logos, infographies)",
        list7_2_4: "Maquettes de produits photoréalistes",
        list7_2_5: "Intégration avec ChatGPT pour création de contenu",
        list7_2_6: "Interface simple et conviviale pour débutants",

        strengthsLabel: "Forces :",
        weaknessesLabel: "Faiblesses :",

        list8_1_s1: "Qualité d'image et esthétique de classe mondiale",
        list8_1_s2: "Outils d'édition et de variation puissants",
        list8_1_s3: "Grande communauté créative pour l'inspiration",
        list8_1_s4: "Niveaux de tarification flexibles",

        list8_1_w1: "Le flux de travail basé sur Discord peut être déroutant",
        list8_1_w2: "Moins de précision dans le suivi des prompts",
        list8_1_w3: "Mauvais rendu de texte dans les images",
        list8_1_w4: "Génération publique (sauf si plan Pro)",

        list8_2_s1: "Excellente précision de prompt",
        list8_2_s2: "Intégré avec ChatGPT",
        list8_2_s3: "Bon rendu de texte",
        list8_2_s4: "Interface conviviale",
        list8_2_s5: "Génération privée",

        list8_2_w1: "Nécessite un abonnement ChatGPT Plus",
        list8_2_w2: "Capacités d'édition limitées",
        list8_2_w3: "Moins d'options de style",
        list8_2_w4: "Les limites de taux peuvent être restrictives",

        para9_1: "Pour les Artistes et Créatifs :",
        para9_1_desc: " Midjourney V6. La qualité d'image est inégalée et les possibilités créatives sont infinies.",
        para9_2: "Pour les Affaires et le Marketing :",
        para9_2_desc: " DALL-E 3. La précision du prompt, le rendu de texte et l'intégration ChatGPT le rendent plus pratique pour les applications commerciales.",
        para9_3: "Pour les Débutants :",
        para9_3_desc: " DALL-E 3. L'interface ChatGPT est plus intuitive et vous obtenez des outils d'écriture IA inclus.",
        para9_4: "Meilleur Rapport Qualité-Prix :",
        para9_4_desc: " Si vous avez besoin à la fois de génération d'images et d'un assistant IA, DALL-E 3 via ChatGPT Plus (20$/mois) est d'excellent rapport qualité-prix. Si vous n'avez besoin que d'images, Midjourney Basic (10$/mois) est moins cher.",
        para9_5: "La Configuration Ultime :",
        para9_5_desc: " Abonnez-vous aux deux ! De nombreux utilisateurs expérimentés utilisent Midjourney pour le travail artistique et DALL-E 3 pour les visualisations précises et pratiques. Coût combiné : 30-50$/mois.",

        footerDesc: "Votre source de confiance pour les avis, comparaisons et guides d'outils IA.",
        footerCategories: "Catégories",
        footerResources: "Ressources",
        footerCopyright: "© 2026 GenuisNet.ai. Tous droits réservés."
    },

    de: {
        pageTitle: "Midjourney V6 vs DALL-E 3: Der Ultimative Bildgenerierungs-Vergleich | GenuisNet.ai",
        metaDescription: "Midjourney V6 vs DALL-E 3 Vergleich 2026. Detaillierte Analyse mit Beispielbildern, Preisaufschlüsselung und Empfehlungen zur Auswahl des besten KI-Bildgenerators.",
        metaKeywords: "Midjourney vs DALL-E 3, KI-Bildgenerierung, Midjourney V6, DALL-E 3, KI-Kunst",

        heroTitle: "Midjourney V6 vs DALL-E 3: Der Ultimative Bildgenerierungs-Vergleich",
        heroExcerpt: "Detaillierter Vergleich mit Beispielbildern, Preisanalyse und Empfehlungen, um Ihnen bei der Auswahl des besten KI-Bildgenerators für Ihre Bedürfnisse zu helfen.",

        heading1: "Zusammenfassung",
        heading2: "Schneller Vergleich",
        heading3: "Bildqualität und Ästhetik",
        heading4: "Prompt-Genauigkeit",
        heading5: "Preisaufschlüsselung",
        heading6: "Benutzeroberfläche und Workflow",
        heading7: "Anwendungsfall-Empfehlungen",
        heading8: "Stärken und Schwächen",
        heading9: "Endgültiges Urteil",

        subheading3_1: "Midjourney V6: Künstlerische Exzellenz",
        subheading3_2: "DALL-E 3: Fotorealistische Präzision",
        subheading5_1: "Midjourney",
        subheading5_2: "DALL-E 3",
        subheading6_1: "Midjourney (Discord)",
        subheading6_2: "DALL-E 3 (ChatGPT)",
        subheading7_1: "Wählen Sie Midjourney, wenn Sie Folgendes benötigen:",
        subheading7_2: "Wählen Sie DALL-E 3, wenn Sie Folgendes benötigen:",
        subheading8_1: "Midjourney V6",
        subheading8_2: "DALL-E 3",

        para1_1: "Midjourney V6 glänzt bei der Erstellung atemberaubender, künstlerischer Bilder mit außergewöhnlichen Details und ästhetischer Qualität. Es ist perfekt für kreative Profis, Künstler und alle, die Schönheit und Kunst schätzen.",
        para1_2: "DALL-E 3 konzentriert sich auf Prompt-Genauigkeit und Fotorealismus. Es ist ideal für präzise Visualisierungen, Marketingmaterialien und Benutzer, die zuverlässige, konsistente Ergebnisse in ChatGPT integriert benötigen.",

        tableFeature: "Funktion",
        tableMidjourney: "Midjourney V6",
        tableDallE: "DALL-E 3",
        tablePricing: "Preisgestaltung",
        tablePricingMJ: "$10-60/Monat",
        tablePricingDE: "$20/Monat (ChatGPT Plus)",
        tableInterface: "Benutzeroberfläche",
        tableInterfaceMJ: "Discord",
        tableInterfaceDE: "ChatGPT",
        tableImageQuality: "Bildqualität",
        tableImageQualityMJ: "10/10 - Atemberaubend",
        tableImageQualityDE: "8/10 - Ausgezeichnet",
        tablePromptAccuracy: "Prompt-Genauigkeit",
        tablePromptAccuracyMJ: "7/10 - Kreative Interpretation",
        tablePromptAccuracyDE: "9/10 - Sehr präzise",
        tableTextInImages: "Text in Bildern",
        tableTextMJ: "Begrenzt",
        tableTextDE: "Sehr gut",
        tableStyleOptions: "Stiloptionen",
        tableStyleMJ: "Umfangreich",
        tableStyleDE: "Moderat",
        tableSpeed: "Geschwindigkeit",
        tableSpeedMJ: "~60 Sekunden",
        tableSpeedDE: "~30 Sekunden",
        tableEditing: "Bearbeitung",
        tableEditingMJ: "Variieren, Zoom, Schwenken",
        tableEditingDE: "Begrenzte Variationen",
        tableCommercial: "Kommerzielle Nutzung",
        tableCommercialMJ: "Erlaubt (Bezahlpläne)",
        tableCommercialDE: "Erlaubt",

        para3_1: "Midjourney hat seinen Ruf damit aufgebaut, atemberaubend schöne Bilder zu produzieren. Version 6 liefert:",
        list3_1_1: "Außergewöhnliche Details:",
        list3_1_1_desc: " Unglaubliche Textur, Beleuchtung und Tiefe",
        list3_1_2: "Künstlerische Kohärenz:",
        list3_1_2_desc: " Bilder, die professionell komponiert wirken",
        list3_1_3: "Stilvielfalt:",
        list3_1_3_desc: " Vom Fotorealismus bis zur abstrakten Kunst",
        list3_1_4: "Filmische Qualität:",
        list3_1_4_desc: " Perfekt für Konzeptkunst und Geschichtenerzählen",

        para3_2: "DALL-E 3 konzentriert sich auf Genauigkeit und Fotorealismus:",
        list3_2_1: "Konsistenter Fotorealismus:",
        list3_2_1_desc: " Zuverlässige realistische Bilder",
        list3_2_2: "Präzise Darstellungen:",
        list3_2_2_desc: " Objekte und Szenen entsprechen präzise den Beschreibungen",
        list3_2_3: "Textwiedergabe:",
        list3_2_3_desc: " Kann lesbaren Text in Bildern generieren (Logos, Schilder)",
        list3_2_4: "Natürliche Kompositionen:",
        list3_2_4_desc: " Weniger \"KI-generiertes\" Aussehen",

        para4_1: "DALL-E 3 gewinnt hier. Es folgt Prompts wörtlicher und enthält spezifische Details, die Sie anfordern. ChatGPT hilft auch dabei, Ihren Prompt vor der Generierung zu verfeinern.",
        para4_2: "Midjourney nimmt kreative Freiheiten, was atemberaubende Ergebnisse erzeugen kann, aber möglicherweise nicht Ihrer genauen Vision entspricht. Sie benötigen oft mehrere Iterationen.",

        list5_1_1: "Basic Plan:",
        list5_1_1_desc: " $10/Monat (~200 Bilder)",
        list5_1_2: "Standard Plan:",
        list5_1_2_desc: " $30/Monat (~900 Bilder, Fast-Modus)",
        list5_1_3: "Pro Plan:",
        list5_1_3_desc: " $60/Monat (~1800 Bilder, Stealth-Modus)",

        list5_2_1: "ChatGPT Plus:",
        list5_2_1_desc: " $20/Monat (enthält alle ChatGPT-Funktionen)",
        list5_2_2: "Ratenlimit: ~40 Bilder/3 Stunden",
        list5_2_3: "Keine eigenständige Preisgestaltung—muss ChatGPT Plus abonnieren",

        para5_1: "Wert-Sieger: DALL-E 3, wenn Sie bereits ChatGPT Plus wollen. Midjourney Basic ($10), wenn Sie nur Bildgenerierung benötigen.",

        list6_1_1: "Erfordert Discord-Konto",
        list6_1_2: "\"/imagine\" + Prompt in Discord eingeben",
        list6_1_3: "Bilder erscheinen in öffentlichen Kanälen (außer bei Pro mit Stealth)",
        list6_1_4: "Leistungsstarke Bearbeitungswerkzeuge (Variieren, Zoom Out, Pan)",
        list6_1_5: "Steilere Lernkurve",

        list6_2_1: "In ChatGPT-Oberfläche integriert",
        list6_2_2: "Natürlichsprachliche Konversation",
        list6_2_3: "ChatGPT verfeinert Ihren Prompt automatisch",
        list6_2_4: "Private Generierung",
        list6_2_5: "Intuitiver für Anfänger",

        list7_1_1: "Atemberaubende Kunstwerke für kreative Projekte",
        list7_1_2: "Konzeptkunst, Charakterdesign, Weltenbau",
        list7_1_3: "Kunstdrucke oder Portfolio-Stücke",
        list7_1_4: "Fantasy-, Sci-Fi- oder stilisierte Bilder",
        list7_1_5: "Maximale ästhetische Qualität",

        list7_2_1: "Präzise Visualisierungen für Präsentationen",
        list7_2_2: "Marketingmaterialien mit spezifischem Branding",
        list7_2_3: "Bilder mit lesbarem Text (Logos, Infografiken)",
        list7_2_4: "Fotorealistische Produktmodelle",
        list7_2_5: "Integration mit ChatGPT für Content-Erstellung",
        list7_2_6: "Einfache, benutzerfreundliche Oberfläche",

        strengthsLabel: "Stärken:",
        weaknessesLabel: "Schwächen:",

        list8_1_s1: "Erstklassige Bildqualität und Ästhetik",
        list8_1_s2: "Leistungsstarke Bearbeitungs- und Variationswerkzeuge",
        list8_1_s3: "Große kreative Community für Inspiration",
        list8_1_s4: "Flexible Preisniveaus",

        list8_1_w1: "Discord-basierter Workflow kann verwirrend sein",
        list8_1_w2: "Weniger genaue Prompt-Befolgung",
        list8_1_w3: "Schlechte Textwiedergabe in Bildern",
        list8_1_w4: "Öffentliche Generierung (außer bei Pro-Plan)",

        list8_2_s1: "Ausgezeichnete Prompt-Genauigkeit",
        list8_2_s2: "Integriert mit ChatGPT",
        list8_2_s3: "Gute Textwiedergabe",
        list8_2_s4: "Benutzerfreundliche Oberfläche",
        list8_2_s5: "Private Generierung",

        list8_2_w1: "Erfordert ChatGPT Plus-Abonnement",
        list8_2_w2: "Begrenzte Bearbeitungsmöglichkeiten",
        list8_2_w3: "Weniger Stiloptionen",
        list8_2_w4: "Ratenlimits können restriktiv sein",

        para9_1: "Für Künstler und Kreative:",
        para9_1_desc: " Midjourney V6. Die Bildqualität ist unübertroffen und die kreativen Möglichkeiten sind endlos.",
        para9_2: "Für Business und Marketing:",
        para9_2_desc: " DALL-E 3. Prompt-Genauigkeit, Textwiedergabe und ChatGPT-Integration machen es praktischer für kommerzielle Anwendungen.",
        para9_3: "Für Anfänger:",
        para9_3_desc: " DALL-E 3. Die ChatGPT-Oberfläche ist intuitiver und Sie erhalten KI-Schreibwerkzeuge inklusive.",
        para9_4: "Bester Wert:",
        para9_4_desc: " Wenn Sie sowohl Bildgenerierung als auch einen KI-Assistenten benötigen, ist DALL-E 3 über ChatGPT Plus ($20/Monat) ein ausgezeichneter Wert. Wenn Sie nur Bilder benötigen, ist Midjourney Basic ($10/Monat) günstiger.",
        para9_5: "Das Ultimative Setup:",
        para9_5_desc: " Abonnieren Sie beide! Viele Power-User verwenden Midjourney für künstlerische Arbeit und DALL-E 3 für präzise, praktische Visualisierungen. Kombinierte Kosten: $30-50/Monat.",

        footerDesc: "Ihre vertrauenswürdige Quelle für KI-Tool-Bewertungen, Vergleiche und Leitfäden.",
        footerCategories: "Kategorien",
        footerResources: "Ressourcen",
        footerCopyright: "© 2026 GenuisNet.ai. Alle Rechte vorbehalten."
    },

    pt: {
        pageTitle: "Midjourney V6 vs DALL-E 3: O Confronto Definitivo de Geração de Imagens | GenuisNet.ai",
        metaDescription: "Comparação Midjourney V6 vs DALL-E 3 2026. Análise detalhada com imagens de amostra, detalhamento de preços e recomendações para escolher o melhor gerador de imagens IA.",
        metaKeywords: "Midjourney vs DALL-E 3, geração de imagens IA, Midjourney V6, DALL-E 3, arte IA",

        heroTitle: "Midjourney V6 vs DALL-E 3: O Confronto Definitivo de Geração de Imagens",
        heroExcerpt: "Comparação detalhada com imagens de amostra, análise de preços e recomendações para ajudá-lo a escolher o melhor gerador de imagens IA para suas necessidades.",

        heading1: "Resumo Executivo",
        heading2: "Comparação Rápida",
        heading3: "Qualidade de Imagem e Estética",
        heading4: "Precisão do Prompt",
        heading5: "Detalhamento de Preços",
        heading6: "Interface e Fluxo de Trabalho",
        heading7: "Recomendações de Casos de Uso",
        heading8: "Pontos Fortes e Fracos",
        heading9: "Veredicto Final",

        subheading3_1: "Midjourney V6: Excelência Artística",
        subheading3_2: "DALL-E 3: Precisão Fotorrealista",
        subheading5_1: "Midjourney",
        subheading5_2: "DALL-E 3",
        subheading6_1: "Midjourney (Discord)",
        subheading6_2: "DALL-E 3 (ChatGPT)",
        subheading7_1: "Escolha Midjourney se você precisa:",
        subheading7_2: "Escolha DALL-E 3 se você precisa:",
        subheading8_1: "Midjourney V6",
        subheading8_2: "DALL-E 3",

        para1_1: "Midjourney V6 se destaca na criação de imagens artísticas deslumbrantes com detalhes excepcionais e qualidade estética. É perfeito para profissionais criativos, artistas e qualquer pessoa que valorize beleza e arte.",
        para1_2: "DALL-E 3 foca em precisão de prompt e fotorrealismo. É ideal para visualizações precisas, materiais de marketing e usuários que precisam de resultados confiáveis e consistentes integrados ao ChatGPT.",

        tableFeature: "Recurso",
        tableMidjourney: "Midjourney V6",
        tableDallE: "DALL-E 3",
        tablePricing: "Preço",
        tablePricingMJ: "$10-60/mês",
        tablePricingDE: "$20/mês (ChatGPT Plus)",
        tableInterface: "Interface",
        tableInterfaceMJ: "Discord",
        tableInterfaceDE: "ChatGPT",
        tableImageQuality: "Qualidade de Imagem",
        tableImageQualityMJ: "10/10 - Deslumbrante",
        tableImageQualityDE: "8/10 - Excelente",
        tablePromptAccuracy: "Precisão do Prompt",
        tablePromptAccuracyMJ: "7/10 - Interpretação criativa",
        tablePromptAccuracyDE: "9/10 - Muito preciso",
        tableTextInImages: "Texto em Imagens",
        tableTextMJ: "Limitado",
        tableTextDE: "Muito bom",
        tableStyleOptions: "Opções de Estilo",
        tableStyleMJ: "Extenso",
        tableStyleDE: "Moderado",
        tableSpeed: "Velocidade",
        tableSpeedMJ: "~60 segundos",
        tableSpeedDE: "~30 segundos",
        tableEditing: "Edição",
        tableEditingMJ: "Variar, Zoom, Panorâmica",
        tableEditingDE: "Variações limitadas",
        tableCommercial: "Uso Comercial",
        tableCommercialMJ: "Permitido (planos pagos)",
        tableCommercialDE: "Permitido",

        para3_1: "Midjourney construiu sua reputação produzindo imagens de beleza de tirar o fôlego. A versão 6 oferece:",
        list3_1_1: "Detalhes excepcionais:",
        list3_1_1_desc: " Textura, iluminação e profundidade incríveis",
        list3_1_2: "Coerência artística:",
        list3_1_2_desc: " Imagens que parecem profissionalmente compostas",
        list3_1_3: "Versatilidade de estilo:",
        list3_1_3_desc: " De fotorrealismo a arte abstrata",
        list3_1_4: "Qualidade cinematográfica:",
        list3_1_4_desc: " Perfeito para arte conceitual e narrativa",

        para3_2: "DALL-E 3 foca em precisão e fotorrealismo:",
        list3_2_1: "Fotorrealismo consistente:",
        list3_2_1_desc: " Imagens realistas confiáveis",
        list3_2_2: "Representações precisas:",
        list3_2_2_desc: " Objetos e cenas correspondem precisamente às descrições",
        list3_2_3: "Renderização de texto:",
        list3_2_3_desc: " Pode gerar texto legível em imagens (logos, placas)",
        list3_2_4: "Composições naturais:",
        list3_2_4_desc: " Menos aparência \"gerada por IA\"",

        para4_1: "DALL-E 3 vence aqui. Ele segue prompts mais literalmente e inclui detalhes específicos que você solicita. ChatGPT também ajuda a refinar seu prompt antes da geração.",
        para4_2: "Midjourney toma liberdades criativas, o que pode produzir resultados deslumbrantes, mas pode não corresponder à sua visão exata. Você frequentemente precisará de múltiplas iterações.",

        list5_1_1: "Plano Básico:",
        list5_1_1_desc: " $10/mês (~200 imagens)",
        list5_1_2: "Plano Padrão:",
        list5_1_2_desc: " $30/mês (~900 imagens, modo Rápido)",
        list5_1_3: "Plano Pro:",
        list5_1_3_desc: " $60/mês (~1800 imagens, modo Stealth)",

        list5_2_1: "ChatGPT Plus:",
        list5_2_1_desc: " $20/mês (inclui todos os recursos do ChatGPT)",
        list5_2_2: "Limite de taxa: ~40 imagens/3 horas",
        list5_2_3: "Sem preço autônomo—deve assinar ChatGPT Plus",

        para5_1: "Vencedor em Valor: DALL-E 3 se você já quer ChatGPT Plus. Midjourney Basic ($10) se você só precisa de geração de imagens.",

        list6_1_1: "Requer conta Discord",
        list6_1_2: "Digite \"/imagine\" + prompt no Discord",
        list6_1_3: "Imagens aparecem em canais públicos (a menos que seja Pro com Stealth)",
        list6_1_4: "Ferramentas de edição poderosas (Variar, Zoom Out, Pan)",
        list6_1_5: "Curva de aprendizado mais íngreme",

        list6_2_1: "Integrado à interface ChatGPT",
        list6_2_2: "Conversação em linguagem natural",
        list6_2_3: "ChatGPT refina seu prompt automaticamente",
        list6_2_4: "Geração privada",
        list6_2_5: "Mais intuitivo para iniciantes",

        list7_1_1: "Arte deslumbrante para projetos criativos",
        list7_1_2: "Arte conceitual, design de personagens, construção de mundos",
        list7_1_3: "Impressões de arte ou peças de portfólio",
        list7_1_4: "Imagens de fantasia, ficção científica ou estilizadas",
        list7_1_5: "Máxima qualidade estética",

        list7_2_1: "Visualizações precisas para apresentações",
        list7_2_2: "Materiais de marketing com branding específico",
        list7_2_3: "Imagens com texto legível (logos, infográficos)",
        list7_2_4: "Maquetes de produtos fotorrealistas",
        list7_2_5: "Integração com ChatGPT para criação de conteúdo",
        list7_2_6: "Interface simples e amigável para iniciantes",

        strengthsLabel: "Pontos Fortes:",
        weaknessesLabel: "Pontos Fracos:",

        list8_1_s1: "Qualidade de imagem e estética de primeira classe",
        list8_1_s2: "Ferramentas de edição e variação poderosas",
        list8_1_s3: "Grande comunidade criativa para inspiração",
        list8_1_s4: "Níveis de preço flexíveis",

        list8_1_w1: "Fluxo de trabalho baseado em Discord pode ser confuso",
        list8_1_w2: "Menos precisão ao seguir prompts",
        list8_1_w3: "Renderização de texto ruim em imagens",
        list8_1_w4: "Geração pública (a menos que seja plano Pro)",

        list8_2_s1: "Excelente precisão de prompt",
        list8_2_s2: "Integrado com ChatGPT",
        list8_2_s3: "Boa renderização de texto",
        list8_2_s4: "Interface amigável",
        list8_2_s5: "Geração privada",

        list8_2_w1: "Requer assinatura ChatGPT Plus",
        list8_2_w2: "Capacidades de edição limitadas",
        list8_2_w3: "Menos opções de estilo",
        list8_2_w4: "Limites de taxa podem ser restritivos",

        para9_1: "Para Artistas e Criativos:",
        para9_1_desc: " Midjourney V6. A qualidade da imagem é incomparável e as possibilidades criativas são infinitas.",
        para9_2: "Para Negócios e Marketing:",
        para9_2_desc: " DALL-E 3. Precisão de prompt, renderização de texto e integração ChatGPT o tornam mais prático para aplicações comerciais.",
        para9_3: "Para Iniciantes:",
        para9_3_desc: " DALL-E 3. A interface ChatGPT é mais intuitiva e você obtém ferramentas de escrita IA incluídas.",
        para9_4: "Melhor Valor:",
        para9_4_desc: " Se você precisa de geração de imagens e um assistente IA, DALL-E 3 via ChatGPT Plus ($20/mês) é excelente valor. Se você só precisa de imagens, Midjourney Basic ($10/mês) é mais barato.",
        para9_5: "A Configuração Definitiva:",
        para9_5_desc: " Assine ambos! Muitos usuários avançados usam Midjourney para trabalho artístico e DALL-E 3 para visualizações precisas e práticas. Custo combinado: $30-50/mês.",

        footerDesc: "Sua fonte confiável para avaliações, comparações e guias de ferramentas IA.",
        footerCategories: "Categorias",
        footerResources: "Recursos",
        footerCopyright: "© 2026 GenuisNet.ai. Todos os direitos reservados."
    },

    // Simplified versions for ZH, JA, KO, AR, HI (key elements only for brevity)
    zh: { pageTitle: "Midjourney V6 vs DALL-E 3：终极图像生成对决 | GenuisNet.ai", footerDesc: "您值得信赖的 AI 工具评论、比较和指南来源。", footerCategories: "类别", footerResources: "资源", footerCopyright: "© 2026 GenuisNet.ai. 保留所有权利。" },
    ja: { pageTitle: "Midjourney V6 vs DALL-E 3：究極の画像生成対決 | GenuisNet.ai", footerDesc: "AIツールのレビュー、比較、ガイドの信頼できる情報源。", footerCategories: "カテゴリー", footerResources: "リソース", footerCopyright: "© 2026 GenuisNet.ai. 全著作権所有。" },
    ko: { pageTitle: "Midjourney V6 vs DALL-E 3：궁극의 이미지 생성 대결 | GenuisNet.ai", footerDesc: "AI 도구 리뷰, 비교 및 가이드의 신뢰할 수 있는 출처.", footerCategories: "카테고리", footerResources: "리소스", footerCopyright: "© 2026 GenuisNet.ai. 모든 권리 보유." },
    ar: { pageTitle: "Midjourney V6 مقابل DALL-E 3: المواجهة النهائية لتوليد الصور | GenuisNet.ai", footerDesc: "مصدرك الموثوق لمراجعات ومقارنات وأدلة أدوات الذكاء الاصطناعي.", footerCategories: "الفئات", footerResources: "الموارد", footerCopyright: "© 2026 GenuisNet.ai. جميع الحقوق محفوظة." },
    hi: { pageTitle: "Midjourney V6 vs DALL-E 3: अंतिम छवि निर्माण टकराव | GenuisNet.ai", footerDesc: "AI टूल समीक्षाओं, तुलनाओं और गाइड के लिए आपका विश्वसनीय स्रोत।", footerCategories: "श्रेणियाँ", footerResources: "संसाधन", footerCopyright: "© 2026 GenuisNet.ai. सर्वाधिकार सुरक्षित।" }
};

// Initialize i18n for this article
function initArticleI18n() {
    console.log('🌍 Article i18n initializing...');
    const currentLang = localStorage.getItem('selectedLanguage') || 'en';
    console.log('📍 Current language:', currentLang);
    applyArticleTranslations(currentLang);

    document.addEventListener('languageChanged', (e) => {
        console.log('🔄 Language changed to:', e.detail.language);
        applyArticleTranslations(e.detail.language);
    });
    console.log('✅ Article i18n initialized successfully');
}

function applyArticleTranslations(lang) {
    console.log('🔧 Applying article translations for language:', lang);
    const t = articleTranslations[lang] || articleTranslations.en;

    // If language is simplified (ZH, JA, KO, AR, HI), only translate basic elements
    const isSimplifiedLang = ['zh', 'ja', 'ko', 'ar', 'hi'].includes(lang);

    // Update page title and meta
    document.title = t.pageTitle || articleTranslations.en.pageTitle;
    const metaDesc = document.querySelector('meta[name="description"]');
    const metaKeywords = document.querySelector('meta[name="keywords"]');
    if (metaDesc && t.metaDescription) metaDesc.content = t.metaDescription;
    if (metaKeywords && t.metaKeywords) metaKeywords.content = t.metaKeywords;

    // Get all elements with data-i18n attributes
    const i18nElements = document.querySelectorAll('[data-i18n]');
    console.log(`📍 Found ${i18nElements.length} elements with data-i18n attributes`);

    let translatedCount = 0;
    let skippedCount = 0;

    i18nElements.forEach(element => {
        const key = element.getAttribute('data-i18n');

        // For simplified languages, only translate basic elements (headings, hero, footer)
        if (isSimplifiedLang) {
            const isBasicElement = key.startsWith('heading') ||
                                   key.startsWith('hero') ||
                                   key.startsWith('footer') ||
                                   key.startsWith('table');
            if (!isBasicElement) {
                skippedCount++;
                return;
            }
        }

        // Get translation for this key
        const translation = t[key];

        if (translation) {
            // Handle different element types
            const tagName = element.tagName.toLowerCase();

            if (tagName === 'p' && element.querySelector('strong')) {
                // For paragraphs with strong tags, preserve the HTML structure
                const strongText = element.querySelector('strong').textContent;

                // Special handling for para1_1 and para1_2 (contains product names)
                if (key === 'para1_1' || key === 'para1_2') {
                    const productName = key === 'para1_1' ? 'Midjourney V6' : 'DALL-E 3';
                    element.innerHTML = `<strong>${productName}</strong> ${translation.replace(productName + ' ', '').replace(productName, '')}`;
                }
                // Special handling for Final Verdict paragraphs with labels
                else if (key.startsWith('para9_')) {
                    const labelKey = key.replace('_desc', '');
                    const label = t[labelKey];
                    const desc = t[key + '_desc'] || translation;
                    if (label && key.indexOf('_desc') === -1) {
                        element.innerHTML = `<strong>${label}</strong><span data-i18n="${key}_desc">${desc}</span>`;
                    } else if (key.indexOf('_desc') !== -1) {
                        element.textContent = translation;
                    }
                } else {
                    element.innerHTML = translation;
                }
            } else if (tagName === 'li' && (element.querySelector('strong') || element.querySelector('span[data-i18n]'))) {
                // For list items with strong tags and spans, handle each part separately
                const strong = element.querySelector('strong');
                const span = element.querySelector('span[data-i18n]');

                if (strong && strong.hasAttribute('data-i18n')) {
                    const strongKey = strong.getAttribute('data-i18n');
                    if (t[strongKey]) {
                        strong.textContent = t[strongKey];
                    }
                }

                if (span) {
                    const spanKey = span.getAttribute('data-i18n');
                    if (t[spanKey]) {
                        span.textContent = t[spanKey];
                    }
                }
            } else {
                // For simple elements, just replace text content
                element.textContent = translation;
            }

            translatedCount++;
        } else {
            // Translation key not found, use English fallback
            const fallback = articleTranslations.en[key];
            if (fallback && lang !== 'en') {
                element.textContent = fallback;
                console.warn(`⚠️ Translation key "${key}" not found for language "${lang}", using English fallback`);
            }
        }
    });

    console.log(`✅ Article translations applied: ${translatedCount} translated, ${skippedCount} skipped (simplified language)`);
}

// Initialize on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initArticleI18n);
} else {
    initArticleI18n();
}

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { articleTranslations, applyArticleTranslations };
}
