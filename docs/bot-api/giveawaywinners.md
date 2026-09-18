Source: https://core.telegram.org/bots/api#giveawaywinners
Snapshot: 2026-09-18T08:17:54Z

#### GiveawayWinners

This object represents a message about the completion of a giveaway with public winners.

| Field | Type | Description |
| --- | --- | --- |
| chat | [Chat](https://core.telegram.org/bots/api#chat) | The chat that created the giveaway |
| giveaway_message_id | Integer | Identifier of the message with the giveaway in the chat |
| winners_selection_date | Integer | Point in time (Unix timestamp) when winners of the giveaway were selected |
| winner_count | Integer | Total number of winners in the giveaway |
| winners | Array of [User](https://core.telegram.org/bots/api#user) | List of up to 100 winners of the giveaway |
| additional_chat_count | Integer | *Optional*. The number of other chats the user had to join in order to be eligible for the giveaway |
| prize_star_count | Integer | *Optional*. The number of Telegram Stars that were split between giveaway winners; for Telegram Star giveaways only |
| premium_subscription_month_count | Integer | *Optional*. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only |
| unclaimed_prize_count | Integer | *Optional*. Number of undistributed prizes |
| only_new_members | True | *Optional*. *True*, if only users who had joined the chats after the giveaway started were eligible to win |
| was_refunded | True | *Optional*. *True*, if the giveaway was canceled because the payment for it was refunded |
| prize_description | String | *Optional*. Description of additional giveaway prize |