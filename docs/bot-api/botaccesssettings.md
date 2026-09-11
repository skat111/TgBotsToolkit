Source: https://core.telegram.org/bots/api#botaccesssettings
Snapshot: 2026-09-11T06:04:42Z

#### BotAccessSettings

This object describes the access settings of a bot.

| Field | Type | Description |
| --- | --- | --- |
| is_access_restricted | Boolean | *True*, if only selected users can access the bot. The bot's owner can always access it. |
| added_users | Array of [User](https://core.telegram.org/bots/api#user) | *Optional*. The list of other users who have access to the bot if the access is restricted |