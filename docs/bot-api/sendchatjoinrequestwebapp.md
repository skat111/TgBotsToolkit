Source: https://core.telegram.org/bots/api#sendchatjoinrequestwebapp
Snapshot: 2026-09-17T08:42:18Z

#### sendChatJoinRequestWebApp

Use this method to process a received chat join request query by showing a Mini App to the user before deciding the outcome. Call [answerChatJoinRequestQuery](https://core.telegram.org/bots/api#answerchatjoinrequestquery) to resolve the join request query based on the user interaction with the Mini App. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_join_request_query_id | String | Yes | Unique identifier of the join request query |
| web_app_url | String | Yes | An HTTPS URL of a Web App to be opened with additional data as specified in [Initializing Web Apps](https://core.telegram.org/bots/webapps#initializing-mini-apps) |