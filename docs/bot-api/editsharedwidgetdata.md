Source: https://core.telegram.org/bots/api#editsharedwidgetdata
Snapshot: 2026-11-14T10:30:31Z

#### editSharedWidgetData

Use this method to edit public data of a shared widget created by the bot. A shared widget can be edited at most once per second. On success, *True* is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| widget_id | String | Yes | Unique identifier of the shared widget |
| public_data | String | Yes | New public data of the widget, 0-1024 bytes; pass an empty string to remove the public data |
| cache_time | Integer | Optional | The maximum amount of time in seconds that the public data of the widget may be cached client-side; 5-3600. If omitted, then the current value is kept, which is 30 by default. |