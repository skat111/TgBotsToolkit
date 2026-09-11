Source: https://core.telegram.org/bots/api#stopmessagelivelocation
Snapshot: 2026-09-11T06:04:42Z

#### stopMessageLiveLocation

Use this method to stop updating a live location message before *live_period* expires. On success, if the message is not an inline message, the edited [Message](https://core.telegram.org/bots/api#message) is returned, otherwise *True* is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Optional | Unique identifier of the business connection on behalf of which the message to be edited was sent |
| chat_id | Integer or String | Optional | Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`. |
| message_id | Integer | Optional | Required if *inline_message_id* is not specified. Identifier of the message with live location to stop. |
| inline_message_id | String | Optional | Required if *chat_id* and *message_id* are not specified. Identifier of the inline message. |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | Optional | A JSON-serialized object for a new [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) |