Source: https://core.telegram.org/bots/api#inlinequeryresultcachedsticker
Snapshot: 2026-09-22T08:35:37Z

#### InlineQueryResultCachedSticker

Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the sticker.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *sticker* |
| id | String | Unique identifier for this result, 1-64 bytes |
| sticker_file_id | String | A valid file identifier of the sticker |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input_message_content | [InputMessageContent](https://core.telegram.org/bots/api#inputmessagecontent) | *Optional*. Content of the message to be sent instead of the sticker |