Source: https://core.telegram.org/bots/api#inputrichblockphoto
Snapshot: 2026-09-16T08:38:32Z

#### InputRichBlockPhoto

A block with a photo, corresponding to the HTML tag `<img>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “photo” |
| photo | [InputMediaPhoto](https://core.telegram.org/bots/api#inputmediaphoto) | The photo. Caption is ignored. |
| caption | [RichBlockCaption](https://core.telegram.org/bots/api#richblockcaption) | *Optional*. Caption of the block |