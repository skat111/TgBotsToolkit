Source: https://core.telegram.org/bots/api#richblockphoto
Snapshot: 2026-09-12T07:57:24Z

#### RichBlockPhoto

A block with a photo, corresponding to the HTML tag `<img>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “photo” |
| photo | Array of [PhotoSize](https://core.telegram.org/bots/api#photosize) | Available sizes of the photo |
| has_spoiler | True | *Optional*. *True*, if the media preview is covered by a spoiler animation |
| caption | [RichBlockCaption](https://core.telegram.org/bots/api#richblockcaption) | *Optional*. Caption of the block |