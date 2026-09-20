Source: https://core.telegram.org/bots/api#choseninlineresult
Snapshot: 2026-09-20T08:38:20Z

#### ChosenInlineResult

Represents a [result](https://core.telegram.org/bots/api#inlinequeryresult) of an inline query that was chosen by the user and sent to their chat partner.

| Field | Type | Description |
| --- | --- | --- |
| result_id | String | The unique identifier for the result that was chosen |
| from | [User](https://core.telegram.org/bots/api#user) | The user that chose the result |
| location | [Location](https://core.telegram.org/bots/api#location) | *Optional*. Sender location, only for bots that require user location |
| inline_message_id | String | *Optional*. Identifier of the sent inline message. Available only if there is an [inline keyboard](https://core.telegram.org/bots/api#inlinekeyboardmarkup) attached to the message. Will be also received in [callback queries](https://core.telegram.org/bots/api#callbackquery) and can be used to [edit](https://core.telegram.org/bots/api#updating-messages) the message. |
| query | String | The query that was used to obtain the result |

**Note:** It is necessary to enable [inline feedback](https://core.telegram.org/bots/inline#collecting-feedback) via [@BotFather](https://t.me/botfather) in order to receive these objects in updates.