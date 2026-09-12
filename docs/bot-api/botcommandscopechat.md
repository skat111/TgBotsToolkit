Source: https://core.telegram.org/bots/api#botcommandscopechat
Snapshot: 2026-09-12T07:57:24Z

#### BotCommandScopeChat

Represents the [scope](https://core.telegram.org/bots/api#botcommandscope) of bot commands, covering a specific chat.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Scope type, must be *chat* |
| chat_id | Integer or String | Unique identifier for the target chat or username of the target supergroup in the format `@username`. Channel direct messages chats and channel chats aren't supported. |