Source: https://core.telegram.org/bots/api#polloption
Snapshot: 2026-09-24T08:30:39Z

#### PollOption

This object contains information about one answer option in a poll.

| Field | Type | Description |
| --- | --- | --- |
| persistent_id | String | Unique identifier of the option, persistent on option addition and deletion |
| text | String | Option text, 1-100 characters |
| text_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. Special entities that appear in the option *text*. Currently, only custom emoji entities are allowed in poll option texts |
| media | [PollMedia](https://core.telegram.org/bots/api#pollmedia) | *Optional*. Media added to the poll option |
| voter_count | Integer | Number of users who voted for this option; may be 0 if unknown |
| added_by_user | [User](https://core.telegram.org/bots/api#user) | *Optional*. User who added the option; omitted if the option wasn't added by a user after poll creation |
| added_by_chat | [Chat](https://core.telegram.org/bots/api#chat) | *Optional*. Chat that added the option; omitted if the option wasn't added by a chat after poll creation |
| addition_date | Integer | *Optional*. Point in time (Unix timestamp) when the option was added; omitted if the option existed in the original poll |