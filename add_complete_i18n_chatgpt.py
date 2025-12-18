#!/usr/bin/env python3
"""
Script COMPLET pour ajouter data-i18n à TOUS les éléments de chatgpt.html
Traite: Hero, Stats, CTA, Overview, Features, Pros/Cons, Pricing, Use Cases, Comparison, FAQ, Sidebar
"""

import json

def wrap_text(text, key):
    """Enveloppe le texte dans un span avec data-i18n"""
    return f'<span data-i18n="{key}">{text}</span>'

def add_complete_i18n():
    file_path = "GenuisNet.ai/pages/reviews/chatbots/chatgpt.html"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    translations_en = {}
    translations_es = {}
    count = 0

    # Liste de TOUS les remplacements (pattern, key, text_en, text_es)
    # Format: (old_html, new_html, key, text_en, text_es)

    replacements = [
        # ==================== HERO SECTION ====================
        ('ChatGPT Review 2026', 'review.chatgpt.title', 'ChatGPT Review 2026', 'Revisión de ChatGPT 2026'),
        ('by OpenAI', 'review.chatgpt.company', 'by OpenAI', 'por OpenAI'),
        ('Most Popular AI', 'review.chatgpt.badge.popular', 'Most Popular AI', 'IA Más Popular'),
        ('GPT-4 Turbo', 'review.chatgpt.badge.gpt4', 'GPT-4 Turbo', 'GPT-4 Turbo'),
        ('Free Tier Available', 'review.chatgpt.badge.free', 'Free Tier Available', 'Nivel Gratis Disponible'),
        ('Expert Rating', 'review.chatgpt.rating', 'Expert Rating', 'Calificación de Expertos'),

        # ==================== QUICK STATS ====================
        ('Monthly Active Users', 'review.chatgpt.stats.users', 'Monthly Active Users', 'Usuarios Activos Mensuales'),
        ('Context Window', 'review.chatgpt.stats.context', 'Context Window', 'Ventana de Contexto'),
        ('Languages Supported', 'review.chatgpt.stats.languages', 'Languages Supported', 'Idiomas Soportados'),
        ('Starting Price', 'review.chatgpt.stats.price', 'Starting Price', 'Precio Inicial'),
        ('Launch Year', 'review.chatgpt.stats.year', 'Launch Year', 'Año de Lanzamiento'),

        # ==================== CTA & BUTTONS ====================
        ('Try It Now', 'review.chatgpt.cta.title', 'Try It Now', 'Pruébalo Ahora'),
        ('Try Free', 'review.chatgpt.btn.try', 'Try Free', 'Probar Gratis'),
        ('View Pricing', 'review.chatgpt.btn.pricing', 'View Pricing', 'Ver Precios'),
        ('Get ChatGPT', 'review.chatgpt.sidebar.get', 'Get ChatGPT', 'Obtener ChatGPT'),

        # ==================== SECTION TITLES ====================
        ('Overview', 'review.common.overview', 'Overview', 'Resumen'),
        ('Key Features', 'review.common.features', 'Key Features', 'Características Clave'),
        ('Pros & Cons', 'review.common.proscons', 'Pros & Cons', 'Ventajas y Desventajas'),
        ('Pricing Plans', 'review.common.pricing', 'Pricing Plans', 'Planes de Precios'),
        ('Best Use Cases', 'review.common.usecases', 'Best Use Cases', 'Mejores Casos de Uso'),
        ('Comparison with Competitors', 'review.common.comparison', 'Comparison with Competitors', 'Comparación con Competidores'),
        ('Screenshots & Interface', 'review.common.screenshots', 'Screenshots & Interface', 'Capturas de Pantalla e Interfaz'),
        ('Final Verdict', 'review.common.verdict', 'Final Verdict', 'Veredicto Final'),
        ('Frequently Asked Questions', 'review.common.faq', 'Frequently Asked Questions', 'Preguntas Frecuentes'),
        ('Table of Contents', 'review.common.toc', 'Table of Contents', 'Tabla de Contenidos'),
        ('Compare With', 'review.common.compare', 'Compare With', 'Comparar Con'),
        ('Quick Info', 'review.common.quickinfo', 'Quick Info', 'Información Rápida'),

        # ==================== OVERVIEW SECTION ====================
        ("ChatGPT is OpenAI's flagship conversational AI product and the world's most widely used AI chatbot. Launched in November 2022, it revolutionized the AI industry and brought large language models into mainstream use. Today, with GPT-4 Turbo powering its premium tier, ChatGPT remains at the forefront of AI assistants.",
         'review.chatgpt.overview.p1',
         "ChatGPT is OpenAI's flagship conversational AI product and the world's most widely used AI chatbot. Launched in November 2022, it revolutionized the AI industry and brought large language models into mainstream use. Today, with GPT-4 Turbo powering its premium tier, ChatGPT remains at the forefront of AI assistants.",
         "ChatGPT es el producto insignia de IA conversacional de OpenAI y el chatbot de IA más utilizado del mundo. Lanzado en noviembre de 2022, revolucionó la industria de la IA y llevó los modelos de lenguaje grandes al uso general. Hoy, con GPT-4 Turbo impulsando su nivel premium, ChatGPT permanece a la vanguardia de los asistentes de IA."),

        ("What makes ChatGPT stand out is its versatility. Whether you need help writing an essay, debugging code, brainstorming ideas, analyzing data, or just having a conversation, ChatGPT handles it all with remarkable competence. The addition of vision capabilities, DALL-E image generation, and custom GPTs has transformed it from a simple chatbot into a comprehensive AI platform.",
         'review.chatgpt.overview.p2',
         "What makes ChatGPT stand out is its versatility. Whether you need help writing an essay, debugging code, brainstorming ideas, analyzing data, or just having a conversation, ChatGPT handles it all with remarkable competence. The addition of vision capabilities, DALL-E image generation, and custom GPTs has transformed it from a simple chatbot into a comprehensive AI platform.",
         "Lo que hace destacar a ChatGPT es su versatilidad. Ya sea que necesites ayuda escribiendo un ensayo, depurando código, generando ideas, analizando datos o simplemente teniendo una conversación, ChatGPT lo maneja todo con notable competencia. La adición de capacidades de visión, generación de imágenes DALL-E y GPTs personalizados lo ha transformado de un simple chatbot en una plataforma integral de IA."),

        # ==================== FEATURE CARDS ====================
        ('The latest and most capable model with enhanced reasoning, longer context (128K), and knowledge up to April 2026.',
         'review.chatgpt.feature.gpt4.desc',
         'The latest and most capable model with enhanced reasoning, longer context (128K), and knowledge up to April 2026.',
         'El modelo más reciente y capaz con razonamiento mejorado, contexto más largo (128K) y conocimiento hasta abril de 2026.'),

        ('Vision Capabilities', 'review.chatgpt.feature.vision.title', 'Vision Capabilities', 'Capacidades de Visión'),
        ('Upload images for analysis, explanation, and extraction. Works with screenshots, diagrams, and documents.',
         'review.chatgpt.feature.vision.desc',
         'Upload images for analysis, explanation, and extraction. Works with screenshots, diagrams, and documents.',
         'Sube imágenes para análisis, explicación y extracción. Funciona con capturas de pantalla, diagramas y documentos.'),

        ('DALL-E 3 Integration', 'review.chatgpt.feature.dalle.title', 'DALL-E 3 Integration', 'Integración DALL-E 3'),
        ('Generate high-quality images directly in chat. Create, edit, and iterate on visual content seamlessly.',
         'review.chatgpt.feature.dalle.desc',
         'Generate high-quality images directly in chat. Create, edit, and iterate on visual content seamlessly.',
         'Genera imágenes de alta calidad directamente en el chat. Crea, edita e itera sobre contenido visual sin problemas.'),

        ('Code Interpreter', 'review.chatgpt.feature.code.title', 'Code Interpreter', 'Intérprete de Código'),
        ('Execute Python code, analyze data files, create visualizations, and perform complex calculations.',
         'review.chatgpt.feature.code.desc',
         'Execute Python code, analyze data files, create visualizations, and perform complex calculations.',
         'Ejecuta código Python, analiza archivos de datos, crea visualizaciones y realiza cálculos complejos.'),

        ('Custom GPTs', 'review.chatgpt.feature.custom.title', 'Custom GPTs', 'GPTs Personalizados'),
        ('Build specialized AI assistants for specific tasks. Access thousands of community-created GPTs in the store.',
         'review.chatgpt.feature.custom.desc',
         'Build specialized AI assistants for specific tasks. Access thousands of community-created GPTs in the store.',
         'Crea asistentes de IA especializados para tareas específicas. Accede a miles de GPTs creados por la comunidad en la tienda.'),

        ('Web Browsing', 'review.chatgpt.feature.web.title', 'Web Browsing', 'Navegación Web'),
        ('Search the internet in real-time for up-to-date information. Cite sources and provide current data.',
         'review.chatgpt.feature.web.desc',
         'Search the internet in real-time for up-to-date information. Cite sources and provide current data.',
         'Busca en internet en tiempo real para obtener información actualizada. Cita fuentes y proporciona datos actuales.'),

        # ==================== ADDITIONAL FEATURES ====================
        ('Additional Features', 'review.common.additional', 'Additional Features', 'Características Adicionales'),
        ('Voice Conversations:', 'review.chatgpt.addfeature.voice.title', 'Voice Conversations:', 'Conversaciones de Voz:'),
        ('Talk to ChatGPT using natural voice on mobile devices with multiple voice options',
         'review.chatgpt.addfeature.voice.desc',
         'Talk to ChatGPT using natural voice on mobile devices with multiple voice options',
         'Habla con ChatGPT usando voz natural en dispositivos móviles con múltiples opciones de voz'),

        ('Memory:', 'review.chatgpt.addfeature.memory.title', 'Memory:', 'Memoria:'),
        ('ChatGPT can remember context from previous conversations for personalized responses',
         'review.chatgpt.addfeature.memory.desc',
         'ChatGPT can remember context from previous conversations for personalized responses',
         'ChatGPT puede recordar el contexto de conversaciones anteriores para respuestas personalizadas'),

        ('Canvas:', 'review.chatgpt.addfeature.canvas.title', 'Canvas:', 'Canvas:'),
        ('New collaborative workspace for writing and coding with real-time editing',
         'review.chatgpt.addfeature.canvas.desc',
         'New collaborative workspace for writing and coding with real-time editing',
         'Nuevo espacio de trabajo colaborativo para escritura y codificación con edición en tiempo real'),

        ('File Uploads:', 'review.chatgpt.addfeature.files.title', 'File Uploads:', 'Carga de Archivos:'),
        ('Upload PDFs, documents, spreadsheets, and other files for analysis',
         'review.chatgpt.addfeature.files.desc',
         'Upload PDFs, documents, spreadsheets, and other files for analysis',
         'Sube PDFs, documentos, hojas de cálculo y otros archivos para análisis'),

        ('Multi-modal Output:', 'review.chatgpt.addfeature.multimodal.title', 'Multi-modal Output:', 'Salida Multimodal:'),
        ('Generate text, images, and code in single responses',
         'review.chatgpt.addfeature.multimodal.desc',
         'Generate text, images, and code in single responses',
         'Genera texto, imágenes y código en respuestas únicas'),

        ('API Access:', 'review.chatgpt.addfeature.api.title', 'API Access:', 'Acceso API:'),
        ('Developers can integrate GPT-4 into their applications via the OpenAI API',
         'review.chatgpt.addfeature.api.desc',
         'Developers can integrate GPT-4 into their applications via the OpenAI API',
         'Los desarrolladores pueden integrar GPT-4 en sus aplicaciones a través de la API de OpenAI'),

        # ==================== PROS & CONS ====================
        ('Advantages', 'review.common.advantages', 'Advantages', 'Ventajas'),
        ('Disadvantages', 'review.common.disadvantages', 'Disadvantages', 'Desventajas'),

        # Pros (10 items)
        ('Industry-leading ecosystem with custom GPTs and plugins',
         'review.chatgpt.pro.1',
         'Industry-leading ecosystem with custom GPTs and plugins',
         'Ecosistema líder en la industria con GPTs personalizados y complementos'),

        ('Excellent general knowledge and reasoning',
         'review.chatgpt.pro.2',
         'Excellent general knowledge and reasoning',
         'Excelente conocimiento general y razonamiento'),

        ('Built-in image generation with DALL-E 3',
         'review.chatgpt.pro.3',
         'Built-in image generation with DALL-E 3',
         'Generación de imágenes integrada con DALL-E 3'),

        ('Best-in-class mobile apps for iOS and Android',
         'review.chatgpt.pro.4',
         'Best-in-class mobile apps for iOS and Android',
         'Aplicaciones móviles de primera clase para iOS y Android'),

        ('Vision capabilities for image analysis',
         'review.chatgpt.pro.5',
         'Vision capabilities for image analysis',
         'Capacidades de visión para análisis de imágenes'),

        ('Code interpreter for data analysis',
         'review.chatgpt.pro.6',
         'Code interpreter for data analysis',
         'Intérprete de código para análisis de datos'),

        ('Regular updates and improvements',
         'review.chatgpt.pro.7',
         'Regular updates and improvements',
         'Actualizaciones y mejoras regulares'),

        ('Generous free tier available',
         'review.chatgpt.pro.8',
         'Generous free tier available',
         'Generoso nivel gratuito disponible'),

        ('Multi-modal capabilities in one interface',
         'review.chatgpt.pro.9',
         'Multi-modal capabilities in one interface',
         'Capacidades multimodales en una interfaz'),

        ('Enterprise features with SOC 2 compliance',
         'review.chatgpt.pro.10',
         'Enterprise features with SOC 2 compliance',
         'Funciones empresariales con cumplimiento SOC 2'),

        # Cons (8 items)
        ('Can be verbose and repetitive',
         'review.chatgpt.con.1',
         'Can be verbose and repetitive',
         'Puede ser verboso y repetitivo'),

        ('Knowledge cutoff (not real-time by default)',
         'review.chatgpt.con.2',
         'Knowledge cutoff (not real-time by default)',
         'Corte de conocimiento (no en tiempo real por defecto)'),

        ('Rate limits on GPT-4 even for paying users',
         'review.chatgpt.con.3',
         'Rate limits on GPT-4 even for paying users',
         'Límites de tasa en GPT-4 incluso para usuarios de pago'),

        ('Smaller context window than Claude (128K vs 200K)',
         'review.chatgpt.con.4',
         'Smaller context window than Claude (128K vs 200K)',
         'Ventana de contexto más pequeña que Claude (128K vs 200K)'),

        ('Occasional hallucinations with factual claims',
         'review.chatgpt.con.5',
         'Occasional hallucinations with factual claims',
         'Alucinaciones ocasionales con afirmaciones fácticas'),

        ('Plus subscription required for best features',
         'review.chatgpt.con.6',
         'Plus subscription required for best features',
         'Suscripción Plus requerida para las mejores funciones'),

        ('No built-in citations in standard mode',
         'review.chatgpt.con.7',
         'No built-in citations in standard mode',
         'Sin citas integradas en modo estándar'),

        ('Can be slow during peak usage times',
         'review.chatgpt.con.8',
         'Can be slow during peak usage times',
         'Puede ser lento durante horas pico'),
    ]

    # Apply each replacement
    for text, key, text_en, text_es in replacements:
        if text in content and f'data-i18n="{key}"' not in content:
            # Wrap the text
            wrapped = wrap_text(text, key)
            content = content.replace(f'>{text}<', f'>{wrapped}<', 1)
            translations_en[key] = text_en
            translations_es[key] = text_es
            count += 1
            print(f"✅ {key}")

    # Save results
    if count > 0:
        # Backup
        backup_path = file_path + '.fullbackup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)

        # Save modified HTML
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        # Save translations
        with open('chatgpt_translations_en.json', 'w', encoding='utf-8') as f:
            json.dump(translations_en, f, indent=2, ensure_ascii=False)

        with open('chatgpt_translations_es.json', 'w', encoding='utf-8') as f:
            json.dump(translations_es, f, indent=2, ensure_ascii=False)

        print(f"\n🎉 {count} éléments modifiés!")
        print(f"📝 Backup: {backup_path}")
        print(f"📄 EN: chatgpt_translations_en.json ({len(translations_en)} clés)")
        print(f"📄 ES: chatgpt_translations_es.json ({len(translations_es)} clés)")
    else:
        print("\nℹ️  Aucune modification")

if __name__ == "__main__":
    add_complete_i18n()
