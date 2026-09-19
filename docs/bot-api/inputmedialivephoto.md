Source: https://core.telegram.org/bots/api#inputmedialivephoto
Snapshot: 2026-09-19T08:05:57Z

#### InputMediaLivePhoto

Represents a live photo to be sent.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the media, must be *live_photo* |
| media | String | Video of the live photo to send. Pass a file_id to send a file that exists on the Telegram servers (recommended) or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api#sending-files). Sending live photos by a URL is currently unsupported. |
| photo | String | The static photo to send. Pass a file_id to send a file that exists on the Telegram servers (recommended) or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api#sending-files). Sending live photos by a URL is currently unsupported. |
| caption | String | *Optional*. Caption of the live photo to be sent, 0-1024 characters after entities parsing |
| parse_mode | String | *Optional*. Mode for parsing entities in the live photo caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| caption_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode* |
| show_caption_above_media | Boolean | *Optional*. Pass *True* if the caption must be shown above the message media |
| has_spoiler | Boolean | *Optional*. Pass *True* if the live photo needs to be covered with a spoiler animation |