Source: https://core.telegram.org/bots/api#unbanchatsenderchat
Snapshot: 2026-09-11T06:04:42Z

#### unbanChatSenderChat

Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target channel in the format `@username` |
| sender_chat_id | Integer | Yes | Unique identifier of the target sender chat |