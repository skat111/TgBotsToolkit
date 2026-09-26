Source: https://core.telegram.org/bots/api#approvesuggestedpost
Snapshot: 2026-09-26T08:38:44Z

#### approveSuggestedPost

Use this method to approve a suggested post in a direct messages chat. The bot must have the 'can_post_messages' administrator right in the corresponding channel chat. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer | Yes | Unique identifier for the target direct messages chat |
| message_id | Integer | Yes | Identifier of a suggested post message to approve |
| send_date | Integer | Optional | Point in time (Unix timestamp) when the post is expected to be published; omit if the date has already been specified when the suggested post was created. If specified, then the date must be not more than 2678400 seconds (30 days) in the future. |