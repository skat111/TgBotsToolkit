Source: https://core.telegram.org/bots/api#repoststory
Snapshot: 2026-09-14T08:59:05Z

#### repostStory

Reposts a story on behalf of a business account from another business account. Both business accounts must be managed by the same bot, and the story on the source account must have been posted (or reposted) by the bot. Requires the *can_manage_stories* business bot right for both business accounts. Returns [Story](https://core.telegram.org/bots/api#story) on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Yes | Unique identifier of the business connection |
| from_chat_id | Integer | Yes | Unique identifier of the chat which posted the story that should be reposted |
| from_story_id | Integer | Yes | Unique identifier of the story that should be reposted |
| active_period | Integer | Yes | Period after which the story is moved to the archive, in seconds; must be one of `6 * 3600`, `12 * 3600`, `86400`, or `2 * 86400` |
| post_to_chat_page | Boolean | Optional | Pass *True* to keep the story accessible after it expires |
| protect_content | Boolean | Optional | Pass *True* if the content of the story must be protected from forwarding and screenshotting |