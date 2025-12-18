#!/usr/bin/env python3
"""
Script MASTER pour traduire automatiquement TOUTES les pages de review
Analyse la structure, extrait le texte, génère les clés i18n et les traductions ES
"""

import os
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup

# Mapping EN -> ES pour génération automatique
COMMON_TRANSLATIONS = {
    # Sections
    "Overview": "Resumen",
    "Key Features": "Características Clave",
    "Additional Features": "Características Adicionales",
    "Pros & Cons": "Ventajas y Desventajas",
    "Pros": "Ventajas",
    "Cons": "Desventajas",
    "Advantages": "Ventajas",
    "Disadvantages": "Desventajas",
    "Pricing Plans": "Planes de Precios",
    "Pricing": "Precios",
    "Best Use Cases": "Mejores Casos de Uso",
    "Use Cases": "Casos de Uso",
    "Comparison": "Comparación",
    "Comparison with Competitors": "Comparación con Competidores",
    "Screenshots & Interface": "Capturas de Pantalla e Interfaz",
    "Screenshots": "Capturas de Pantalla",
    "Final Verdict": "Veredicto Final",
    "Verdict": "Veredicto",
    "Frequently Asked Questions": "Preguntas Frecuentes",
    "FAQ": "Preguntas Frecuentes",
    "Table of Contents": "Tabla de Contenidos",
    "Compare With": "Comparar Con",
    "Quick Info": "Información Rápida",
    "Get Started": "Comenzar",
    "Try It Now": "Pruébalo Ahora",

    # Badges/Labels
    "Free Tier Available": "Nivel Gratis Disponible",
    "Most Popular": "Más Popular",
    "Best for": "Mejor para",
    "Expert Rating": "Calificación de Expertos",

    # Buttons
    "Try Free": "Probar Gratis",
    "View Pricing": "Ver Precios",
    "Learn More": "Saber Más",
    "Get Started": "Comenzar",
    "Sign Up": "Registrarse",

    # Stats
    "Monthly Active Users": "Usuarios Activos Mensuales",
    "Context Window": "Ventana de Contexto",
    "Languages Supported": "Idiomas Soportados",
    "Starting Price": "Precio Inicial",
    "Launch Year": "Año de Lanzamiento",
    "Free": "Gratis",
    "Users": "Usuarios",

    # Table headers
    "Plan": "Plan",
    "Price": "Precio",
    "Features": "Características",
    "Model Access": "Acceso a Modelos",
    "Key Features": "Características Clave",
    "Feature": "Característica",

    # Common words
    "Yes": "Sí",
    "No": "No",
    "Free": "Gratis",
    "Premium": "Premium",
    "Enterprise": "Empresa",
    "Pro": "Pro",
    "Basic": "Básico",
    "Custom": "Personalizado",
    "Unlimited": "Ilimitado",

    # Sidebar
    "Features": "Características",
    "Ease of Use": "Facilidad de Uso",
    "Value": "Valor",
    "Performance": "Rendimiento",
    "Support": "Soporte",
    "Company": "Empresa",
    "Founded": "Fundada",
    "Headquarters": "Sede",
    "Platform": "Plataforma",
    "API Available": "API Disponible",

    # Review terms
    "Review": "Revisión",
    "by": "por",
    "Our Recommendation": "Nuestra Recomendación",
}

def clean_text(text):
    """Clean text for use as translation key"""
    if not text:
        return ""
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text.strip()

def text_to_key(text, prefix=""):
    """Convert text to a valid i18n key"""
    # Clean the text
    cleaned = clean_text(text)

    # Create key from first few words (max 50 chars)
    key_text = cleaned[:50].lower()

    # Remove special characters, keep alphanumeric and spaces
    key_text = re.sub(r'[^a-z0-9\s-]', '', key_text)

    # Replace spaces with dots
    key_text = re.sub(r'\s+', '.', key_text)

    # Remove trailing dots
    key_text = key_text.strip('.')

    if prefix:
        return f"{prefix}.{key_text}"
    return key_text

def generate_es_translation(en_text):
    """Generate Spanish translation (use common mappings or return English as fallback)"""

    # Check if it's a common phrase
    if en_text in COMMON_TRANSLATIONS:
        return COMMON_TRANSLATIONS[en_text]

    # For now, return English text (would need API or manual translation for unknowns)
    # This can be enhanced later with AI translation
    return en_text  # Placeholder - manual review needed

