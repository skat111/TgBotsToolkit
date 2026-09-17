Source: https://core.telegram.org/bots/api#inputrichblocklistitem
Snapshot: 2026-09-17T08:42:18Z

#### InputRichBlockListItem

An item of a list to be sent.

| Field | Type | Description |
| --- | --- | --- |
| blocks | Array of [InputRichBlock](https://core.telegram.org/bots/api#inputrichblock) | The content of the item |
| has_checkbox | True | *Optional*. Pass *True* if the item has a checkbox |
| is_checked | True | *Optional*. Pass *True* if the item has a checked checkbox |
| value | Integer | *Optional*. For ordered lists, the numeric value of the item label |
| type | String | *Optional*. For ordered lists, the type of the item label; must be one of “a” for lowercase letters, “A” for uppercase letters, “i” for lowercase Roman numerals, “I” for uppercase Roman numerals, or “1” for decimal numbers |