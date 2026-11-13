Source: https://core.telegram.org/bots/api#richblocklist
Snapshot: 2026-11-13T11:03:46Z

#### RichBlockList

A list of blocks, corresponding to the HTML tag `<ul>` or `<ol>` with multiple nested tags `<li>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “list” |
| items | Array of [RichBlockListItem](https://core.telegram.org/bots/api#richblocklistitem) | Items of the list |