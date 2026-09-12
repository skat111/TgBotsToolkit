Source: https://core.telegram.org/bots/api#setbusinessaccountprofilephoto
Snapshot: 2026-09-12T07:57:24Z

#### setBusinessAccountProfilePhoto

Changes the profile photo of a managed business account. Requires the *can_edit_profile_photo* business bot right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Yes | Unique identifier of the business connection |
| photo | [InputProfilePhoto](https://core.telegram.org/bots/api#inputprofilephoto) | Yes | The new profile photo to set |
| is_public | Boolean | Optional | Pass *True* to set the public photo, which will be visible even if the main photo is hidden by the business account's privacy settings. An account can have only one public photo. |