Source: https://core.telegram.org/bots/api#chatshared
Snapshot: 2026-09-13T08:21:39Z

#### ChatShared

This object contains information about a chat that was shared with the bot using a [KeyboardButtonRequestChat](https://core.telegram.org/bots/api#keyboardbuttonrequestchat) button.

| Field | Type | Description |
| --- | --- | --- |
| request_id | Integer | Identifier of the request |
| chat_id | Integer | Identifier of the shared chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot may not have access to the chat and could be unable to use this identifier, unless the chat is already known to the bot by some other means. |
| title | String | *Optional*. Title of the chat, if the title was requested by the bot |
| username | String | *Optional*. Username of the chat, if the username was requested by the bot and available |
| photo | Array of [PhotoSize](https://core.telegram.org/bots/api#photosize) | *Optional*. Available sizes of the chat photo, if the photo was requested by the bot |