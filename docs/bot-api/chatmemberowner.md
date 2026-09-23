Source: https://core.telegram.org/bots/api#chatmemberowner
Snapshot: 2026-09-23T08:37:58Z

#### ChatMemberOwner

Represents a [chat member](https://core.telegram.org/bots/api#chatmember) that owns the chat and has all administrator privileges.

| Field | Type | Description |
| --- | --- | --- |
| status | String | The member's status in the chat, always “creator” |
| user | [User](https://core.telegram.org/bots/api#user) | Information about the user |
| is_anonymous | Boolean | *True*, if the user's presence in the chat is hidden |
| custom_title | String | *Optional*. Custom title for this user |