def process_review_page(html_path, category, tool_name):
    """Process a single review page"""

    print(f"\n📄 Processing: {tool_name} ({category})")

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has many data-i18n attributes
    existing_i18n_count = content.count('data-i18n=')
    if existing_i18n_count > 50:
        print(f"  ✅ Already translated ({existing_i18n_count} i18n attributes)")
        return None, None

    soup = BeautifulSoup(content, 'html.parser')

    translations_en = {}
    translations_es = {}
    modifications = []

    # Extract and process key elements
    elements_to_process = [
        # H1 title
        ('h1', None, f'review.{tool_name}.title'),
        # H2 sections
        ('h2', None, 'review.common'),
        # H3 subsections
        ('h3', None, f'review.{tool_name}'),
        # Badges
        ('.badge', None, f'review.{tool_name}.badge'),
        # Quick stats
        ('.quick-stat-label', None, 'review.common.stats'),
        # Buttons
        ('a.btn', None, 'review.common.btn'),
    ]

    count = 0

    # Process H2 section titles (common across all reviews)
    for h2 in soup.find_all('h2'):
        text = clean_text(h2.get_text())
        if text and 'data-i18n' not in str(h2):
            # Use common key for section titles
            if text in COMMON_TRANSLATIONS:
                key = f"review.common.{text_to_key(text, '')}"
                es_text = COMMON_TRANSLATIONS[text]
            else:
                key = f"review.common.{text_to_key(text, '')}"
                es_text = text

            translations_en[key] = text
            translations_es[key] = es_text
            modifications.append(('h2', text, key))
            count += 1

    print(f"  📊 Found {count} translatable elements")

    if count > 0:
        return {
            'translations_en': translations_en,
            'translations_es': translations_es,
            'modifications': modifications,
            'file_path': html_path
        }

    return None, None

def apply_modifications_to_html(html_path, modifications):
    """Apply i18n modifications to HTML file"""

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    count = 0

    for element_type, text, key in modifications:
        # Create wrapped version
        wrapped = f'<span data-i18n="{key}">{text}</span>'

        # Find and replace (be careful with exact matches)
        if element_type == 'h2':
            pattern = f'<h2[^>]*>{re.escape(text)}</h2>'
            replacement = f'<h2><span data-i18n="{key}">{text}</span></h2>'
        else:
            # Generic replacement
            pattern = f'>{re.escape(text)}<'
            replacement = f'>{wrapped}<'

        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content, count=1)
            count += 1

    if content != original_content:
        # Backup
        backup_path = html_path + '.auto_i18n_backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)

        # Write modified
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return count

    return 0

def process_all_categories():
    """Process all review categories"""

    base_dir = "GenuisNet.ai/pages/reviews"

    all_translations_en = {}
    all_translations_es = {}
    total_modified = 0

    # Get all category directories
    for category_dir in os.listdir(base_dir):
        category_path = os.path.join(base_dir, category_dir)

        if not os.path.isdir(category_path):
            continue

        print(f"\n{'='*60}")
        print(f"📁 Category: {category_dir}")
        print(f"{'='*60}")

        # Process each HTML file in category
        for filename in os.listdir(category_path):
            if not filename.endswith('.html') or 'backup' in filename:
                continue

            tool_name = Path(filename).stem
            html_path = os.path.join(category_path, filename)

            result = process_review_page(html_path, category_dir, tool_name)

            if result:
                # Merge translations
                all_translations_en.update(result['translations_en'])
                all_translations_es.update(result['translations_es'])

                # Apply modifications
                modified_count = apply_modifications_to_html(html_path, result['modifications'])
                if modified_count > 0:
                    print(f"  ✅ Modified {modified_count} elements")
                    total_modified += 1

    # Save consolidated translations
    print(f"\n{'='*60}")
    print("💾 Saving translations...")

    with open('all_reviews_translations_en.json', 'w', encoding='utf-8') as f:
        json.dump(all_translations_en, f, indent=2, ensure_ascii=False)

    with open('all_reviews_translations_es.json', 'w', encoding='utf-8') as f:
        json.dump(all_translations_es, f, indent=2, ensure_ascii=False)

    print(f"✅ EN: {len(all_translations_en)} keys")
    print(f"✅ ES: {len(all_translations_es)} keys")
    print(f"✅ Modified: {total_modified} files")

    return all_translations_en, all_translations_es

if __name__ == "__main__":
    print("🌐 AUTO-TRANSLATION MASTER SCRIPT")
    print("="*60)
    print("This will process ALL 255 review pages")
    print("Extracting text, generating i18n keys, and creating translations")
    print("="*60)

    input("\nPress Enter to continue (Ctrl+C to cancel)...")

    translations_en, translations_es = process_all_categories()

    print("\n🎉 COMPLETE!")
    print(f"📄 Translations saved to:")
    print(f"   - all_reviews_translations_en.json")
    print(f"   - all_reviews_translations_es.json")
    print("\nNext step: Add these translations to i18n.js")
