Source: https://core.telegram.org/bots/api#inputsharedwidgetmessagecontent
Snapshot: 2026-11-10T11:16:42Z

#### InputSharedWidgetMessageContent

Represents the [content](https://core.telegram.org/bots/api#inputmessagecontent) of a message with a shared widget to be sent as the result of an inline query. Currently, widgets can't be sent in response to inline queries in the production environment.

| Field | Type | Description |
| --- | --- | --- |
| widget_id | String | Unique identifier of the shared widget created by the bot |
| chat_data | String | *Optional*. Data of the widget, which is specific to the message, 0-1024 bytes |
| caption | String | *Optional*. Widget caption, 0-1024 characters after entities parsing |
| parse_mode | String | *Optional*. Mode for parsing entities in the widget caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| caption_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode* |
| show_caption_above_media | Boolean | *Optional*. Pass *True* if the caption must be shown above the widget |