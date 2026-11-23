Source: https://core.telegram.org/bots/api#choseninlineresult
Snapshot: 2026-11-23T12:52:14Z

#### ChosenInlineResult

Represents a [result](https://core.telegram.org/bots/api#inlinequeryresult) of an inline query that was chosen by the user and sent to their chat partner.

| Field | Type | Description |
| --- | --- | --- |
| result_id | String | The unique identifier for the result that was chosen |
| from | [User](https://core.telegram.org/bots/api#user) | The user that chose the result |
| location | [Location](https://core.telegram.org/bots/api#location) | *Optional*. Sender location, only for bots that enabled user location requests via [@BotFather](https://t.me/botfather) or using the parameter *needs_inline_query_location* of the method [setMySettings](https://core.telegram.org/bots/api#setmysettings) |
| inline_message_id | String | *Optional*. Identifier of the sent inline message. Available only if there is an [inline keyboard](https://core.telegram.org/bots/api#inlinekeyboardmarkup) attached to the message. Will be also received in [callback queries](https://core.telegram.org/bots/api#callbackquery) and can be used to [edit](https://core.telegram.org/bots/api#updating-messages) the message. |
| query | String | The query that was used to obtain the result |

**Note:** It is necessary to enable [inline feedback](https://core.telegram.org/bots/inline#collecting-feedback) via [@BotFather](https://t.me/botfather) or using the parameter *inline_feedback_share_denominator* of the method [setMySettings](https://core.telegram.org/bots/api#setmysettings) in order to receive these objects in updates.