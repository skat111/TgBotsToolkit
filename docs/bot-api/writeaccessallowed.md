Source: https://core.telegram.org/bots/api#writeaccessallowed
Snapshot: 2026-11-23T12:52:14Z

#### WriteAccessAllowed

This object represents a service message about a user allowing a bot to write messages after adding it to the attachment menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method [requestWriteAccess](https://core.telegram.org/bots/webapps#initializing-mini-apps), or about a user being invited to the private chat with the bot by the owner of the bot.

| Field | Type | Description |
| --- | --- | --- |
| from_request | Boolean | *Optional*. *True*, if the access was granted after the user accepted an explicit request from a Web App sent by the method [requestWriteAccess](https://core.telegram.org/bots/webapps#initializing-mini-apps) |
| web_app_name | String | *Optional*. Name of the Web App, if the access was granted when the Web App was launched from a link |
| from_attachment_menu | Boolean | *Optional*. *True*, if the access was granted when the bot was added to the attachment or side menu |
| inviter | [User](https://core.telegram.org/bots/api#user) | *Optional*. The owner of the bot, if the access was granted when the owner invited the user to the private chat with the bot. Bot owners can invite up to 10 users at once by pressing the link `https://t.me/botinvite/<bot_username>`. |