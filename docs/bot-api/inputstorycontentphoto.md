Source: https://core.telegram.org/bots/api#inputstorycontentphoto
Snapshot: 2026-09-11T06:04:42Z

#### InputStoryContentPhoto

Describes a photo to post as a story.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the content, must be *photo* |
| photo | String | The photo to post as a story. The photo must be of the size 1080x1920 and must not exceed 10 MB. The photo can't be reused and can only be uploaded as a new file, so you can pass “attach://<file_attach_name>” if the photo was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](https://core.telegram.org/bots/api#sending-files) |