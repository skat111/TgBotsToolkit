Source: https://core.telegram.org/bots/api#inputstorycontentvideo
Snapshot: 2026-09-23T08:37:58Z

#### InputStoryContentVideo

Describes a video to post as a story.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the content, must be *video* |
| video | String | The video to post as a story. The video must be of the size 720x1280, streamable, encoded with H.265 codec, with key frames added each second in the MPEG4 format, and must not exceed 30 MB. The video can't be reused and can only be uploaded as a new file, so you can pass “attach://<file_attach_name>” if the video was uploaded using multipart/form-data under <file_attach_name>. [More information on Sending Files »](https://core.telegram.org/bots/api#sending-files) |
| duration | Float | *Optional*. Precise duration of the video in seconds; 0-60 |
| cover_frame_timestamp | Float | *Optional*. Timestamp in seconds of the frame that will be used as the static cover for the story. Defaults to 0.0. |
| is_animation | Boolean | *Optional*. Pass *True* if the video has no sound |