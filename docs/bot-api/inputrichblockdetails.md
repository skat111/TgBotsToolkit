Source: https://core.telegram.org/bots/api#inputrichblockdetails
Snapshot: 2026-09-16T08:38:32Z

#### InputRichBlockDetails

An expandable block for details disclosure, corresponding to the HTML tag `<details>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “details” |
| summary | [RichText](https://core.telegram.org/bots/api#richtext) | Always shown summary of the block |
| blocks | Array of [InputRichBlock](https://core.telegram.org/bots/api#inputrichblock) | Content of the block |
| is_open | True | *Optional*. Pass *True* if the content of the block is visible by default |