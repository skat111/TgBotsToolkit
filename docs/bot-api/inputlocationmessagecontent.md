Source: https://core.telegram.org/bots/api#inputlocationmessagecontent
Snapshot: 2026-09-26T08:38:44Z

#### InputLocationMessageContent

Represents the [content](https://core.telegram.org/bots/api#inputmessagecontent) of a location message to be sent as the result of an inline query.

| Field | Type | Description |
| --- | --- | --- |
| latitude | Float | Latitude of the location in degrees |
| longitude | Float | Longitude of the location in degrees |
| horizontal_accuracy | Float | *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500 |
| live_period | Integer | *Optional*. Period in seconds during which the location can be updated, must be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely |
| heading | Integer | *Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. |
| proximity_alert_radius | Integer | *Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. |