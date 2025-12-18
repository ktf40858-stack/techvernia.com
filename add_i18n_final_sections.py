#!/usr/bin/env python3
"""
Script pour ajouter les dernières sections: Use Cases 2-3, FAQ, Sidebar, Verdict
"""

import json

def wrap_text(text, key):
    return f'<span data-i18n="{key}">{text}</span>'

def add_final_sections_i18n():
    file_path = "GenuisNet.ai/pages/reviews/chatbots/chatgpt.html"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    translations_en = {}
    translations_es = {}
    count = 0

    replacements = [
        # ==================== USE CASE 2: Software Development ====================
        ('Software Development Acceleration',
         'review.chatgpt.case2.title',
         'Software Development Acceleration',
         'Aceleración del Desarrollo de Software'),

        ('Tech Startup', 'review.chatgpt.case2.industry', 'Tech Startup', 'Startup Tecnológica'),

        ('A early-stage SaaS startup with limited engineering resources needed to build and ship features faster to compete with well-funded competitors. Code quality and documentation were suffering under time pressure.',
         'review.chatgpt.case2.desc',
         'A early-stage SaaS startup with limited engineering resources needed to build and ship features faster to compete with well-funded competitors. Code quality and documentation were suffering under time pressure.',
         'Una startup SaaS en etapa temprana con recursos de ingeniería limitados necesitaba construir y lanzar funciones más rápido para competir con competidores bien financiados. La calidad del código y la documentación sufrían bajo presión de tiempo.'),

        ('Small team of 3 developers handling full-stack development, DevOps, bug fixes, and technical debt. Shipping new features took 3-4 weeks, and documentation was months behind.',
         'review.chatgpt.case2.challenge',
         'Small team of 3 developers handling full-stack development, DevOps, bug fixes, and technical debt. Shipping new features took 3-4 weeks, and documentation was months behind.',
         'Pequeño equipo de 3 desarrolladores manejando desarrollo full-stack, DevOps, corrección de errores y deuda técnica. El lanzamiento de nuevas funciones tomaba 3-4 semanas y la documentación estaba meses atrasada.'),

        ('Code Generation & Boilerplate',
         'review.chatgpt.case2.step1.title',
         'Code Generation & Boilerplate',
         'Generación de Código y Plantillas'),

        ('Used ChatGPT to generate API endpoints, database schemas, and React components based on requirements',
         'review.chatgpt.case2.step1.desc',
         'Used ChatGPT to generate API endpoints, database schemas, and React components based on requirements',
         'Usó ChatGPT para generar endpoints de API, esquemas de base de datos y componentes React basados en requisitos'),

        ('Debugging & Code Review',
         'review.chatgpt.case2.step2.title',
         'Debugging & Code Review',
         'Depuración y Revisión de Código'),

        ('Pasted error logs and code into ChatGPT to get instant debugging suggestions and optimization ideas',
         'review.chatgpt.case2.step2.desc',
         'Pasted error logs and code into ChatGPT to get instant debugging suggestions and optimization ideas',
         'Pegó registros de errores y código en ChatGPT para obtener sugerencias de depuración instantáneas e ideas de optimización'),

        ('Automated Documentation',
         'review.chatgpt.case2.step3.title',
         'Automated Documentation',
         'Documentación Automatizada'),

        ('Generated API documentation, README files, and inline comments automatically from code',
         'review.chatgpt.case2.step3.desc',
         'Generated API documentation, README files, and inline comments automatically from code',
         'Generó documentación de API, archivos README y comentarios en línea automáticamente desde el código'),

        ('Test Case Creation',
         'review.chatgpt.case2.step4.title',
         'Test Case Creation',
         'Creación de Casos de Prueba'),

        ('ChatGPT wrote unit tests and integration tests based on the implementation code',
         'review.chatgpt.case2.step4.desc',
         'ChatGPT wrote unit tests and integration tests based on the implementation code',
         'ChatGPT escribió pruebas unitarias y pruebas de integración basadas en el código de implementación'),

        ('Faster Shipping', 'review.chatgpt.result.shipping', 'Faster Shipping', 'Lanzamiento Más Rápido'),
        ('Less Bugs', 'review.chatgpt.result.bugs', 'Less Bugs', 'Menos Errores'),
        ('Docs Coverage', 'review.chatgpt.result.docs', 'Docs Coverage', 'Cobertura de Documentación'),
        ('Productivity ↑', 'review.chatgpt.result.productivity', 'Productivity ↑', 'Productividad ↑'),

        ('CodeFlow SaaS - Early Stage Startup',
         'review.chatgpt.case2.company',
         'CodeFlow SaaS - Early Stage Startup',
         'CodeFlow SaaS - Startup en Etapa Temprana'),

        # ==================== USE CASE 3: Education ====================
        ('Personalized Learning & Tutoring',
         'review.chatgpt.case3.title',
         'Personalized Learning & Tutoring',
         'Aprendizaje y Tutoría Personalizados'),

        ('Education', 'review.chatgpt.case3.industry', 'Education', 'Educación'),

        ('An online tutoring platform wanted to provide 24/7 personalized help to students without dramatically increasing costs. Students needed immediate answers to homework questions and concept explanations.',
         'review.chatgpt.case3.desc',
         'An online tutoring platform wanted to provide 24/7 personalized help to students without dramatically increasing costs. Students needed immediate answers to homework questions and concept explanations.',
         'Una plataforma de tutoría en línea quería proporcionar ayuda personalizada 24/7 a los estudiantes sin aumentar dramáticamente los costos. Los estudiantes necesitaban respuestas inmediatas a preguntas de tarea y explicaciones de conceptos.'),

        ('Students often studied late at night when human tutors weren\'t available. Scaling 1-on-1 tutoring was expensive, and students needed different learning styles and paces.',
         'review.chatgpt.case3.challenge',
         'Students often studied late at night when human tutors weren\'t available. Scaling 1-on-1 tutoring was expensive, and students needed different learning styles and paces.',
         'Los estudiantes a menudo estudiaban tarde en la noche cuando los tutores humanos no estaban disponibles. Escalar la tutoría 1 a 1 era costoso y los estudiantes necesitaban diferentes estilos y ritmos de aprendizaje.'),

        ('Custom Subject-Specific GPTs',
         'review.chatgpt.case3.step1.title',
         'Custom Subject-Specific GPTs',
         'GPTs Personalizados Específicos por Materia'),

        ('Created specialized GPTs for Math, Science, History, and Languages with appropriate teaching styles',
         'review.chatgpt.case3.step1.desc',
         'Created specialized GPTs for Math, Science, History, and Languages with appropriate teaching styles',
         'Creó GPTs especializados para Matemáticas, Ciencias, Historia e Idiomas con estilos de enseñanza apropiados'),

        ('Socratic Method Teaching',
         'review.chatgpt.case3.step2.title',
         'Socratic Method Teaching',
         'Enseñanza Método Socrático'),

        ('Configured ChatGPT to guide students to answers with questions rather than giving direct solutions',
         'review.chatgpt.case3.step2.desc',
         'Configured ChatGPT to guide students to answers with questions rather than giving direct solutions',
         'Configuró ChatGPT para guiar a los estudiantes a las respuestas con preguntas en lugar de dar soluciones directas'),

        ('Visual Learning Support',
         'review.chatgpt.case3.step3.title',
         'Visual Learning Support',
         'Soporte de Aprendizaje Visual'),

        ('Used DALL-E integration to generate diagrams, charts, and visual aids for complex concepts',
         'review.chatgpt.case3.step3.desc',
         'Used DALL-E integration to generate diagrams, charts, and visual aids for complex concepts',
         'Usó la integración DALL-E para generar diagramas, gráficos y ayudas visuales para conceptos complejos'),

        ('Progress Tracking',
         'review.chatgpt.case3.step4.title',
         'Progress Tracking',
         'Seguimiento del Progreso'),

        ('Analyzed conversation patterns to identify struggling topics and recommend targeted lessons',
         'review.chatgpt.case3.step4.desc',
         'Analyzed conversation patterns to identify struggling topics and recommend targeted lessons',
         'Analizó patrones de conversación para identificar temas difíciles y recomendar lecciones específicas'),

        ('Availability', 'review.chatgpt.result.availability', 'Availability', 'Disponibilidad'),
        ('Cost Savings', 'review.chatgpt.result.costsavings', 'Cost Savings', 'Ahorro de Costos'),
        ('Student Capacity', 'review.chatgpt.result.capacity', 'Student Capacity', 'Capacidad de Estudiantes'),
        ('Student Rating', 'review.chatgpt.result.studentrating', 'Student Rating', 'Calificación de Estudiantes'),

        ('LearnSmart Platform - 5,000+ students',
         'review.chatgpt.case3.company',
         'LearnSmart Platform - 5,000+ students',
         'Plataforma LearnSmart - 5,000+ estudiantes'),

        # ==================== SCREENSHOTS ====================
        ('Explore ChatGPT\'s interface and key features through these detailed screenshots:',
         'review.chatgpt.screenshots.intro',
         'Explore ChatGPT\'s interface and key features through these detailed screenshots:',
         'Explora la interfaz y características clave de ChatGPT a través de estas capturas de pantalla detalladas:'),

        ('Main Chat Interface',
         'review.chatgpt.screenshot.main.title',
         'Main Chat Interface',
         'Interfaz Principal del Chat'),

        ('Clean and intuitive conversation interface with all features accessible',
         'review.chatgpt.screenshot.main.desc',
         'Clean and intuitive conversation interface with all features accessible',
         'Interfaz de conversación limpia e intuitiva con todas las funciones accesibles'),

        # ==================== VERDICT ====================
        ('Our Recommendation',
         'review.chatgpt.verdict.title',
         'Our Recommendation',
         'Nuestra Recomendación'),

        ('ChatGPT remains the most versatile and feature-rich AI assistant available. While competitors like Claude excel in specific areas (coding, long documents) and Gemini offers better Google integration, ChatGPT\'s combination of strong general capabilities, extensive ecosystem, image generation, and regular improvements make it the best all-around choice for most users. The free tier is surprisingly capable, but the $20/month Plus subscription unlocks the full potential and is worth it for power users.',
         'review.chatgpt.verdict.text',
         'ChatGPT remains the most versatile and feature-rich AI assistant available. While competitors like Claude excel in specific areas (coding, long documents) and Gemini offers better Google integration, ChatGPT\'s combination of strong general capabilities, extensive ecosystem, image generation, and regular improvements make it the best all-around choice for most users. The free tier is surprisingly capable, but the $20/month Plus subscription unlocks the full potential and is worth it for power users.',
         'ChatGPT sigue siendo el asistente de IA más versátil y rico en funciones disponible. Mientras que competidores como Claude sobresalen en áreas específicas (codificación, documentos largos) y Gemini ofrece mejor integración con Google, la combinación de ChatGPT de fuertes capacidades generales, ecosistema extenso, generación de imágenes y mejoras regulares lo convierten en la mejor opción integral para la mayoría de los usuarios. El nivel gratuito es sorprendentemente capaz, pero la suscripción Plus de $20/mes desbloquea todo el potencial y vale la pena para usuarios avanzados.'),

        # ==================== FAQ ====================
        ('Is ChatGPT free to use?',
         'review.chatgpt.faq1.question',
         'Is ChatGPT free to use?',
         '¿ChatGPT es gratis?'),

        ('Yes, ChatGPT offers a free tier that includes access to GPT-4o mini and limited GPT-4 usage. For full access to GPT-4, DALL-E, Code Interpreter, and other premium features, you\'ll need ChatGPT Plus at $20/month.',
         'review.chatgpt.faq1.answer',
         'Yes, ChatGPT offers a free tier that includes access to GPT-4o mini and limited GPT-4 usage. For full access to GPT-4, DALL-E, Code Interpreter, and other premium features, you\'ll need ChatGPT Plus at $20/month.',
         'Sí, ChatGPT ofrece un nivel gratuito que incluye acceso a GPT-4o mini y uso limitado de GPT-4. Para acceso completo a GPT-4, DALL-E, Intérprete de Código y otras funciones premium, necesitarás ChatGPT Plus por $20/mes.'),

        ('What\'s the difference between GPT-3.5 and GPT-4?',
         'review.chatgpt.faq2.question',
         'What\'s the difference between GPT-3.5 and GPT-4?',
         '¿Cuál es la diferencia entre GPT-3.5 y GPT-4?'),

        ('GPT-4 is significantly more capable than GPT-3.5. It offers better reasoning, more accurate responses, longer context window (128K vs 4K tokens), vision capabilities, and handles complex tasks much better. GPT-4 is available to Plus subscribers, while free users get limited access.',
         'review.chatgpt.faq2.answer',
         'GPT-4 is significantly more capable than GPT-3.5. It offers better reasoning, more accurate responses, longer context window (128K vs 4K tokens), vision capabilities, and handles complex tasks much better. GPT-4 is available to Plus subscribers, while free users get limited access.',
         'GPT-4 es significativamente más capaz que GPT-3.5. Ofrece mejor razonamiento, respuestas más precisas, ventana de contexto más larga (128K vs 4K tokens), capacidades de visión y maneja tareas complejas mucho mejor. GPT-4 está disponible para suscriptores Plus, mientras que los usuarios gratuitos obtienen acceso limitado.'),

        ('Can ChatGPT access the internet?',
         'review.chatgpt.faq3.question',
         'Can ChatGPT access the internet?',
         '¿ChatGPT puede acceder a internet?'),

        ('Yes, ChatGPT Plus users have access to web browsing capabilities, allowing it to search the internet for current information. Free users have limited browsing access. You can also enable or disable this feature in settings.',
         'review.chatgpt.faq3.answer',
         'Yes, ChatGPT Plus users have access to web browsing capabilities, allowing it to search the internet for current information. Free users have limited browsing access. You can also enable or disable this feature in settings.',
         'Sí, los usuarios de ChatGPT Plus tienen acceso a capacidades de navegación web, permitiéndole buscar en internet información actual. Los usuarios gratuitos tienen acceso limitado a la navegación. También puedes habilitar o deshabilitar esta función en la configuración.'),

        ('Is ChatGPT good for coding?',
         'review.chatgpt.faq4.question',
         'Is ChatGPT good for coding?',
         '¿ChatGPT es bueno para programar?'),

        ('ChatGPT is excellent for coding assistance. It can write, debug, explain, and optimize code in most programming languages. The Code Interpreter feature allows it to actually execute Python code. However, for complex coding projects, tools like GitHub Copilot or Claude might be more specialized.',
         'review.chatgpt.faq4.answer',
         'ChatGPT is excellent for coding assistance. It can write, debug, explain, and optimize code in most programming languages. The Code Interpreter feature allows it to actually execute Python code. However, for complex coding projects, tools like GitHub Copilot or Claude might be more specialized.',
         'ChatGPT es excelente para asistencia de codificación. Puede escribir, depurar, explicar y optimizar código en la mayoría de lenguajes de programación. La función Intérprete de Código le permite ejecutar código Python. Sin embargo, para proyectos de codificación complejos, herramientas como GitHub Copilot o Claude podrían ser más especializadas.'),

        ('How does ChatGPT compare to Claude?',
         'review.chatgpt.faq5.question',
         'How does ChatGPT compare to Claude?',
         '¿Cómo se compara ChatGPT con Claude?'),

        ('Both are excellent AI assistants. ChatGPT excels in versatility, ecosystem (Custom GPTs, plugins), and image generation. Claude offers a larger context window (200K vs 128K), often produces better code, and tends to be more nuanced in responses. Claude lacks image generation but excels at long document analysis.',
         'review.chatgpt.faq5.answer',
         'Both are excellent AI assistants. ChatGPT excels in versatility, ecosystem (Custom GPTs, plugins), and image generation. Claude offers a larger context window (200K vs 128K), often produces better code, and tends to be more nuanced in responses. Claude lacks image generation but excels at long document analysis.',
         'Ambos son excelentes asistentes de IA. ChatGPT sobresale en versatilidad, ecosistema (GPTs personalizados, complementos) y generación de imágenes. Claude ofrece una ventana de contexto más grande (200K vs 128K), a menudo produce mejor código y tiende a ser más matizado en las respuestas. Claude carece de generación de imágenes pero sobresale en el análisis de documentos largos.'),

        # ==================== SIDEBAR ====================
        ('Features', 'review.sidebar.features', 'Features', 'Características'),
        ('Ease of Use', 'review.sidebar.ease', 'Ease of Use', 'Facilidad de Uso'),
        ('Value', 'review.sidebar.value', 'Value', 'Valor'),
        ('Performance', 'review.sidebar.performance', 'Performance', 'Rendimiento'),
        ('Support', 'review.sidebar.support', 'Support', 'Soporte'),

        # Related tools
        ('Best for Coding', 'review.sidebar.bestcoding', 'Best for Coding', 'Mejor para Codificación'),
        ('Best Google Integration', 'review.sidebar.bestgoogle', 'Best Google Integration', 'Mejor Integración Google'),
        ('Best for Research', 'review.sidebar.bestresearch', 'Best for Research', 'Mejor para Investigación'),

        # Quick Info
        ('Company', 'review.quickinfo.company', 'Company', 'Empresa'),
        ('Founded', 'review.quickinfo.founded', 'Founded', 'Fundada'),
        ('Headquarters', 'review.quickinfo.headquarters', 'Headquarters', 'Sede'),
        ('Platform', 'review.quickinfo.platform', 'Platform', 'Plataforma'),
        ('API Available', 'review.quickinfo.api', 'API Available', 'API Disponible'),

        ('OpenAI', 'review.chatgpt.company.name', 'OpenAI', 'OpenAI'),
        ('2015', 'review.chatgpt.founded', '2015', '2015'),
        ('San Francisco, CA', 'review.chatgpt.hq', 'San Francisco, CA', 'San Francisco, CA'),
        ('Web, iOS, Android', 'review.chatgpt.platforms', 'Web, iOS, Android', 'Web, iOS, Android'),
        ('Yes', 'review.common.yes', 'Yes', 'Sí'),
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

        # Merge with existing
        try:
            with open('chatgpt_translations_en.json', 'r', encoding='utf-8') as f:
                existing_en = json.load(f)
            with open('chatgpt_translations_es.json', 'r', encoding='utf-8') as f:
                existing_es = json.load(f)

            existing_en.update(translations_en)
            existing_es.update(translations_es)

            with open('chatgpt_translations_en.json', 'w', encoding='utf-8') as f:
                json.dump(existing_en, f, indent=2, ensure_ascii=False)
            with open('chatgpt_translations_es.json', 'w', encoding='utf-8') as f:
                json.dump(existing_es, f, indent=2, ensure_ascii=False)

            print(f"\n🎉 {count} nouveaux éléments ajoutés!")
            print(f"📄 Total EN: {len(existing_en)} clés")
            print(f"📄 Total ES: {len(existing_es)} clés")
        except Exception as e:
            print(f"Erreur: {e}")
    else:
        print("\nℹ️  Aucune modification")

if __name__ == "__main__":
    add_final_sections_i18n()
