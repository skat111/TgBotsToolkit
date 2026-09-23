Source: https://core.telegram.org/bots/api#messageoriginchannel
Snapshot: 2026-09-23T08:37:58Z

#### MessageOriginChannel

The message was originally sent to a channel chat.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the message origin, always “channel” |
| date | Integer | Date the message was sent originally in Unix time |
| chat | [Chat](https://core.telegram.org/bots/api#chat) | Channel chat to which the message was originally sent |
| message_id | Integer | Unique message identifier inside the chat |
| author_signature | String | *Optional*. Signature of the original post author |