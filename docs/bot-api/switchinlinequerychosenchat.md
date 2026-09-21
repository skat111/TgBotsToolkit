Source: https://core.telegram.org/bots/api#switchinlinequerychosenchat
Snapshot: 2026-09-21T09:00:24Z

#### SwitchInlineQueryChosenChat

This object represents an inline button that switches the current user to inline mode in a chosen chat, with an optional default inline query.

| Field | Type | Description |
| --- | --- | --- |
| query | String | *Optional*. The default inline query to be inserted in the input field. If left empty, only the bot's username will be inserted. |
| allow_user_chats | Boolean | *Optional*. *True*, if private chats with users can be chosen |
| allow_bot_chats | Boolean | *Optional*. *True*, if private chats with bots can be chosen |
| allow_group_chats | Boolean | *Optional*. *True*, if group and supergroup chats can be chosen |
| allow_channel_chats | Boolean | *Optional*. *True*, if channel chats can be chosen |