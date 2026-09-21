Source: https://core.telegram.org/bots/api#poststory
Snapshot: 2026-09-21T09:00:24Z

#### postStory

Posts a story on behalf of a managed business account. Requires the *can_manage_stories* business bot right. Returns [Story](https://core.telegram.org/bots/api#story) on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Yes | Unique identifier of the business connection |
| content | [InputStoryContent](https://core.telegram.org/bots/api#inputstorycontent) | Yes | Content of the story |
| active_period | Integer | Yes | Period after which the story is moved to the archive, in seconds; must be one of `6 * 3600`, `12 * 3600`, `86400`, or `2 * 86400` |
| caption | String | Optional | Caption of the story, 0-2048 characters after entities parsing |
| parse_mode | String | Optional | Mode for parsing entities in the story caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| caption_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | Optional | A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse_mode* |
| areas | Array of [StoryArea](https://core.telegram.org/bots/api#storyarea) | Optional | A JSON-serialized list of clickable areas to be shown on the story |
| post_to_chat_page | Boolean | Optional | Pass *True* to keep the story accessible after it expires |
| protect_content | Boolean | Optional | Pass *True* if the content of the story must be protected from forwarding and screenshotting |