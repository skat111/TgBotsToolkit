Source: https://core.telegram.org/bots/api#passportdata
Snapshot: 2026-09-17T08:42:18Z

#### PassportData

Describes Telegram Passport data shared with the bot by the user.

| Field | Type | Description |
| --- | --- | --- |
| data | Array of [EncryptedPassportElement](https://core.telegram.org/bots/api#encryptedpassportelement) | Array with information about documents and other Telegram Passport elements that was shared with the bot |
| credentials | [EncryptedCredentials](https://core.telegram.org/bots/api#encryptedcredentials) | Encrypted credentials required to decrypt the data |