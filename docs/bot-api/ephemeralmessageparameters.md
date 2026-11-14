Source: https://core.telegram.org/bots/api#ephemeralmessageparameters
Snapshot: 2026-11-14T10:30:31Z

#### EphemeralMessageParameters

| Field | Type | Description |
| --- | --- | --- |
| receiver_user_id | Integer | *Optional*. Identifier of the user who will receive the message; required unless the message is sent as an ephemeral reply to a callback query. If omitted, then the parameter *chat_id* of the method is ignored. If specified together with *callback_query_id*, then it must be the identifier of the user who pressed the button. Must be omitted for messages sent in chats where the bot isn't a member, unless the message is a reply to an ephemeral message. It is not guaranteed that the user will receive the message, especially if they are offline. See [here](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details. |
| callback_query_id | String | *Optional*. Identifier of the callback query which triggered the message, if any. If specified and *receiver_user_id* is omitted, then the message is sent as an ephemeral reply to the callback query and will be shown only to the user who pressed the button. Ephemeral replies can't be sent to callback queries from messages in channel direct messages chats. The bot must still answer the callback query using [answerCallbackQuery](https://core.telegram.org/bots/api#answercallbackquery). |
| replace_callback_query_message | Boolean | *Optional*. Pass *True* if the ephemeral message must be shown in place of the original message. Must be *False* for callback queries from ephemeral messages, which must be edited using regular *editEphemeralMessage…* methods. |