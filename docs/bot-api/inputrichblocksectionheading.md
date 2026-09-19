Source: https://core.telegram.org/bots/api#inputrichblocksectionheading
Snapshot: 2026-09-19T08:05:57Z

#### InputRichBlockSectionHeading

A section heading, corresponding to the HTML tags `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, or `<h6>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “heading” |
| text | [RichText](https://core.telegram.org/bots/api#richtext) | Text of the block |
| size | Integer | Relative size of the text font; 1-6, 1 is the largest, 6 is the smallest |