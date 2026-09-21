Source: https://core.telegram.org/bots/api#inputpaidmedialivephoto
Snapshot: 2026-09-21T09:00:24Z

#### InputPaidMediaLivePhoto

The paid media to send is a live photo.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the media, must be *live_photo* |
| media | String | Video of the live photo to send. Pass a file_id to send a file that exists on the Telegram servers (recommended) or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api#sending-files). Sending live photos by a URL is currently unsupported. |
| photo | String | The static photo to send. Pass a file_id to send a file that exists on the Telegram servers (recommended) or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api#sending-files). Sending live photos by a URL is currently unsupported. |