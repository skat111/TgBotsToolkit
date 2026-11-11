Source: https://core.telegram.org/bots/api#sharedwidgetquery
Snapshot: 2026-11-11T11:02:11Z

#### SharedWidgetQuery

This object represents an incoming query from a forwarded message with a shared widget created by the bot. Use [answerWidgetQuery](https://core.telegram.org/bots/api#answerwidgetquery) to answer the query. Each user can send at most 5 queries per 5 seconds to the bot from all its widgets.

| Field | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier for this query |
| from | [User](https://core.telegram.org/bots/api#user) | Sender |
| type | [WidgetQueryType](https://core.telegram.org/bots/api#widgetquerytype) | Type of the query |
| data | String | Data of the query, 1-64 bytes |
| widget_id | String | Unique identifier of the shared widget, which sent the query |