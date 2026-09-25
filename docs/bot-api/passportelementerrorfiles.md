Source: https://core.telegram.org/bots/api#passportelementerrorfiles
Snapshot: 2026-09-25T08:52:18Z

#### PassportElementErrorFiles

Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Error source, must be *files* |
| type | String | The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration” |
| file_hashes | Array of String | List of base64-encoded file hashes |
| message | String | Error message |