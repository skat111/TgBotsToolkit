Source: https://core.telegram.org/bots/api#deletemycommands
Snapshot: 2026-09-12T07:57:24Z

#### deleteMyCommands

Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, [higher level commands](https://core.telegram.org/bots/api#determining-list-of-commands) will be shown to affected users. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| scope | [BotCommandScope](https://core.telegram.org/bots/api#botcommandscope) | Optional | A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to [BotCommandScopeDefault](https://core.telegram.org/bots/api#botcommandscopedefault). |
| language_code | String | Optional | A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands. |