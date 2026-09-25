Source: https://core.telegram.org/bots/api#ephemeralmessageparameters
Snapshot: 2026-09-25T08:52:18Z

#### EphemeralMessageParameters

| Field | Type | Description |
| --- | --- | --- |
| receiver_user_id | Integer | Identifier of the user who will receive the message. It is not guaranteed that the user will receive the message, especially if they are offline. See [here](https://core.telegram.org/bots/api#ephemeral-messages-and-commands) for more details. |
| callback_query_id | String | *Optional*. Identifier of the callback query which triggered the message, if any |
| replace_callback_query_message | Boolean | *Optional*. Pass *True* if the ephemeral message must be shown in place of the original message. Must be *False* for callback queries from ephemeral messages, which must be edited using regular *editEphemeralMessage…* methods. |