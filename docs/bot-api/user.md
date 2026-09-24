Source: https://core.telegram.org/bots/api#user
Snapshot: 2026-09-24T08:30:39Z

#### User

This object represents a Telegram user or bot.

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. |
| is_bot | Boolean | *True*, if this user is a bot |
| first_name | String | User's or bot's first name |
| last_name | String | *Optional*. User's or bot's last name |
| username | String | *Optional*. User's or bot's username |
| language_code | String | *Optional*. [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) of the user's language |
| is_premium | True | *Optional*. *True*, if this user is a Telegram Premium user |
| added_to_attachment_menu | True | *Optional*. *True*, if this user added the bot to the attachment menu |
| can_join_groups | Boolean | *Optional*. *True*, if the bot can be invited to groups. Returned only in [getMe](https://core.telegram.org/bots/api#getme). |
| can_read_all_group_messages | Boolean | *Optional*. *True*, if [privacy mode](https://core.telegram.org/bots/features#privacy-mode) is disabled for the bot. Returned only in [getMe](https://core.telegram.org/bots/api#getme). |
| supports_guest_queries | Boolean | *Optional*. *True*, if the bot supports guest queries from chats it is not a member of. Returned only in [getMe](https://core.telegram.org/bots/api#getme). |
| supports_inline_queries | Boolean | *Optional*. *True*, if the bot supports inline queries. Returned only in [getMe](https://core.telegram.org/bots/api#getme). |
| can_connect_to_business | Boolean | *Optional*. *True*, if the bot can be connected to a user account to manage it. Returned only in [getMe](https://core.telegram.org/bots/api#getme). |
| has_main_web_app | Boolean | *Optional*. *True*, if the bot has a main Web App. Returned only in [getMe](https://core.telegram.org/bots/api#getme). |
| has_topics_enabled | Boolean | *Optional*. *True*, if the bot has forum topic mode enabled in private chats. Returned only in [getMe](https://core.telegram.org/bots/api#getme). |
| allows_users_to_create_topics | Boolean | *Optional*. *True*, if the bot allows users to create and delete topics in private chats. Returned only in [getMe](https://core.telegram.org/bots/api#getme). |
| can_manage_bots | Boolean | *Optional*. *True*, if other bots can be created to be controlled by the bot. Returned only in [getMe](https://core.telegram.org/bots/api#getme). |
| supports_join_request_queries | Boolean | *Optional*. *True*, if the bot supports join request queries and can be assigned to process them. Returned only in [getMe](https://core.telegram.org/bots/api#getme). |