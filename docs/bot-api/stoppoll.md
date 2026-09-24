Source: https://core.telegram.org/bots/api#stoppoll
Snapshot: 2026-09-24T08:30:39Z

#### stopPoll

Use this method to stop a poll which was sent by the bot. On success, the stopped [Poll](https://core.telegram.org/bots/api#poll) is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Optional | Unique identifier of the business connection on behalf of which the message to be edited was sent |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username` |
| message_id | Integer | Yes | Identifier of the original message with the poll |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | Optional | A JSON-serialized object for a new message [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) |