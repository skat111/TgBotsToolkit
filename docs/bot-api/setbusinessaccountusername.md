Source: https://core.telegram.org/bots/api#setbusinessaccountusername
Snapshot: 2026-09-15T08:44:15Z

#### setBusinessAccountUsername

Changes the username of a managed business account. Requires the *can_change_username* business bot right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Yes | Unique identifier of the business connection |
| username | String | Optional | The new value of the username for the business account; 0-32 characters |