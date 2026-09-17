Source: https://core.telegram.org/bots/api#inputrichblockanimation
Snapshot: 2026-09-17T08:42:18Z

#### InputRichBlockAnimation

A block with an animation, corresponding to the HTML tag `<video>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “animation” |
| animation | [InputMediaAnimation](https://core.telegram.org/bots/api#inputmediaanimation) | The animation. Caption is ignored. |
| caption | [RichBlockCaption](https://core.telegram.org/bots/api#richblockcaption) | *Optional*. Caption of the block |