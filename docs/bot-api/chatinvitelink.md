Source: https://core.telegram.org/bots/api#chatinvitelink
Snapshot: 2026-09-17T08:42:18Z

#### ChatInviteLink

Represents an invite link for a chat.

| Field | Type | Description |
| --- | --- | --- |
| invite_link | String | The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with “…”. |
| creator | [User](https://core.telegram.org/bots/api#user) | Creator of the link |
| creates_join_request | Boolean | *True*, if users joining the chat via the link need to be approved by chat administrators |
| is_primary | Boolean | *True*, if the link is primary |
| is_revoked | Boolean | *True*, if the link is revoked |
| name | String | *Optional*. Invite link name |
| expire_date | Integer | *Optional*. Point in time (Unix timestamp) when the link will expire or has been expired |
| member_limit | Integer | *Optional*. The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999 |
| pending_join_request_count | Integer | *Optional*. Number of pending join requests created using this link |
| subscription_period | Integer | *Optional*. The number of seconds the subscription will be active for before the next payment |
| subscription_price | Integer | *Optional*. The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat using the link |