Source: https://core.telegram.org/bots/api#getmydefaultadministratorrights
Snapshot: 2026-11-25T13:00:03Z

#### getMyDefaultAdministratorRights

Use this method to get the current default administrator rights of the bot. Returns [ChatAdministratorRights](https://core.telegram.org/bots/api#chatadministratorrights) on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| for_channels | Boolean | Optional | Pass *True* to get the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be returned. |