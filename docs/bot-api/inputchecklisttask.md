Source: https://core.telegram.org/bots/api#inputchecklisttask
Snapshot: 2026-09-25T08:52:18Z

#### InputChecklistTask

Describes a task to add to a checklist.

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier of the task; must be positive and unique among all task identifiers currently present in the checklist |
| text | String | Text of the task; 1-100 characters after entities parsing |
| parse_mode | String | *Optional*. Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details. |
| text_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. List of special entities that appear in the text, which can be specified instead of parse_mode. Currently, only *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, *custom_emoji*, and *date_time* entities are allowed. |