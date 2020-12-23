/**
 * Create language options for language switcher select.
 * On select, change URL to that language.
 */
function setupLanguageSwitcher() {
  const currentLanguage = document.documentElement.getAttribute('lang');
  const select = document.getElementById('language');

  select.addEventListener("change", (event) => {
    const value = event.target.value;
    if (value === "en") {
      location.href = "/";
    } else {
      location.href = "/" + event.target.value;
    }
  });

  const addLanguage = function (value, label) {
    const option = document.createElement("option");
    option.appendChild(document.createTextNode(label));
    option.value = value;
    if (value === currentLanguage) {
      option.selected = true;
    }
    select.appendChild(option);
  };

  addLanguage("en", "English");
  addLanguage("ru", "Русский");
  addLanguage("fa", "فارسی");
}

setupLanguageSwitcher();
