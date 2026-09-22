Source: https://core.telegram.org/bots/api#answerwebappquery
Snapshot: 2026-09-22T08:35:37Z

#### answerWebAppQuery

Use this method to set the result of an interaction with a [Web App](https://core.telegram.org/bots/webapps) and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a [SentWebAppMessage](https://core.telegram.org/bots/api#sentwebappmessage) object is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| web_app_query_id | String | Yes | Unique identifier for the query to be answered |
| result | [InlineQueryResult](https://core.telegram.org/bots/api#inlinequeryresult) | Yes | A JSON-serialized object describing the message to be sent |