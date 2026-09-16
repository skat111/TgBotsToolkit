Source: https://core.telegram.org/bots/api#inputrichblocklist
Snapshot: 2026-09-16T08:38:32Z

#### InputRichBlockList

A list of blocks, corresponding to the HTML tag `<ul>` or `<ol>` with multiple nested tags `<li>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “list” |
| items | Array of [InputRichBlockListItem](https://core.telegram.org/bots/api#inputrichblocklistitem) | Items of the list |