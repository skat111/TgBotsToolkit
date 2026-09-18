Source: https://core.telegram.org/bots/api#checklisttasksdone
Snapshot: 2026-09-18T08:17:54Z

#### ChecklistTasksDone

Describes a service message about checklist tasks marked as done or not done.

| Field | Type | Description |
| --- | --- | --- |
| checklist_message | [Message](https://core.telegram.org/bots/api#message) | *Optional*. Message containing the checklist whose tasks were marked as done or not done. Note that the [Message](https://core.telegram.org/bots/api#message) object in this field will not contain the *reply_to_message* field even if it itself is a reply. |
| marked_as_done_task_ids | Array of Integer | *Optional*. Identifiers of the tasks that were marked as done |
| marked_as_not_done_task_ids | Array of Integer | *Optional*. Identifiers of the tasks that were marked as not done |