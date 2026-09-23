Source: https://core.telegram.org/bots/api#passportelementerrorunspecified
Snapshot: 2026-09-23T08:37:58Z

#### PassportElementErrorUnspecified

Represents an issue in an unspecified place. The error is considered resolved when new data is added.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Error source, must be *unspecified* |
| type | String | Type of element of the user's Telegram Passport which has the issue |
| element_hash | String | Base64-encoded element hash |
| message | String | Error message |