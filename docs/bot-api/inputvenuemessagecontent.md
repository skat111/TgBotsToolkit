Source: https://core.telegram.org/bots/api#inputvenuemessagecontent
Snapshot: 2026-09-13T08:21:39Z

#### InputVenueMessageContent

Represents the [content](https://core.telegram.org/bots/api#inputmessagecontent) of a venue message to be sent as the result of an inline query.

| Field | Type | Description |
| --- | --- | --- |
| latitude | Float | Latitude of the venue in degrees |
| longitude | Float | Longitude of the venue in degrees |
| title | String | Name of the venue |
| address | String | Address of the venue |
| foursquare_id | String | *Optional*. Foursquare identifier of the venue, if known |
| foursquare_type | String | *Optional*. Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.) |
| google_place_id | String | *Optional*. Google Places identifier of the venue |
| google_place_type | String | *Optional*. Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).) |