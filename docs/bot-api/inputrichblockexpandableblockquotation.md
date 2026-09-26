Source: https://core.telegram.org/bots/api#inputrichblockexpandableblockquotation
Snapshot: 2026-09-26T08:38:44Z

#### InputRichBlockExpandableBlockQuotation

A block quotation, corresponding to the HTML tag `<blockquote>` with custom attribute `"expandable"`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “expandable_blockquote” |
| text | [RichText](https://core.telegram.org/bots/api#richtext) | Content of the block |
| credit | [RichText](https://core.telegram.org/bots/api#richtext) | *Optional*. Credit of the block |