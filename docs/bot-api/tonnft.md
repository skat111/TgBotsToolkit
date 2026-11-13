Source: https://core.telegram.org/bots/api#tonnft
Snapshot: 2026-11-13T11:03:46Z

#### TonNft

This object represents an NFT in the TON blockchain.

| Field | Type | Description |
| --- | --- | --- |
| address | String | Address of the NFT |
| collection_address | String | *Optional*. Address of the collection to which the NFT belongs; omitted if unknown |
| index | String | Index of the NFT among all NFTs from the collection as a decimal number |
| name | String | Name of the NFT |
| description | String | Description of the NFT |
| attributes | Array of [TonNftAttribute](https://core.telegram.org/bots/api#tonnftattribute) | *Optional*. Attributes of the NFT |
| gift | [UniqueGift](https://core.telegram.org/bots/api#uniquegift) | *Optional*. The unique gift corresponding to the NFT |