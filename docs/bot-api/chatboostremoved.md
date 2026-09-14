Source: https://core.telegram.org/bots/api#chatboostremoved
Snapshot: 2026-09-14T08:59:05Z

#### ChatBoostRemoved

This object represents a boost removed from a chat.

| Field | Type | Description |
| --- | --- | --- |
| chat | [Chat](https://core.telegram.org/bots/api#chat) | Chat which was boosted |
| boost_id | String | Unique identifier of the boost |
| remove_date | Integer | Point in time (Unix timestamp) when the boost was removed |
| source | [ChatBoostSource](https://core.telegram.org/bots/api#chatboostsource) | Source of the removed boost |