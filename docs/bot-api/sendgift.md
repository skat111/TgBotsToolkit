Source: https://core.telegram.org/bots/api#sendgift
Snapshot: 2026-09-17T08:42:18Z

#### sendGift

Sends a gift to the given user or channel chat. The gift can't be converted to Telegram Stars by the receiver. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | Integer | Optional | Required if *chat_id* is not specified. Unique identifier of the target user who will receive the gift. |
| chat_id | Integer or String | Optional | Required if *user_id* is not specified. Unique identifier for the chat or username of the channel (in the format `@username`) that will receive the gift. |
| gift_id | String | Yes | Identifier of the gift; limited gifts can't be sent to channel chats |
| pay_for_upgrade | Boolean | Optional | Pass *True* to pay for the gift upgrade from the bot's balance, thereby making the upgrade free for the receiver |
| text | String | Optional | Text that will be shown along with the gift; 0-128 characters |
| text_parse_mode | String | Optional | Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, “custom_emoji”, and “date_time” are ignored. |
| text_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | Optional | A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of *text_parse_mode*. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, “custom_emoji”, and “date_time” are ignored. |