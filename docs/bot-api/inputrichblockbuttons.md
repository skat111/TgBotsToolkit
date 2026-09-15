Source: https://core.telegram.org/bots/api#inputrichblockbuttons
Snapshot: 2026-09-15T08:44:15Z

#### InputRichBlockButtons

A block containing a list of buttons that are shown in one row, corresponding to the custom HTML tag `<tg-button-row>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “buttons” |
| buttons | Array of [RichMessageButton](https://core.telegram.org/bots/api#richmessagebutton) | List of 1-8 buttons to send |
| align | String | *Optional*. Horizontal alignment of the buttons. Currently, must be one of “left”, “center”, or “right”. |