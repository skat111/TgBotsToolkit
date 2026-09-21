Source: https://core.telegram.org/bots/api#polloptionadded
Snapshot: 2026-09-21T09:00:24Z

#### PollOptionAdded

Describes a service message about an option added to a poll.

| Field | Type | Description |
| --- | --- | --- |
| poll_message | [MaybeInaccessibleMessage](https://core.telegram.org/bots/api#maybeinaccessiblemessage) | *Optional*. Message containing the poll to which the option was added, if known. Note that the [Message](https://core.telegram.org/bots/api#message) object in this field will not contain the *reply_to_message* field even if it itself is a reply. |
| option_persistent_id | String | Unique identifier of the added option |
| option_text | String | Option text |
| option_text_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. Special entities that appear in the *option_text* |