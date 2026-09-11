Source: https://core.telegram.org/bots/api#setmycommands
Snapshot: 2026-09-11T06:04:42Z

#### setMyCommands

Use this method to change the list of the bot's commands. See [this manual](https://core.telegram.org/bots/features#commands) for more details about bot commands. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| commands | Array of [BotCommand](https://core.telegram.org/bots/api#botcommand) | Yes | A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most 100 commands can be specified. |
| scope | [BotCommandScope](https://core.telegram.org/bots/api#botcommandscope) | Optional | A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to [BotCommandScopeDefault](https://core.telegram.org/bots/api#botcommandscopedefault). |
| language_code | String | Optional | A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands. |