Source: https://core.telegram.org/bots/api#passportelementerrortranslationfile
Snapshot: 2026-09-25T08:52:18Z

#### PassportElementErrorTranslationFile

Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Error source, must be *translation_file* |
| type | String | Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration” |
| file_hash | String | Base64-encoded file hash |
| message | String | Error message |