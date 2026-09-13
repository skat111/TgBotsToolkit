Source: https://core.telegram.org/bots/api#chat
Snapshot: 2026-09-13T08:21:39Z

#### Chat

This object represents a chat.

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. |
| type | String | Type of the chat, can be either “private”, “group”, “supergroup” or “channel” |
| title | String | *Optional*. Title, for supergroups, channels and group chats |
| username | String | *Optional*. Username, for private chats, supergroups and channels if available |
| first_name | String | *Optional*. First name of the other party in a private chat |
| last_name | String | *Optional*. Last name of the other party in a private chat |
| is_forum | True | *Optional*. *True*, if the supergroup chat is a forum (has [topics](https://telegram.org/blog/topics-in-groups-collectible-usernames#topics-in-groups) enabled) |
| is_direct_messages | True | *Optional*. *True*, if the chat is the direct messages chat of a channel |