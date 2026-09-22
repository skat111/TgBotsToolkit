Source: https://core.telegram.org/bots/api#inputinvoicemessagecontent
Snapshot: 2026-09-22T08:35:37Z

#### InputInvoiceMessageContent

Represents the [content](https://core.telegram.org/bots/api#inputmessagecontent) of an invoice message to be sent as the result of an inline query.

| Field | Type | Description |
| --- | --- | --- |
| title | String | Product name, 1-32 characters |
| description | String | Product description, 1-255 characters |
| payload | String | Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes. |
| provider_token | String | *Optional*. Payment provider token, obtained via [@BotFather](https://t.me/botfather). Pass an empty string for payments in [Telegram Stars](https://t.me/BotNews/90). |
| currency | String | Three-letter ISO 4217 currency code, see [more on currencies](https://core.telegram.org/bots/payments#supported-currencies). Pass “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90). |
| prices | Array of [LabeledPrice](https://core.telegram.org/bots/api#labeledprice) | Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in [Telegram Stars](https://t.me/BotNews/90). |
| max_tip_amount | Integer | *Optional*. The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of `US$ 1.45` pass `max_tip_amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in [Telegram Stars](https://t.me/BotNews/90). |
| suggested_tip_amounts | Array of Integer | *Optional*. A JSON-serialized Array of suggested amounts of tip in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max_tip_amount*. |
| provider_data | String | *Optional*. A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider. |
| photo_url | String | *Optional*. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. |
| photo_size | Integer | *Optional*. Photo size in bytes |
| photo_width | Integer | *Optional*. Photo width |
| photo_height | Integer | *Optional*. Photo height |
| need_name | Boolean | *Optional*. Pass *True* if you require the user's full name to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90). |
| need_phone_number | Boolean | *Optional*. Pass *True* if you require the user's phone number to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90). |
| need_email | Boolean | *Optional*. Pass *True* if you require the user's email address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90). |
| need_shipping_address | Boolean | *Optional*. Pass *True* if you require the user's shipping address to complete the order. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90). |
| send_phone_number_to_provider | Boolean | *Optional*. Pass *True* if the user's phone number should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90). |
| send_email_to_provider | Boolean | *Optional*. Pass *True* if the user's email address should be sent to the provider. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90). |
| is_flexible | Boolean | *Optional*. Pass *True* if the final price depends on the shipping method. Ignored for payments in [Telegram Stars](https://t.me/BotNews/90). |