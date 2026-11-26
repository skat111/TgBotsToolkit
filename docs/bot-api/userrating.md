Source: https://core.telegram.org/bots/api#userrating
Snapshot: 2026-11-26T12:40:52Z

#### UserRating

This object describes the rating of a user based on their Telegram Star spending.

| Field | Type | Description |
| --- | --- | --- |
| level | Integer | Current level of the user, indicating their reliability when purchasing digital goods and services. A higher level suggests a more trustworthy customer; a negative level is likely a reason for concern. |
| rating | Integer | Numerical value of the user's rating; the higher the rating, the better |
| current_level_rating | Integer | The rating value required to get the current level |
| next_level_rating | Integer | *Optional*. The rating value required to get to the next level; omitted if the maximum level was reached |