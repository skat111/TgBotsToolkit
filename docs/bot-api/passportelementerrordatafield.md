Source: https://core.telegram.org/bots/api#passportelementerrordatafield
Snapshot: 2026-09-25T08:52:18Z

#### PassportElementErrorDataField

Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Error source, must be *data* |
| type | String | The section of the user's Telegram Passport which has the error, one of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address” |
| field_name | String | Name of the data field which has the error |
| data_hash | String | Base64-encoded data hash |
| message | String | Error message |