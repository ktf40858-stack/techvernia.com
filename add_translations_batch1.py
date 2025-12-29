import json
import os

base_dir = r'C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\seo'

with open(os.path.join(base_dir, 'frase-batch1.json'), 'r', encoding='utf-8') as f:
    batch1 = json.load(f)

batch1['es'] = {
    "review.common.try.it.now": "Pruébalo Ahora",
    "review.frase.start.free.trial": "Comenzar Prueba Gratuita →",
    "review.frase.view.pricing": "Ver Precios",
    "review.common.overview": "Descripción General",
    "review.frase.frase.is.an.all-in-one.ai-powered": "Frase es una plataforma todo en uno impulsada por IA para investigación, escritura y optimización de contenido, diseñada para ayudar a los creadores de contenido a producir artículos optimizados para SEO de manera más rápida y efectiva. Con más de 30,000 usuarios incluyendo especialistas en marketing, agencias y equipos de contenido, Frase combina potente análisis SERP, generación de contenido con IA y herramientas de optimización en un flujo de trabajo simplificado que te lleva desde la investigación hasta el contenido publicado.",
    "review.frase.what.makes.frase.unique.is": "Lo que hace único a Frase es su enfoque integral de la creación de contenido. La plataforma comienza con un análisis profundo de SERP para comprender qué está clasificando para tus palabras clave objetivo, genera resúmenes de contenido impulsados por IA con encabezados y temas recomendados, y proporciona un escritor de IA para ayudar a redactar contenido. El optimizador de contenido luego califica tu trabajo en tiempo real, asegurando que esté completamente optimizado antes de la publicación. Este flujo de trabajo de extremo a extremo hace que Frase sea particularmente valioso para equipos que necesitan producir contenido SEO de alta calidad a escala.",
    "review.frase.trusted.by.companies.like.hubspot": "Confiado por empresas como HubSpot, Mailchimp y Semrush, Frase sobresale en responder la pregunta clave: \"¿Sobre qué debo escribir para clasificar para esta palabra clave?\" El analizador SERP de la plataforma extrae información de páginas mejor clasificadas, identifica preguntas comunes que la gente hace y sugiere estructura de contenido, todo impulsado por IA para ahorrarte horas de investigación manual.",
    "review.common.key.features": "Características Clave",
    "review.frase.automatically.generate.comprehensive.content.briefs": "Genere automáticamente resúmenes de contenido completos con encabezados, temas y preguntas sugeridos para responder basados en el análisis SERP.",
    "review.frase.analyze.top-ranking.pages.for.any": "Analice páginas mejor clasificadas para cualquier palabra clave. Extraiga temas clave, estadísticas y patrones de contenido que impulsan las clasificaciones.",
    "review.frase.generate.high-quality.content.paragraphs.and": "Genere párrafos y secciones de contenido de alta calidad usando IA. Cree primeros borradores más rápido con asistencia de escritura GPT.",
    "review.frase.build.seo-optimized.content.outlines.by": "Construya esquemas de contenido optimizados para SEO extrayendo encabezados de páginas mejor clasificadas. Comience con estructuras probadas.",
    "review.frase.real-time.content.scoring.as.you": "Puntuación de contenido en tiempo real mientras escribe. Obtenga retroalimentación instantánea sobre el uso de palabras clave, cobertura de temas y optimización.",
    "review.frase.discover.questions.people.are.asking": "Descubra preguntas que la gente está haciendo sobre su tema. Responda la intención del usuario con contenido completo y útil.",
    "review.frase.track.content.performance.keyword.rankings": "Rastree el rendimiento del contenido, clasificaciones de palabras clave y puntajes de optimización. Mida el impacto de sus esfuerzos de contenido.",
    "review.frase.connect.with.google.docs.wordpress": "Conéctese con Google Docs, WordPress y otras herramientas. Integre perfectamente Frase en su flujo de trabajo existente.",
    "review.frase.pros.cons": "Pros y Contras",
    "review.frase.all-in-one.content.workflow": "Flujo de trabajo de contenido todo en uno",
    "review.frase.powerful.serp.analysis": "Análisis SERP potente",
    "review.frase.ai.content.brief.generation": "Generación de resúmenes de contenido con IA",
    "review.frase.built-in.ai.writing.assistant": "Asistente de escritura con IA integrado",
    "review.frase.real-time.optimization.scoring": "Puntuación de optimización en tiempo real",
    "review.frase.affordable.pricing.for.features.offered": "Precios asequibles para las funciones ofrecidas",
    "review.frase.great.question.research.tool": "Excelente herramienta de investigación de preguntas",
    "review.frase.wordpress.and.google.docs.integration": "Integración con WordPress y Google Docs",
    "review.frase.fast.content.brief.creation": "Creación rápida de resúmenes de contenido",
    "review.frase.excellent.for.content.teams": "Excelente para equipos de contenido",
    "review.frase.ai.writing.quality.varies": "La calidad de escritura con IA varía"
}

with open(os.path.join(base_dir, 'frase-batch1.json'), 'w', encoding='utf-8') as f:
    json.dump(batch1, f, ensure_ascii=False, indent=2)

print("Updated frase-batch1.json with ES translations")
