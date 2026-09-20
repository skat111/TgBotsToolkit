Source: https://core.telegram.org/bots/api#audio
Snapshot: 2026-09-20T08:38:20Z

#### Audio

This object represents an audio file to be treated as music by the Telegram clients.

| Field | Type | Description |
| --- | --- | --- |
| file_id | String | Identifier for this file, which can be used to download or reuse the file |
| file_unique_id | String | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. |
| duration | Integer | Duration of the audio in seconds as defined by the sender |
| performer | String | *Optional*. Performer of the audio as defined by the sender or by audio tags |
| title | String | *Optional*. Title of the audio as defined by the sender or by audio tags |
| file_name | String | *Optional*. Original filename as defined by the sender |
| mime_type | String | *Optional*. MIME type of the file as defined by the sender |
| file_size | Integer | *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. |
| thumbnail | [PhotoSize](https://core.telegram.org/bots/api#photosize) | *Optional*. Thumbnail of the album cover to which the music file belongs |