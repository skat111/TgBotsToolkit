Source: https://core.telegram.org/bots/api#verifychat
Snapshot: 2026-11-13T11:03:46Z

#### verifyChat

Verifies a chat [on behalf of the organization](https://telegram.org/verify#third-party-verification) which is represented by the bot. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot, supergroup, or channel in the format `@username`. Channel direct messages chats can't be verified. |
| custom_description | String | Optional | Custom description for the verification; 0-70 characters. Must be empty if the organization isn't allowed to provide a custom verification description. |
| custom_description_parse_mode | String | Optional | Mode for parsing entities in the custom description. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. Only “text_link” entities are supported. |
| custom_description_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | Optional | A JSON-serialized list of special entities that appear in the custom description, which can be specified instead of *custom_description_parse_mode*. Only “text_link” entities are supported. |