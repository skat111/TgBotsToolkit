Source: https://core.telegram.org/bots/api#getcustomemojistickers
Snapshot: 2026-09-22T08:35:37Z

#### getCustomEmojiStickers

Use this method to get information about custom emoji stickers by their identifiers. Returns an Array of [Sticker](https://core.telegram.org/bots/api#sticker) objects.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| custom_emoji_ids | Array of String | Yes | A JSON-serialized list of custom emoji identifiers. At most 200 custom emoji identifiers can be specified. |