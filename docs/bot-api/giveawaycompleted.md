Source: https://core.telegram.org/bots/api#giveawaycompleted
Snapshot: 2026-09-23T08:37:58Z

#### GiveawayCompleted

This object represents a service message about the completion of a giveaway without public winners.

| Field | Type | Description |
| --- | --- | --- |
| winner_count | Integer | Number of winners in the giveaway |
| unclaimed_prize_count | Integer | *Optional*. Number of undistributed prizes |
| giveaway_message | [Message](https://core.telegram.org/bots/api#message) | *Optional*. Message with the giveaway that was completed, if it wasn't deleted |
| is_star_giveaway | True | *Optional*. *True*, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway. |