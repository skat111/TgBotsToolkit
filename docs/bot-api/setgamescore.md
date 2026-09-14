Source: https://core.telegram.org/bots/api#setgamescore
Snapshot: 2026-09-14T08:59:05Z

#### setGameScore

Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the [Message](https://core.telegram.org/bots/api#message) is returned, otherwise *True* is returned. Returns an error, if the new score is not greater than the user's current score in the chat and *force* is *False*.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | Integer | Yes | User identifier |
| score | Integer | Yes | New score, must be non-negative |
| force | Boolean | Optional | Pass *True* if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters. |
| disable_edit_message | Boolean | Optional | Pass *True* if the game message should not be automatically edited to include the current scoreboard |
| chat_id | Integer | Optional | Required if *inline_message_id* is not specified. Unique identifier for the target chat. |
| message_id | Integer | Optional | Required if *inline_message_id* is not specified. Identifier of the sent message. |
| inline_message_id | String | Optional | Required if *chat_id* and *message_id* are not specified. Identifier of the inline message. |