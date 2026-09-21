Source: https://core.telegram.org/bots/api#closeforumtopic
Snapshot: 2026-09-21T09:00:24Z

#### closeForumTopic

Use this method to close an open topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights, unless it is the creator of the topic. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| message_thread_id | Integer | Yes | Unique identifier for the target message thread of the forum topic |