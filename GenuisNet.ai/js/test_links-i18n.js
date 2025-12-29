// TEST_LINKS I18N
const test_linksTranslations = {
  "en": {
      "review.test_links.ccie.enterprise": "CCIE Enterprise",
      "review.test_links.ccna": "CCNA",
      "review.test_links.ccnp.enterprise": "CCNP Enterprise",
      "review.test_links.devnet.associate": "DevNet Associate",
      "review.test_links.infrastructure.specialist": "Infrastructure Specialist",
      "review.test_links.test.certification.links": "Test Certification Links",
      "review.test_links.wireless.specialist": "Wireless Specialist"
  },
  "de": {
      "review.test_links.ccie.enterprise": "CCIE Enterprise",
      "review.test_links.ccna": "CCNA",
      "review.test_links.ccnp.enterprise": "CCNP Enterprise",
      "review.test_links.devnet.associate": "DevNet Associate",
      "review.test_links.infrastructure.specialist": "Infrastructure Specialist",
      "review.test_links.test.certification.links": "Test Certification Links",
      "review.test_links.wireless.specialist": "Wireless Specialist"
  },
  "fr": {
      "review.test_links.ccie.enterprise": "CCIE Enterprise",
      "review.test_links.ccna": "CCNA",
      "review.test_links.ccnp.enterprise": "CCNP Enterprise",
      "review.test_links.devnet.associate": "DevNet Associate",
      "review.test_links.infrastructure.specialist": "Infrastructure Specialist",
      "review.test_links.test.certification.links": "Test Certification Links",
      "review.test_links.wireless.specialist": "Wireless Specialist"
  },
  "es": {
      "review.test_links.ccie.enterprise": "CCIE Enterprise",
      "review.test_links.ccna": "CCNA",
      "review.test_links.ccnp.enterprise": "CCNP Enterprise",
      "review.test_links.devnet.associate": "DevNet Associate",
      "review.test_links.infrastructure.specialist": "Infrastructure Specialist",
      "review.test_links.test.certification.links": "Test Certification Links",
      "review.test_links.wireless.specialist": "Wireless Specialist"
  },
  "pt": {
      "review.test_links.ccie.enterprise": "CCIE Enterprise",
      "review.test_links.ccna": "CCNA",
      "review.test_links.ccnp.enterprise": "CCNP Enterprise",
      "review.test_links.devnet.associate": "DevNet Associate",
      "review.test_links.infrastructure.specialist": "Infrastructure Specialist",
      "review.test_links.test.certification.links": "Test Certification Links",
      "review.test_links.wireless.specialist": "Wireless Specialist"
  },
  "zh": {
      "review.test_links.ccie.enterprise": "CCIE Enterprise",
      "review.test_links.ccna": "CCNA",
      "review.test_links.ccnp.enterprise": "CCNP Enterprise",
      "review.test_links.devnet.associate": "DevNet Associate",
      "review.test_links.infrastructure.specialist": "Infrastructure Specialist",
      "review.test_links.test.certification.links": "Test Certification Links",
      "review.test_links.wireless.specialist": "Wireless Specialist"
  },
  "ja": {
      "review.test_links.ccie.enterprise": "CCIE Enterprise",
      "review.test_links.ccna": "CCNA",
      "review.test_links.ccnp.enterprise": "CCNP Enterprise",
      "review.test_links.devnet.associate": "DevNet Associate",
      "review.test_links.infrastructure.specialist": "Infrastructure Specialist",
      "review.test_links.test.certification.links": "Test Certification Links",
      "review.test_links.wireless.specialist": "Wireless Specialist"
  },
  "ko": {
      "review.test_links.ccie.enterprise": "CCIE Enterprise",
      "review.test_links.ccna": "CCNA",
      "review.test_links.ccnp.enterprise": "CCNP Enterprise",
      "review.test_links.devnet.associate": "DevNet Associate",
      "review.test_links.infrastructure.specialist": "Infrastructure Specialist",
      "review.test_links.test.certification.links": "Test Certification Links",
      "review.test_links.wireless.specialist": "Wireless Specialist"
  },
  "ar": {
      "review.test_links.ccie.enterprise": "CCIE Enterprise",
      "review.test_links.ccna": "CCNA",
      "review.test_links.ccnp.enterprise": "CCNP Enterprise",
      "review.test_links.devnet.associate": "DevNet Associate",
      "review.test_links.infrastructure.specialist": "Infrastructure Specialist",
      "review.test_links.test.certification.links": "Test Certification Links",
      "review.test_links.wireless.specialist": "Wireless Specialist"
  },
  "hi": {
      "review.test_links.ccie.enterprise": "CCIE Enterprise",
      "review.test_links.ccna": "CCNA",
      "review.test_links.ccnp.enterprise": "CCNP Enterprise",
      "review.test_links.devnet.associate": "DevNet Associate",
      "review.test_links.infrastructure.specialist": "Infrastructure Specialist",
      "review.test_links.test.certification.links": "Test Certification Links",
      "review.test_links.wireless.specialist": "Wireless Specialist"
  }
};


function getTest_linksTranslation(key, lang) {
  if (test_linksTranslations[lang] && test_linksTranslations[lang][key]) {
    return test_linksTranslations[lang][key];
  }
  if (test_linksTranslations.en && test_linksTranslations.en[key]) {
    return test_linksTranslations.en[key];
  }
  return null;
}

function applyTest_linksTranslations(lang) {
  console.log(`🔥 Applying test_links translations for: ${lang}`);
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.getAttribute('data-i18n');
    if (key && (key.startsWith('review.test_links.') || key.startsWith('review.common.'))) {
      const translation = getTest_linksTranslation(key, lang);
      if (translation) {
        element.textContent = translation;
        count++;
      }
    }
  });
  console.log(`✅ Applied ${count} test_links translations`);
}

window.addEventListener('languageChanged', (e) => {
  const lang = e.detail.language;
  setTimeout(() => applyTest_linksTranslations(lang), 200);
});

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    applyTest_linksTranslations(currentLang);
  });
} else {
  const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
  applyTest_linksTranslations(currentLang);
}

console.log('✅ test_links i18n loaded');
