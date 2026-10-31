Source: https://core.telegram.org/bots/api#richtextanchorlink
Snapshot: 2026-10-31T09:42:22Z

#### RichTextAnchorLink

A link to an anchor.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the rich text, always “anchor_link” |
| text | [RichText](https://core.telegram.org/bots/api#richtext) | The link text |
| anchor_name | String | The name of the anchor. If the name is empty, then the link brings back to the top of the message. |