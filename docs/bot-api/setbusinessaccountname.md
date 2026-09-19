Source: https://core.telegram.org/bots/api#setbusinessaccountname
Snapshot: 2026-09-19T08:05:57Z

#### setBusinessAccountName

Changes the first and last name of a managed business account. Requires the *can_change_name* business bot right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Yes | Unique identifier of the business connection |
| first_name | String | Yes | The new value of the first name for the business account; 1-64 characters |
| last_name | String | Optional | The new value of the last name for the business account; 0-64 characters |