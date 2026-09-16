Source: https://core.telegram.org/bots/api#richblockblockquotation
Snapshot: 2026-09-16T08:38:32Z

#### RichBlockBlockQuotation

A block quotation, corresponding to the HTML tag `<blockquote>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “blockquote” |
| blocks | Array of [RichBlock](https://core.telegram.org/bots/api#richblock) | Content of the block |
| credit | [RichText](https://core.telegram.org/bots/api#richtext) | *Optional*. Credit of the block |