Source: https://core.telegram.org/bots/api#setstickermaskposition
Snapshot: 2026-09-11T06:04:42Z

#### setStickerMaskPosition

Use this method to change the [mask position](https://core.telegram.org/bots/api#maskposition) of a mask sticker. The sticker must belong to a sticker set that was created by the bot. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sticker | String | Yes | File identifier of the sticker |
| mask_position | [MaskPosition](https://core.telegram.org/bots/api#maskposition) | Optional | A JSON-serialized object with the position where the mask should be placed on faces. Omit the parameter to remove the mask position. |