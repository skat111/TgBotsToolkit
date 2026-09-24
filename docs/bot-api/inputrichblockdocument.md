Source: https://core.telegram.org/bots/api#inputrichblockdocument
Snapshot: 2026-09-24T08:30:39Z

#### InputRichBlockDocument

A block with a general file, corresponding to the custom HTML tag `<tg-document>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “document” |
| document | [InputMediaDocument](https://core.telegram.org/bots/api#inputmediadocument) | The document. Caption is ignored. |
| caption | [RichBlockCaption](https://core.telegram.org/bots/api#richblockcaption) | *Optional*. Caption of the block |