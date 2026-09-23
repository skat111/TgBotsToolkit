Source: https://core.telegram.org/bots/api#chatmemberadministrator
Snapshot: 2026-09-23T08:37:58Z

#### ChatMemberAdministrator

Represents a [chat member](https://core.telegram.org/bots/api#chatmember) that has some additional privileges.

| Field | Type | Description |
| --- | --- | --- |
| status | String | The member's status in the chat, always “administrator” |
| user | [User](https://core.telegram.org/bots/api#user) | Information about the user |
| can_be_edited | Boolean | *True*, if the bot is allowed to edit administrator privileges of that user |
| is_anonymous | Boolean | *True*, if the user's presence in the chat is hidden |
| can_manage_chat | Boolean | *True*, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages, ignore slow mode, and send messages to the chat without paying Telegram Stars. Implied by any other administrator privilege. |
| can_delete_messages | Boolean | *True*, if the administrator can delete messages of other users |
| can_manage_video_chats | Boolean | *True*, if the administrator can manage video chats |
| can_restrict_members | Boolean | *True*, if the administrator can restrict, ban or unban chat members, or access supergroup statistics |
| can_promote_members | Boolean | *True*, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user) |
| can_change_info | Boolean | *True*, if the user is allowed to change the chat title, photo and other settings |
| can_invite_users | Boolean | *True*, if the user is allowed to invite new users to the chat |
| can_post_stories | Boolean | *True*, if the administrator can post stories to the chat |
| can_edit_stories | Boolean | *True*, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat's story archive |
| can_delete_stories | Boolean | *True*, if the administrator can delete stories posted by other users |
| can_post_messages | Boolean | *Optional*. *True*, if the administrator can post messages in the channel, approve suggested posts, or access channel statistics; for channels only |
| can_edit_messages | Boolean | *Optional*. *True*, if the administrator can edit messages of other users and can pin messages; for channels only |
| can_pin_messages | Boolean | *Optional*. *True*, if the user is allowed to pin messages; for groups and supergroups only |
| can_manage_topics | Boolean | *Optional*. *True*, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only |
| can_manage_direct_messages | Boolean | *Optional*. *True*, if the administrator can manage direct messages of the channel and decline suggested posts; for channels only |
| can_manage_tags | Boolean | *Optional*. *True*, if the administrator can edit the tags of regular members; for groups and supergroups only |
| can_send_welcome_messages | Boolean | *True*, if the administrator can manage chat welcome messages or directly send them in the case of bots |
| custom_title | String | *Optional*. Custom title for this user |