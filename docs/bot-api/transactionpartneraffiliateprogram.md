Source: https://core.telegram.org/bots/api#transactionpartneraffiliateprogram
Snapshot: 2026-09-20T08:38:20Z

#### TransactionPartnerAffiliateProgram

Describes the affiliate program that issued the affiliate commission received via this transaction.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the transaction partner, always “affiliate_program” |
| sponsor_user | [User](https://core.telegram.org/bots/api#user) | *Optional*. Information about the bot that sponsored the affiliate program |
| commission_per_mille | Integer | The number of Telegram Stars received by the bot for each 1000 Telegram Stars received by the affiliate program sponsor from referred users |