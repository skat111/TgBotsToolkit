Source: https://core.telegram.org/bots/api#chatsharethemeemoji
Snapshot: 2026-11-12T11:19:03Z

#### ChatShareThemeEmoji

The theme with emoji placed on a background.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the theme, always “emoji” |
| emojis | Array of [EmojiType](https://core.telegram.org/bots/api#emojitype) | The emoji; 0-6 regular or custom emoji |
| background_backdrop_id | Integer | *Optional*. Identifier of the backdrop used as the background; omitted if the default background is used. Use [getChatShareThemeBackdrops](https://core.telegram.org/bots/api#getchatsharethemebackdrops) to get details about the backdrop. |