Source: https://core.telegram.org/bots/api#replyparameters
Snapshot: 2026-09-13T08:21:39Z

#### ReplyParameters

Describes reply parameters for the message that is being sent.

| Field | Type | Description |
| --- | --- | --- |
| message_id | Integer | *Optional*. Identifier of the message that will be replied to in the current chat, or in the chat *chat_id* if it is specified. Required if *ephemeral_message_id* isn't specified. |
| chat_id | Integer or String | *Optional*. If the message to be replied to is from a different chat, unique identifier for the chat or username of the bot, supergroup or channel in the format `@username`. Not supported for messages sent on behalf of a business account, messages from channel direct messages chats and ephemeral messages. |
| ephemeral_message_id | Integer | *Optional*. Identifier of the incoming ephemeral message that will be replied to in the current chat. A reply to an ephemeral message must itself be an ephemeral message. An ephemeral message may only be replied to within 15 seconds of being sent. Required if *message_id* isn't specified. |
| allow_sending_without_reply | Boolean | *Optional*. Pass *True* if the message should be sent even if the specified message to be replied to is not found. Always *False* for replies in another chat or forum topic, and sent ephemeral messages. Always *True* for messages sent on behalf of a business account. |
| quote | String | *Optional*. Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, *custom_emoji*, and *date_time* entities. The message will fail to send if the quote isn't found in the original message. Ignored for ephemeral messages. |
| quote_parse_mode | String | *Optional*. Mode for parsing entities in the quote. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| quote_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. A JSON-serialized list of special entities that appear in the quote. It can be specified instead of *quote_parse_mode*. |
| quote_position | Integer | *Optional*. Position of the quote in the original message in UTF-16 code units |
| checklist_task_id | Integer | *Optional*. Identifier of the specific checklist task to be replied to |
| poll_option_id | String | *Optional*. Persistent identifier of the specific poll option to be replied to |