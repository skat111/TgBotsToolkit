Source: https://core.telegram.org/bots/api#forumtopiccreated
Snapshot: 2026-09-20T08:38:20Z

#### ForumTopicCreated

This object represents a service message about a new forum topic created in the chat.

| Field | Type | Description |
| --- | --- | --- |
| name | String | Name of the topic |
| icon_color | Integer | Color of the topic icon in RGB format |
| icon_custom_emoji_id | String | *Optional*. Unique identifier of the custom emoji shown as the topic icon |
| is_name_implicit | True | *Optional*. *True*, if the name of the topic wasn't specified explicitly by its creator and likely needs to be changed by the bot |