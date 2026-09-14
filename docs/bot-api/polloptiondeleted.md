Source: https://core.telegram.org/bots/api#polloptiondeleted
Snapshot: 2026-09-14T08:59:05Z

#### PollOptionDeleted

Describes a service message about an option deleted from a poll.

| Field | Type | Description |
| --- | --- | --- |
| poll_message | [MaybeInaccessibleMessage](https://core.telegram.org/bots/api#maybeinaccessiblemessage) | *Optional*. Message containing the poll from which the option was deleted, if known. Note that the [Message](https://core.telegram.org/bots/api#message) object in this field will not contain the *reply_to_message* field even if it itself is a reply. |
| option_persistent_id | String | Unique identifier of the deleted option |
| option_text | String | Option text |
| option_text_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. Special entities that appear in the *option_text* |