Source: https://core.telegram.org/bots/api#getuserprofileaudios
Snapshot: 2026-09-17T08:42:18Z

#### getUserProfileAudios

Use this method to get a list of profile audios for a user. Returns a [UserProfileAudios](https://core.telegram.org/bots/api#userprofileaudios) object.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | Integer | Yes | Unique identifier of the target user |
| offset | Integer | Optional | Sequential number of the first audio to be returned. By default, all audios are returned. |
| limit | Integer | Optional | Limits the number of audios to be retrieved. Values between 1-100 are accepted. Defaults to 100. |