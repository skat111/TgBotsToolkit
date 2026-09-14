Source: https://core.telegram.org/bots/api#messageoriginuser
Snapshot: 2026-09-14T08:59:05Z

#### MessageOriginUser

The message was originally sent by a known user.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the message origin, always “user” |
| date | Integer | Date the message was sent originally in Unix time |
| sender_user | [User](https://core.telegram.org/bots/api#user) | User that sent the message originally |