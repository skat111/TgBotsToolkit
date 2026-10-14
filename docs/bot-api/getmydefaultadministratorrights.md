Source: https://core.telegram.org/bots/api#getmydefaultadministratorrights
Snapshot: 2026-10-14T08:46:29Z

#### getMyDefaultAdministratorRights

Use this method to get the current default administrator rights of the bot. Returns [ChatAdministratorRights](https://core.telegram.org/bots/api#chatadministratorrights) on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| for_channels | Boolean | Optional | Pass *True* to get default administrator rights of the bot in channels. Otherwise, default administrator rights of the bot for groups and supergroups will be returned. |