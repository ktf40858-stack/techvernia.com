// TEST SIMPLE I18N
const testsimpleTranslations = {
  "en": {
      "review.test-simple.ccna.-.cliquez.ici": "CCNA - Cliquez ici",
      "review.test-simple.ce.lien.devrait.ouvrir.ccnahtml": "Ce lien devrait ouvrir ccna.html",
      "review.test-simple.ce.lien.devrait.ouvrir.devnet-associatehtml": "Ce lien devrait ouvrir devnet-associate.html",
      "review.test-simple.devnet.-.cliquez.ici": "DevNet - Cliquez ici",
      "review.test-simple.test.des.liens.de.certification": "Test des liens de certification"
  },
  "de": {
      "review.test-simple.ccna.-.cliquez.ici": "CCNA - Cliquez ici",
      "review.test-simple.ce.lien.devrait.ouvrir.ccnahtml": "Ce lien devrait ouvrir ccna.html",
      "review.test-simple.ce.lien.devrait.ouvrir.devnet-associatehtml": "Ce lien devrait ouvrir devnet-associate.html",
      "review.test-simple.devnet.-.cliquez.ici": "DevNet - Cliquez ici",
      "review.test-simple.test.des.liens.de.certification": "Test des liens de certification"
  },
  "fr": {
      "review.test-simple.ccna.-.cliquez.ici": "CCNA - Cliquez ici",
      "review.test-simple.ce.lien.devrait.ouvrir.ccnahtml": "Ce lien devrait ouvrir ccna.html",
      "review.test-simple.ce.lien.devrait.ouvrir.devnet-associatehtml": "Ce lien devrait ouvrir devnet-associate.html",
      "review.test-simple.devnet.-.cliquez.ici": "DevNet - Cliquez ici",
      "review.test-simple.test.des.liens.de.certification": "Test des liens de certification"
  },
  "es": {
      "review.test-simple.ccna.-.cliquez.ici": "CCNA - Cliquez ici",
      "review.test-simple.ce.lien.devrait.ouvrir.ccnahtml": "Ce lien devrait ouvrir ccna.html",
      "review.test-simple.ce.lien.devrait.ouvrir.devnet-associatehtml": "Ce lien devrait ouvrir devnet-associate.html",
      "review.test-simple.devnet.-.cliquez.ici": "DevNet - Cliquez ici",
      "review.test-simple.test.des.liens.de.certification": "Test des liens de certification"
  },
  "pt": {
      "review.test-simple.ccna.-.cliquez.ici": "CCNA - Cliquez ici",
      "review.test-simple.ce.lien.devrait.ouvrir.ccnahtml": "Ce lien devrait ouvrir ccna.html",
      "review.test-simple.ce.lien.devrait.ouvrir.devnet-associatehtml": "Ce lien devrait ouvrir devnet-associate.html",
      "review.test-simple.devnet.-.cliquez.ici": "DevNet - Cliquez ici",
      "review.test-simple.test.des.liens.de.certification": "Test des liens de certification"
  },
  "zh": {
      "review.test-simple.ccna.-.cliquez.ici": "CCNA - Cliquez ici",
      "review.test-simple.ce.lien.devrait.ouvrir.ccnahtml": "Ce lien devrait ouvrir ccna.html",
      "review.test-simple.ce.lien.devrait.ouvrir.devnet-associatehtml": "Ce lien devrait ouvrir devnet-associate.html",
      "review.test-simple.devnet.-.cliquez.ici": "DevNet - Cliquez ici",
      "review.test-simple.test.des.liens.de.certification": "Test des liens de certification"
  },
  "ja": {
      "review.test-simple.ccna.-.cliquez.ici": "CCNA - Cliquez ici",
      "review.test-simple.ce.lien.devrait.ouvrir.ccnahtml": "Ce lien devrait ouvrir ccna.html",
      "review.test-simple.ce.lien.devrait.ouvrir.devnet-associatehtml": "Ce lien devrait ouvrir devnet-associate.html",
      "review.test-simple.devnet.-.cliquez.ici": "DevNet - Cliquez ici",
      "review.test-simple.test.des.liens.de.certification": "Test des liens de certification"
  },
  "ko": {
      "review.test-simple.ccna.-.cliquez.ici": "CCNA - Cliquez ici",
      "review.test-simple.ce.lien.devrait.ouvrir.ccnahtml": "Ce lien devrait ouvrir ccna.html",
      "review.test-simple.ce.lien.devrait.ouvrir.devnet-associatehtml": "Ce lien devrait ouvrir devnet-associate.html",
      "review.test-simple.devnet.-.cliquez.ici": "DevNet - Cliquez ici",
      "review.test-simple.test.des.liens.de.certification": "Test des liens de certification"
  },
  "ar": {
      "review.test-simple.ccna.-.cliquez.ici": "CCNA - Cliquez ici",
      "review.test-simple.ce.lien.devrait.ouvrir.ccnahtml": "Ce lien devrait ouvrir ccna.html",
      "review.test-simple.ce.lien.devrait.ouvrir.devnet-associatehtml": "Ce lien devrait ouvrir devnet-associate.html",
      "review.test-simple.devnet.-.cliquez.ici": "DevNet - Cliquez ici",
      "review.test-simple.test.des.liens.de.certification": "Test des liens de certification"
  },
  "hi": {
      "review.test-simple.ccna.-.cliquez.ici": "CCNA - Cliquez ici",
      "review.test-simple.ce.lien.devrait.ouvrir.ccnahtml": "Ce lien devrait ouvrir ccna.html",
      "review.test-simple.ce.lien.devrait.ouvrir.devnet-associatehtml": "Ce lien devrait ouvrir devnet-associate.html",
      "review.test-simple.devnet.-.cliquez.ici": "DevNet - Cliquez ici",
      "review.test-simple.test.des.liens.de.certification": "Test des liens de certification"
  }
};


function getTestsimpleTranslation(key, lang) {
  if (testsimpleTranslations[lang] && testsimpleTranslations[lang][key]) {
    return testsimpleTranslations[lang][key];
  }
  if (testsimpleTranslations.en && testsimpleTranslations.en[key]) {
    return testsimpleTranslations.en[key];
  }
  return null;
}

function applyTestsimpleTranslations(lang) {
  console.log(`🔥 Applying test-simple translations for: ${lang}`);
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.getAttribute('data-i18n');
    if (key && (key.startsWith('review.test-simple.') || key.startsWith('review.common.'))) {
      const translation = getTestsimpleTranslation(key, lang);
      if (translation) {
        element.textContent = translation;
        count++;
      }
    }
  });
  console.log(`✅ Applied ${count} test-simple translations`);
}

window.addEventListener('languageChanged', (e) => {
  const lang = e.detail.language;
  setTimeout(() => applyTestsimpleTranslations(lang), 200);
});

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    applyTestsimpleTranslations(currentLang);
  });
} else {
  const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
  applyTestsimpleTranslations(currentLang);
}

console.log('✅ test-simple i18n loaded');
