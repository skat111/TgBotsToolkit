Source: https://core.telegram.org/bots/api#answerinlinequery
Snapshot: 2026-09-16T08:38:32Z

#### answerInlineQuery

Use this method to send answers to an inline query. On success, *True* is returned.  
No more than **50** results per query are allowed.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| inline_query_id | String | Yes | Unique identifier for the answered query |
| results | Array of [InlineQueryResult](https://core.telegram.org/bots/api#inlinequeryresult) | Yes | A JSON-serialized Array of results for the inline query |
| cache_time | Integer | Optional | The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300. |
| is_personal | Boolean | Optional | Pass *True* if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query. |
| next_offset | String | Optional | Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes. |
| button | [InlineQueryResultsButton](https://core.telegram.org/bots/api#inlinequeryresultsbutton) | Optional | A JSON-serialized object describing a button to be shown above inline query results |