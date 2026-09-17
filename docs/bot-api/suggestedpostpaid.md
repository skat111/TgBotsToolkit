Source: https://core.telegram.org/bots/api#suggestedpostpaid
Snapshot: 2026-09-17T08:42:18Z

#### SuggestedPostPaid

Describes a service message about a successful payment for a suggested post.

| Field | Type | Description |
| --- | --- | --- |
| suggested_post_message | [Message](https://core.telegram.org/bots/api#message) | *Optional*. Message containing the suggested post. Note that the [Message](https://core.telegram.org/bots/api#message) object in this field will not contain the *reply_to_message* field even if it itself is a reply. |
| currency | String | Currency in which the payment was made. Currently, one of “XTR” for Telegram Stars or “TON” for TON grams. |
| amount | Integer | *Optional*. The amount of the currency that was received by the channel in nanograms; for payments in TON grams only |
| star_amount | [StarAmount](https://core.telegram.org/bots/api#staramount) | *Optional*. The amount of Telegram Stars that was received by the channel; for payments in Telegram Stars only |