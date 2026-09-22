Source: https://core.telegram.org/bots/api#richblockbuttons
Snapshot: 2026-09-22T08:35:37Z

#### RichBlockButtons

A block containing a list of buttons that are shown in one row, corresponding to the custom HTML tag `<tg-button-row>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “buttons” |
| buttons | Array of [RichMessageButton](https://core.telegram.org/bots/api#richmessagebutton) | The buttons |
| align | String | *Optional*. Horizontal alignment of the buttons. Currently, must be one of “left”, “center”, or “right”. |