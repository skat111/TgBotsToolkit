Source: https://core.telegram.org/bots/api#suggestedpostapprovalfailed
Snapshot: 2026-09-26T08:38:44Z

#### SuggestedPostApprovalFailed

Describes a service message about the failed approval of a suggested post. Currently, only caused by insufficient user funds at the time of approval.

| Field | Type | Description |
| --- | --- | --- |
| suggested_post_message | [Message](https://core.telegram.org/bots/api#message) | *Optional*. Message containing the suggested post whose approval has failed. Note that the [Message](https://core.telegram.org/bots/api#message) object in this field will not contain the *reply_to_message* field even if it itself is a reply. |
| price | [SuggestedPostPrice](https://core.telegram.org/bots/api#suggestedpostprice) | Expected price of the post |