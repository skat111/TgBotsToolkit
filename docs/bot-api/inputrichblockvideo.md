Source: https://core.telegram.org/bots/api#inputrichblockvideo
Snapshot: 2026-09-13T08:21:39Z

#### InputRichBlockVideo

A block with a video, corresponding to the HTML tag `<video>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “video” |
| video | [InputMediaVideo](https://core.telegram.org/bots/api#inputmediavideo) | The video. Caption is ignored. |
| caption | [RichBlockCaption](https://core.telegram.org/bots/api#richblockcaption) | *Optional*. Caption of the block |