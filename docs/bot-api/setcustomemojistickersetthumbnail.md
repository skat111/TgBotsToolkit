Source: https://core.telegram.org/bots/api#setcustomemojistickersetthumbnail
Snapshot: 2026-09-17T08:42:18Z

#### setCustomEmojiStickerSetThumbnail

Use this method to set the thumbnail of a custom emoji sticker set. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| name | String | Yes | Sticker set name |
| custom_emoji_id | String | Optional | Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail |