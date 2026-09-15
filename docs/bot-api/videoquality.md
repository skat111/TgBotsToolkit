Source: https://core.telegram.org/bots/api#videoquality
Snapshot: 2026-09-15T08:44:15Z

#### VideoQuality

This object represents a video file of a specific quality.

| Field | Type | Description |
| --- | --- | --- |
| file_id | String | Identifier for this file, which can be used to download or reuse the file |
| file_unique_id | String | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. |
| width | Integer | Video width |
| height | Integer | Video height |
| codec | String | Codec that was used to encode the video, for example, “h264”, “h265”, or “av01” |
| file_size | Integer | *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. |