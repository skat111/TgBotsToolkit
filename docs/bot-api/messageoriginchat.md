Source: https://core.telegram.org/bots/api#messageoriginchat
Snapshot: 2026-09-16T08:38:32Z

#### MessageOriginChat

The message was originally sent on behalf of a chat to a group chat.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the message origin, always “chat” |
| date | Integer | Date the message was sent originally in Unix time |
| sender_chat | [Chat](https://core.telegram.org/bots/api#chat) | Chat that sent the message originally |
| author_signature | String | *Optional*. For messages originally sent by an anonymous chat administrator, original message author signature |