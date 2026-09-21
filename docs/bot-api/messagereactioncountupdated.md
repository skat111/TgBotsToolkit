Source: https://core.telegram.org/bots/api#messagereactioncountupdated
Snapshot: 2026-09-21T09:00:24Z

#### MessageReactionCountUpdated

This object represents reaction changes on a message with anonymous reactions.

| Field | Type | Description |
| --- | --- | --- |
| chat | [Chat](https://core.telegram.org/bots/api#chat) | The chat containing the message |
| message_id | Integer | Unique message identifier inside the chat |
| date | Integer | Date of the change in Unix time |
| reactions | Array of [ReactionCount](https://core.telegram.org/bots/api#reactioncount) | List of reactions that are present on the message |