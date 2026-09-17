Source: https://core.telegram.org/bots/api#suggestedpostdeclined
Snapshot: 2026-09-17T08:42:18Z

#### SuggestedPostDeclined

Describes a service message about the rejection of a suggested post.

| Field | Type | Description |
| --- | --- | --- |
| suggested_post_message | [Message](https://core.telegram.org/bots/api#message) | *Optional*. Message containing the suggested post. Note that the [Message](https://core.telegram.org/bots/api#message) object in this field will not contain the *reply_to_message* field even if it itself is a reply. |
| comment | String | *Optional*. Comment with which the post was declined |