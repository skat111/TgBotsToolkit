Source: https://core.telegram.org/bots/api#inputrichblockblockquotation
Snapshot: 2026-10-14T08:46:29Z

#### InputRichBlockBlockQuotation

A block quotation, corresponding to the HTML tag `<blockquote>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “blockquote” |
| blocks | Array of [InputRichBlock](https://core.telegram.org/bots/api#inputrichblock) | Content of the block |
| credit | [RichText](https://core.telegram.org/bots/api#richtext) | *Optional*. Credit of the block |