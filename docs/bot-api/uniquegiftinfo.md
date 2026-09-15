Source: https://core.telegram.org/bots/api#uniquegiftinfo
Snapshot: 2026-09-15T08:44:15Z

#### UniqueGiftInfo

Describes a service message about a unique gift that was sent or received.

| Field | Type | Description |
| --- | --- | --- |
| gift | [UniqueGift](https://core.telegram.org/bots/api#uniquegift) | Information about the gift |
| origin | String | Origin of the gift. Currently, either “upgrade” for gifts upgraded from regular gifts, “transfer” for gifts transferred from other users or channels, “resale” for gifts bought from other users, “gifted_upgrade” for upgrades purchased after the gift was sent, or “offer” for gifts bought or sold through gift purchase offers. |
| text | String | *Optional*. Text of the message that was added to the gift |
| entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. Special entities that appear in the text |
| is_private | True | *Optional*. *True*, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them |
| last_resale_currency | String | *Optional*. For gifts bought from other users, the currency in which the payment for the gift was done. Currently, one of “XTR” for Telegram Stars or “TON” for TON grams. |
| last_resale_amount | Integer | *Optional*. For gifts bought from other users, the price paid for the gift in either Telegram Stars or nanograms |
| owned_gift_id | String | *Optional*. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts |
| transfer_star_count | Integer | *Optional*. Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift |
| next_transfer_date | Integer | *Optional*. Point in time (Unix timestamp) when the gift can be transferred. If it is in the past, then the gift can be transferred now. |