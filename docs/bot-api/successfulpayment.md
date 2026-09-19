Source: https://core.telegram.org/bots/api#successfulpayment
Snapshot: 2026-09-19T08:05:57Z

#### SuccessfulPayment

This object contains basic information about a successful payment. Note that if the buyer initiates a chargeback with the relevant payment provider following this transaction, the funds may be debited from your balance. This is outside of Telegram's control.

| Field | Type | Description |
| --- | --- | --- |
| currency | String | Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90) |
| total_amount | Integer | Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). |
| invoice_payload | String | Bot-specified invoice payload |
| subscription_expiration_date | Integer | *Optional*. Expiration date of the subscription, in Unix time; for recurring payments only |
| is_recurring | True | *Optional*. *True*, if the payment is a recurring payment for a subscription |
| is_first_recurring | True | *Optional*. *True*, if the payment is the first payment for a subscription |
| shipping_option_id | String | *Optional*. Identifier of the shipping option chosen by the user |
| order_info | [OrderInfo](https://core.telegram.org/bots/api#orderinfo) | *Optional*. Order information provided by the user |
| telegram_payment_charge_id | String | Telegram payment identifier |
| provider_payment_charge_id | String | Provider payment identifier |