Source: https://core.telegram.org/bots/api#inputrichblockpreformatted
Snapshot: 2026-11-07T10:16:45Z

#### InputRichBlockPreformatted

A preformatted text block, corresponding to the nested HTML tags `<pre>` and `<code>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “pre” |
| text | [RichText](https://core.telegram.org/bots/api#richtext) | Text of the block |
| language | String | *Optional*. The programming language of the text |