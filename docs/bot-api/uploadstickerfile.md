Source: https://core.telegram.org/bots/api#uploadstickerfile
Snapshot: 2026-09-26T08:38:44Z

#### uploadStickerFile

Use this method to upload a file with a sticker for later use in the [createNewStickerSet](https://core.telegram.org/bots/api#createnewstickerset), [addStickerToSet](https://core.telegram.org/bots/api#addstickertoset), or [replaceStickerInSet](https://core.telegram.org/bots/api#replacestickerinset) methods (the file can be used multiple times). Returns the uploaded [File](https://core.telegram.org/bots/api#file) on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | Integer | Yes | User identifier of sticker file owner |
| sticker | [InputFile](https://core.telegram.org/bots/api#inputfile) | Yes | A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM format. See [<https://core.telegram.org/stickers>](https://core.telegram.org/stickers) for technical requirements. [More information on Sending Files »](https://core.telegram.org/bots/api#sending-files) |
| sticker_format | String | Yes | Format of the sticker, must be one of “static”, “animated”, “video” |