Source: https://core.telegram.org/bots/api#getchatmember
Snapshot: 2026-09-24T08:30:39Z

#### getChatMember

Use this method to get information about a member of a chat. The method is only guaranteed to work for other users if the bot is an administrator in the chat. Returns a [ChatMember](https://core.telegram.org/bots/api#chatmember) object on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup or channel in the format `@username` |
| user_id | Integer | Yes | Unique identifier of the target user |