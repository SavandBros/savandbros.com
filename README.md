# [Savand Bros](https://savandbros.com)

Source code of Savand Bros website.

## Development

Install hugo and type `hugo server -D` for live reload or `hugo` to build to `/public`.

## Translations

All the translation files are located under `i18n/` directory and the source of localizations is `i18n/en.json`.

In case of adding a new text to the content, add the translation to tha that file and once you're done, make sure to run the `sync-trans` command to sync all the translation files.

```bash
> npm run sync-trans
```

It will add any new or missing translations to other translation files.


## License

Savandbros.com website source code is licensed and distributed under GPLv3.
