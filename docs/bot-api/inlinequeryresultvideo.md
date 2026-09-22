Source: https://core.telegram.org/bots/api#inlinequeryresultvideo
Snapshot: 2026-09-22T08:35:37Z

#### InlineQueryResultVideo

Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the video.

> If an InlineQueryResultVideo message contains an embedded video (e.g., YouTube), you **must** replace its content using *input_message_content*.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *video* |
| id | String | Unique identifier for this result, 1-64 bytes |
| video_url | String | A valid URL for the embedded video player or video file |
| mime_type | String | MIME type of the content of the video URL, “text/html” or “video/mp4” |
| thumbnail_url | String | URL of the thumbnail (JPEG only) for the video |
| title | String | Title for the result |
| caption | String | *Optional*. Caption of the video to be sent, 0-1024 characters after entities parsing |
| parse_mode | String | *Optional*. Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| caption_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode* |
| show_caption_above_media | Boolean | *Optional*. Pass *True* if the caption must be shown above the message media |
| video_width | Integer | *Optional*. Video width |
| video_height | Integer | *Optional*. Video height |
| video_duration | Integer | *Optional*. Video duration in seconds |
| description | String | *Optional*. Short description of the result |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input_message_content | [InputMessageContent](https://core.telegram.org/bots/api#inputmessagecontent) | *Optional*. Content of the message to be sent instead of the video. This field is **required** if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video). |