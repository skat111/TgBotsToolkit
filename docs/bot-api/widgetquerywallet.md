Source: https://core.telegram.org/bots/api#widgetquerywallet
Snapshot: 2026-11-14T10:30:31Z

#### WidgetQueryWallet

This object describes a TON wallet of the user, which is used in a query from a widget.

| Field | Type | Description |
| --- | --- | --- |
| address | String | Address of the wallet |
| amount | String | Balance of the wallet, in the *smallest units* of the cryptocurrency, as a decimal number |
| public_key | String | *Optional*. Hex-encoded public key of the wallet; omitted if unknown |
| state_init | String | *Optional*. Base64-encoded serialized StateInit of the wallet contract; omitted if and only if *public_key* is omitted |