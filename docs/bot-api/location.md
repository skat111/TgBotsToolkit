Source: https://core.telegram.org/bots/api#location
Snapshot: 2026-09-11T06:04:42Z

#### Location

This object represents a point on the map.

| Field | Type | Description |
| --- | --- | --- |
| latitude | Float | Latitude as defined by the sender |
| longitude | Float | Longitude as defined by the sender |
| horizontal_accuracy | Float | *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500 |
| live_period | Integer | *Optional*. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only. |
| heading | Integer | *Optional*. The direction in which user is moving, in degrees; 1-360. For active live locations only. |
| proximity_alert_radius | Integer | *Optional*. The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only. |