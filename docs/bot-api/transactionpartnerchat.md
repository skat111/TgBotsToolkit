Source: https://core.telegram.org/bots/api#transactionpartnerchat
Snapshot: 2026-09-12T07:57:24Z

#### TransactionPartnerChat

Describes a transaction with a chat.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the transaction partner, always “chat” |
| chat | [Chat](https://core.telegram.org/bots/api#chat) | Information about the chat |
| gift | [Gift](https://core.telegram.org/bots/api#gift) | *Optional*. The gift sent to the chat by the bot |