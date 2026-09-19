Source: https://core.telegram.org/bots/api#sendchecklist
Snapshot: 2026-09-19T08:05:57Z

#### sendChecklist

Use this method to send a checklist on behalf of a connected business account. On success, the sent [Message](https://core.telegram.org/bots/api#message) is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Yes | Unique identifier of the business connection on behalf of which the message will be sent |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot in the format `@username` |
| checklist | [InputChecklist](https://core.telegram.org/bots/api#inputchecklist) | Yes | A JSON-serialized object for the checklist to send |
| disable_notification | Boolean | Optional | Sends the message silently. Users will receive a notification with no sound. |
| protect_content | Boolean | Optional | Protects the contents of the sent message from forwarding and saving |
| message_effect_id | String | Optional | Unique identifier of the message effect to be added to the message |
| reply_parameters | [ReplyParameters](https://core.telegram.org/bots/api#replyparameters) | Optional | A JSON-serialized object for description of the message to reply to |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | Optional | A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) |