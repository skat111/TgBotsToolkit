Source: https://core.telegram.org/bots/api#richblockexpandableblockquotation
Snapshot: 2026-11-28T11:51:36Z

#### RichBlockExpandableBlockQuotation

A block quotation, corresponding to the HTML tag `<blockquote>` with the custom attribute `"expandable"`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “expandable_blockquote” |
| blocks | Array of [RichBlock](https://core.telegram.org/bots/api#richblock) | Content of the block |
| credit | [RichText](https://core.telegram.org/bots/api#richtext) | *Optional*. Credit of the block |