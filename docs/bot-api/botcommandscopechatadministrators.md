Source: https://core.telegram.org/bots/api#botcommandscopechatadministrators
Snapshot: 2026-09-26T08:38:44Z

#### BotCommandScopeChatAdministrators

Represents the [scope](https://core.telegram.org/bots/api#botcommandscope) of bot commands, covering all administrators of a specific group or supergroup chat.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Scope type, must be *chat_administrators* |
| chat_id | Integer or String | Unique identifier for the target chat or username of the target supergroup in the format `@username`. Channel direct messages chats and channel chats aren't supported. |