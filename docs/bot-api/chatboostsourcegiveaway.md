Source: https://core.telegram.org/bots/api#chatboostsourcegiveaway
Snapshot: 2026-09-18T08:17:54Z

#### ChatBoostSourceGiveaway

The boost was obtained by the creation of a Telegram Premium or a Telegram Star giveaway. This boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription for Telegram Premium giveaways and *prize_star_count* / 500 times for one year for Telegram Star giveaways.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Source of the boost, always “giveaway” |
| giveaway_message_id | Integer | Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn't sent yet. |
| user | [User](https://core.telegram.org/bots/api#user) | *Optional*. User that won the prize in the giveaway if any; for Telegram Premium giveaways only |
| prize_star_count | Integer | *Optional*. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only |
| is_unclaimed | True | *Optional*. *True*, if the giveaway was completed, but there was no user to win the prize |