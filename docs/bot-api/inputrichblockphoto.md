Source: https://core.telegram.org/bots/api#inputrichblockphoto
Snapshot: 2026-09-12T07:57:24Z

#### InputRichBlockPhoto

A block with a photo, corresponding to the HTML tag `<img>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “photo” |
| photo | [InputMediaPhoto](https://core.telegram.org/bots/api#inputmediaphoto) | The photo. Caption is ignored. |
| caption | [RichBlockCaption](https://core.telegram.org/bots/api#richblockcaption) | *Optional*. Caption of the block |