Source: https://core.telegram.org/bots/api#rich-message-formatting-options
Snapshot: 2026-09-11T06:04:42Z

#### Rich Message Formatting Options

[Rich messages](https://core.telegram.org/bots/api#inputrichmessage) support advanced structured formatting options like headings, lists, tables, media, block quotations, collapsible blocks, footnotes, and formulas. Telegram clients will render them accordingly. You can specify rich message content using [Markdown-style](https://core.telegram.org/bots/api#rich-markdown-style) or [HTML-style](https://core.telegram.org/bots/api#rich-html-style) formatting, or explicit [blocks](https://core.telegram.org/bots/api#inputrichblock).

Plain URLs, e-mail addresses, username mentions, hashtags, cashtags, bot commands, phone numbers, and bank card numbers are detected automatically. To disable automatic entity detection, pass *True* in the *skip_entity_detection* field. Note that Telegram clients will display an alert to the user before opening an inline link ('Open this link?' together with the full URL).

When [Markdown-style](https://core.telegram.org/bots/api#rich-markdown-style) or [HTML-style](https://core.telegram.org/bots/api#rich-html-style) formatting is used, you can use links in the form `tg://photo?id=...`, `tg://video?id=...`, `tg://document?id=...`, and `tg://audio?id=...` instead of an HTTP URL to reuse previously uploaded files or upload a new file.

###### Rich Message Limits

Rich messages are subject to the following limits:

* Up to **32768 UTF-8 characters** in the rich message text, including custom emoji alternative text and formula source.
* Up to **500 blocks**, including nested blocks, list items, ordered list items, table rows, quotation blocks, and details blocks.
* Up to **16 levels** of nested formatting and blocks.
* Up to **50 media attachments** in total.
* Up to **20 columns** in a table.

###### Rich Markdown style

To use this mode, pass rich message content in the *markdown* field. Use the following syntax in your message:

```
**bold text**
__bold text__
*italic text*
_italic text_
~~strikethrough text~~
`inline fixed-width code`
==marked text==
||spoiler||

[inline URL](https://t.me/)
[inline e-mail](mailto:user@example.com)
[inline phone number](tel:+123456789)
[inline mention of a user](tg://user?id=123456789)
![![👍](//telegram.org/img/emoji/40/F09F918D.png)](tg://emoji?id=5368324170671202286)
![22:45 tomorrow](tg://time?unix=1647531900&format=wDT)
$x^2 + y^2$
\#hashtag $USD +12345678901, card: 4242 4242 4242 4242, https://t.me t.me a@t.me /command @username
all the text above was on the same line

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

Paragraph text

```python
  print('pre-formatted fixed-width code block written in the Python programming language')
```

---

- unordered list item
* unordered list item
+ unordered list item

1. ordered list item
2. ordered list item

- [ ] task list item
- [x] completed task list item

>Block quotation started
>
>Block quotation continued on the next line
>Block quotation continued on the same line
>
>The last line of the block quotation

![](https://telegram.org/example/photo.jpg)
![](https://telegram.org/example/video.mp4)
![](https://telegram.org/example/audio.mp3)
![](https://telegram.org/example/audio.ogg)
![](https://telegram.org/example/animation.gif)
![](https://telegram.org/example/document.zip)

![](https://telegram.org/example/photo.jpg "Photo caption")
![](https://telegram.org/example/video.mp4 "Video caption")
![](https://telegram.org/example/audio.mp3 "Audio caption")
![](https://telegram.org/example/audio.ogg "Voice note caption")
![](https://telegram.org/example/animation.gif "Animation caption")
![](https://telegram.org/example/document.zip "Document caption")

| Header 1 | Header 2 |
|:---------|:--------:|
| left     | center   |

Text with a reference[^id1] and another one[^id2].

[^id1]: Definition of the first footnote.
[^id2]: Definition of the second footnote.

$$E = mc^2$$

```math
E = mc^2
```

## Example Nested Syntax Report for _Q1_
Intro with <u>underlined text</u>, ==marked text==, and $x^2 + y^2$.
**Bold _italic <u>underlined italic bold</u> italic_ bold**
<u>In inline tags, nested **markdown** is parsed</u>
>Quote with **bold text, ~~strikethrough, and <tg-spoiler>spoiler</tg-spoiler>~~**, plus [a link](https://t.me/).

- List item with `code`, <sup>superscript</sup>, <sub>subscript</sub>, and a footnote[^note]
- Another item with **bold <tg-spoiler><code>spoiler code</code></tg-spoiler>**
- Another item with ~~strikethrough and <ins>inserted text</ins>~~

| Metric | Value |
|:-------|------:|
| Speed  | **42** <sup>ms</sup> |
| Status | <tg-spoiler>ready</tg-spoiler> |

[^note]: Footnote with _italic text_ and <u>HTML underline</u>.

---

# Details blocks can contain Markdown content:

<details open><summary>Summary with **bold text**</summary>

### Details heading
- List item with _italic text_
- List item with <tg-spoiler>spoiler</tg-spoiler>

</details>

# Collages and slideshows can contain Markdown media blocks:

<tg-collage>

![](https://telegram.org/example/photo.jpg)
![](https://telegram.org/example/video.mp4)

</tg-collage>

<tg-slideshow>

![](https://telegram.org/example/photo.jpg)
![](https://telegram.org/example/video.mp4)

</tg-slideshow>
```

For formatting features that don't have Markdown syntax, use [HTML tags](https://core.telegram.org/bots/api#rich-html-style):

```
<u>underlined text</u>, <ins>underlined text</ins>
<sub>subscript text</sub>
<sup>superscript text</sup>
<a name="chapter-1"></a>
<aside>Pull quote<cite>The Author</cite></aside>
<details open><summary>Title</summary>Content</details>
<tg-map lat="41.9" long="12.5" zoom="14"/>
<tg-collage><img src="https://telegram.org/example/photo.jpg"/><figcaption>Caption<cite>The Author</cite></figcaption></tg-collage>
<tg-slideshow><img src="https://telegram.org/example/photo.jpg"/><video src="https://telegram.org/example/video.mp4"/><figcaption>Slideshow caption<cite>The Author</cite></figcaption></tg-slideshow>
<p>Inline buttons:
  <tg-button type="url" style="success" url="https://t.me">url</tg-button>
  <tg-button type="url" url="tg://user?id=777000">user</tg-button>
  <tg-button type="callback_data" style="link" data="callback">callback with the date <tg-time unix="1647531900" format="wDT">22:45 tomorrow</tg-time> and the custom emoji <tg-emoji emoji-id="5368324170671202286">![👍](//telegram.org/img/emoji/40/F09F918D.png)</tg-emoji></tg-button>
  <tg-button type="web_app" style="danger" url="https://telegram.org">Mini App (private chats only)</tg-button>
  <tg-button type="login_url" url="https://t.me" forward-text="forward text" request-write-access>login (requires domain set up via @BotFather)</tg-button>
  <tg-button type="switch_inline_query" style="primary" query="inline">inline</tg-button>
  <tg-button type="switch_inline_query_current_chat" query="inline 2">inline 2</tg-button>
  <tg-button type="switch_inline_query_chosen_chat" query="inline 3" allow-user-chats allow-bot-chats allow-group-chats allow-channel-chats>inline 3</tg-button>
  <tg-button type="copy_text" text="...copy">Copy</tg-button>
  <tg-button type="disabled">Disabled</tg-button>
</p>
<tg-button-row align="left">
  <tg-button type="url" url="https://t.me">url</tg-button>
  <tg-button type="url" style="success" url="tg://user?id=777000">user</tg-button>
  <tg-button type="callback_data" style="link" data="callback">callback</tg-button>
</tg-button-row>
<tg-button-row align="center">
  <tg-button type="web_app" url="https://telegram.org">Mini App (private chats only)</tg-button>
</tg-button-row>
<tg-button-row align="center">
  <tg-button type="login_url" style="danger" url="https://t.me" forward-text="forward text" request-write-access>login (requires domain set up via @BotFather)</tg-button>
</tg-button-row>
<tg-button-row align="right">
  <tg-button type="switch_inline_query" query="inline">inline</tg-button>
  <tg-button type="switch_inline_query_current_chat" query="inline 2">inline 2</tg-button>
  <tg-button type="switch_inline_query_chosen_chat" query="inline 3" allow-user-chats allow-group-chats allow-channel-chats>inline 3</tg-button>
</tg-button-row>
<tg-button-row>
  <tg-button type="copy_text" text="...copy">Copy</tg-button>
  <tg-button type="disabled" style="primary">Disabled</tg-button>
</tg-button-row>
```

Additionally, you can use the following tag in [sendRichMessageDraft](https://core.telegram.org/bots/api#sendrichmessagedraft):

```
<tg-thinking>Thinking...</tg-thinking>
```

Please note:

* Rich Markdown is compatible with GitHub Flavored Markdown where possible and can contain arbitrary HTML. Supported rich message HTML tags are parsed as described in [Rich HTML style](https://core.telegram.org/bots/api#rich-html-style).
* Media can be specified only as a separate block.
* Media blocks support only HTTP and HTTPS URLs.
* Media type is determined by the MIME type and the URL of the media.
* In media syntax, the optional title after the URL is used as the caption; for example, ![](url "Photo caption") displays “Photo caption” under the media.
* Table cells can contain only inline formatting.
* Formula source is treated as raw LaTeX.
* Markdown isn't parsed inside block HTML tags other than <details>, <tg-collage> and <tg-slideshow>, therefore only HTML tags can be used there.
* See [date-time entity formatting](https://core.telegram.org/bots/api#date-time-entity-formatting) for more details about supported date-time formats.

###### Rich HTML style

To use this mode, pass rich message content in the *html* field. The following tags are currently supported:

```
<a name="chapter-0"></a>
<b>bold text</b>, <strong>bold text</strong>
<i>italic text</i>, <em>italic text</em>
<u>underlined text</u>, <ins>underlined text</ins>
<s>strikethrough text</s>, <strike>strikethrough text</strike>, <del>strikethrough text</del>
<code>inline fixed-width code</code>
<mark>marked text</mark>
<sub>subscript text</sub>
<sup>superscript text</sup>
<tg-spoiler>spoiler</tg-spoiler>

<a href="#note-1">Reference</a>
<a href="https://t.me/">inline URL</a>
<a href="mailto:user@example.com">inline e-mail</a>
<a href="tel:+123456789">inline phone number</a>
<a href="tg://user?id=123456789">inline mention of a user</a>
<a href="#chapter-1">in-document link</a>
<a name="chapter-1"></a>

<tg-reference name="note-1">Referenced text</tg-reference>
<tg-emoji emoji-id="5368324170671202286">![👍](//telegram.org/img/emoji/40/F09F918D.png)</tg-emoji>
<img src="tg://emoji?id=5368324170671202286" alt="![👍](//telegram.org/img/emoji/40/F09F918D.png)"/>
<tg-time unix="1647531900" format="wDT">22:45 tomorrow</tg-time>
<tg-math>x^2 + y^2</tg-math>

#hashtag $USD +12345678901, card: 4242 4242 4242 4242, https://t.me t.me a@t.me /command @username

all the text above was on the same line

<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>

<a name="chapter-2"></a>

<p>Paragraph text</p>
<pre>pre-formatted fixed-width code block</pre>
<pre><code class="language-python">  print('pre-formatted fixed-width code block written in the Python programming language')</code></pre>
<footer>Footer text</footer>
<hr/>
<ul><li>unordered list item</li></ul>
<ol><li>ordered list item</li></ol>
<ol start="3" type="a" reversed><li>ordered list item</li></ol>
<ol><li value="7" type="i">ordered list item with explicit number</li></ol>
<ul>
<li><input type="checkbox" checked>Checked checkbox</li>
<li><input type="checkbox">Unchecked checkbox</li>
</ul>

<blockquote>Block quotation started<br>Block quotation continued<br>The last line of the block quotation<cite>The Author</cite></blockquote>
<blockquote expandable>Expandable block quotation started<br>Expandable block quotation continued<br>Expandable block quotation continued<br>Expandable block quotation continued<br>The last line of the expandable block quotation<cite>The Author</cite></blockquote>
<aside>Pull quote<cite>The Author</cite></aside>

<img src="https://telegram.org/example/photo.jpg"/>
<video src="https://telegram.org/example/video.mp4"></video>
<audio src="https://telegram.org/example/audio.mp3"></audio>
<audio src="https://telegram.org/example/audio.ogg"></audio>
<video src="https://telegram.org/example/animation.gif"></video>
<tg-document src="https://telegram.org/example/document.zip"></tg-document>

<figure><img src="https://telegram.org/example/photo.jpg" tg-spoiler/><figcaption>Photo caption<cite>Photo credit</cite></figcaption></figure>
<figure><video src="https://telegram.org/example/video.mp4" tg-spoiler></video><figcaption>Video caption</figcaption></figure>
<figure><audio src="https://telegram.org/example/audio.mp3"></audio><figcaption>Audio caption</figcaption></figure>
<figure><audio src="https://telegram.org/example/audio.ogg"></audio><figcaption>Voice note caption</figcaption></figure>
<figure><video src="https://telegram.org/example/animation.gif" tg-spoiler></video><figcaption>Animation caption</figcaption></figure>
<figure><tg-document src="https://telegram.org/example/document.zip"></tg-document><figcaption>Document caption</figcaption></figure>

<tg-map lat="41.9" long="12.5" zoom="14"/>
<figure><tg-map lat="41.9" long="12.5" zoom="14"/><figcaption>Map caption</figcaption></figure>

<tg-collage><img src="https://telegram.org/example/photo.jpg"/><video src="https://telegram.org/example/video.mp4"/></tg-collage>
<tg-collage><video src="https://telegram.org/example/video.mp4"/><img src="https://telegram.org/example/photo.jpg"/><figcaption>Collage caption</figcaption></tg-collage>
<tg-slideshow><img src="https://telegram.org/example/photo.jpg"/><video src="https://telegram.org/example/video.mp4"/></tg-slideshow>
<tg-slideshow><video src="https://telegram.org/example/video.mp4"/><img src="https://telegram.org/example/photo.jpg"/><figcaption>Slideshow caption</figcaption></tg-slideshow>

<table><tr><th>Header 1</th><th>Header 2</th></tr><tr><td>Value 1</td><td>Value 2</td></tr></table>
<table bordered striped compact><caption>Table caption</caption>
<tr><td colspan="2" rowspan="2" align="left">Value</td><td align="center">Value2</td><td align="right">Value3</td></tr>
<tr><td valign="top">Value4</td><td valign="middle">Value5</td><td valign="bottom">Value6</td></tr>
<tr><td>Value7</td></tr></table>

<details><summary>Title</summary>Content</details>
<details open><summary>Title</summary>Content</details>
<tg-math-block>E = mc^2</tg-math-block>
<p>Inline buttons:
  <tg-button type="url" style="success" url="https://t.me">url</tg-button>
  <tg-button type="url" url="tg://user?id=777000">user</tg-button>
  <tg-button type="callback_data" style="link" data="callback">callback with the date <tg-time unix="1647531900" format="wDT">22:45 tomorrow</tg-time> and the custom emoji <tg-emoji emoji-id="5368324170671202286">![👍](//telegram.org/img/emoji/40/F09F918D.png)</tg-emoji></tg-button>
  <tg-button type="web_app" style="danger" url="https://telegram.org">Mini App (private chats only)</tg-button>
  <tg-button type="login_url" url="https://t.me" forward-text="forward text" request-write-access>login (requires domain set up via @BotFather)</tg-button>
  <tg-button type="switch_inline_query" style="primary" query="inline">inline</tg-button>
  <tg-button type="switch_inline_query_current_chat" query="inline 2">inline 2</tg-button>
  <tg-button type="switch_inline_query_chosen_chat" query="inline 3" allow-user-chats allow-bot-chats allow-group-chats allow-channel-chats>inline 3</tg-button>
  <tg-button type="copy_text" text="...copy">Copy</tg-button>
  <tg-button type="disabled">Disabled</tg-button>
</p>
<tg-button-row align="left">
  <tg-button type="url" url="https://t.me">url</tg-button>
  <tg-button type="url" style="success" url="tg://user?id=777000">user</tg-button>
  <tg-button type="callback_data" style="link" data="callback">callback</tg-button>
</tg-button-row>
<tg-button-row align="center">
  <tg-button type="web_app" url="https://telegram.org">Mini App (private chats only)</tg-button>
</tg-button-row>
<tg-button-row align="center">
  <tg-button type="login_url" style="danger" url="https://t.me" forward-text="forward text" request-write-access>login (requires domain set up via @BotFather)</tg-button>
</tg-button-row>
<tg-button-row align="right">
  <tg-button type="switch_inline_query" query="inline">inline</tg-button>
  <tg-button type="switch_inline_query_current_chat" query="inline 2">inline 2</tg-button>
  <tg-button type="switch_inline_query_chosen_chat" query="inline 3" allow-user-chats allow-group-chats allow-channel-chats>inline 3</tg-button>
</tg-button-row>
<tg-button-row>
  <tg-button type="copy_text" text="...copy">Copy</tg-button>
  <tg-button type="disabled" style="primary">Disabled</tg-button>
</tg-button-row>
```

Additionally, you can use the following tag in [sendRichMessageDraft](https://core.telegram.org/bots/api#sendrichmessagedraft):

```
<tg-thinking>Thinking...</tg-thinking>
```

Please note:

* Only the tags mentioned above are currently supported.
* All numerical HTML entities are supported.
* The API currently supports only the following named HTML entities: `&lt;`, `&gt;`, `&amp;`, `&quot;`, `&apos;`, `&nbsp;`, `&hellip;`, `&mdash;`, `&ndash;`, `&lsquo;`, `&rsquo;`, `&ldquo;` and `&rdquo;`.
* Use nested `pre` and `code` tags to define the programming language for a pre-formatted block.
* Programming language can't be specified for standalone `code` tags.
* Links `mailto:...`, `tel:...`, and `tg://user?id=...` are rendered as e-mail links, phone links, and inline mentions respectively. Other supported links are rendered as regular inline links.
* Images, videos, and audio files can be specified only as separate media blocks.
* Media blocks support only HTTP and HTTPS URLs.
* An empty `<a name="..."></a>` on its own creates an anchor that can be linked to with `<a href="#...">...</a>`.
* In `<figcaption>`, you can use `<cite>` tags to specify caption credit.
* Use `<tg-reference name="...">...</tg-reference>` to define referenced text that can be linked to with `<a href="#...">...</a>`.
* The body of a `<details>` tag can contain rich message content. If the `open` attribute is specified, the block is expanded by default.
* Formula source is treated as raw LaTeX.
* See [date-time entity formatting](https://core.telegram.org/bots/api#date-time-entity-formatting) for more details about supported date-time formats.