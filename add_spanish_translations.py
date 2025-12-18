#!/usr/bin/env python3
"""
Script pour ajouter les traductions espagnoles manquantes dans i18n.js
"""

def add_spanish_translations():
    """Ajoute les traductions espagnoles manquantes"""

    file_path = "GenuisNet.ai/js/i18n.js"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Traductions à remplacer dans la section espagnole (es:)
    replacements = {
        # Descriptions des AI
        '"section.claude-by-anthropic-represents": "Claude by Anthropic represents the cutting edge of conversational AI. With its massive 200K token context window and exceptional coding abilities, it\'s revolutionizing how we interact with AI assistants.",':
            '"section.claude-by-anthropic-represents": "Claude de Anthropic representa la vanguardia de la IA conversacional. Con su masiva ventana de contexto de 200K tokens y capacidades excepcionales de codificación, está revolucionando la forma en que interactuamos con los asistentes de IA.",',

        '"section.midjourney-leads-the-ai-art-re": "Midjourney leads the AI art revolution with stunning, photorealistic image generation. From concept art to marketing materials, it transforms simple text prompts into professional-grade visuals.",':
            '"section.midjourney-leads-the-ai-art-re": "Midjourney lidera la revolución del arte IA con una generación de imágenes fotorrealistas impresionantes. Desde arte conceptual hasta materiales de marketing, transforma simples indicaciones de texto en visuales de calidad profesional.",',

        '"section.cursor-is-revolutionizing-soft": "Cursor is revolutionizing software development with its AI-first approach. Write code with natural language, refactor entire codebases, and debug faster than ever before.",':
            '"section.cursor-is-revolutionizing-soft": "Cursor está revolucionando el desarrollo de software con su enfoque centrado en IA. Escribe código con lenguaje natural, refactoriza bases de código completas y depura más rápido que nunca.",',

        '"section.chatgpt-by-openai-sparked-the-": "ChatGPT by OpenAI sparked the AI revolution. From writing and coding to analysis and creativity, it\'s the most versatile AI assistant available today.",':
            '"section.chatgpt-by-openai-sparked-the-": "ChatGPT de OpenAI inició la revolución de la IA. Desde escribir y codificar hasta análisis y creatividad, es el asistente de IA más versátil disponible hoy.",',

        '"section.runway-is-pushing-the-boundari": "Runway is pushing the boundaries of AI video generation. Create cinematic videos from text, extend footage seamlessly, and edit with unprecedented creative control.",':
            '"section.runway-is-pushing-the-boundari": "Runway está ampliando los límites de la generación de video IA. Crea videos cinematográficos desde texto, extiende metraje sin problemas y edita con un control creativo sin precedentes.",',

        '"section.elevenlabs-delivers-the-most-n": "ElevenLabs delivers the most natural-sounding AI voices on the market. Perfect for audiobooks, podcasts, video narration, and multilingual content creation.",':
            '"section.elevenlabs-delivers-the-most-n": "ElevenLabs ofrece las voces de IA más naturales del mercado. Perfecto para audiolibros, podcasts, narración de video y creación de contenido multilingüe.",',

        # Taglines
        '"section.the-ai-assistant-that-thinks-b": "The AI assistant that thinks before it speaks",':
            '"section.the-ai-assistant-that-thinks-b": "El asistente de IA que piensa antes de hablar",',

        '"section.create-breathtaking-art-from-t": "Create breathtaking art from text",':
            '"section.create-breathtaking-art-from-t": "Crea arte impresionante desde texto",',

        '"section.the-ai-first-code-editor": "The AI-first code editor",':
            '"section.the-ai-first-code-editor": "El editor de código centrado en IA",',

        '"section.the-ai-that-started-it-all": "The AI that started it all",':
            '"section.the-ai-that-started-it-all": "La IA que lo empezó todo",',

        '"section.the-most-realistic-ai-voices": "The most realistic AI voices",':
            '"section.the-most-realistic-ai-voices": "Las voces de IA más realistas",',

        '"section.hollywood-quality-ai-video-gen": "Hollywood-quality AI video generation",':
            '"section.hollywood-quality-ai-video-gen": "Generación de video IA con calidad de Hollywood",',

        # Why GenuisNet.ai
        '"section.from-chatgpt-to-specialized-en": "From ChatGPT to specialized enterprise solutions, we cover every AI tool that matters",':
            '"section.from-chatgpt-to-specialized-en": "Desde ChatGPT hasta soluciones empresariales especializadas, cubrimos todas las herramientas de IA que importan",',

        '"section.every-tool-is-tested-in-actual": "Every tool is tested in actual workflows, not just theoretical benchmarks",':
            '"section.every-tool-is-tested-in-actual": "Cada herramienta se prueba en flujos de trabajo reales, no solo en benchmarks teóricos",',

        '"section.step-by-step-tutorials-and-com": "Step-by-step tutorials and comparisons to help you make informed decisions",':
            '"section.step-by-step-tutorials-and-com": "Tutoriales paso a paso y comparaciones para ayudarte a tomar decisiones informadas",',

        '"section.ratings-and-reviews-from-a-glo": "Ratings and reviews from a global community of AI enthusiasts",':
            '"section.ratings-and-reviews-from-a-glo": "Calificaciones y reseñas de una comunidad global de entusiastas de la IA",',

        '"section.real-world-testing": "Real-World Testing",':
            '"section.real-world-testing": "Pruebas en el Mundo Real",',

        # Labels
        '"section.users": "Users",':
            '"section.users": "Usuarios",',

        '"section.users-2": "Users",':
            '"section.users-2": "Usuarios",',

        '"section.voices": "Voices",':
            '"section.voices": "Voces",',

        '"section.resolution": "Resolution",':
            '"section.resolution": "Resolución",',
    }

    # Trouver la section espagnole
    es_start = content.find('es: {', content.find('// ==================== SPANISH ===================='))
    if es_start == -1:
        es_start = content.find('es: {')

    de_start = content.find('// ==================== GERMAN ====================')

    if es_start == -1 or de_start == -1:
        print("❌ Section espagnole non trouvée")
        return

    before_es = content[:es_start]
    es_section = content[es_start:de_start]
    after_es = content[de_start:]

    # Appliquer les remplacements
    count = 0
    for old, new in replacements.items():
        if old in es_section:
            es_section = es_section.replace(old, new, 1)
            count += 1
            # Extraire le nom de la clé pour l'affichage
            key = old.split('"')[1]
            print(f"✅ {key}")

    # Reconstruire le contenu
    content = before_es + es_section + after_es

    # Écrire les modifications
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\n✅ {count} traductions espagnoles ajoutées!")
    else:
        print("\nℹ️  Aucune modification nécessaire")

if __name__ == "__main__":
    add_spanish_translations()
