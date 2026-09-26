Source: https://core.telegram.org/bots/api#richblockthinking
Snapshot: 2026-09-26T08:38:44Z

#### RichBlockThinking

A block with a “Thinking…” placeholder, corresponding to the custom HTML tag `<tg-thinking>`. The block may be used only in [sendRichMessageDraft](https://core.telegram.org/bots/api#sendrichmessagedraft), therefore it can't be received in messages. See [<https://t.me/addemoji/AIActions>](https://t.me/addemoji/AIActions) for examples of custom emoji that are recommended for usage in the block.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “thinking” |
| text | [RichText](https://core.telegram.org/bots/api#richtext) | Text of the block. See [<https://t.me/addemoji/AIActions>](https://t.me/addemoji/AIActions) for examples of custom emoji that are recommended for usage in the block. |