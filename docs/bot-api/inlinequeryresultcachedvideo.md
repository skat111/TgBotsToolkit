Source: https://core.telegram.org/bots/api#inlinequeryresultcachedvideo
Snapshot: 2026-09-23T08:37:58Z

#### InlineQueryResultCachedVideo

Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the video.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *video* |
| id | String | Unique identifier for this result, 1-64 bytes |
| video_file_id | String | A valid file identifier for the video file |
| title | String | Title for the result |
| description | String | *Optional*. Short description of the result |
| caption | String | *Optional*. Caption of the video to be sent, 0-1024 characters after entities parsing |
| parse_mode | String | *Optional*. Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| caption_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode* |
| show_caption_above_media | Boolean | *Optional*. Pass *True* if the caption must be shown above the message media |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input_message_content | [InputMessageContent](https://core.telegram.org/bots/api#inputmessagecontent) | *Optional*. Content of the message to be sent instead of the video |