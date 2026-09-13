Source: https://core.telegram.org/bots/api#affiliateinfo
Snapshot: 2026-09-13T08:21:39Z

#### AffiliateInfo

Contains information about the affiliate that received a commission via this transaction.

| Field | Type | Description |
| --- | --- | --- |
| affiliate_user | [User](https://core.telegram.org/bots/api#user) | *Optional*. The bot or the user that received an affiliate commission if it was received by a bot or a user |
| affiliate_chat | [Chat](https://core.telegram.org/bots/api#chat) | *Optional*. The chat that received an affiliate commission if it was received by a chat |
| commission_per_mille | Integer | The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by the bot from referred users |
| amount | Integer | Integer amount of Telegram Stars received by the affiliate from the transaction, rounded to 0; can be negative for refunds |
| nanostar_amount | Integer | *Optional*. The number of 1/1000000000 shares of Telegram Stars received by the affiliate; from -999999999 to 999999999; can be negative for refunds |