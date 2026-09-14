Source: https://core.telegram.org/bots/api#sendpoll
Snapshot: 2026-09-14T08:59:05Z

#### sendPoll

Use this method to send a native poll. On success, the sent [Message](https://core.telegram.org/bots/api#message) is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Optional | Unique identifier of the business connection on behalf of which the message will be sent |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`. Polls can't be sent to channel direct messages chats. |
| message_thread_id | Integer | Optional | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only |
| question | String | Yes | Poll question, 1-300 characters |
| question_parse_mode | String | Optional | Mode for parsing entities in the question. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. Currently, only custom emoji entities are allowed. |
| question_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | Optional | A JSON-serialized list of special entities that appear in the poll question. It can be specified instead of *question_parse_mode*. |
| options | Array of [InputPollOption](https://core.telegram.org/bots/api#inputpolloption) | Yes | A JSON-serialized list of 1-12 answer options |
| is_anonymous | Boolean | Optional | *True*, if the poll needs to be anonymous, defaults to *True* |
| type | String | Optional | Poll type, “quiz” or “regular”, defaults to “regular” |
| allows_multiple_answers | Boolean | Optional | Pass *True* if the poll allows multiple answers, defaults to *False* |
| allows_revoting | Boolean | Optional | Pass *True* if the poll allows to change chosen answer options, defaults to *False* for quizzes and to *True* for regular polls |
| shuffle_options | Boolean | Optional | Pass *True* if the poll options must be shown in random order |
| allow_adding_options | Boolean | Optional | Pass *True* if answer options can be added to the poll after creation; not supported for anonymous polls and quizzes |
| hide_results_until_closes | Boolean | Optional | Pass *True* if poll results must be shown only after the poll closes |
| members_only | Boolean | Optional | Pass *True* if voting is limited to users who have been members of the chat where the poll is being sent for more than 24 hours; for channel chats only |
| country_codes | Array of String | Optional | A JSON-serialized list of 0-12 two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes indicating the countries from which users can vote in the poll; for channel chats only. Use “FT” as a country code to allow users with anonymous numbers to vote. If omitted or empty, then users from any country can participate in the poll. |
| correct_option_ids | Array of Integer | Optional | A JSON-serialized list of monotonically increasing 0-based identifiers of the correct answer options, required for polls in quiz mode |
| explanation | String | Optional | Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing |
| explanation_parse_mode | String | Optional | Mode for parsing entities in the explanation. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| explanation_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | Optional | A JSON-serialized list of special entities that appear in the poll explanation. It can be specified instead of *explanation_parse_mode*. |
| explanation_media | [InputPollMedia](https://core.telegram.org/bots/api#inputpollmedia) | Optional | Media added to the quiz explanation |
| open_period | Integer | Optional | Amount of time in seconds the poll will be active after creation, 5-2628000. Can't be used together with *close_date*. |
| close_date | Integer | Optional | Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 2628000 seconds in the future. Can't be used together with *open_period*. |
| is_closed | Boolean | Optional | Pass *True* if the poll needs to be immediately closed. This can be useful for poll preview. |
| description | String | Optional | Description of the poll to be sent, 0-1024 characters after entities parsing |
| description_parse_mode | String | Optional | Mode for parsing entities in the poll description. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| description_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | Optional | A JSON-serialized list of special entities that appear in the poll description, which can be specified instead of *description_parse_mode* |
| media | [InputPollMedia](https://core.telegram.org/bots/api#inputpollmedia) | Optional | Media added to the poll description |
| disable_notification | Boolean | Optional | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |
| protect_content | Boolean | Optional | Protects the contents of the sent message from forwarding and saving |
| allow_paid_broadcast | Boolean | Optional | Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance. |
| message_effect_id | String | Optional | Unique identifier of the message effect to be added to the message; for private chats only |
| reply_parameters | [ReplyParameters](https://core.telegram.org/bots/api#replyparameters) | Optional | Description of the message to reply to |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) or [ReplyKeyboardMarkup](https://core.telegram.org/bots/api#replykeyboardmarkup) or [ReplyKeyboardRemove](https://core.telegram.org/bots/api#replykeyboardremove) or [ForceReply](https://core.telegram.org/bots/api#forcereply) | Optional | Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user. |