Source: https://core.telegram.org/bots/api#inputrichmessagemedia
Snapshot: 2026-09-14T08:59:05Z

#### InputRichMessageMedia

Describes a media element embedded in an outgoing rich message.

| Field | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the media used in a `tg://photo?id=`, `tg://video?id=`, `tg://document?id=`, or `tg://audio?id=` link. 1-64 characters, only `A-Z`, `a-z`, `0-9`, `_` and `-` are allowed. |
| media | [InputMediaAnimation](https://core.telegram.org/bots/api#inputmediaanimation) or [InputMediaAudio](https://core.telegram.org/bots/api#inputmediaaudio) or [InputMediaDocument](https://core.telegram.org/bots/api#inputmediadocument) or [InputMediaPhoto](https://core.telegram.org/bots/api#inputmediaphoto) or [InputMediaVideo](https://core.telegram.org/bots/api#inputmediavideo) or [InputMediaVoiceNote](https://core.telegram.org/bots/api#inputmediavoicenote) | The media to be sent. Everything except the media itself and its properties is ignored. |