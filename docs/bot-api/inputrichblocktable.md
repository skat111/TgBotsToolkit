Source: https://core.telegram.org/bots/api#inputrichblocktable
Snapshot: 2026-09-26T08:38:44Z

#### InputRichBlockTable

A table, corresponding to the HTML tag `<table>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “table” |
| cells | Array of Array of [RichBlockTableCell](https://core.telegram.org/bots/api#richblocktablecell) | Cells of the table |
| is_bordered | True | *Optional*. Pass *True* if the table has borders |
| is_striped | True | *Optional*. Pass *True* if the table is striped |
| is_compact | True | *Optional*. Pass *True* if table cells must have smaller indents |
| caption | [RichText](https://core.telegram.org/bots/api#richtext) | *Optional*. Caption of the table |