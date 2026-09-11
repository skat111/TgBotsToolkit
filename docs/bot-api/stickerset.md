Source: https://core.telegram.org/bots/api#stickerset
Snapshot: 2026-09-11T06:04:42Z

#### StickerSet

This object represents a sticker set.

| Field | Type | Description |
| --- | --- | --- |
| name | String | Sticker set name |
| title | String | Sticker set title |
| sticker_type | String | Type of stickers in the set, currently one of “regular”, “mask”, “custom_emoji” |
| stickers | Array of [Sticker](https://core.telegram.org/bots/api#sticker) | List of all set stickers |
| thumbnail | [PhotoSize](https://core.telegram.org/bots/api#photosize) | *Optional*. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format |