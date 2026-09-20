Source: https://core.telegram.org/bots/api#setchatpermissions
Snapshot: 2026-09-20T08:38:20Z

#### setChatPermissions

Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the *can_restrict_members* administrator rights. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| permissions | [ChatPermissions](https://core.telegram.org/bots/api#chatpermissions) | Yes | A JSON-serialized object for new default chat permissions |
| use_independent_chat_permissions | Boolean | Optional | Pass *True* if chat permissions are set independently. Otherwise, the *can_send_other_messages* and *can_add_web_page_previews* permissions will imply the *can_send_messages*, *can_send_audios*, *can_send_documents*, *can_send_photos*, *can_send_videos*, *can_send_video_notes*, and *can_send_voice_notes* permissions; the *can_send_polls* permission will imply the *can_send_messages* permission. |