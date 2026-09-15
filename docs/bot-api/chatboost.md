Source: https://core.telegram.org/bots/api#chatboost
Snapshot: 2026-09-15T08:44:15Z

#### ChatBoost

This object contains information about a chat boost.

| Field | Type | Description |
| --- | --- | --- |
| boost_id | String | Unique identifier of the boost |
| add_date | Integer | Point in time (Unix timestamp) when the chat was boosted |
| expiration_date | Integer | Point in time (Unix timestamp) when the boost will automatically expire, unless the booster's Telegram Premium subscription is prolonged |
| source | [ChatBoostSource](https://core.telegram.org/bots/api#chatboostsource) | Source of the added boost |