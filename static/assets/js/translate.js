document.getElementById('langToggle').addEventListener('click', function () {
    var currentLang = this.textContent;
    var newLang = currentLang === 'ENG' ? 'FRE' : 'ENG';
    this.textContent = newLang;
  
    var googleTranslateCombo = document.querySelector('.goog-te-combo');
    if (newLang === 'FRE') {
      googleTranslateCombo.value = 'fr';
    } else {
      googleTranslateCombo.value = 'en';
    }
    googleTranslateCombo.dispatchEvent(new Event('change'));
  });
  
  function setInitialLanguage() {
    var googleTranslateCombo = document.querySelector('.goog-te-combo');
    if (googleTranslateCombo) {
      var userLang = navigator.language || navigator.userLanguage;
      if (userLang.includes('fr')) {
        googleTranslateCombo.value = 'fr';
        document.getElementById('langToggle').textContent = 'FRE';
      } else {
        googleTranslateCombo.value = 'en';
        document.getElementById('langToggle').textContent = 'ENG';
      }
      googleTranslateCombo.dispatchEvent(new Event('change'));
    }
  }
  
  window.onload = function () {
    setTimeout(setInitialLanguage, 1000); // Wait for Google Translate to load
  };
  