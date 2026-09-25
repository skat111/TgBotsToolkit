Source: https://core.telegram.org/bots/api#inputsticker
Snapshot: 2026-09-25T08:52:18Z

#### InputSticker

This object describes a sticker to be added to a sticker set.

| Field | Type | Description |
| --- | --- | --- |
| sticker | String | The added sticker. Pass a *file_id* as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new file using multipart/form-data under <file_attach_name> name. Animated and video stickers can't be uploaded via HTTP URL. [More information on Sending Files »](https://core.telegram.org/bots/api#sending-files) |
| format | String | Format of the added sticker, must be one of “static” for a **.WEBP** or **.PNG** image, “animated” for a **.TGS** animation, “video” for a **.WEBM** video |
| emoji_list | Array of String | List of 1-20 emoji associated with the sticker |
| mask_position | [MaskPosition](https://core.telegram.org/bots/api#maskposition) | *Optional*. Position where the mask should be placed on faces. For “mask” stickers only. |
| keywords | Array of String | *Optional*. List of 0-20 search keywords for the sticker with total length of up to 64 characters. For “regular” and “custom_emoji” stickers only. |