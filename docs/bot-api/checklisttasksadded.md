Source: https://core.telegram.org/bots/api#checklisttasksadded
Snapshot: 2026-09-22T08:35:37Z

#### ChecklistTasksAdded

Describes a service message about tasks added to a checklist.

| Field | Type | Description |
| --- | --- | --- |
| checklist_message | [Message](https://core.telegram.org/bots/api#message) | *Optional*. Message containing the checklist to which the tasks were added. Note that the [Message](https://core.telegram.org/bots/api#message) object in this field will not contain the *reply_to_message* field even if it itself is a reply. |
| tasks | Array of [ChecklistTask](https://core.telegram.org/bots/api#checklisttask) | List of tasks added to the checklist |