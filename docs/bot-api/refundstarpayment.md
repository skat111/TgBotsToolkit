Source: https://core.telegram.org/bots/api#refundstarpayment
Snapshot: 2026-09-25T08:52:18Z

#### refundStarPayment

Refunds a successful payment in [Telegram Stars](https://t.me/BotNews/90). Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | Integer | Yes | Identifier of the user whose payment will be refunded |
| telegram_payment_charge_id | String | Yes | Telegram payment identifier |