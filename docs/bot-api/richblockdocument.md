Source: https://core.telegram.org/bots/api#richblockdocument
Snapshot: 2026-09-12T07:57:24Z

#### RichBlockDocument

A block with a general file, corresponding to the custom HTML tag `<tg-document>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “document” |
| document | [Document](https://core.telegram.org/bots/api#document) | The document |
| caption | [RichBlockCaption](https://core.telegram.org/bots/api#richblockcaption) | *Optional*. Caption of the block |