Source: https://core.telegram.org/bots/api#inputprofilephotoanimated
Snapshot: 2026-09-20T08:38:20Z

#### InputProfilePhotoAnimated

An animated profile photo in the MPEG4 format.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the profile photo, must be *animated* |
| animation | String | The animated profile photo. Profile photos can't be reused and can only be uploaded as a new file, so you can pass “attach://<file_attach_name>” if the photo was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](https://core.telegram.org/bots/api#sending-files) |
| main_frame_timestamp | Float | *Optional*. Timestamp in seconds of the frame that will be used as the static profile photo. Defaults to 0.0. |