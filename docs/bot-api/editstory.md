Source: https://core.telegram.org/bots/api#editstory
Snapshot: 2026-09-22T08:35:37Z

#### editStory

Edits a story previously posted by the bot on behalf of a managed business account. Requires the *can_manage_stories* business bot right. Returns [Story](https://core.telegram.org/bots/api#story) on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Yes | Unique identifier of the business connection |
| story_id | Integer | Yes | Unique identifier of the story to edit |
| content | [InputStoryContent](https://core.telegram.org/bots/api#inputstorycontent) | Yes | Content of the story |
| caption | String | Optional | Caption of the story, 0-2048 characters after entities parsing |
| parse_mode | String | Optional | Mode for parsing entities in the story caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| caption_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | Optional | A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode* |
| areas | Array of [StoryArea](https://core.telegram.org/bots/api#storyarea) | Optional | A JSON-serialized list of clickable areas to be shown on the story |