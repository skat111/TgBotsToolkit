Source: https://core.telegram.org/bots/api#uniquegiftmodel
Snapshot: 2026-09-16T08:38:32Z

#### UniqueGiftModel

This object describes the model of a unique gift.

| Field | Type | Description |
| --- | --- | --- |
| name | String | Name of the model |
| sticker | [Sticker](https://core.telegram.org/bots/api#sticker) | The sticker that represents the unique gift |
| rarity_per_mille | Integer | The number of unique gifts that receive this model for every 1000 gift upgrades. Always 0 for crafted gifts. |
| rarity | String | *Optional*. Rarity of the model if it is a crafted model. Currently, can be “uncommon”, “rare”, “epic”, or “legendary”. |