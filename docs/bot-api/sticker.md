Source: https://core.telegram.org/bots/api#sticker
Snapshot: 2026-09-23T08:37:58Z

#### Sticker

This object represents a sticker.

| Field | Type | Description |
| --- | --- | --- |
| file_id | String | Identifier for this file, which can be used to download or reuse the file |
| file_unique_id | String | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. |
| type | String | Type of the sticker, currently one of “regular”, “mask”, “custom_emoji”. The type of the sticker is independent from its format, which is determined by the fields *is_animated* and *is_video*. |
| width | Integer | Sticker width |
| height | Integer | Sticker height |
| is_animated | Boolean | *True*, if the sticker is [animated](https://telegram.org/blog/animated-stickers) |
| is_video | Boolean | *True*, if the sticker is a [video sticker](https://telegram.org/blog/video-stickers-better-reactions) |
| thumbnail | [PhotoSize](https://core.telegram.org/bots/api#photosize) | *Optional*. Sticker thumbnail in the .WEBP or .JPG format |
| emoji | String | *Optional*. Emoji associated with the sticker |
| set_name | String | *Optional*. Name of the sticker set to which the sticker belongs |
| premium_animation | [File](https://core.telegram.org/bots/api#file) | *Optional*. For premium regular stickers, premium animation for the sticker |
| mask_position | [MaskPosition](https://core.telegram.org/bots/api#maskposition) | *Optional*. For mask stickers, the position where the mask should be placed |
| custom_emoji_id | String | *Optional*. For custom emoji stickers, unique identifier of the custom emoji |
| needs_repainting | True | *Optional*. *True*, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places |
| file_size | Integer | *Optional*. File size in bytes |