Source: https://core.telegram.org/bots/api#getgamehighscores
Snapshot: 2026-09-23T08:37:58Z

#### getGameHighScores

Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. Returns an Array of [GameHighScore](https://core.telegram.org/bots/api#gamehighscore) objects.

> This method will currently return scores for the target user, plus two of their closest neighbors on each side. Will also return the top three users if the user and their neighbors are not among them. Please note that this behavior is subject to change.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | Integer | Yes | Target user id |
| chat_id | Integer | Optional | Required if *inline_message_id* is not specified. Unique identifier for the target chat. |
| message_id | Integer | Optional | Required if *inline_message_id* is not specified. Identifier of the sent message. |
| inline_message_id | String | Optional | Required if *chat_id* and *message_id* are not specified. Identifier of the inline message. |