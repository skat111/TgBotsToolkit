Source: https://core.telegram.org/bots/api#messageid
Snapshot: 2026-09-15T08:44:15Z

#### MessageId

This object represents a unique message identifier.

| Field | Type | Description |
| --- | --- | --- |
| message_id | Integer | Unique message identifier. In specific instances (e.g., message containing a video sent to a big chat), the server might automatically schedule a message instead of sending it immediately. In such cases, this field will be 0 and the relevant message will be unusable until it is actually sent. |