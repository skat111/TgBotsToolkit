Source: https://core.telegram.org/bots/api#labeledprice
Snapshot: 2026-09-22T08:35:37Z

#### LabeledPrice

This object represents a portion of the price for goods or services.

| Field | Type | Description |
| --- | --- | --- |
| label | String | Portion label |
| amount | Integer | Price of the product in the *smallest units* of the [currency](https://core.telegram.org/bots/payments#supported-currencies) (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). |