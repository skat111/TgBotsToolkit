Source: https://core.telegram.org/bots/api#businessconnection
Snapshot: 2026-09-26T08:38:44Z

#### BusinessConnection

Describes the connection of the bot with a business account.

| Field | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the business connection |
| user | [User](https://core.telegram.org/bots/api#user) | Business account user that created the business connection |
| user_chat_id | Integer | Identifier of a private chat with the user who created the business connection. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. |
| date | Integer | Date the connection was established in Unix time |
| rights | [BusinessBotRights](https://core.telegram.org/bots/api#businessbotrights) | *Optional*. Rights of the business bot |
| is_enabled | Boolean | *True*, if the connection is active |