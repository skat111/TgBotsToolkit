Source: https://core.telegram.org/bots/api#inputrichmessage
Snapshot: 2026-09-12T07:57:24Z

#### InputRichMessage

Describes a rich message to be sent. Exactly **one** of the fields *html*, *markdown*, or *blocks* must be used.

| Field | Type | Description |
| --- | --- | --- |
| blocks | Array of [InputRichBlock](https://core.telegram.org/bots/api#inputrichblock) | *Optional*. Content of the rich message to send described as a list of blocks |
| html | String | *Optional*. Content of the rich message to send described using HTML formatting. See [rich message formatting options](https://core.telegram.org/bots/api#rich-message-formatting-options) for more details. Use *media* field to specify the media used in the message. |
| markdown | String | *Optional*. Content of the rich message to send described using Markdown formatting. See [rich message formatting options](https://core.telegram.org/bots/api#rich-message-formatting-options) for more details. Use *media* field to specify the media used in the message. |
| media | Array of [InputRichMessageMedia](https://core.telegram.org/bots/api#inputrichmessagemedia) | *Optional*. List of media that are specified in the *markdown* or *html* fields using `tg://photo?id=`, `tg://video?id=`, `tg://document?id=`, and `tg://audio?id=` links |
| is_rtl | Boolean | *Optional*. Pass *True* if the rich message must be shown right-to-left |
| skip_entity_detection | Boolean | *Optional*. Pass *True* to skip automatic detection of entities (e.g., URLs, email addresses, username mentions, hashtags, cashtags, bot commands, or phone numbers) in the text |