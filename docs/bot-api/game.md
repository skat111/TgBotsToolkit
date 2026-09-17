Source: https://core.telegram.org/bots/api#game
Snapshot: 2026-09-17T08:42:18Z

#### Game

This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

| Field | Type | Description |
| --- | --- | --- |
| title | String | Title of the game |
| description | String | Description of the game |
| photo | Array of [PhotoSize](https://core.telegram.org/bots/api#photosize) | Photo that will be displayed in the game message in chats |
| text | String | *Optional*. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls [setGameScore](https://core.telegram.org/bots/api#setgamescore), or manually edited using [editMessageText](https://core.telegram.org/bots/api#editmessagetext). 0-4096 characters. |
| text_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. Special entities that appear in *text*, such as usernames, URLs, bot commands, etc. |
| animation | [Animation](https://core.telegram.org/bots/api#animation) | *Optional*. Animation that will be displayed in the game message in chats. Upload via [BotFather](https://t.me/botfather). |