Source: https://core.telegram.org/bots/api#edituserstarsubscription
Snapshot: 2026-09-23T08:37:58Z

#### editUserStarSubscription

Allows the bot to cancel or re-enable extension of a subscription paid in Telegram Stars. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | Integer | Yes | Identifier of the user whose subscription will be edited |
| telegram_payment_charge_id | String | Yes | Telegram payment identifier for the subscription |
| is_canceled | Boolean | Yes | Pass *True* to cancel extension of the user subscription; the subscription must be active up to the end of the current subscription period. Pass *False* to allow the user to re-enable a subscription that was previously canceled by the bot. |