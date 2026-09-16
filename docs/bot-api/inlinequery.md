Source: https://core.telegram.org/bots/api#inlinequery
Snapshot: 2026-09-16T08:38:32Z

#### InlineQuery

This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

| Field | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier for this query |
| from | [User](https://core.telegram.org/bots/api#user) | Sender |
| query | String | Text of the query (up to 256 characters) |
| offset | String | Offset of the results to be returned, can be controlled by the bot |
| chat_type | String | *Optional*. Type of the chat from which the inline query was sent. Can be either “sender” for a private chat with the inline query sender, “private”, “group”, “supergroup”, or “channel”. The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat. |
| location | [Location](https://core.telegram.org/bots/api#location) | *Optional*. Sender location, only for bots that request user location |