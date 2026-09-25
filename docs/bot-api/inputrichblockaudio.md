Source: https://core.telegram.org/bots/api#inputrichblockaudio
Snapshot: 2026-09-25T08:52:18Z

#### InputRichBlockAudio

A block with a music file, corresponding to the HTML tag `<audio>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “audio” |
| audio | [InputMediaAudio](https://core.telegram.org/bots/api#inputmediaaudio) | The audio. Caption is ignored. |
| caption | [RichBlockCaption](https://core.telegram.org/bots/api#richblockcaption) | *Optional*. Caption of the block |