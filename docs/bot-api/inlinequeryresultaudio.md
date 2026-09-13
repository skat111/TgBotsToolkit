Source: https://core.telegram.org/bots/api#inlinequeryresultaudio
Snapshot: 2026-09-13T08:21:39Z

#### InlineQueryResultAudio

Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the audio.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *audio* |
| id | String | Unique identifier for this result, 1-64 bytes |
| audio_url | String | A valid URL for the audio file |
| title | String | Title |
| caption | String | *Optional*. Caption, 0-1024 characters after entities parsing |
| parse_mode | String | *Optional*. Mode for parsing entities in the audio caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| caption_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse_mode* |
| performer | String | *Optional*. Performer |
| audio_duration | Integer | *Optional*. Audio duration in seconds |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input_message_content | [InputMessageContent](https://core.telegram.org/bots/api#inputmessagecontent) | *Optional*. Content of the message to be sent instead of the audio |