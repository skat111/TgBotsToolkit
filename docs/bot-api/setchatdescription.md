Source: https://core.telegram.org/bots/api#setchatdescription
Snapshot: 2026-09-26T08:38:44Z

#### setChatDescription

Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target channel in the format `@username` |
| description | String | Optional | New chat description, 0-255 characters |