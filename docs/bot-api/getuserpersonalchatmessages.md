Source: https://core.telegram.org/bots/api#getuserpersonalchatmessages
Snapshot: 2026-09-23T08:37:58Z

#### getUserPersonalChatMessages

Use this method to get the last messages from the personal chat (i.e., the chat currently added to their profile) of a given user. On success, an Array of [Message](https://core.telegram.org/bots/api#message) objects is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | Integer | Yes | Unique identifier for the target user |
| limit | Integer | Yes | The maximum number of messages to return; 1-20 |