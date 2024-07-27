function googleTranslateElementInit() {
    new google.translate.TranslateElement({
        pageLanguage: 'en',
        includedLanguages: 'en,fr',
        layout: google.translate.TranslateElement.InlineLayout.SIMPLE
    }, 'google_translate_element');
}

document.addEventListener('DOMContentLoaded', function() {
    const langToggle = document.getElementById('langToggle');
    let currentLang = 'en';

    langToggle.addEventListener('click', function() {
        currentLang = (currentLang === 'en') ? 'fr' : 'en';
        langToggle.textContent = (currentLang === 'en') ? 'ENG' : 'FRE';
        changeLanguage(currentLang);
    });

    function changeLanguage(lang) {
        const translateSelect = document.querySelector('.goog-te-combo');
        if (translateSelect) {
            translateSelect.value = lang;
            translateSelect.dispatchEvent(new Event('change'));
        } else {
            console.error("Translation select box not found.");
        }
    }
});
