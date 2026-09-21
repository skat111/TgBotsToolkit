Source: https://core.telegram.org/bots/api#passportelementerrortranslationfiles
Snapshot: 2026-09-21T09:00:24Z

#### PassportElementErrorTranslationFiles

Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Error source, must be *translation_files* |
| type | String | Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration” |
| file_hashes | Array of String | List of base64-encoded file hashes |
| message | String | Error message |