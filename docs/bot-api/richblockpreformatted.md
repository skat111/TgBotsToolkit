Source: https://core.telegram.org/bots/api#richblockpreformatted
Snapshot: 2026-09-18T08:17:54Z

#### RichBlockPreformatted

A preformatted text block, corresponding to the nested HTML tags `<pre>` and `<code>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “pre” |
| text | [RichText](https://core.telegram.org/bots/api#richtext) | Text of the block |
| language | String | *Optional*. The programming language of the text |