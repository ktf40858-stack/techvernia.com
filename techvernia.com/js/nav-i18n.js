// NAVIGATION I18N
const navTranslations = {
  "en": {
    "nav.home": "Home",
    "nav.guides": "Guides",
    "nav.compare": "Compare",
    "nav.about": "About",
    "nav.blog": "Blog",
    "nav.contact": "Contact"
  },
  "es": {
    "nav.home": "Inicio",
    "nav.guides": "Guías",
    "nav.compare": "Comparar",
    "nav.about": "Acerca de",
    "nav.blog": "Blog",
    "nav.contact": "Contacto"
  },
  "fr": {
    "nav.home": "Accueil",
    "nav.guides": "Guides",
    "nav.compare": "Comparer",
    "nav.about": "À propos",
    "nav.blog": "Blog",
    "nav.contact": "Contact"
  },
  "de": {
    "nav.home": "Startseite",
    "nav.guides": "Leitfaden",
    "nav.compare": "Vergleich",
    "nav.about": "Über uns",
    "nav.blog": "Blog",
    "nav.contact": "Kontakt"
  },
  "pt": {
    "nav.home": "Início",
    "nav.guides": "Guias",
    "nav.compare": "Comparar",
    "nav.about": "Sobre",
    "nav.blog": "Blog",
    "nav.contact": "Contato"
  },
  "zh": {
    "nav.home": "首页",
    "nav.guides": "指南",
    "nav.compare": "比较",
    "nav.about": "关于",
    "nav.blog": "博客",
    "nav.contact": "联系"
  },
  "ja": {
    "nav.home": "ホーム",
    "nav.guides": "ガイド",
    "nav.compare": "比較",
    "nav.about": "について",
    "nav.blog": "ブログ",
    "nav.contact": "お問い合わせ"
  },
  "ko": {
    "nav.home": "홈",
    "nav.guides": "가이드",
    "nav.compare": "비교",
    "nav.about": "소개",
    "nav.blog": "블로그",
    "nav.contact": "연락처"
  },
  "ar": {
    "nav.home": "الرئيسية",
    "nav.guides": "الأدلة",
    "nav.compare": "قارن",
    "nav.about": "حول",
    "nav.blog": "مدونة",
    "nav.contact": "اتصل"
  },
  "hi": {
    "nav.home": "होम",
    "nav.guides": "गाइड",
    "nav.compare": "तुलना",
    "nav.about": "के बारे में",
    "nav.blog": "ब्लॉग",
    "nav.contact": "संपर्क"
  }
};

function getNavTranslation(key, lang) {
    return (navTranslations[lang] && navTranslations[lang][key]) ||
           (navTranslations.en && navTranslations.en[key]) || null;
}

function applyNavTranslations(lang) {
    let count = 0;
    document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        if (key && key.startsWith("nav.")) {
            const translation = getNavTranslation(key, lang);
            if (translation) { el.textContent = translation; count++; }
        }
    });
    
}

window.addEventListener("languageChanged", e => setTimeout(() => applyNavTranslations(e.detail.language), 200));

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => applyNavTranslations(window.i18n?.getCurrentLanguage() || "en"));
} else {
    applyNavTranslations(window.i18n?.getCurrentLanguage() || "en");
}
