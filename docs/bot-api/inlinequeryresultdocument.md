Source: https://core.telegram.org/bots/api#inlinequeryresultdocument
Snapshot: 2026-09-17T08:42:18Z

#### InlineQueryResultDocument

Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the file. Currently, only **.PDF** and **.ZIP** files can be sent using this method.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *document* |
| id | String | Unique identifier for this result, 1-64 bytes |
| title | String | Title for the result |
| caption | String | *Optional*. Caption of the document to be sent, 0-1024 characters after entities parsing |
| parse_mode | String | *Optional*. Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| caption_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode* |
| document_url | String | A valid URL for the file |
| mime_type | String | MIME type of the content of the file, either “application/pdf” or “application/zip” |
| description | String | *Optional*. Short description of the result |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input_message_content | [InputMessageContent](https://core.telegram.org/bots/api#inputmessagecontent) | *Optional*. Content of the message to be sent instead of the file |
| thumbnail_url | String | *Optional*. URL of the thumbnail (JPEG only) for the file |
| thumbnail_width | Integer | *Optional*. Thumbnail width |
| thumbnail_height | Integer | *Optional*. Thumbnail height |