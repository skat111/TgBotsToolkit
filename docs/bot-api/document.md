Source: https://core.telegram.org/bots/api#document
Snapshot: 2026-09-16T08:38:32Z

#### Document

This object represents a general file (as opposed to [photos](https://core.telegram.org/bots/api#photosize), [voice messages](https://core.telegram.org/bots/api#voice) and [audio files](https://core.telegram.org/bots/api#audio)).

| Field | Type | Description |
| --- | --- | --- |
| file_id | String | Identifier for this file, which can be used to download or reuse the file |
| file_unique_id | String | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. |
| thumbnail | [PhotoSize](https://core.telegram.org/bots/api#photosize) | *Optional*. Document thumbnail as defined by the sender |
| file_name | String | *Optional*. Original filename as defined by the sender |
| mime_type | String | *Optional*. MIME type of the file as defined by the sender |
| file_size | Integer | *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. |