Source: https://core.telegram.org/bots/api#inputtextmessagecontent
Snapshot: 2026-09-24T08:30:39Z

#### InputTextMessageContent

Represents the [content](https://core.telegram.org/bots/api#inputmessagecontent) of a text message to be sent as the result of an inline query.

| Field | Type | Description |
| --- | --- | --- |
| message_text | String | Text of the message to be sent, 1-4096 characters |
| parse_mode | String | *Optional*. Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. List of special entities that appear in message text, which can be specified instead of *parse_mode* |
| link_preview_options | [LinkPreviewOptions](https://core.telegram.org/bots/api#linkpreviewoptions) | *Optional*. Link preview generation options for the message |