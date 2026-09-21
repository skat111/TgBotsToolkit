Source: https://core.telegram.org/bots/api#getmycommands
Snapshot: 2026-09-21T09:00:24Z

#### getMyCommands

Use this method to get the current list of the bot's commands for the given scope and user language. Returns an Array of [BotCommand](https://core.telegram.org/bots/api#botcommand) objects. If commands aren't set, an empty list is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| scope | [BotCommandScope](https://core.telegram.org/bots/api#botcommandscope) | Optional | A JSON-serialized object, describing scope of users. Defaults to [BotCommandScopeDefault](https://core.telegram.org/bots/api#botcommandscopedefault). |
| language_code | String | Optional | A two-letter ISO 639-1 language code or an empty string |