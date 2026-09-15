Source: https://core.telegram.org/bots/api#richblocktablecell
Snapshot: 2026-09-15T08:44:15Z

#### RichBlockTableCell

Cell in a table.

| Field | Type | Description |
| --- | --- | --- |
| text | [RichText](https://core.telegram.org/bots/api#richtext) | *Optional*. Text in the cell. If omitted, then the cell is invisible. |
| is_header | True | *Optional*. *True*, if the cell is a header cell |
| colspan | Integer | *Optional*. The number of columns the cell spans if it is bigger than 1 |
| rowspan | Integer | *Optional*. The number of rows the cell spans if it is bigger than 1 |
| align | String | Horizontal cell content alignment. Currently, must be one of “left”, “center”, or “right”. |
| valign | String | Vertical cell content alignment. Currently, must be one of “top”, “middle”, or “bottom”. |