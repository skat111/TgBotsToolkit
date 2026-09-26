Source: https://core.telegram.org/bots/api#inputprofilephotostatic
Snapshot: 2026-09-26T08:38:44Z

#### InputProfilePhotoStatic

A static profile photo in the .JPG format.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the profile photo, must be *static* |
| photo | String | The static profile photo. Profile photos can't be reused and can only be uploaded as a new file, so you can pass “attach://<file_attach_name>” if the photo was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](https://core.telegram.org/bots/api#sending-files) |