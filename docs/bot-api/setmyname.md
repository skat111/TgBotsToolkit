Source: https://core.telegram.org/bots/api#setmyname
Snapshot: 2026-09-22T08:35:37Z

#### setMyName

Use this method to change the bot's name. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| name | String | Optional | New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language. |
| language_code | String | Optional | A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose language there is no dedicated name. |