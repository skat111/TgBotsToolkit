Source: https://core.telegram.org/bots/api#inaccessiblemessage
Snapshot: 2026-09-19T08:05:57Z

#### InaccessibleMessage

This object describes a message that was deleted or is otherwise inaccessible to the bot.

| Field | Type | Description |
| --- | --- | --- |
| chat | [Chat](https://core.telegram.org/bots/api#chat) | Chat the message belonged to |
| message_id | Integer | Unique message identifier inside the chat |
| date | Integer | Always 0. The field can be used to differentiate regular and inaccessible messages. |