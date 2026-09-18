Source: https://core.telegram.org/bots/api#inputrichblockmap
Snapshot: 2026-09-18T08:17:54Z

#### InputRichBlockMap

A block with a map, corresponding to the custom HTML tag `<tg-map>`. The map's width and height must not exceed 10000 in total. The width and height ratio must be at most 20.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “map” |
| location | [Location](https://core.telegram.org/bots/api#location) | Location of the center of the map |
| zoom | Integer | *Optional*. Map zoom level; 0-24 |
| width | Integer | *Optional*. Map width; 0-10000 |
| height | Integer | *Optional*. Map height; 0-10000 |
| caption | [RichBlockCaption](https://core.telegram.org/bots/api#richblockcaption) | *Optional*. Caption of the block |