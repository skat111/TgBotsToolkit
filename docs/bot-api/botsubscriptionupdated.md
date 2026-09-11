Source: https://core.telegram.org/bots/api#botsubscriptionupdated
Snapshot: 2026-09-11T06:04:42Z

#### BotSubscriptionUpdated

This object contains information about changes to a user payment subscription toward the current bot.

| Field | Type | Description |
| --- | --- | --- |
| user | [User](https://core.telegram.org/bots/api#user) | User who subscribed for payments toward the bot |
| invoice_payload | String | Bot-specified invoice payload |
| state | String | The new state of the subscription. Currently, it can be one of “canceled” if the user canceled the subscription, “active” if the user re-enabled a previously canceled subscription, or “failed” if payment for the subscription failed. |