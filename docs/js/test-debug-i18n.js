// TEST DEBUG I18N
const testdebugTranslations = {
  "en": {
      "review.test-debug.console.log": "Console Log:",
      "review.test-debug.test.1.lien.direct.simple": "Test 1: Lien Direct Simple",
      "review.test-debug.test.2.bouton.avec.javascript": "Test 2: Bouton avec JavaScript",
      "review.test-debug.test.3.vrifier.si.le": "Test 3: Vérifier si le fichier existe",
      "review.test-debug.test.4.chemin.absolu": "Test 4: Chemin absolu",
      "review.test-debug.test.de.navigation.-.certifications": "Test de Navigation - Certifications"
  },
  "de": {
      "review.test-debug.console.log": "Console Log:",
      "review.test-debug.test.1.lien.direct.simple": "Test 1: Lien Direct Simple",
      "review.test-debug.test.2.bouton.avec.javascript": "Test 2: Bouton avec JavaScript",
      "review.test-debug.test.3.vrifier.si.le": "Test 3: Vérifier si le fichier existe",
      "review.test-debug.test.4.chemin.absolu": "Test 4: Chemin absolu",
      "review.test-debug.test.de.navigation.-.certifications": "Test de Navigation - Certifications"
  },
  "fr": {
      "review.test-debug.console.log": "Console Log:",
      "review.test-debug.test.1.lien.direct.simple": "Test 1: Lien Direct Simple",
      "review.test-debug.test.2.bouton.avec.javascript": "Test 2: Bouton avec JavaScript",
      "review.test-debug.test.3.vrifier.si.le": "Test 3: Vérifier si le fichier existe",
      "review.test-debug.test.4.chemin.absolu": "Test 4: Chemin absolu",
      "review.test-debug.test.de.navigation.-.certifications": "Test de Navigation - Certifications"
  },
  "es": {
      "review.test-debug.console.log": "Console Log:",
      "review.test-debug.test.1.lien.direct.simple": "Test 1: Lien Direct Simple",
      "review.test-debug.test.2.bouton.avec.javascript": "Test 2: Bouton avec JavaScript",
      "review.test-debug.test.3.vrifier.si.le": "Test 3: Vérifier si le fichier existe",
      "review.test-debug.test.4.chemin.absolu": "Test 4: Chemin absolu",
      "review.test-debug.test.de.navigation.-.certifications": "Test de Navigation - Certifications"
  },
  "pt": {
      "review.test-debug.console.log": "Console Log:",
      "review.test-debug.test.1.lien.direct.simple": "Test 1: Lien Direct Simple",
      "review.test-debug.test.2.bouton.avec.javascript": "Test 2: Bouton avec JavaScript",
      "review.test-debug.test.3.vrifier.si.le": "Test 3: Vérifier si le fichier existe",
      "review.test-debug.test.4.chemin.absolu": "Test 4: Chemin absolu",
      "review.test-debug.test.de.navigation.-.certifications": "Test de Navigation - Certifications"
  },
  "zh": {
      "review.test-debug.console.log": "Console Log:",
      "review.test-debug.test.1.lien.direct.simple": "Test 1: Lien Direct Simple",
      "review.test-debug.test.2.bouton.avec.javascript": "Test 2: Bouton avec JavaScript",
      "review.test-debug.test.3.vrifier.si.le": "Test 3: Vérifier si le fichier existe",
      "review.test-debug.test.4.chemin.absolu": "Test 4: Chemin absolu",
      "review.test-debug.test.de.navigation.-.certifications": "Test de Navigation - Certifications"
  },
  "ja": {
      "review.test-debug.console.log": "Console Log:",
      "review.test-debug.test.1.lien.direct.simple": "Test 1: Lien Direct Simple",
      "review.test-debug.test.2.bouton.avec.javascript": "Test 2: Bouton avec JavaScript",
      "review.test-debug.test.3.vrifier.si.le": "Test 3: Vérifier si le fichier existe",
      "review.test-debug.test.4.chemin.absolu": "Test 4: Chemin absolu",
      "review.test-debug.test.de.navigation.-.certifications": "Test de Navigation - Certifications"
  },
  "ko": {
      "review.test-debug.console.log": "Console Log:",
      "review.test-debug.test.1.lien.direct.simple": "Test 1: Lien Direct Simple",
      "review.test-debug.test.2.bouton.avec.javascript": "Test 2: Bouton avec JavaScript",
      "review.test-debug.test.3.vrifier.si.le": "Test 3: Vérifier si le fichier existe",
      "review.test-debug.test.4.chemin.absolu": "Test 4: Chemin absolu",
      "review.test-debug.test.de.navigation.-.certifications": "Test de Navigation - Certifications"
  },
  "ar": {
      "review.test-debug.console.log": "Console Log:",
      "review.test-debug.test.1.lien.direct.simple": "Test 1: Lien Direct Simple",
      "review.test-debug.test.2.bouton.avec.javascript": "Test 2: Bouton avec JavaScript",
      "review.test-debug.test.3.vrifier.si.le": "Test 3: Vérifier si le fichier existe",
      "review.test-debug.test.4.chemin.absolu": "Test 4: Chemin absolu",
      "review.test-debug.test.de.navigation.-.certifications": "Test de Navigation - Certifications"
  },
  "hi": {
      "review.test-debug.console.log": "Console Log:",
      "review.test-debug.test.1.lien.direct.simple": "Test 1: Lien Direct Simple",
      "review.test-debug.test.2.bouton.avec.javascript": "Test 2: Bouton avec JavaScript",
      "review.test-debug.test.3.vrifier.si.le": "Test 3: Vérifier si le fichier existe",
      "review.test-debug.test.4.chemin.absolu": "Test 4: Chemin absolu",
      "review.test-debug.test.de.navigation.-.certifications": "Test de Navigation - Certifications"
  }
};


function getTestdebugTranslation(key, lang) {
  if (testdebugTranslations[lang] && testdebugTranslations[lang][key]) {
    return testdebugTranslations[lang][key];
  }
  if (testdebugTranslations.en && testdebugTranslations.en[key]) {
    return testdebugTranslations.en[key];
  }
  return null;
}

function applyTestdebugTranslations(lang) {
  
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.getAttribute('data-i18n');
    if (key && (key.startsWith('review.test-debug.') || key.startsWith('review.common.'))) {
      const translation = getTestdebugTranslation(key, lang);
      if (translation) {
        element.textContent = translation;
        count++;
      }
    }
  });
  
}

document.addEventListener('languageChanged', (e) => {
  const lang = e.detail.language;
  setTimeout(() => applyTestdebugTranslations(lang), 200);
});

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    applyTestdebugTranslations(currentLang);
  });
} else {
  const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
  applyTestdebugTranslations(currentLang);
}


