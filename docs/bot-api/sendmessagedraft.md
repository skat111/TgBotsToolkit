Source: https://core.telegram.org/bots/api#sendmessagedraft
Snapshot: 2026-09-14T08:59:05Z

#### sendMessageDraft

Use this method to stream a partial message to a user while the message is being generated. Note that the streamed draft is ephemeral and acts as a temporary 30-second preview - once the output is finalized, you **must** call [sendMessage](https://core.telegram.org/bots/api#sendmessage) with the complete message to persist it in the user's chat. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer | Yes | Unique identifier for the target private chat |
| message_thread_id | Integer | Optional | Unique identifier for the target message thread |
| draft_id | Integer | Yes | Unique identifier of the message draft; must be non-zero. Changes to drafts with the same identifier are animated. Otherwise, the draft is replaced without animation. |
| text | String | Optional | Text of the message to be sent, 0-4096 characters after entities parsing. Pass an empty text to show a “Thinking…” placeholder. |
| parse_mode | String | Optional | Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | Optional | A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse_mode* |
| can_stop | Boolean | Optional | Pass *True* to show the user a button to stop further drafts. The bot will receive an [Update](https://core.telegram.org/bots/api#update) “stopped_message_generation” if the user presses the button. |
| keep_on_stop | Boolean | Optional | Pass *True* to keep the draft in the chat when the button is pressed. The draft will still disappear after a short time or if the bot sends a message. To fully preserve the partial draft, the bot should send it as a new message. |