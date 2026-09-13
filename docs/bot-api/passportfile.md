Source: https://core.telegram.org/bots/api#passportfile
Snapshot: 2026-09-13T08:21:39Z

#### PassportFile

This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.

| Field | Type | Description |
| --- | --- | --- |
| file_id | String | Identifier for this file, which can be used to download or reuse the file |
| file_unique_id | String | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. |
| file_size | Integer | File size in bytes |
| file_date | Integer | Unix time when the file was uploaded |