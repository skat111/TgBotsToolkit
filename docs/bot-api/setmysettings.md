Source: https://core.telegram.org/bots/api#setmysettings
Snapshot: 2026-11-27T12:28:14Z

#### setMySettings

Use this method to change the settings of the bot. Settings that aren't specified remain unchanged. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| supports_inline_queries | Boolean | Optional | Pass *True* to enable [inline mode](https://core.telegram.org/bots/api#inline-mode) for the bot or *False* to disable it |
| inline_query_placeholder | String | Optional | New placeholder for inline queries, which is shown in the input field after the bot's username. Pass an empty string to use the default placeholder. |
| needs_inline_query_location | Boolean | Optional | Pass *True* to request the location of the user with every inline query to the bot or *False* to stop requesting it |
| inline_feedback_share_denominator | Integer | Optional | Denominator of the share of [chosen inline results](https://core.telegram.org/bots/api#choseninlineresult) received by the bot; the bot receives 1 out of *inline_feedback_share_denominator* chosen results. Must be one of 1, 10, 100, or 1000. Pass 0 to stop receiving chosen inline results. |
| can_join_groups | Boolean | Optional | Pass *True* to allow adding the bot to groups or *False* to disallow it |
| can_read_all_group_messages | Boolean | Optional | Pass *True* to disable [privacy mode](https://core.telegram.org/bots/features#privacy-mode) for the bot or *False* to enable it |
| can_connect_to_business | Boolean | Optional | Pass *True* to allow connecting the bot to user accounts to manage them or *False* to disallow it |
| can_manage_bots | Boolean | Optional | Pass *True* to allow creating other bots that will be controlled by the bot or *False* to disallow it |
| supports_guest_queries | Boolean | Optional | Pass *True* to allow guest queries to the bot from chats it isn't a member of or *False* to disallow them |
| supports_join_request_queries | Boolean | Optional | Pass *True* to allow assigning the bot to process join request queries or *False* to disallow it |
| has_topics_enabled | Boolean | Optional | Pass *True* to enable forum topic mode in private chats with the bot or *False* to disable it |
| allows_users_to_create_topics | Boolean | Optional | Pass *True* to allow users to create and delete topics in private chats with the bot or *False* to disallow it |
| has_topic_sidebar | Boolean | Optional | Pass *True* to show topics in private chats with the bot in a sidebar or *False* to stop showing them in a sidebar |
| can_communicate_with_bots | Boolean | Optional | Pass *True* to allow the bot to communicate with other bots in groups, private chats, and through business accounts or *False* to disallow it |
| callback_query_mode | String | Optional | Mode in which the bot receives [callback queries](https://core.telegram.org/bots/api#callbackquery) from buttons in messages sent by the bot. Must be one of “default” (the field *message* is always used and contains an [InaccessibleMessage](https://core.telegram.org/bots/api#inaccessiblemessage) if the message is inaccessible to the bot), “auto” (the field *inline_message_id* is used instead of the field *message* if the message is inaccessible to the bot; the field *message* can still contain an inaccessible message if the message has just been deleted), or “inline” (the field *inline_message_id* is always used instead of the field *message*). |