Source: https://core.telegram.org/bots/api#chatjoinrequest
Snapshot: 2026-09-19T08:05:57Z

#### ChatJoinRequest

Represents a join request sent to a chat.

| Field | Type | Description |
| --- | --- | --- |
| chat | [Chat](https://core.telegram.org/bots/api#chat) | Chat to which the request was sent |
| from | [User](https://core.telegram.org/bots/api#user) | User that sent the join request |
| user_chat_id | Integer | Identifier of a private chat with the user who sent the join request. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot can use this identifier for 5 minutes to send messages until the join request is processed, assuming no other administrator contacted the user. |
| date | Integer | Date the request was sent in Unix time |
| bio | String | *Optional*. Bio of the user |
| invite_link | [ChatInviteLink](https://core.telegram.org/bots/api#chatinvitelink) | *Optional*. Chat invite link that was used by the user to send the join request |
| query_id | String | *Optional*. Identifier of the join request query; for bots assigned to process join requests only. If present, then the bot must call [sendChatJoinRequestWebApp](https://core.telegram.org/bots/api#sendchatjoinrequestwebapp) or directly call [answerChatJoinRequestQuery](https://core.telegram.org/bots/api#answerchatjoinrequestquery) within 10 seconds. |