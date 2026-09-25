Source: https://core.telegram.org/bots/api#webhookinfo
Snapshot: 2026-09-25T08:52:18Z

#### WebhookInfo

Describes the current status of a webhook.

| Field | Type | Description |
| --- | --- | --- |
| url | String | Webhook URL, may be empty if webhook is not set up |
| has_custom_certificate | Boolean | *True*, if a custom certificate was provided for webhook certificate checks |
| pending_update_count | Integer | Number of updates awaiting delivery |
| ip_address | String | *Optional*. Currently used webhook IP address |
| last_error_date | Integer | *Optional*. Unix time for the most recent error that happened when trying to deliver an update via webhook |
| last_error_message | String | *Optional*. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook |
| last_synchronization_error_date | Integer | *Optional*. Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters |
| max_connections | Integer | *Optional*. The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery |
| allowed_updates | Array of String | *Optional*. A list of update types the bot is subscribed to. Defaults to all update types except *chat_member*, *message_reaction*, and *message_reaction_count*. |