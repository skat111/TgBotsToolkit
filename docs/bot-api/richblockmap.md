Source: https://core.telegram.org/bots/api#richblockmap
Snapshot: 2026-09-19T08:05:57Z

#### RichBlockMap

A block with a map, corresponding to the custom HTML tag `<tg-map>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “map” |
| location | [Location](https://core.telegram.org/bots/api#location) | Location of the center of the map |
| zoom | Integer | Map zoom level |
| width | Integer | Expected width of the map |
| height | Integer | Expected height of the map |
| caption | [RichBlockCaption](https://core.telegram.org/bots/api#richblockcaption) | *Optional*. Caption of the block |