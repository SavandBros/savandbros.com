# i18n

Each folder contains an `index.json` with keys as translation keys and value as translated value.

Always make sure that `dir` value is the last item and for RTL languages it should be set to "rtl" otherwise "ltr".

For organizing purposes follow this order:

- Keys as words with `_` instead of spaces (`{ "hello_world': "Hello World" }`).
- Keys as constants with dict values (`foo: { "bar": "Bar of Bar" }`).
- Keys as constants (`{ "title": "Savand Bros" }`).
