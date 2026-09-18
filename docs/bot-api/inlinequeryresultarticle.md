Source: https://core.telegram.org/bots/api#inlinequeryresultarticle
Snapshot: 2026-09-18T08:17:54Z

#### InlineQueryResultArticle

Represents a link to an article or web page.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *article* |
| id | String | Unique identifier for this result, 1-64 Bytes |
| title | String | Title of the result |
| input_message_content | [InputMessageContent](https://core.telegram.org/bots/api#inputmessagecontent) | Content of the message to be sent |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| url | String | *Optional*. URL of the result |
| description | String | *Optional*. Short description of the result |
| thumbnail_url | String | *Optional*. Url of the thumbnail for the result |
| thumbnail_width | Integer | *Optional*. Thumbnail width |
| thumbnail_height | Integer | *Optional*. Thumbnail height |