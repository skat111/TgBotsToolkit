Source: https://core.telegram.org/bots/api#setchatphoto
Snapshot: 2026-09-18T08:17:54Z

#### setChatPhoto

Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target channel in the format `@username` |
| photo | [InputFile](https://core.telegram.org/bots/api#inputfile) | Yes | New chat photo, uploaded using multipart/form-data |