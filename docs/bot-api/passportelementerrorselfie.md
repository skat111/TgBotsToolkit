Source: https://core.telegram.org/bots/api#passportelementerrorselfie
Snapshot: 2026-09-22T08:35:37Z

#### PassportElementErrorSelfie

Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Error source, must be *selfie* |
| type | String | The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport” |
| file_hash | String | Base64-encoded hash of the file with the selfie |
| message | String | Error message |