Source: https://core.telegram.org/bots/api#unpinchatmessage
Snapshot: 2026-09-24T08:30:39Z

#### unpinChatMessage

Use this method to remove a message from the list of pinned messages in a chat. In private chats and channel direct messages chats, all messages can be unpinned. Conversely, the bot must be an administrator with the 'can_pin_messages' right or the 'can_edit_messages' right to unpin messages in groups and channels respectively. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Optional | Unique identifier of the business connection on behalf of which the message will be unpinned |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target channel in the format `@username` |
| message_id | Integer | Optional | Identifier of the message to unpin. Required if *business_connection_id* is specified. If not specified, the most recent pinned message (by sending date) will be unpinned. |