#!/usr/bin/env node

/**
 * SyncTrans
 *
 * Will sync all the translation files from the source (English).
 *
 * In simple words, when source language has new strings/ids to be translated, it will add those to translation files
 * so they don't become outdated.
 *
 * When the source translation contains:
 *
 * en.json
 * ```json
 * [
 *   {
 *     "id": "savand_bros",
 *     "translation": "Savand Bros"
 *   },
 *   {
 *     "id": "create_website",
 *     "translation": "Create a Website"
 *   },
 *   {
 *     "id": "start_blog",
 *     "translation": "Start a Blog"
 *   },
 * ]
 * ```
 *
 * While target translation contains:
 *
 * fa.json
 * ```json
 * [
 *   {
 *     "id": "savand_bros",
 *     "translation": "ساوند بروز"
 *   },
 *   {
 *    "id": "create_website",
 *    "translation": "ساخت یک وبسایت"
 *   }
 * ]
 * ```
 *
 * It wil turn the `fa.json` translation file into:
 *
 * fa.json
 * ```json
 * [
 *   {
 *     "id": "savand_bros",
 *     "translation": "ساوند بروز"
 *   },
 *   {
 *    "id": "create_website",
 *    "translation": "ساخت یک وبسایت"
 *   },
 *   {
 *     "id": "start_blog",
 *     "translation": "Start a Blog"
 *   }
 * ]
 * ```
 */
const fs = require('fs');
const SOURCE_LOCALE = 'en';
const targetlocales = ['fa', 'ru'];

/**
 * flattenTrans
 *
 * Turn the given list of translation in format of [{id: "transId", translation: "Trnslation text"}, ...]
 * inot a flatten array that is easy to look up, like: {transId: "Trnslation text", ...}.
 *
 * @param {Array.<Object.<String, String>>} translationData
 * @returns {Object.<String, String>}
 */
function flattenTrans(translationData) {
  let flattenTranslation = {};

  for (let key in translationData) {
    if (!translationData.hasOwnProperty(key)) {
      continue;
    }

    let tranlation = translationData[key];
    flattenTranslation[tranlation.id] = tranlation.translation;
  }

  return flattenTranslation;
}

/**
 * flatten2ListTrans
 *
 * Turn a flatten list of translation from {transId: "Trnslation text", ...}
 * into [{id: "transId", translation: "Trnslation text"}, ...]
 *
 * to be compatible with Hugo i18n formaat.
 *
 * @param {Object.<String, String>}  flattenTrans 
 * @returns {Array.<Object.<String, String>>}
 */
function flatten2ListTrans(flattenTrans) {
  let listTrans = [];

  for (let key in flattenTrans) {
    if (!flattenTrans.hasOwnProperty(key)) {
      continue;
    }

    listTrans.push({ id: key, translation: flattenTrans[key] });
  }

  return listTrans;
}

fs.readFile(`i18n/${SOURCE_LOCALE}.json`, 'utf8', function (err, data) {
  if (err) {
    throw err;
  }

  const sourceTrans = JSON.parse(data);
  const flattenSourceTrans = flattenTrans(sourceTrans);


  targetlocales.forEach(function (targetLocale) {
    let targetTransFileName = `i18n/${targetLocale}.json`;

    fs.readFile(targetTransFileName, 'utf8', function (err, data) {
      if (err) {
        throw err;
      }

      let targetTrans = JSON.parse(data);
      let flattemTargetTrans = flattenTrans(targetTrans);


      for (let key in flattenSourceTrans) {
        if (!flattenSourceTrans.hasOwnProperty(key)) {
          continue;
        }

        if (!flattemTargetTrans.hasOwnProperty(key)) {
          flattemTargetTrans[key] = flattenSourceTrans[key]
        }
      }

      fs.writeFile(targetTransFileName, JSON.stringify(flatten2ListTrans(flattemTargetTrans), null, 2) + '\n', function (err) {
        if (err) {
          throw err;
        }

        console.log(`Synced Locale ${targetLocale}!`);
      });
    });
  });
});
