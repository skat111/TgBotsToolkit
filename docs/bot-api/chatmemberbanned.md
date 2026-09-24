Source: https://core.telegram.org/bots/api#chatmemberbanned
Snapshot: 2026-09-24T08:30:39Z

#### ChatMemberBanned

Represents a [chat member](https://core.telegram.org/bots/api#chatmember) that was banned in the chat and can't return to the chat or view chat messages.

| Field | Type | Description |
| --- | --- | --- |
| status | String | The member's status in the chat, always “kicked” |
| user | [User](https://core.telegram.org/bots/api#user) | Information about the user |
| until_date | Integer | Date when restrictions will be lifted for this user; Unix time. If 0, then the user is banned forever. |