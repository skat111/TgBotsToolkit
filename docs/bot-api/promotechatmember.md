Source: https://core.telegram.org/bots/api#promotechatmember
Snapshot: 2026-09-14T08:59:05Z

#### promoteChatMember

Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass *False* for all boolean parameters to demote a user. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target channel in the format `@username` |
| user_id | Integer | Yes | Unique identifier of the target user |
| is_anonymous | Boolean | Optional | Pass *True* if the administrator's presence in the chat is hidden |
| can_manage_chat | Boolean | Optional | Pass *True* if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages, ignore slow mode, and send messages to the chat without paying Telegram Stars. Implied by any other administrator privilege. |
| can_delete_messages | Boolean | Optional | Pass *True* if the administrator can delete messages of other users |
| can_manage_video_chats | Boolean | Optional | Pass *True* if the administrator can manage video chats |
| can_restrict_members | Boolean | Optional | Pass *True* if the administrator can restrict, ban or unban chat members, or access supergroup statistics. For backward compatibility, defaults to *True* for promotions of channel administrators. |
| can_promote_members | Boolean | Optional | Pass *True* if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by him) |
| can_change_info | Boolean | Optional | Pass *True* if the administrator can change chat title, photo and other settings |
| can_invite_users | Boolean | Optional | Pass *True* if the administrator can invite new users to the chat |
| can_post_stories | Boolean | Optional | Pass *True* if the administrator can post stories to the chat |
| can_edit_stories | Boolean | Optional | Pass *True* if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat's story archive |
| can_delete_stories | Boolean | Optional | Pass *True* if the administrator can delete stories posted by other users |
| can_post_messages | Boolean | Optional | Pass *True* if the administrator can post messages in the channel, approve suggested posts, or access channel statistics; for channels only |
| can_edit_messages | Boolean | Optional | Pass *True* if the administrator can edit messages of other users and can pin messages; for channels only |
| can_pin_messages | Boolean | Optional | Pass *True* if the administrator can pin messages; for supergroups only |
| can_manage_topics | Boolean | Optional | Pass *True* if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only |
| can_manage_direct_messages | Boolean | Optional | Pass *True* if the administrator can manage direct messages within the channel and decline suggested posts; for channels only |
| can_manage_tags | Boolean | Optional | Pass *True* if the administrator can edit the tags of regular members; for groups and supergroups only |
| can_send_welcome_messages | Boolean | Optional | Pass *True* if the administrator can manage chat welcome messages or directly send them in the case of bots |