Source: https://core.telegram.org/bots/api#passportdata
Snapshot: 2026-11-25T13:00:03Z

#### PassportData

Describes Telegram Passport data shared with the bot by the user.

| Field | Type | Description |
| --- | --- | --- |
| data | Array of [EncryptedPassportElement](https://core.telegram.org/bots/api#encryptedpassportelement) | Array with information shared with the bot about documents and other Telegram Passport elements |
| credentials | [EncryptedCredentials](https://core.telegram.org/bots/api#encryptedcredentials) | Encrypted credentials required to decrypt the data |