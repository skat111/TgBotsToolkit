Source: https://core.telegram.org/bots/api#acceptedgifttypes
Snapshot: 2026-09-13T08:21:39Z

#### AcceptedGiftTypes

This object describes the types of gifts that can be gifted to a user or a chat.

| Field | Type | Description |
| --- | --- | --- |
| unlimited_gifts | Boolean | *True*, if unlimited regular gifts are accepted |
| limited_gifts | Boolean | *True*, if limited regular gifts are accepted |
| unique_gifts | Boolean | *True*, if unique gifts or gifts that can be upgraded to unique for free are accepted |
| premium_subscription | Boolean | *True*, if a Telegram Premium subscription is accepted |
| gifts_from_channels | Boolean | *True*, if transfers of unique gifts from channels are accepted |