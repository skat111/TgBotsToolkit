Source: https://core.telegram.org/bots/api#videonote
Snapshot: 2026-09-16T08:38:32Z

#### VideoNote

This object represents a [video message](https://telegram.org/blog/video-messages-and-telescope).

| Field | Type | Description |
| --- | --- | --- |
| file_id | String | Identifier for this file, which can be used to download or reuse the file |
| file_unique_id | String | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. |
| length | Integer | Video width and height (diameter of the video message) as defined by the sender |
| duration | Integer | Duration of the video in seconds as defined by the sender |
| thumbnail | [PhotoSize](https://core.telegram.org/bots/api#photosize) | *Optional*. Video thumbnail |
| file_size | Integer | *Optional*. File size in bytes |