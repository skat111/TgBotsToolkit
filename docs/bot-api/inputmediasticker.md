Source: https://core.telegram.org/bots/api#inputmediasticker
Snapshot: 2026-09-14T08:59:05Z

#### InputMediaSticker

Represents a sticker file to be sent.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the media, must be *sticker* |
| media | String | File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a .WEBP sticker from the Internet, or pass “attach://<file_attach_name>” to upload a new .WEBP, .TGS, or .WEBM sticker using multipart/form-data under <file_attach_name> name. [More information on Sending Files »](https://core.telegram.org/bots/api#sending-files) |
| emoji | String | *Optional*. Emoji associated with the sticker; only for just uploaded stickers |