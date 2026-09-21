Source: https://core.telegram.org/bots/api#botcommandscopechatmember
Snapshot: 2026-09-21T09:00:24Z

#### BotCommandScopeChatMember

Represents the [scope](https://core.telegram.org/bots/api#botcommandscope) of bot commands, covering a specific member of a group or supergroup chat.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Scope type, must be *chat_member* |
| chat_id | Integer or String | Unique identifier for the target chat or username of the target supergroup in the format `@username`. Channel direct messages chats and channel chats aren't supported. |
| user_id | Integer | Unique identifier of the target user |