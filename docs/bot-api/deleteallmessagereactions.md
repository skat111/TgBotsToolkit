Source: https://core.telegram.org/bots/api#deleteallmessagereactions
Snapshot: 2026-09-12T07:57:24Z

#### deleteAllMessageReactions

Use this method to remove up to 10000 recent reactions in a group or a supergroup chat added by a given user or chat. The bot must have the 'can_delete_messages' administrator right in the chat. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| user_id | Integer | Optional | Identifier of the user whose reactions will be removed, if the reactions were added by a user |
| actor_chat_id | Integer | Optional | Identifier of the chat whose reactions will be removed, if the reactions were added by a chat |