Source: https://core.telegram.org/bots/api#getchatadministrators
Snapshot: 2026-09-17T08:42:18Z

#### getChatAdministrators

Use this method to get a list of administrators in a chat. Returns an Array of [ChatMember](https://core.telegram.org/bots/api#chatmember) objects.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup or channel in the format `@username` |
| return_bots | Boolean | Optional | Pass *True* to additionally receive all bots that are administrators of the chat. By default, bots other than the current bot are omitted. |