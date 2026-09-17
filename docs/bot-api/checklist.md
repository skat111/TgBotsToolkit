Source: https://core.telegram.org/bots/api#checklist
Snapshot: 2026-09-17T08:42:18Z

#### Checklist

Describes a checklist.

| Field | Type | Description |
| --- | --- | --- |
| title | String | Title of the checklist |
| title_entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. Special entities that appear in the checklist title |
| tasks | Array of [ChecklistTask](https://core.telegram.org/bots/api#checklisttask) | List of tasks in the checklist |
| others_can_add_tasks | True | *Optional*. *True*, if users other than the creator of the list can add tasks to the list |
| others_can_mark_tasks_as_done | True | *Optional*. *True*, if users other than the creator of the list can mark tasks as done or not done |