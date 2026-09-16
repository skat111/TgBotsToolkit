Source: https://core.telegram.org/bots/api#answershippingquery
Snapshot: 2026-09-16T08:38:32Z

#### answerShippingQuery

If you sent an invoice requesting a shipping address and the parameter *is_flexible* was specified, the Bot API will send an [Update](https://core.telegram.org/bots/api#update) with a *shipping_query* field to the bot. Use this method to reply to shipping queries. On success, *True* is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| shipping_query_id | String | Yes | Unique identifier for the query to be answered |
| ok | Boolean | Yes | Pass *True* if delivery to the specified address is possible and *False* if there are any problems (for example, if delivery to the specified address is not possible) |
| shipping_options | Array of [ShippingOption](https://core.telegram.org/bots/api#shippingoption) | Optional | Required if *ok* is *True*. A JSON-serialized Array of available shipping options. |
| error_message | String | Optional | Required if *ok* is *False*. Error message in human readable form that explains why it is impossible to complete the order (e.g. “Sorry, delivery to your desired address is unavailable”). Telegram will display this message to the user. |