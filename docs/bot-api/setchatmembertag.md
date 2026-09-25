Source: https://core.telegram.org/bots/api#setchatmembertag
Snapshot: 2026-09-25T08:52:18Z

#### setChatMemberTag

Use this method to set a tag for a regular member in a group or a supergroup. The bot must be an administrator in the chat for this to work and must have the *can_manage_tags* administrator right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| user_id | Integer | Yes | Unique identifier of the target user |
| tag | String | Optional | New tag for the member; 0-16 characters, emoji are not allowed |