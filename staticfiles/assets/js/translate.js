document.addEventListener('DOMContentLoaded', function() {
    const langToggle = document.getElementById('langToggle');
    let currentLang = 'en';

    // Function to initialize Google Translate
    function googleTranslateElementInit() {
        new google.translate.TranslateElement({
            pageLanguage: 'en',
            includedLanguages: 'en,fr',
            layout: google.translate.TranslateElement.InlineLayout.SIMPLE
        }, 'google_translate_element');
    }

    // Load Google Translate script
    const googleTranslateScript = document.createElement('script');
    googleTranslateScript.type = 'text/javascript';
    googleTranslateScript.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
    document.head.appendChild(googleTranslateScript);

    // Event listener for language toggle button
    langToggle.addEventListener('click', function() {
        if (currentLang === 'en') {
            currentLang = 'fr';
            langToggle.textContent = 'FRE';
            changeLanguage('fr');
        } else {
            currentLang = 'en';
            langToggle.textContent = 'ENG';
            changeLanguage('en');
        }
    });

    // Function to change language using Google Translate
    function changeLanguage(lang) {
        const select = document.querySelector('.goog-te-combo');
        if (select) {
            select.value = lang;
            select.dispatchEvent(new Event('change'));
        }
    }
});
document.addEventListener('DOMContentLoaded', function() {
    const langToggle = document.getElementById('langToggle');
    let currentLang = 'en';

    // Function to initialize Google Translate
    function googleTranslateElementInit() {
        new google.translate.TranslateElement({
            pageLanguage: 'en',
            includedLanguages: 'en,fr',
            layout: google.translate.TranslateElement.InlineLayout.SIMPLE
        }, 'google_translate_element');
    }

    // Load Google Translate script
    const googleTranslateScript = document.createElement('script');
    googleTranslateScript.type = 'text/javascript';
    googleTranslateScript.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
    document.head.appendChild(googleTranslateScript);

    // Event listener for language toggle button
    langToggle.addEventListener('click', function() {
        if (currentLang === 'en') {
            currentLang = 'fr';
            langToggle.textContent = 'FRE';
            changeLanguage('fr');
        } else {
            currentLang = 'en';
            langToggle.textContent = 'ENG';
            changeLanguage('en');
        }
    });

    // Function to change language using Google Translate
    function changeLanguage(lang) {
        const select = document.querySelector('.goog-te-combo');
        if (select) {
            select.value = lang;
            select.dispatchEvent(new Event('change'));
        }
    }
});
document.addEventListener('DOMContentLoaded', function() {
    const langToggle = document.getElementById('langToggle');
    let currentLang = 'en';

    // Function to initialize Google Translate
    function googleTranslateElementInit() {
        new google.translate.TranslateElement({
            pageLanguage: 'en',
            includedLanguages: 'en,fr',
            layout: google.translate.TranslateElement.InlineLayout.SIMPLE
        }, 'google_translate_element');
    }

    // Load Google Translate script
    const googleTranslateScript = document.createElement('script');
    googleTranslateScript.type = 'text/javascript';
    googleTranslateScript.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
    document.head.appendChild(googleTranslateScript);

    // Event listener for language toggle button
    langToggle.addEventListener('click', function() {
        if (currentLang === 'en') {
            currentLang = 'fr';
            langToggle.textContent = 'FRE';
            changeLanguage('fr');
        } else {
            currentLang = 'en';
            langToggle.textContent = 'ENG';
            changeLanguage('en');
        }
    });

    // Function to change language using Google Translate
    function changeLanguage(lang) {
        const select = document.querySelector('.goog-te-combo');
        if (select) {
            select.value = lang;
            select.dispatchEvent(new Event('change'));
        }
    }
});
