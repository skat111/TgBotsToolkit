Source: https://core.telegram.org/bots/api#setbusinessaccountbio
Snapshot: 2026-11-25T13:00:03Z

#### setBusinessAccountBio

Changes the bio of a managed business account. Requires the *can_edit_bio* business bot right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Yes | Unique identifier of the business connection |
| bio | String | Optional | The new value of the bio for the business account; 0-140 characters |