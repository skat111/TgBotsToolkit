Source: https://core.telegram.org/bots/api#deletemessagereaction
Snapshot: 2026-09-23T08:37:58Z

#### deleteMessageReaction

Use this method to remove a reaction from a message in a group or a supergroup chat. The bot must have the 'can_delete_messages' administrator right in the chat. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| message_id | Integer | Yes | Identifier of the target message |
| user_id | Integer | Optional | Identifier of the user whose reaction will be removed, if the reaction was added by a user |
| actor_chat_id | Integer | Optional | Identifier of the chat whose reaction will be removed, if the reaction was added by a chat |