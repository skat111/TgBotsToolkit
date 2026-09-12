Source: https://core.telegram.org/bots/api#replacestickerinset
Snapshot: 2026-09-12T07:57:24Z

#### replaceStickerInSet

Use this method to replace an existing sticker in a sticker set with a new one. The method is equivalent to calling [deleteStickerFromSet](https://core.telegram.org/bots/api#deletestickerfromset), then [addStickerToSet](https://core.telegram.org/bots/api#addstickertoset), then [setStickerPositionInSet](https://core.telegram.org/bots/api#setstickerpositioninset). Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | Integer | Yes | User identifier of the sticker set owner |
| name | String | Yes | Sticker set name |
| old_sticker | String | Yes | File identifier of the replaced sticker |
| sticker | [InputSticker](https://core.telegram.org/bots/api#inputsticker) | Yes | A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set remains unchanged. |