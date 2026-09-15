Source: https://core.telegram.org/bots/api#suggestedpostrefunded
Snapshot: 2026-09-15T08:44:15Z

#### SuggestedPostRefunded

Describes a service message about a payment refund for a suggested post.

| Field | Type | Description |
| --- | --- | --- |
| suggested_post_message | [Message](https://core.telegram.org/bots/api#message) | *Optional*. Message containing the suggested post. Note that the [Message](https://core.telegram.org/bots/api#message) object in this field will not contain the *reply_to_message* field even if it itself is a reply. |
| reason | String | Reason for the refund. Currently, one of “post_deleted” if the post was deleted within 24 hours of being posted or removed from scheduled messages without being posted, or “payment_refunded” if the payer refunded their payment. |