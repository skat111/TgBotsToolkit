Source: https://core.telegram.org/bots/api#richtextdatetime
Snapshot: 2026-09-21T09:00:24Z

#### RichTextDateTime

Formatted date and time.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the rich text, always “date_time” |
| text | [RichText](https://core.telegram.org/bots/api#richtext) | The text |
| unix_time | Integer | The Unix time associated with the entity |
| date_time_format | String | The string that defines the formatting of the date and time. See [date-time entity formatting](https://core.telegram.org/bots/api#date-time-entity-formatting) for more details. |