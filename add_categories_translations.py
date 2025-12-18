#!/usr/bin/env python3
"""
Script pour ajouter les traductions des catégories dans i18n.js
"""

def add_categories_translations():
    """Ajoute les traductions des catégories"""

    file_path = "GenuisNet.ai/js/i18n.js"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Traductions pour l'anglais
    en_translations = {
        '"cat.chatbots.full":': '"cat.chatbots-short": "AI Chatbots",\n        "cat.chatbots-card-desc": "Conversational AI assistants for all your needs",\n        "cat.chatbots.full":',
        '"cat.writing.full":': '"cat.writing-short": "AI Writing",\n        "cat.writing-card-desc": "Create engaging content with AI-powered tools",\n        "cat.writing.full":',
        '"cat.image.full":': '"cat.image-generation": "AI Image Generation",\n        "cat.image-card-desc": "Transform text into stunning visuals",\n        "cat.image.full":',
        '"cat.video.full":': '"cat.video-short": "AI Video",\n        "cat.video-card-desc": "Generate and edit videos with AI",\n        "cat.video.full":',
        '"cat.audio.full":': '"cat.audio-short": "AI Audio",\n        "cat.audio-card-desc": "Voice synthesis and music generation",\n        "cat.audio.full":',
        '"cat.coding.full":': '"cat.coding-short": "AI Coding",\n        "cat.coding-card-desc": "Code faster with AI-powered assistants",\n        "cat.coding.full":',
        '"cat.productivity.full":': '"cat.productivity-short": "AI Productivity",\n        "cat.productivity-card-desc": "Automate workflows and boost efficiency",\n        "cat.productivity.full":',
        '"cat.seo.full":': '"cat.seo-short": "AI SEO & Marketing",\n        "cat.seo-card-desc": "Optimize content and grow your audience",\n        "cat.seo.full":',
        '"cat.business.full":': '"cat.business-short": "AI Business",\n        "cat.business-card-desc": "Enterprise solutions and analytics",\n        "cat.business.full":',
        '"cat.networking.full":': '"cat.networking-short": "AI Networking",\n        "cat.networking-card-desc": "Network automation and AIOps",\n        "cat.networking.full":',
        '"cat.cybersecurity.full":': '"cat.cybersecurity-short": "AI Cybersecurity",\n        "cat.cybersecurity-card-desc": "Advanced threat detection and response",\n        "cat.cybersecurity.full":',
    }

    # Ajouter les traductions pour "architecture" et "medical"
    architecture_en = '"cat.architecture-short": "AI Architecture",\n        "cat.architecture-card-desc": "Building design and planning tools",\n        '
    medical_en = '"cat.medical-short": "AI Medical",\n        "cat.medical-card-desc": "Healthcare and diagnostic solutions",\n        '
    common_tools = '"common.tools": "tools",\n        '

    # Trouver où insérer (après cybersecurity dans la section EN)
    en_section_marker = '"cat.cybersecurity.full": "Darktrace, CrowdStrike, SentinelOne and more AI-powered security tools.",'
    if en_section_marker in content:
        content = content.replace(
            en_section_marker,
            en_section_marker + '\n        ' + architecture_en + medical_en + common_tools
        )
        print("✅ Ajouté: architecture, medical, tools (EN)")

    # Appliquer les traductions EN
    for old, new in en_translations.items():
        if old in content:
            content = content.replace(old, new, 1)
            print(f"✅ Traduit (EN): {old[:30]}...")

    # Traductions pour l'espagnol
    es_translations = {
        '"cat.chatbots.full":': '"cat.chatbots-short": "Chatbots IA",\n        "cat.chatbots-card-desc": "Asistentes de IA conversacionales para todas tus necesidades",\n        "cat.chatbots.full":',
        '"cat.writing.full":': '"cat.writing-short": "Escritura IA",\n        "cat.writing-card-desc": "Crea contenido atractivo con herramientas impulsadas por IA",\n        "cat.writing.full":',
        '"cat.image.full":': '"cat.image-generation": "Generación de Imágenes IA",\n        "cat.image-card-desc": "Transforma texto en visuales impresionantes",\n        "cat.image.full":',
        '"cat.video.full":': '"cat.video-short": "Video IA",\n        "cat.video-card-desc": "Genera y edita videos con IA",\n        "cat.video.full":',
        '"cat.audio.full":': '"cat.audio-short": "Audio IA",\n        "cat.audio-card-desc": "Síntesis de voz y generación de música",\n        "cat.audio.full":',
        '"cat.coding.full":': '"cat.coding-short": "Codificación IA",\n        "cat.coding-card-desc": "Codifica más rápido con asistentes impulsados por IA",\n        "cat.coding.full":',
        '"cat.productivity.full":': '"cat.productivity-short": "Productividad IA",\n        "cat.productivity-card-desc": "Automatiza flujos de trabajo y aumenta la eficiencia",\n        "cat.productivity.full":',
        '"cat.seo.full":': '"cat.seo-short": "SEO y Marketing IA",\n        "cat.seo-card-desc": "Optimiza contenido y haz crecer tu audiencia",\n        "cat.seo.full":',
        '"cat.business.full":': '"cat.business-short": "Negocios IA",\n        "cat.business-card-desc": "Soluciones empresariales y análisis",\n        "cat.business.full":',
        '"cat.networking.full":': '"cat.networking-short": "Redes IA",\n        "cat.networking-card-desc": "Automatización de redes y AIOps",\n        "cat.networking.full":',
        '"cat.cybersecurity.full":': '"cat.cybersecurity-short": "Ciberseguridad IA",\n        "cat.cybersecurity-card-desc": "Detección y respuesta avanzada de amenazas",\n        "cat.cybersecurity.full":',
    }

    # Trouver la section ES
    es_section_marker_search = 'es: {\n        // Navigation\n        "nav.home": "Inicio",'
    es_cyber_marker = '"cat.cybersecurity.full": "Darktrace, CrowdStrike, SentinelOne y más herramientas de seguridad impulsadas por IA.",'

    if es_cyber_marker in content:
        architecture_es = '"cat.architecture-short": "Arquitectura IA",\n        "cat.architecture-card-desc": "Herramientas de diseño y planificación de edificios",\n        '
        medical_es = '"cat.medical-short": "Medicina IA",\n        "cat.medical-card-desc": "Soluciones de salud y diagnóstico",\n        '
        common_tools_es = '"common.tools": "herramientas",\n        '

        content = content.replace(
            es_cyber_marker,
            es_cyber_marker + '\n        ' + architecture_es + medical_es + common_tools_es
        )
        print("✅ Ajouté: architecture, medical, tools (ES)")

    # Appliquer les traductions ES (seulement dans la section ES)
    es_start = content.find('// ==================== SPANISH ====================')
    de_start = content.find('// ==================== GERMAN ====================')

    if es_start != -1 and de_start != -1:
        before_es = content[:es_start]
        es_section = content[es_start:de_start]
        after_es = content[de_start:]

        for old, new in es_translations.items():
            if old in es_section:
                es_section = es_section.replace(old, new, 1)
                print(f"✅ Traduit (ES): {old[:30]}...")

        content = before_es + es_section + after_es

    # Écrire les modifications
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print("\n✅ Toutes les traductions ont été ajoutées!")
    else:
        print("\nℹ️  Aucune modification nécessaire")

if __name__ == "__main__":
    add_categories_translations()
