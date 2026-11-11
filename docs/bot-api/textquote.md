Source: https://core.telegram.org/bots/api#textquote
Snapshot: 2026-11-11T11:02:11Z

#### TextQuote

This object contains information about the quoted part of a message that is replied to by the given message.

| Field | Type | Description |
| --- | --- | --- |
| text | String | Text of the quoted part of a message that is replied to by the given message; may be empty if the quote was chosen from a rich message |
| entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. Special entities that appear in the quote. Currently, only *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, *custom_emoji*, and *date_time* entities are kept in quotes. |
| rich_texts | Array of [RichText](https://core.telegram.org/bots/api#richtext) | *Optional*. Rich text of the quote if it was chosen from a [rich message](https://core.telegram.org/bots/api#richmessage). May contain only plain text, [RichTextBold](https://core.telegram.org/bots/api#richtextbold), [RichTextItalic](https://core.telegram.org/bots/api#richtextitalic), [RichTextUnderline](https://core.telegram.org/bots/api#richtextunderline), [RichTextStrikethrough](https://core.telegram.org/bots/api#richtextstrikethrough), [RichTextSpoiler](https://core.telegram.org/bots/api#richtextspoiler), [RichTextSubscript](https://core.telegram.org/bots/api#richtextsubscript), [RichTextSuperscript](https://core.telegram.org/bots/api#richtextsuperscript), [RichTextDateTime](https://core.telegram.org/bots/api#richtextdatetime), [RichTextCustomEmoji](https://core.telegram.org/bots/api#richtextcustomemoji), [RichTextMathematicalExpression](https://core.telegram.org/bots/api#richtextmathematicalexpression), and arrays of them. |
| position | Integer | Approximate quote position in the original message in UTF-16 code units as specified by the sender. For quotes from rich messages, it is the position in the text formed by joining plain texts of all quotable texts of the message, separated by line feeds. |
| is_manual | True | *Optional*. *True*, if the quote was chosen manually by the message sender. Otherwise, the quote was added automatically by the server. |