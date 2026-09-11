Source: https://core.telegram.org/bots/api#removebusinessaccountprofilephoto
Snapshot: 2026-09-11T06:04:42Z

#### removeBusinessAccountProfilePhoto

Removes the current profile photo of a managed business account. Requires the *can_edit_profile_photo* business bot right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Yes | Unique identifier of the business connection |
| is_public | Boolean | Optional | Pass *True* to remove the public photo, which is visible even if the main photo is hidden by the business account's privacy settings. After the main photo is removed, the previous profile photo (if present) becomes the main photo. |