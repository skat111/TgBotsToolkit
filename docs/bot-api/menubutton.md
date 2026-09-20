Source: https://core.telegram.org/bots/api#menubutton
Snapshot: 2026-09-20T08:38:20Z

#### MenuButton

This object describes the bot's menu button in a private chat. It should be one of

* [MenuButtonCommands](https://core.telegram.org/bots/api#menubuttoncommands)
* [MenuButtonWebApp](https://core.telegram.org/bots/api#menubuttonwebapp)
* [MenuButtonDefault](https://core.telegram.org/bots/api#menubuttondefault)

If a menu button other than [MenuButtonDefault](https://core.telegram.org/bots/api#menubuttondefault) is set for a private chat, then it is applied in the chat. Otherwise the default menu button is applied. By default, the menu button opens the list of bot commands.