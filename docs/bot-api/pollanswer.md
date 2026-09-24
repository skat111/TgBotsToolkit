Source: https://core.telegram.org/bots/api#pollanswer
Snapshot: 2026-09-24T08:30:39Z

#### PollAnswer

This object represents an answer of a user in a non-anonymous poll.

| Field | Type | Description |
| --- | --- | --- |
| poll_id | String | Unique poll identifier |
| voter_chat | [Chat](https://core.telegram.org/bots/api#chat) | *Optional*. The chat that changed the answer to the poll, if the voter is anonymous |
| user | [User](https://core.telegram.org/bots/api#user) | *Optional*. The user that changed the answer to the poll, if the voter isn't anonymous |
| option_ids | Array of Integer | 0-based identifiers of chosen answer options. May be empty if the vote was retracted. |
| option_persistent_ids | Array of String | Persistent identifiers of the chosen answer options. May be empty if the vote was retracted. |