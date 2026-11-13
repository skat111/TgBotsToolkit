Source: https://core.telegram.org/bots/api#tonwallettransfer
Snapshot: 2026-11-13T11:03:46Z

#### TonWalletTransfer

Describes a service message about a transfer with a TON wallet.

| Field | Type | Description |
| --- | --- | --- |
| transaction_id | String | Unique identifier of the transaction; may be empty if the transfer hasn't been sent yet |
| peer_address | String | Address of the transfer peer in the TON blockchain |
| amount | String | The amount of transferred cryptocurrency, in the *smallest units* of the cryptocurrency, as a decimal number; negative for outgoing transfers |
| comment | String | *Optional*. Comment added to the transfer; omitted if the comment is encrypted |