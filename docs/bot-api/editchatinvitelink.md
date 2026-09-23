Source: https://core.telegram.org/bots/api#editchatinvitelink
Snapshot: 2026-09-23T08:37:58Z

#### editChatInviteLink

Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a [ChatInviteLink](https://core.telegram.org/bots/api#chatinvitelink) object.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target channel in the format `@username` |
| invite_link | String | Yes | The invite link to edit |
| name | String | Optional | Invite link name; 0-32 characters |
| expire_date | Integer | Optional | Point in time (Unix timestamp) when the link will expire |
| member_limit | Integer | Optional | The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999 |
| creates_join_request | Boolean | Optional | *True*, if users joining the chat via the link need to be approved by chat administrators. If *True*, *member_limit* can't be specified. |