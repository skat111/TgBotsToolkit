Source: https://core.telegram.org/bots/api#messagegenerationstopped
Snapshot: 2026-09-14T08:59:05Z

#### MessageGenerationStopped

This object describes an update about a user stopping message generation.

| Field | Type | Description |
| --- | --- | --- |
| chat | [Chat](https://core.telegram.org/bots/api#chat) | Chat in which the message is generated |
| message_thread_id | Integer | *Optional*. Unique identifier of the message thread in which the message is generated |
| draft_id | Integer | Unique identifier of the message draft which was stopped |