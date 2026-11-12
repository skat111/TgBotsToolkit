Source: https://core.telegram.org/bots/api#widgetquerytypesenttransaction
Snapshot: 2026-11-12T11:19:03Z

#### WidgetQueryTypeSentTransaction

The query notifies the bot about a transaction sent from a TON wallet of the user who sent the query.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the query, always “sent_transaction” |
| wallet | [WidgetQueryWallet](https://core.telegram.org/bots/api#widgetquerywallet) | The wallet from which the transaction was sent |
| msg_hash | String | Value of *msg_hash* of the transaction |