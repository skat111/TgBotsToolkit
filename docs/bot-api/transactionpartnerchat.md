Source: https://core.telegram.org/bots/api#transactionpartnerchat
Snapshot: 2026-11-17T11:56:55Z

#### TransactionPartnerChat

Describes a transaction with a chat.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the transaction partner, always “chat” |
| chat | [Chat](https://core.telegram.org/bots/api#chat) | Information about the chat |
| gift | [Gift](https://core.telegram.org/bots/api#gift) | *Optional*. The gift sent to the chat by the bot |