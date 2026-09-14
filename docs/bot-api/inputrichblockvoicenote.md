Source: https://core.telegram.org/bots/api#inputrichblockvoicenote
Snapshot: 2026-09-14T08:59:05Z

#### InputRichBlockVoiceNote

A block with a voice note, corresponding to the HTML tag `<audio>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “voice_note” |
| voice_note | [InputMediaVoiceNote](https://core.telegram.org/bots/api#inputmediavoicenote) | The voice note. Caption is ignored. |
| caption | [RichBlockCaption](https://core.telegram.org/bots/api#richblockcaption) | *Optional*. Caption of the block |