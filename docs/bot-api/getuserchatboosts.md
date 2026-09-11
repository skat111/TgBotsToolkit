Source: https://core.telegram.org/bots/api#getuserchatboosts
Snapshot: 2026-09-11T06:04:42Z

#### getUserChatBoosts

Use this method to get the list of boosts added to a chat by a user. Requires administrator rights in the chat. Returns a [UserChatBoosts](https://core.telegram.org/bots/api#userchatboosts) object.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the chat or username of the channel in the format `@username` |
| user_id | Integer | Yes | Unique identifier of the target user |