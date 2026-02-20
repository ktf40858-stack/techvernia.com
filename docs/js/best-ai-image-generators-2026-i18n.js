// Internationalization for Best AI Image Generators 2026 Blog Article
// This file contains translations for the blog post content

const blogI18n = {
    en: {
        // This is the default language, content is in the HTML file
    },
    fr: {
        title: "Meilleurs Générateurs d'Images IA 2026 : Midjourney vs DALL-E vs Flux",
        subtitle: "Analyse complète des 5 meilleurs outils de création d'images IA avec tests de qualité, analyse des prix et cas d'usage réels",
        readTime: "16 min de lecture",
        date: "13 février 2026",
        author: "Par Kodjo Apedoh"
    },
    es: {
        title: "Mejores Generadores de Imágenes IA 2026: Midjourney vs DALL-E vs Flux",
        subtitle: "Análisis completo de las 5 mejores herramientas de creación de imágenes IA con pruebas de calidad, análisis de precios y casos de uso reales",
        readTime: "16 min de lectura",
        date: "13 de febrero de 2026",
        author: "Por Kodjo Apedoh"
    },
    de: {
        title: "Beste KI-Bildgeneratoren 2026: Midjourney vs DALL-E vs Flux",
        subtitle: "Umfassende Analyse der 5 besten KI-Bilderstellungstools mit Qualitätstests, Preisanalyse und realen Anwendungsfällen",
        readTime: "16 Min. Lesezeit",
        date: "13. Februar 2026",
        author: "Von Kodjo Apedoh"
    },
    pt: {
        title: "Melhores Geradores de Imagens IA 2026: Midjourney vs DALL-E vs Flux",
        subtitle: "Análise completa das 5 melhores ferramentas de criação de imagens IA com testes de qualidade, análise de preços e casos de uso reais",
        readTime: "16 min de leitura",
        date: "13 de fevereiro de 2026",
        author: "Por Kodjo Apedoh"
    },
    zh: {
        title: "2026年最佳AI图像生成器：Midjourney vs DALL-E vs Flux",
        subtitle: "对5大AI图像创建工具进行全面分析，包括质量测试、价格分析和实际用例",
        readTime: "16分钟阅读",
        date: "2026年2月13日",
        author: "作者：Kodjo Apedoh"
    },
    ja: {
        title: "2026年最高のAI画像生成ツール：Midjourney vs DALL-E vs Flux",
        subtitle: "品質テスト、価格分析、実際のユースケースを含む、トップ5のAI画像作成ツールの包括的な分析",
        readTime: "16分で読めます",
        date: "2026年2月13日",
        author: "著者：Kodjo Apedoh"
    },
    ko: {
        title: "2026년 최고의 AI 이미지 생성기: Midjourney vs DALL-E vs Flux",
        subtitle: "품질 테스트, 가격 분석 및 실제 사용 사례를 포함한 상위 5개 AI 이미지 생성 도구의 종합 분석",
        readTime: "16분 읽기",
        date: "2026년 2월 13일",
        author: "저자: Kodjo Apedoh"
    },
    ar: {
        title: "أفضل مولدات الصور بالذكاء الاصطناعي 2026: Midjourney vs DALL-E vs Flux",
        subtitle: "تحليل شامل لأفضل 5 أدوات لإنشاء الصور بالذكاء الاصطناعي مع اختبارات الجودة وتحليل الأسعار وحالات الاستخدام الواقعية",
        readTime: "16 دقيقة قراءة",
        date: "13 فبراير 2026",
        author: "بقلم: Kodjo Apedoh"
    },
    hi: {
        title: "सर्वश्रेष्ठ AI इमेज जेनरेटर 2026: Midjourney vs DALL-E vs Flux",
        subtitle: "गुणवत्ता परीक्षण, मूल्य विश्लेषण और वास्तविक उपयोग के मामलों के साथ शीर्ष 5 AI इमेज निर्माण उपकरणों का व्यापक विश्लेषण",
        readTime: "16 मिनट पढ़ें",
        date: "13 फरवरी 2026",
        author: "लेखक: Kodjo Apedoh"
    }
};

// Apply translations when page loads
document.addEventListener('DOMContentLoaded', function() {
    const currentLang = localStorage.getItem('preferred-language') || 'en';

    if (currentLang !== 'en' && blogI18n[currentLang]) {
        const translations = blogI18n[currentLang];

        // Update meta tags
        if (translations.title) {
            document.title = translations.title + ' | TechVernia';
            const h1 = document.querySelector('h1');
            if (h1) h1.textContent = translations.title;
        }

        if (translations.subtitle) {
            const subtitle = document.querySelector('.subtitle');
            if (subtitle) subtitle.textContent = translations.subtitle;
        }

        // Update meta items
        const metaItems = document.querySelectorAll('.meta-item span');
        if (metaItems[0] && translations.readTime) metaItems[0].textContent = translations.readTime;
        if (metaItems[1] && translations.date) metaItems[1].textContent = translations.date;
        if (metaItems[2] && translations.author) metaItems[2].textContent = translations.author;
    }
});
