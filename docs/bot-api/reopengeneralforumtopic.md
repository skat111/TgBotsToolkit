Source: https://core.telegram.org/bots/api#reopengeneralforumtopic
Snapshot: 2026-09-22T08:35:37Z

#### reopenGeneralForumTopic

Use this method to reopen a closed 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the *can_manage_topics* administrator rights. The topic will be automatically unhidden if it was hidden. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |