Source: https://core.telegram.org/bots/api#storyareatypelocation
Snapshot: 2026-09-15T08:44:15Z

#### StoryAreaTypeLocation

Describes a story area pointing to a location. Currently, a story can have up to 10 location areas.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the area, always “location” |
| latitude | Float | Location latitude in degrees |
| longitude | Float | Location longitude in degrees |
| address | [LocationAddress](https://core.telegram.org/bots/api#locationaddress) | *Optional*. Address of the location |