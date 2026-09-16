Source: https://core.telegram.org/bots/api#precheckoutquery
Snapshot: 2026-09-16T08:38:32Z

#### PreCheckoutQuery

This object contains information about an incoming pre-checkout query.

| Field | Type | Description |
| --- | --- | --- |
| id | String | Unique query identifier |
| from | [User](https://core.telegram.org/bots/api#user) | User who sent the query |
| currency | String | Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90) |
| total_amount | Integer | Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). |
| invoice_payload | String | Bot-specified invoice payload |
| shipping_option_id | String | *Optional*. Identifier of the shipping option chosen by the user |
| order_info | [OrderInfo](https://core.telegram.org/bots/api#orderinfo) | *Optional*. Order information provided by the user |