Source: https://core.telegram.org/bots/api#answerchatjoinrequestquery
Snapshot: 2026-09-13T08:21:39Z

#### answerChatJoinRequestQuery

Use this method to process a received chat join request query. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_join_request_query_id | String | Yes | Unique identifier of the join request query |
| result | String | Yes | Result of the query. Must be either “approve” to allow the user to join the chat, “decline” to disallow the user to join the chat, or “queue” to leave the decision to other administrators. |