Source: https://core.telegram.org/bots/api#sendmediagroup
Snapshot: 2026-09-26T08:38:44Z

#### sendMediaGroup

Use this method to send a group of photos, live photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an Array of [Message](https://core.telegram.org/bots/api#message) objects that were sent is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Optional | Unique identifier of the business connection on behalf of which the message will be sent |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username` |
| message_thread_id | Integer | Optional | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only |
| direct_messages_topic_id | Integer | Optional | Identifier of the direct messages topic to which the messages will be sent; required if the messages are sent to a direct messages chat |
| media | Array of [InputMediaAudio](https://core.telegram.org/bots/api#inputmediaaudio), [InputMediaDocument](https://core.telegram.org/bots/api#inputmediadocument), [InputMediaLivePhoto](https://core.telegram.org/bots/api#inputmedialivephoto), [InputMediaPhoto](https://core.telegram.org/bots/api#inputmediaphoto) and [InputMediaVideo](https://core.telegram.org/bots/api#inputmediavideo) | Yes | A JSON-serialized Array describing messages to be sent, must include 2-10 items |
| disable_notification | Boolean | Optional | Sends messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |
| protect_content | Boolean | Optional | Protects the contents of the sent messages from forwarding and saving |
| allow_paid_broadcast | Boolean | Optional | Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance. |
| message_effect_id | String | Optional | Unique identifier of the message effect to be added to the message; for private chats only |
| reply_parameters | [ReplyParameters](https://core.telegram.org/bots/api#replyparameters) | Optional | Description of the message to reply to |