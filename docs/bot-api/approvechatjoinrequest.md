Source: https://core.telegram.org/bots/api#approvechatjoinrequest
Snapshot: 2026-09-14T08:59:05Z

#### approveChatJoinRequest

Use this method to approve a chat join request. The bot must be an administrator in the chat for this to work and must have the *can_invite_users* administrator right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target channel in the format `@username` |
| user_id | Integer | Yes | Unique identifier of the target user |