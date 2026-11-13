Source: https://core.telegram.org/bots/api#answerwidgetquery
Snapshot: 2026-11-13T11:03:46Z

#### answerWidgetQuery

Use this method to send an answer to a query from a widget. The query must be answered within 15 seconds. The answer is received only by the widget that sent the query and doesn't change data of the widget; use [editMessageWidgetData](https://core.telegram.org/bots/api#editmessagewidgetdata) or [editSharedWidgetData](https://core.telegram.org/bots/api#editsharedwidgetdata) to change it. On success, *True* is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| widget_query_id | String | Yes | Unique identifier for the query to be answered |
| data | String | Optional | Data to be returned to the widget, 0-1024 bytes |