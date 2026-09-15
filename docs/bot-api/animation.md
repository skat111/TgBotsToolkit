Source: https://core.telegram.org/bots/api#animation
Snapshot: 2026-09-15T08:44:15Z

#### Animation

This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

| Field | Type | Description |
| --- | --- | --- |
| file_id | String | Identifier for this file, which can be used to download or reuse the file |
| file_unique_id | String | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. |
| width | Integer | Video width as defined by the sender |
| height | Integer | Video height as defined by the sender |
| duration | Integer | Duration of the video in seconds as defined by the sender |
| thumbnail | [PhotoSize](https://core.telegram.org/bots/api#photosize) | *Optional*. Animation thumbnail as defined by the sender |
| file_name | String | *Optional*. Original animation filename as defined by the sender |
| mime_type | String | *Optional*. MIME type of the file as defined by the sender |
| file_size | Integer | *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. |