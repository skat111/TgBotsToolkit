Source: https://core.telegram.org/bots/api#setuseremojistatus
Snapshot: 2026-09-22T08:35:37Z

#### setUserEmojiStatus

Changes the emoji status for a given user that previously allowed the bot to manage their emoji status via the Mini App method [requestEmojiStatusAccess](https://core.telegram.org/bots/webapps#initializing-mini-apps). Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | Integer | Yes | Unique identifier of the target user |
| emoji_status_custom_emoji_id | String | Optional | Custom emoji identifier of the emoji status to set. Pass an empty string to remove the status. |
| emoji_status_expiration_date | Integer | Optional | Expiration date of the emoji status, if any |