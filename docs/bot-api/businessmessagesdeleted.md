Source: https://core.telegram.org/bots/api#businessmessagesdeleted
Snapshot: 2026-09-19T08:05:57Z

#### BusinessMessagesDeleted

This object is received when messages are deleted from a connected business account.

| Field | Type | Description |
| --- | --- | --- |
| business_connection_id | String | Unique identifier of the business connection |
| chat | [Chat](https://core.telegram.org/bots/api#chat) | Information about a chat in the business account. The bot may not have access to the chat or the corresponding user. |
| message_ids | Array of Integer | The list of identifiers of deleted messages in the chat of the business account |