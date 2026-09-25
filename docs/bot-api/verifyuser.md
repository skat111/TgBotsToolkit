Source: https://core.telegram.org/bots/api#verifyuser
Snapshot: 2026-09-25T08:52:18Z

#### verifyUser

Verifies a user [on behalf of the organization](https://telegram.org/verify#third-party-verification) which is represented by the bot. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | Integer | Yes | Unique identifier of the target user |
| custom_description | String | Optional | Custom description for the verification; 0-70 characters. Must be empty if the organization isn't allowed to provide a custom verification description. |