Source: https://core.telegram.org/bots/api#richblockvoicenote
Snapshot: 2026-09-26T08:38:44Z

#### RichBlockVoiceNote

A block with a voice note, corresponding to the HTML tag `<audio>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “voice_note” |
| voice_note | [Voice](https://core.telegram.org/bots/api#voice) | The voice note |
| caption | [RichBlockCaption](https://core.telegram.org/bots/api#richblockcaption) | *Optional*. Caption of the block |