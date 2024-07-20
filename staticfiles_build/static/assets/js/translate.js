// Function to initialize Google Translate
function googleTranslateElementInit() {
  new google.translate.TranslateElement({
      pageLanguage: 'en',
      includedLanguages: 'en,fr', // Only include English and French
      layout: google.translate.TranslateElement.InlineLayout.SIMPLE
  }, 'google_translate_element');
}

// Load Google Translate script
var googleTranslateScript = document.createElement('script');
googleTranslateScript.type = 'text/javascript';
googleTranslateScript.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
document.head.appendChild(googleTranslateScript);

// Function to change language
function changeLanguage(lang) {
  var selectField = document.querySelector('select.goog-te-combo');
  if (selectField) {
      selectField.value = lang;
      selectField.dispatchEvent(new Event('change'));
  }
}

// Toggle language when button is clicked
document.getElementById('langToggle').addEventListener('click', function() {
  var currentLang = this.textContent;
  if (currentLang === 'ENG') {
      changeLanguage('fr');
      this.textContent = 'FRE';
  } else {
      changeLanguage('en');
      this.textContent = 'ENG';
  }
});