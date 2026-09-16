Source: https://core.telegram.org/bots/api#richblockanimation
Snapshot: 2026-09-16T08:38:32Z

#### RichBlockAnimation

A block with an animation, corresponding to the HTML tag `<video>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “animation” |
| animation | [Animation](https://core.telegram.org/bots/api#animation) | The animation |
| has_spoiler | True | *Optional*. *True*, if the media preview is covered by a spoiler animation |
| caption | [RichBlockCaption](https://core.telegram.org/bots/api#richblockcaption) | *Optional*. Caption of the block |