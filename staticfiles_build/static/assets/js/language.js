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

    function changeLanguage(lang) {
        var iframe = document.getElementsByClassName('goog-te-banner-frame')[0];
        if (!iframe) return;

        var innerDoc = iframe.contentDocument || iframe.contentWindow.document;
        var selectField = innerDoc.getElementsByTagName('select')[0];
        
        if (selectField) {
            for(var i=0; i<selectField.options.length; i++) {
                if(selectField.options[i].value === lang) {
                    selectField.selectedIndex = i;
                    selectField.dispatchEvent(new Event('change'));
                    break;
                }
            }
        }
    }
});