Source: https://core.telegram.org/bots/api#shippingquery
Snapshot: 2026-09-15T08:44:15Z

#### ShippingQuery

This object contains information about an incoming shipping query.

| Field | Type | Description |
| --- | --- | --- |
| id | String | Unique query identifier |
| from | [User](https://core.telegram.org/bots/api#user) | User who sent the query |
| invoice_payload | String | Bot-specified invoice payload |
| shipping_address | [ShippingAddress](https://core.telegram.org/bots/api#shippingaddress) | User specified shipping address |