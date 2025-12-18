#!/usr/bin/env python3
"""
Script pour ajouter data-i18n aux tables (pricing, comparison) et use cases
"""

import json

def wrap_text(text, key):
    return f'<span data-i18n="{key}">{text}</span>'

def add_tables_usecases_i18n():
    file_path = "GenuisNet.ai/pages/reviews/chatbots/chatgpt.html"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    translations_en = {}
    translations_es = {}
    count = 0

    replacements = [
        # ==================== PRICING TABLE ====================
        ('Plan', 'review.table.plan', 'Plan', 'Plan'),
        ('Price', 'review.table.price', 'Price', 'Precio'),
        ('Model Access', 'review.table.model', 'Model Access', 'Acceso a Modelos'),
        ('Key Features', 'review.table.features', 'Key Features', 'Características Clave'),

        # Pricing rows
        ('Free', 'review.chatgpt.plan.free', 'Free', 'Gratis'),
        ('Plus', 'review.chatgpt.plan.plus', 'Plus', 'Plus'),
        ('Team', 'review.chatgpt.plan.team', 'Team', 'Equipo'),
        ('Enterprise', 'review.chatgpt.plan.enterprise', 'Enterprise', 'Empresa'),

        ('GPT-4o mini', 'review.chatgpt.plan.free.model', 'GPT-4o mini', 'GPT-4o mini'),
        ('Basic chat, limited GPT-4 access, web browsing',
         'review.chatgpt.plan.free.features',
         'Basic chat, limited GPT-4 access, web browsing',
         'Chat básico, acceso limitado a GPT-4, navegación web'),

        ('GPT-4, GPT-4o, GPT-4 Turbo', 'review.chatgpt.plan.plus.model', 'GPT-4, GPT-4o, GPT-4 Turbo', 'GPT-4, GPT-4o, GPT-4 Turbo'),
        ('Priority access, DALL-E, Code Interpreter, Custom GPTs, Voice',
         'review.chatgpt.plan.plus.features',
         'Priority access, DALL-E, Code Interpreter, Custom GPTs, Voice',
         'Acceso prioritario, DALL-E, Intérprete de código, GPTs personalizados, Voz'),

        ('All models + higher limits', 'review.chatgpt.plan.team.model', 'All models + higher limits', 'Todos los modelos + límites superiores'),
        ('Admin console, workspace, higher message caps, team features',
         'review.chatgpt.plan.team.features',
         'Admin console, workspace, higher message caps, team features',
         'Consola de administración, espacio de trabajo, límites de mensajes superiores, funciones de equipo'),

        ('All models + unlimited', 'review.chatgpt.plan.enterprise.model', 'All models + unlimited', 'Todos los modelos + ilimitado'),
        ('SSO, advanced security, unlimited high-speed access, dedicated support',
         'review.chatgpt.plan.enterprise.features',
         'SSO, advanced security, unlimited high-speed access, dedicated support',
         'SSO, seguridad avanzada, acceso ilimitado de alta velocidad, soporte dedicado'),

        ('Custom', 'review.common.custom', 'Custom', 'Personalizado'),

        # ==================== USE CASES SECTION ====================
        ('ChatGPT Excels At:', 'review.chatgpt.usecases.excels', 'ChatGPT Excels At:', 'ChatGPT Sobresale En:'),
        ('May Not Be Ideal For:', 'review.chatgpt.usecases.notideal', 'May Not Be Ideal For:', 'Puede No Ser Ideal Para:'),

        # Use case categories
        ('Content Writing:', 'review.chatgpt.usecase.writing.title', 'Content Writing:', 'Escritura de Contenido:'),
        ('Blog posts, articles, marketing copy, social media content',
         'review.chatgpt.usecase.writing.desc',
         'Blog posts, articles, marketing copy, social media content',
         'Publicaciones de blog, artículos, textos de marketing, contenido para redes sociales'),

        ('Coding Assistance:', 'review.chatgpt.usecase.coding.title', 'Coding Assistance:', 'Asistencia de Codificación:'),
        ('Debugging, code explanation, writing functions, learning programming',
         'review.chatgpt.usecase.coding.desc',
         'Debugging, code explanation, writing functions, learning programming',
         'Depuración, explicación de código, escritura de funciones, aprendizaje de programación'),

        ('Research & Analysis:', 'review.chatgpt.usecase.research.title', 'Research & Analysis:', 'Investigación y Análisis:'),
        ('Summarizing documents, answering questions, data analysis',
         'review.chatgpt.usecase.research.desc',
         'Summarizing documents, answering questions, data analysis',
         'Resumir documentos, responder preguntas, análisis de datos'),

        ('Creative Tasks:', 'review.chatgpt.usecase.creative.title', 'Creative Tasks:', 'Tareas Creativas:'),
        ('Brainstorming, storytelling, image generation with DALL-E',
         'review.chatgpt.usecase.creative.desc',
         'Brainstorming, storytelling, image generation with DALL-E',
         'Lluvia de ideas, narración de historias, generación de imágenes con DALL-E'),

        ('Learning & Education:', 'review.chatgpt.usecase.learning.title', 'Learning & Education:', 'Aprendizaje y Educación:'),
        ('Explaining concepts, tutoring, language learning',
         'review.chatgpt.usecase.learning.desc',
         'Explaining concepts, tutoring, language learning',
         'Explicar conceptos, tutoría, aprendizaje de idiomas'),

        ('Business Tasks:', 'review.chatgpt.usecase.business.title', 'Business Tasks:', 'Tareas de Negocios:'),
        ('Email drafting, meeting summaries, presentations',
         'review.chatgpt.usecase.business.desc',
         'Email drafting, meeting summaries, presentations',
         'Redacción de correos, resúmenes de reuniones, presentaciones'),

        ('Data Work:', 'review.chatgpt.usecase.data.title', 'Data Work:', 'Trabajo con Datos:'),
        ('Excel formulas, data visualization, statistical analysis',
         'review.chatgpt.usecase.data.desc',
         'Excel formulas, data visualization, statistical analysis',
         'Fórmulas de Excel, visualización de datos, análisis estadístico'),

        # Not ideal for
        ('Tasks requiring real-time information without web browsing enabled',
         'review.chatgpt.notideal.1',
         'Tasks requiring real-time information without web browsing enabled',
         'Tareas que requieren información en tiempo real sin navegación web habilitada'),

        ('Highly specialized domain expertise (consider domain-specific AI)',
         'review.chatgpt.notideal.2',
         'Highly specialized domain expertise (consider domain-specific AI)',
         'Experiencia en dominios altamente especializados (considere IA específica del dominio)'),

        ('Critical applications requiring 100% accuracy (always verify important facts)',
         'review.chatgpt.notideal.3',
         'Critical applications requiring 100% accuracy (always verify important facts)',
         'Aplicaciones críticas que requieren 100% de precisión (siempre verifique datos importantes)'),

        ('Processing extremely long documents (consider Claude for 200K context)',
         'review.chatgpt.notideal.4',
         'Processing extremely long documents (consider Claude for 200K context)',
         'Procesamiento de documentos extremadamente largos (considere Claude para contexto de 200K)'),

        # ==================== COMPARISON TABLE ====================
        ('Feature', 'review.table.feature', 'Feature', 'Característica'),
        ('Context Window', 'review.table.context', 'Context Window', 'Ventana de Contexto'),
        ('Image Generation', 'review.table.imagegen', 'Image Generation', 'Generación de Imágenes'),
        ('Code Quality', 'review.table.codequality', 'Code Quality', 'Calidad de Código'),
        ('Web Access', 'review.table.webaccess', 'Web Access', 'Acceso Web'),
        ('Plugin Ecosystem', 'review.table.plugins', 'Plugin Ecosystem', 'Ecosistema de Plugins'),
        ('Free Tier', 'review.table.freetier', 'Free Tier', 'Nivel Gratuito'),
        ('Pro Price', 'review.table.proprice', 'Pro Price', 'Precio Pro'),

        # Comparison values
        ('128K tokens', 'review.comp.128k', '128K tokens', '128K tokens'),
        ('200K tokens', 'review.comp.200k', '200K tokens', '200K tokens'),
        ('1M tokens', 'review.comp.1m', '1M tokens', '1M tokens'),
        ('DALL-E 3', 'review.comp.dalle3', 'DALL-E 3', 'DALL-E 3'),
        ('None', 'review.comp.none', 'None', 'Ninguno'),
        ('Imagen 3', 'review.comp.imagen3', 'Imagen 3', 'Imagen 3'),
        ('Excellent', 'review.comp.excellent', 'Excellent', 'Excelente'),
        ('Best', 'review.comp.best', 'Best', 'Mejor'),
        ('Good', 'review.comp.good', 'Good', 'Bueno'),
        ('Yes (Browsing)', 'review.comp.yesbrowse', 'Yes (Browsing)', 'Sí (Navegación)'),
        ('No', 'review.comp.no', 'No', 'No'),
        ('Yes (Real-time)', 'review.comp.yesrealtime', 'Yes (Real-time)', 'Sí (Tiempo Real)'),
        ('Extensive', 'review.comp.extensive', 'Extensive', 'Extenso'),
        ('Limited', 'review.comp.limited', 'Limited', 'Limitado'),
        ('Google Apps', 'review.comp.googleapps', 'Google Apps', 'Google Apps'),
        ('Claude 3.5 Sonnet', 'review.comp.claude35', 'Claude 3.5 Sonnet', 'Claude 3.5 Sonnet'),
        ('Gemini Pro', 'review.comp.geminipro', 'Gemini Pro', 'Gemini Pro'),
        ('$20/month', 'review.comp.20month', '$20/month', '$20/mes'),

        # ==================== REAL USE CASES (détaillés) ====================
        ('Real-World Use Cases & Success Stories',
         'review.chatgpt.realusecases.title',
         'Real-World Use Cases & Success Stories',
         'Casos de Uso Reales e Historias de Éxito'),

        ('Discover how professionals and businesses are using ChatGPT to solve real problems and achieve measurable results:',
         'review.chatgpt.realusecases.intro',
         'Discover how professionals and businesses are using ChatGPT to solve real problems and achieve measurable results:',
         'Descubre cómo profesionales y empresas están usando ChatGPT para resolver problemas reales y lograr resultados medibles:'),

        # Use Case 1: Content Marketing
        ('Content Marketing Automation',
         'review.chatgpt.case1.title',
         'Content Marketing Automation',
         'Automatización de Marketing de Contenidos'),

        ('Marketing Agency', 'review.chatgpt.case1.industry', 'Marketing Agency', 'Agencia de Marketing'),

        ('A mid-sized digital marketing agency was struggling to scale content production for 20+ clients. They needed to create blog posts, social media content, and email campaigns while maintaining quality and brand voice consistency.',
         'review.chatgpt.case1.desc',
         'A mid-sized digital marketing agency was struggling to scale content production for 20+ clients. They needed to create blog posts, social media content, and email campaigns while maintaining quality and brand voice consistency.',
         'Una agencia de marketing digital de tamaño mediano luchaba por escalar la producción de contenido para más de 20 clientes. Necesitaban crear publicaciones de blog, contenido de redes sociales y campañas de correo electrónico mientras mantenían la calidad y la consistencia de la voz de marca.'),

        ('Challenge', 'review.chatgpt.case.challenge', 'Challenge', 'Desafío'),

        ('Manual content creation took 8-10 hours per client per week, limiting scalability and profitability. Writers were overwhelmed, and client satisfaction was declining due to delayed deliverables.',
         'review.chatgpt.case1.challenge',
         'Manual content creation took 8-10 hours per client per week, limiting scalability and profitability. Writers were overwhelmed, and client satisfaction was declining due to delayed deliverables.',
         'La creación manual de contenido tomaba 8-10 horas por cliente por semana, limitando la escalabilidad y rentabilidad. Los escritores estaban abrumados y la satisfacción del cliente estaba disminuyendo debido a entregas retrasadas.'),

        # Case 1 Steps
        ('Created Custom GPTs for Each Client',
         'review.chatgpt.case1.step1.title',
         'Created Custom GPTs for Each Client',
         'Creó GPTs Personalizados para Cada Cliente'),

        ('Built specialized GPTs with specific tone, style, and terminology guidelines for each client\'s brand',
         'review.chatgpt.case1.step1.desc',
         'Built specialized GPTs with specific tone, style, and terminology guidelines for each client\'s brand',
         'Construyó GPTs especializados con tono, estilo y pautas de terminología específicas para la marca de cada cliente'),

        ('Automated First Draft Generation',
         'review.chatgpt.case1.step2.title',
         'Automated First Draft Generation',
         'Generación Automática de Primeros Borradores'),

        ('Used ChatGPT to generate first drafts of blog posts, social posts, and newsletters in seconds',
         'review.chatgpt.case1.step2.desc',
         'Used ChatGPT to generate first drafts of blog posts, social posts, and newsletters in seconds',
         'Usó ChatGPT para generar primeros borradores de publicaciones de blog, publicaciones sociales y boletines en segundos'),

        ('Human Review & Refinement',
         'review.chatgpt.case1.step3.title',
         'Human Review & Refinement',
         'Revisión y Refinamiento Humano'),

        ('Writers focused on editing, fact-checking, and adding unique insights rather than starting from scratch',
         'review.chatgpt.case1.step3.desc',
         'Writers focused on editing, fact-checking, and adding unique insights rather than starting from scratch',
         'Los escritores se enfocaron en editar, verificar hechos y agregar ideas únicas en lugar de empezar desde cero'),

        ('Performance Optimization',
         'review.chatgpt.case1.step4.title',
         'Performance Optimization',
         'Optimización de Rendimiento'),

        ('Analyzed which AI-generated content performed best and refined Custom GPTs accordingly',
         'review.chatgpt.case1.step4.desc',
         'Analyzed which AI-generated content performed best and refined Custom GPTs accordingly',
         'Analizó qué contenido generado por IA tuvo mejor rendimiento y refinó los GPTs personalizados en consecuencia'),

        # Case 1 Results
        ('Time Saved', 'review.chatgpt.result.timesaved', 'Time Saved', 'Tiempo Ahorrado'),
        ('Content Output', 'review.chatgpt.result.contentoutput', 'Content Output', 'Producción de Contenido'),
        ('Cost Reduction', 'review.chatgpt.result.costreduction', 'Cost Reduction', 'Reducción de Costos'),
        ('Client Satisfaction', 'review.chatgpt.result.satisfaction', 'Client Satisfaction', 'Satisfacción del Cliente'),

        ('DigitalBoost Agency - 50 employees',
         'review.chatgpt.case1.company',
         'DigitalBoost Agency - 50 employees',
         'Agencia DigitalBoost - 50 empleados'),
    ]

    # Apply replacements
    for text, key, text_en, text_es in replacements:
        if text in content and f'data-i18n="{key}"' not in content:
            wrapped = wrap_text(text, key)
            content = content.replace(f'>{text}<', f'>{wrapped}<', 1)
            translations_en[key] = text_en
            translations_es[key] = text_es
            count += 1
            print(f"✅ {key}")

    # Save results
    if count > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        # Load existing translations
        try:
            with open('chatgpt_translations_en.json', 'r', encoding='utf-8') as f:
                existing_en = json.load(f)
            with open('chatgpt_translations_es.json', 'r', encoding='utf-8') as f:
                existing_es = json.load(f)

            # Merge
            existing_en.update(translations_en)
            existing_es.update(translations_es)

            with open('chatgpt_translations_en.json', 'w', encoding='utf-8') as f:
                json.dump(existing_en, f, indent=2, ensure_ascii=False)
            with open('chatgpt_translations_es.json', 'w', encoding='utf-8') as f:
                json.dump(existing_es, f, indent=2, ensure_ascii=False)

            print(f"\n🎉 {count} nouveaux éléments ajoutés!")
            print(f"📄 Total EN: {len(existing_en)} clés")
            print(f"📄 Total ES: {len(existing_es)} clés")
        except:
            # Create new files
            with open('chatgpt_translations_en.json', 'w', encoding='utf-8') as f:
                json.dump(translations_en, f, indent=2, ensure_ascii=False)
            with open('chatgpt_translations_es.json', 'w', encoding='utf-8') as f:
                json.dump(translations_es, f, indent=2, ensure_ascii=False)
            print(f"\n🎉 {count} éléments ajoutés!")
    else:
        print("\nℹ️  Aucune modification")

if __name__ == "__main__":
    add_tables_usecases_i18n()
