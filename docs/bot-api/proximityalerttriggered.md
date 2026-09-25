Source: https://core.telegram.org/bots/api#proximityalerttriggered
Snapshot: 2026-09-25T08:52:18Z

#### ProximityAlertTriggered

This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

| Field | Type | Description |
| --- | --- | --- |
| traveler | [User](https://core.telegram.org/bots/api#user) | User that triggered the alert |
| watcher | [User](https://core.telegram.org/bots/api#user) | User that set the alert |
| distance | Integer | The distance between the users |