Source: https://core.telegram.org/bots/api#suggestedpostapproved
Snapshot: 2026-09-15T08:44:15Z

#### SuggestedPostApproved

Describes a service message about the approval of a suggested post.

| Field | Type | Description |
| --- | --- | --- |
| suggested_post_message | [Message](https://core.telegram.org/bots/api#message) | *Optional*. Message containing the suggested post. Note that the [Message](https://core.telegram.org/bots/api#message) object in this field will not contain the *reply_to_message* field even if it itself is a reply. |
| price | [SuggestedPostPrice](https://core.telegram.org/bots/api#suggestedpostprice) | *Optional*. Amount paid for the post |
| send_date | Integer | Date when the post will be published |