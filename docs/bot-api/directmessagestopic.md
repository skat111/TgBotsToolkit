Source: https://core.telegram.org/bots/api#directmessagestopic
Snapshot: 2026-09-26T08:38:44Z

#### DirectMessagesTopic

Describes a topic of a direct messages chat.

| Field | Type | Description |
| --- | --- | --- |
| topic_id | Integer | Unique identifier of the topic. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. |
| user | [User](https://core.telegram.org/bots/api#user) | *Optional*. Information about the user that created the topic. Currently, it is always present. |