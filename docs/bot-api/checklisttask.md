Source: https://core.telegram.org/bots/api#checklisttask
Snapshot: 2026-09-18T08:17:54Z

#### ChecklistTask

Describes a task in a checklist.

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier of the task |
| text | String | Text of the task |
| text_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. Special entities that appear in the task text |
| completed_by_user | [User](https://core.telegram.org/bots/api#user) | *Optional*. User that completed the task; omitted if the task wasn't completed by a user |
| completed_by_chat | [Chat](https://core.telegram.org/bots/api#chat) | *Optional*. Chat that completed the task; omitted if the task wasn't completed by a chat |
| completion_date | Integer | *Optional*. Point in time (Unix timestamp) when the task was completed; 0 if the task wasn't completed |