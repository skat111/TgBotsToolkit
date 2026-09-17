Source: https://core.telegram.org/bots/api#transactionpartneruser
Snapshot: 2026-09-17T08:42:18Z

#### TransactionPartnerUser

Describes a transaction with a user.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the transaction partner, always “user” |
| transaction_type | String | Type of the transaction, currently one of “invoice_payment” for payments via invoices, “paid_media_payment” for payments for paid media, “gift_purchase” for gifts sent by the bot, “premium_purchase” for Telegram Premium subscriptions gifted by the bot, “business_account_transfer” for direct transfers from managed business accounts |
| user | [User](https://core.telegram.org/bots/api#user) | Information about the user |
| affiliate | [AffiliateInfo](https://core.telegram.org/bots/api#affiliateinfo) | *Optional*. Information about the affiliate that received a commission via this transaction. Can be available only for “invoice_payment” and “paid_media_payment” transactions. |
| invoice_payload | String | *Optional*. Bot-specified invoice payload. Can be available only for “invoice_payment” transactions. |
| subscription_period | Integer | *Optional*. The duration of the paid subscription. Can be available only for “invoice_payment” transactions. |
| paid_media | Array of [PaidMedia](https://core.telegram.org/bots/api#paidmedia) | *Optional*. Information about the paid media bought by the user; for “paid_media_payment” transactions only |
| paid_media_payload | String | *Optional*. Bot-specified paid media payload. Can be available only for “paid_media_payment” transactions. |
| gift | [Gift](https://core.telegram.org/bots/api#gift) | *Optional*. The gift sent to the user by the bot; for “gift_purchase” transactions only |
| premium_subscription_duration | Integer | *Optional*. Number of months the gifted Telegram Premium subscription will be active for; for “premium_purchase” transactions only |