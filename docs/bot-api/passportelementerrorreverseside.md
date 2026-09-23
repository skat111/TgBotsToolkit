Source: https://core.telegram.org/bots/api#passportelementerrorreverseside
Snapshot: 2026-09-23T08:37:58Z

#### PassportElementErrorReverseSide

Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Error source, must be *reverse_side* |
| type | String | The section of the user's Telegram Passport which has the issue, one of “driver_license”, “identity_card” |
| file_hash | String | Base64-encoded hash of the file with the reverse side of the document |
| message | String | Error message |