Source: https://core.telegram.org/bots/api#richblockdetails
Snapshot: 2026-09-19T08:05:57Z

#### RichBlockDetails

An expandable block for details disclosure, corresponding to the HTML tag `<details>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “details” |
| summary | [RichText](https://core.telegram.org/bots/api#richtext) | Always shown summary of the block |
| blocks | Array of [RichBlock](https://core.telegram.org/bots/api#richblock) | Content of the block |
| is_open | True | *Optional*. *True*, if the content of the block is visible by default |