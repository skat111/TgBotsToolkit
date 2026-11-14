Source: https://core.telegram.org/bots/api#widget
Snapshot: 2026-11-14T10:30:31Z

#### Widget

This object describes an [HTML widget](https://core.telegram.org/bots/widgets).

| Field | Type | Description |
| --- | --- | --- |
| id | String | *Optional*. Unique identifier of the shared widget, which can be used to send the widget again using the method [sendSharedWidget](https://core.telegram.org/bots/api#sendsharedwidget); omitted if the widget isn't shared |
| width | Integer | *Optional*. Width of the widget in logical pixels; omitted if the widget must occupy the whole width of the message bubble |
| height | Integer | *Optional*. Height of the widget in logical pixels; omitted if the height of the widget isn't fixed |
| html | String | HTML code of the widget |
| public_data | String | *Optional*. Public data of the widget, which is available wherever the widget is shown. All messages with a shared widget have the same public data. |
| chat_data | String | *Optional*. Data of the widget, which is specific to the message |