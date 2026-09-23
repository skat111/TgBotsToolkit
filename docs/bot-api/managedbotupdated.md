Source: https://core.telegram.org/bots/api#managedbotupdated
Snapshot: 2026-09-23T08:37:58Z

#### ManagedBotUpdated

This object contains information about the creation, token update, or owner update of a bot that is managed by the current bot.

| Field | Type | Description |
| --- | --- | --- |
| user | [User](https://core.telegram.org/bots/api#user) | User that created the bot |
| bot | [User](https://core.telegram.org/bots/api#user) | Information about the bot. Token of the bot can be fetched using the method [getManagedBotToken](https://core.telegram.org/bots/api#getmanagedbottoken). |