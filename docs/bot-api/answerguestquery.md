Source: https://core.telegram.org/bots/api#answerguestquery
Snapshot: 2026-09-15T08:44:15Z

#### answerGuestQuery

Use this method to reply to a received guest message. On success, a [SentGuestMessage](https://core.telegram.org/bots/api#sentguestmessage) object is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| guest_query_id | String | Yes | Unique identifier for the query to be answered |
| result | [InlineQueryResult](https://core.telegram.org/bots/api#inlinequeryresult) | Yes | A JSON-serialized object describing the message to be sent |