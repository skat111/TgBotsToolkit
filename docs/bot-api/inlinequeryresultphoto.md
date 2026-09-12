Source: https://core.telegram.org/bots/api#inlinequeryresultphoto
Snapshot: 2026-09-12T07:57:24Z

#### InlineQueryResultPhoto

Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the photo.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *photo* |
| id | String | Unique identifier for this result, 1-64 bytes |
| photo_url | String | A valid URL of the photo. Photo must be in **JPEG** format. Photo size must not exceed 5MB. |
| thumbnail_url | String | URL of the thumbnail for the photo |
| photo_width | Integer | *Optional*. Width of the photo |
| photo_height | Integer | *Optional*. Height of the photo |
| title | String | *Optional*. Title for the result |
| description | String | *Optional*. Short description of the result |
| caption | String | *Optional*. Caption of the photo to be sent, 0-1024 characters after entities parsing |
| parse_mode | String | *Optional*. Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| caption_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode* |
| show_caption_above_media | Boolean | *Optional*. Pass *True* if the caption must be shown above the message media |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input_message_content | [InputMessageContent](https://core.telegram.org/bots/api#inputmessagecontent) | *Optional*. Content of the message to be sent instead of the photo |