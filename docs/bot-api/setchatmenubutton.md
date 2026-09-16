Source: https://core.telegram.org/bots/api#setchatmenubutton
Snapshot: 2026-09-16T08:38:32Z

#### setChatMenuButton

Use this method to change the bot's menu button in a private chat, or the default menu button. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer | Optional | Unique identifier for the target private chat. If not specified, the bot's default menu button will be changed. |
| menu_button | [MenuButton](https://core.telegram.org/bots/api#menubutton) | Optional | A JSON-serialized object for the bot's new menu button. Defaults to [MenuButtonDefault](https://core.telegram.org/bots/api#menubuttondefault). |