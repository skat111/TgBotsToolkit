Source: https://core.telegram.org/bots/api#setstickeremojilist
Snapshot: 2026-09-25T08:52:18Z

#### setStickerEmojiList

Use this method to change the list of emoji assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sticker | String | Yes | File identifier of the sticker |
| emoji_list | Array of String | Yes | A JSON-serialized list of 1-20 emoji associated with the sticker |