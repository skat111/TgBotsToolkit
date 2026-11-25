Source: https://core.telegram.org/bots/api#user
Snapshot: 2026-11-25T13:00:03Z

#### User

This object represents a Telegram user or bot.

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type is safe for storing this identifier. |
| is_bot | Boolean | *True*, if this user is a bot |
| first_name | String | User's or bot's first name |
| last_name | String | *Optional*. User's or bot's last name |
| username | String | *Optional*. User's or bot's username |
| language_code | String | *Optional*. [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) of the user's language |
| is_premium | True | *Optional*. *True*, if this user is a Telegram Premium user |
| added_to_attachment_menu | True | *Optional*. *True*, if this user added the bot to the attachment menu |