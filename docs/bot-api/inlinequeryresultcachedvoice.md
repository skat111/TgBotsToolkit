Source: https://core.telegram.org/bots/api#inlinequeryresultcachedvoice
Snapshot: 2026-09-22T08:35:37Z

#### InlineQueryResultCachedVoice

Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the voice message.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *voice* |
| id | String | Unique identifier for this result, 1-64 bytes |
| voice_file_id | String | A valid file identifier for the voice message |
| title | String | Voice message title |
| caption | String | *Optional*. Caption, 0-1024 characters after entities parsing |
| parse_mode | String | *Optional*. Mode for parsing entities in the voice message caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| caption_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode* |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input_message_content | [InputMessageContent](https://core.telegram.org/bots/api#inputmessagecontent) | *Optional*. Content of the message to be sent instead of the voice message |