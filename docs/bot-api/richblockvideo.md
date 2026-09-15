Source: https://core.telegram.org/bots/api#richblockvideo
Snapshot: 2026-09-15T08:44:15Z

#### RichBlockVideo

A block with a video, corresponding to the HTML tag `<video>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “video” |
| video | [Video](https://core.telegram.org/bots/api#video) | The video |
| has_spoiler | True | *Optional*. *True*, if the media preview is covered by a spoiler animation |
| caption | [RichBlockCaption](https://core.telegram.org/bots/api#richblockcaption) | *Optional*. Caption of the block |