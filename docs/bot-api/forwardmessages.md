Source: https://core.telegram.org/bots/api#forwardmessages
Snapshot: 2026-09-22T08:35:37Z

#### forwardMessages

Use this method to forward multiple messages of any kind. If some of the specified messages can't be found or forwarded, they are skipped. Service messages and messages with protected content can't be forwarded. Album grouping is kept for forwarded messages. On success, an Array of [MessageId](https://core.telegram.org/bots/api#messageid) of the sent messages is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username` |
| message_thread_id | Integer | Optional | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only |
| direct_messages_topic_id | Integer | Optional | Identifier of the direct messages topic to which the messages will be forwarded; required if the messages are forwarded to a direct messages chat |
| from_chat_id | Integer or String | Yes | Unique identifier for the chat where the original messages were sent (or username of the target bot, supergroup or channel in the format `@username`) |
| message_ids | Array of Integer | Yes | A JSON-serialized list of 1-100 identifiers of messages in the chat *from_chat_id* to forward. The identifiers must be specified in a strictly increasing order. |
| disable_notification | Boolean | Optional | Sends the messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |
| protect_content | Boolean | Optional | Protects the contents of the forwarded messages from forwarding and saving |