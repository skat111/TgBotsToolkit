Source: https://core.telegram.org/bots/api#widgetquery
Snapshot: 2026-11-14T10:30:31Z

#### WidgetQuery

This object represents an incoming query from a widget in a message sent by the bot or via the bot. Use [answerWidgetQuery](https://core.telegram.org/bots/api#answerwidgetquery) to answer the query. Each user can send at most 5 queries per 5 seconds to the bot from all its widgets.

| Field | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier for this query |
| from | [User](https://core.telegram.org/bots/api#user) | Sender |
| chat | [Chat](https://core.telegram.org/bots/api#chat) | *Optional*. Chat with the message containing the widget; omitted if the widget is in an inline message |
| message_id | Integer | *Optional*. Identifier of the message containing the widget; omitted if the widget is in an inline message |
| inline_message_id | String | *Optional*. Identifier of the inline message containing the widget |
| chat_instance | String | Global identifier, uniquely corresponding to the chat to which the message with the widget was sent |
| chat_type | String | *Optional*. For widgets in inline messages, type of the chat to which the message was sent. Can be either “sender” for a private chat with the inline query sender, “private”, “group”, “supergroup”, or “channel”. |
| type | [WidgetQueryType](https://core.telegram.org/bots/api#widgetquerytype) | Type of the query |
| data | String | Data of the query, 1-64 bytes |
| widget_id | String | *Optional*. Unique identifier of the shared widget, which sent the query; omitted if the widget isn't shared |