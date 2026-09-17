Source: https://core.telegram.org/bots/api#giftpremiumsubscription
Snapshot: 2026-09-17T08:42:18Z

#### giftPremiumSubscription

Gifts a Telegram Premium subscription to the given user. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | Integer | Yes | Unique identifier of the target user who will receive a Telegram Premium subscription |
| month_count | Integer | Yes | Number of months the Telegram Premium subscription will be active for the user; must be one of 3, 6, or 12 |
| star_count | Integer | Yes | Number of Telegram Stars to pay for the Telegram Premium subscription; must be 1000 for 3 months, 1500 for 6 months, and 2500 for 12 months |
| text | String | Optional | Text that will be shown along with the service message about the subscription; 0-128 characters |
| text_parse_mode | String | Optional | Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, “custom_emoji”, and “date_time” are ignored. |
| text_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | Optional | A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of *text_parse_mode*. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, “custom_emoji”, and “date_time” are ignored. |