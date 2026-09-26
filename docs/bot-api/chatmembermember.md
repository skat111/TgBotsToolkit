Source: https://core.telegram.org/bots/api#chatmembermember
Snapshot: 2026-09-26T08:38:44Z

#### ChatMemberMember

Represents a [chat member](https://core.telegram.org/bots/api#chatmember) that has no additional privileges or restrictions.

| Field | Type | Description |
| --- | --- | --- |
| status | String | The member's status in the chat, always “member” |
| tag | String | *Optional*. Tag of the member |
| user | [User](https://core.telegram.org/bots/api#user) | Information about the user |
| until_date | Integer | *Optional*. Date when the user's subscription will expire; Unix time |