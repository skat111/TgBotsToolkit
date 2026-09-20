Source: https://core.telegram.org/bots/api#inputpolloption
Snapshot: 2026-09-20T08:38:20Z

#### InputPollOption

This object contains information about one answer option in a poll to be sent.

| Field | Type | Description |
| --- | --- | --- |
| text | String | Option text, 1-100 characters |
| text_parse_mode | String | *Optional*. Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. Currently, only custom emoji entities are allowed. |
| text_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. A JSON-serialized list of special entities that appear in the poll option text. It can be specified instead of *text_parse_mode*. |
| media | [InputPollOptionMedia](https://core.telegram.org/bots/api#inputpolloptionmedia) | *Optional*. Media added to the poll option |