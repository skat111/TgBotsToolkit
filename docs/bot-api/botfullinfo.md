Source: https://core.telegram.org/bots/api#botfullinfo
Snapshot: 2026-11-28T11:51:36Z

#### BotFullInfo

This object contains full information about the bot itself.

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier for this bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type is safe for storing this identifier. |
| is_bot | True | Always *True* |
| first_name | String | Bot's first name |
| username | String | *Optional*. Bot's username |
| active_usernames | Array of String | *Optional*. If non-empty, the list of all [active usernames](https://telegram.org/blog/topics-in-groups-collectible-usernames#collectible-usernames) of the bot |
| can_join_groups | Boolean | *True*, if the bot can be added to groups |
| can_read_all_group_messages | Boolean | *True*, if [privacy mode](https://core.telegram.org/bots/features#privacy-mode) is disabled for the bot |
| supports_guest_queries | Boolean | *True*, if the bot supports guest queries from chats it is not a member of |
| supports_inline_queries | Boolean | *True*, if the bot supports inline queries |
| inline_query_placeholder | String | *Optional*. Placeholder for inline queries, which is shown in the input field after the bot's username; omitted if the default placeholder is used |
| needs_inline_query_location | Boolean | *True*, if the bot requests the location of the user with every inline query |
| can_connect_to_business | Boolean | *True*, if the bot can be connected to a user account to manage it |
| has_main_web_app | Boolean | *True*, if the bot has a main Web App |
| has_topics_enabled | Boolean | *True*, if the bot has forum topic mode enabled in private chats |
| allows_users_to_create_topics | Boolean | *True*, if the bot allows users to create and delete topics in private chats |
| has_topic_sidebar | Boolean | *True*, if topics in private chats with the bot are shown in a sidebar |
| can_manage_bots | Boolean | *True*, if other bots can be created to be controlled by the bot |
| supports_join_request_queries | Boolean | *True*, if the bot supports join request queries and can be assigned to process them |