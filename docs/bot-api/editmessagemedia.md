Source: https://core.telegram.org/bots/api#editmessagemedia
Snapshot: 2026-09-16T08:38:32Z

#### editMessageMedia

Use this method to edit animation, audio, document, live photo, photo, or video messages, or to replace a text or a rich message with a media. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo, a live photo, or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited [Message](https://core.telegram.org/bots/api#message) is returned, otherwise *True* is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Optional | Unique identifier of the business connection on behalf of which the message to be edited was sent |
| chat_id | Integer or String | Optional | Required if *inline_message_id* is not specified. Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`. |
| message_id | Integer | Optional | Required if *inline_message_id* is not specified. Identifier of the message to edit. |
| inline_message_id | String | Optional | Required if *chat_id* and *message_id* are not specified. Identifier of the inline message. |
| media | [InputMedia](https://core.telegram.org/bots/api#inputmedia) | Yes | A JSON-serialized object for the new media content of the message |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | Optional | A JSON-serialized object for a new [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) |