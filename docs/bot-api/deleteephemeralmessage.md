Source: https://core.telegram.org/bots/api#deleteephemeralmessage
Snapshot: 2026-09-12T07:57:24Z

#### deleteEphemeralMessage

Use this method to delete an ephemeral message. Note that it is not guaranteed that the user will receive the message deletion event, especially if they are offline. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| receiver_user_id | Integer | Yes | Identifier of the user who received the message |
| ephemeral_message_id | Integer | Yes | Identifier of the ephemeral message to delete |