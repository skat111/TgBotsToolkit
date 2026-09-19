Source: https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif
Snapshot: 2026-09-19T08:05:57Z

#### InlineQueryResultMpeg4Gif

Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the animation.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *mpeg4_gif* |
| id | String | Unique identifier for this result, 1-64 bytes |
| mpeg4_url | String | A valid URL for the MPEG4 file |
| mpeg4_width | Integer | *Optional*. Video width |
| mpeg4_height | Integer | *Optional*. Video height |
| mpeg4_duration | Integer | *Optional*. Video duration in seconds |
| thumbnail_url | String | URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result |
| thumbnail_mime_type | String | *Optional*. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”. |
| title | String | *Optional*. Title for the result |
| caption | String | *Optional*. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing |
| parse_mode | String | *Optional*. Mode for parsing entities in the caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| caption_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode* |
| show_caption_above_media | Boolean | *Optional*. Pass *True* if the caption must be shown above the message media |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input_message_content | [InputMessageContent](https://core.telegram.org/bots/api#inputmessagecontent) | *Optional*. Content of the message to be sent instead of the video animation |