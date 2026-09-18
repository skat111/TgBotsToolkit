Source: https://core.telegram.org/bots/api#keyboardbuttonrequestmanagedbot
Snapshot: 2026-09-18T08:17:54Z

#### KeyboardButtonRequestManagedBot

This object defines the parameters for the creation of a managed bot. Information about the created bot will be shared with the bot using the update *managed_bot* and a [Message](https://core.telegram.org/bots/api#message) with the field *managed_bot_created*.

| Field | Type | Description |
| --- | --- | --- |
| request_id | Integer | Signed 32-bit identifier of the request. Must be unique within the message. |
| suggested_name | String | *Optional*. Suggested name for the bot |
| suggested_username | String | *Optional*. Suggested username for the bot |