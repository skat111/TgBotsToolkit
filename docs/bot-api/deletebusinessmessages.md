Source: https://core.telegram.org/bots/api#deletebusinessmessages
Snapshot: 2026-09-19T08:05:57Z

#### deleteBusinessMessages

Delete messages on behalf of a business account. Requires the *can_delete_sent_messages* business bot right to delete messages sent by the bot itself, or the *can_delete_all_messages* business bot right to delete any message. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Yes | Unique identifier of the business connection on behalf of which to delete the messages |
| message_ids | Array of Integer | Yes | A JSON-serialized list of 1-100 identifiers of messages to delete. All messages must be from the same chat. See [deleteMessage](https://core.telegram.org/bots/api#deletemessage) for limitations on which messages can be deleted. |