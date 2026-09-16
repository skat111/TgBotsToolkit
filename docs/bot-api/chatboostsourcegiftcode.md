Source: https://core.telegram.org/bots/api#chatboostsourcegiftcode
Snapshot: 2026-09-16T08:38:32Z

#### ChatBoostSourceGiftCode

The boost was obtained by the creation of Telegram Premium gift codes to boost a chat. Each such code boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Source of the boost, always “gift_code” |
| user | [User](https://core.telegram.org/bots/api#user) | User for which the gift code was created |