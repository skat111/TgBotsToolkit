Source: https://core.telegram.org/bots/api#inlinequeryresultlocation
Snapshot: 2026-09-22T08:35:37Z

#### InlineQueryResultLocation

Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the location.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *location* |
| id | String | Unique identifier for this result, 1-64 Bytes |
| latitude | Float | Location latitude in degrees |
| longitude | Float | Location longitude in degrees |
| title | String | Location title |
| horizontal_accuracy | Float | *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500 |
| live_period | Integer | *Optional*. Period in seconds during which the location can be updated, must be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely |
| heading | Integer | *Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. |
| proximity_alert_radius | Integer | *Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input_message_content | [InputMessageContent](https://core.telegram.org/bots/api#inputmessagecontent) | *Optional*. Content of the message to be sent instead of the location |
| thumbnail_url | String | *Optional*. Url of the thumbnail for the result |
| thumbnail_width | Integer | *Optional*. Thumbnail width |
| thumbnail_height | Integer | *Optional*. Thumbnail height |