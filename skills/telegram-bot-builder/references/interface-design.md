# Telegram bot interface design guide

Use this guide when defining or implementing the visible experience of a Telegram bot. It covers chat-based interfaces; use a Mini App when the task needs dense forms, free layout, drag-and-drop, charts, maps, or long multi-column content.

The recommendations below are design guidance. API limits and supported formatting come from the bundled official Bot API snapshot. When they conflict, the API reference wins.

## Start with the product, not decoration

Before choosing a visual style, establish:

- the bot's primary job and the action users repeat most;
- whether it runs mainly in private chats, groups, channels, or several contexts;
- audience, language, tone, brand assets, and accessibility needs;
- the three to six destinations that deserve the main menu;
- whether the owner is eligible for custom emoji and wants the bundled set;
- whether a stable illustrated menu or a compact text interface fits the use case;
- whether any workflow is complex enough to become a Mini App.

Aim for a recognizable system rather than constant novelty: one voice, one family of covers, stable button labels, predictable Back and Home positions, and consistent status language.

## The default interaction model

Treat a bot-authored message as a screen. In private chat, prefer one current navigation message that changes in place over a trail of nearly identical menu messages.

For an illustrated main menu:

1. Send a photo with `sendPhoto`.
2. Put the title, short explanation, optional status or quotation, and current context in `caption`.
3. Attach the primary actions as an `InlineKeyboardMarkup`.
4. Save `chat_id` and the returned `message_id` as the user's current screen.
5. On every callback, call `answerCallbackQuery` promptly so Telegram stops the loading indicator.
6. Navigate with `editMessageCaption`, `editMessageReplyMarkup`, or `editMessageMedia`. Reuse Telegram `file_id` values for stable assets.
7. If the stored screen was deleted or can no longer be edited, send a replacement and update the stored message ID.

Use `show_caption_above_media=true` when the text should read like a heading before the hero image. Leave it false when the image is the first visual impression. Check both compositions on a narrow phone screen.

Do not force a single-message shell onto conversational flows. User input, confirmations, receipts, support answers, generated content, and auditable events often deserve separate messages. In groups, avoid deleting or rewriting context other participants may rely on.

### Main menu example using HTML

```html
<b>Название сервиса</b>
<blockquote>Короткая фраза, которая объясняет пользу бота.</blockquote>

Выберите, что хотите сделать:
```

Suggested keyboard shape:

```text
[Primary action]
[Catalog] [Profile]
[Help] [Settings]
```

Use one full-width first row when there is a clear primary action. Use two buttons per row for short peer actions. Use one button per row for long labels, destructive actions, URLs, payments, or actions requiring extra attention.

## Visual hierarchy in Telegram text

Telegram controls the font family, size, colors, and rendering. Create hierarchy with structure and supported entities:

- bold for the screen title, key amount, selected plan, or final result;
- italic for a short secondary note, voice, or attribution;
- underline sparingly for a critical phrase that still needs emphasis after bold;
- strikethrough for a former price or explicitly unavailable option;
- spoiler for user-requested concealment, sensitive values, hints, or answer reveals;
- inline code for identifiers, commands, filenames, and short values;
- preformatted blocks for copyable code, logs, or structured technical output;
- blockquotes for a compact callout, summary, testimonial, rule, or quoted content;
- expandable blockquotes for optional detail that would otherwise dominate the screen;
- inline links for secondary destinations; use buttons for primary actions;
- custom emoji for a small, consistent icon vocabulary when eligibility is confirmed.

Avoid Unicode “fancy font” alphabets. They are not Telegram typography, search and copy poorly, can break screen readers, and often lack Cyrillic. Do not imitate headings with excessive capitals, decorative separators, repeated symbols, or long emoji rows.

Use no more than three emphasis levels on an ordinary screen: title, body, muted note or callout. Keep paragraphs short and leave blank lines between semantic groups. A user should understand the screen before opening the keyboard.

### Quotes and citations are different features

Use a blockquote entity when the quote is part of the bot's own formatted content:

```html
<blockquote>Обычная цитата или выделенный итог.</blockquote>
<blockquote expandable>Подробности, которые можно раскрыть по желанию.</blockquote>
```

Use `ReplyParameters` when the bot replies to an existing Telegram message and must quote an exact substring of it. Its `quote` must match the original message, and `quote_position` uses UTF-16 code units. Never rebuild a real reply quote as a decorative blockquote when provenance matters.

For testimonials or sourced statements, include a short attribution and a link when one exists. Do not style ordinary instructions as quotations merely to add a colored bar.

## Formatting implementation

Prefer HTML when the project has no established parse mode: templates are readable and escaping is straightforward when done centrally. MarkdownV2 is also valid, but every dynamic value must be escaped correctly. Never concatenate untrusted text into either parse mode without escaping it.

Supported classic message styling includes bold, italic, underline, strikethrough, spoiler, blockquote, expandable blockquote, code, preformatted code, links, custom emoji, and date-time entities. Arbitrary fonts, text sizes, text colors, backgrounds, margins, or alignment are not available in classic Bot API messages.

Keep a small rendering layer rather than scattering tags through handlers:

```text
renderScreen(state, locale, capabilities) -> text/caption + entities + keyboard + media
```

This makes escaping, localization, custom-emoji fallbacks, length limits, and snapshots testable in one place. Prefer explicit `MessageEntity` arrays when composing heavily dynamic or nested formatting; remember that offsets and lengths are measured in UTF-16 code units.

Use `caption_entities` for a media screen and `entities` for a text screen. A classic photo caption is limited to 1024 characters after entity parsing; ordinary text has a larger limit. If the menu needs extensive explanation, keep the caption compact and open details in a separate text screen, expandable quote, Rich Message, or Mini App.

## Images and media

Every image should have a job: establish the section, explain a result, preview an item, build trust, or show progress. Avoid a different random illustration on every screen.

For a coherent menu system:

- create one cover family with the same aspect ratio, safe margins, palette, composition, and text treatment;
- keep important subjects away from edges because clients and previews may crop differently;
- avoid baking essential instructions into the image; repeat them in the caption;
- keep text inside artwork brief and large enough for a phone;
- use the bot name or symbol subtly rather than turning every cover into an advertisement;
- retain the returned `file_id` after the first upload and reuse it;
- provide a text-only path when media fails or bandwidth is limited.

Use `editMessageMedia` when a section has its own meaningful cover. Use `editMessageCaption` when the visual identity stays constant and only the screen content changes. Avoid animation on routine navigation; motion is useful for onboarding, completion, or a rare celebratory moment.

Do not claim that an image is “attached to the menu” as a separate Telegram object. The reliable pattern is a media message whose caption and inline keyboard form the menu screen.

## Buttons and navigation

Write buttons as clear actions or destinations: “Создать заказ”, “Мои файлы”, “Назад”. Avoid vague labels such as “Далее” when the result is not obvious. Keep terminology identical between headings, messages, commands, and buttons.

Use inline keyboards for local navigation and contextual actions. Use reply keyboards only when persistent, chat-level actions materially reduce typing. A reply keyboard occupies input space and should be removable. Use the menu button and BotFather command list for stable global entry points, not as substitutes for a clear home screen.

Button rules:

- put the most likely action first;
- keep dangerous actions isolated and require confirmation;
- include Back on subpages and Home in deeper flows;
- do not show controls the user cannot use;
- preserve user context when returning from a detail screen;
- paginate long lists instead of building a wall of buttons;
- encode compact opaque identifiers in `callback_data`; it is limited to 64 bytes;
- never place secrets or trusted authorization state in callback data;
- acknowledge callbacks immediately, then perform slow work;
- use a brief callback toast for lightweight confirmation and an alert only when interruption is necessary.

Current Bot API supports optional button styles such as `primary`, `success`, and `danger`, plus custom emoji icons and disabled buttons. Use color semantically and sparingly. The label must remain understandable without color or an icon.

## State, feedback, and recovery

Every action needs an immediate visible response. For fast callbacks, update the screen. For slow work, acknowledge the callback, show a compact working state, then replace it with the result.

Use stable patterns:

- loading: state what is happening and allow cancellation when feasible;
- empty: explain why the list is empty and offer the next useful action;
- success: name what changed and show the next step;
- validation error: keep entered values when possible and point to the exact field;
- system error: explain what the user can do now; keep technical details out of the primary message;
- expired state: refresh safely instead of leaving dead buttons;
- destructive confirmation: name the object and consequence, then offer Cancel and Confirm;
- retry: make repeated callbacks idempotent so double taps do not duplicate payments, orders, or jobs.

Never leave a callback spinner running. Never silently fail after a button press. Avoid success messages that merely say “Done” without identifying the completed action.

## Copy and tone

Write for scanning on a phone. Lead with the result or required action. Put explanation after it. Prefer one idea per paragraph and one primary call to action per screen.

Use emoji as icons, not punctuation. Assign stable meanings, for example: check for completed, warning for attention, lock for privacy, folder for files. When custom emoji are enabled, keep their Unicode fallbacks and meanings identical across the interface.

Avoid fake urgency, excessive exclamation marks, guilt, and unexplained technical errors. Confirm irreversible or costly actions with concrete language. Localize whole messages and button labels; do not mix languages unless the product requires it.

## Rich Messages and Mini Apps

The bundled Bot API 10.3 snapshot includes Rich Messages with headings, paragraphs, lists, quotes, tables, media, details, and other structured blocks. Consider them for long reports, AI output, documentation, catalogs, or structured results. Keep core navigation and critical actions usable with familiar message and keyboard patterns unless the target clients and bot framework have been verified against Rich Messages.

Choose a Mini App when the workflow needs several inputs on one screen, live validation, custom charts, maps, dense comparison, complex filtering, drag-and-drop, or branded layout beyond Telegram message formatting. Preserve a clear route back to the chat and summarize important outcomes in chat after the Mini App closes.

## Accessibility and internationalization

- Never encode status only through color, emoji, image, or button position.
- Keep meaningful Unicode fallback text for custom emoji.
- Do not put essential text only inside an image.
- Use descriptive button labels and readable link text.
- Test long translations, right-to-left text when supported, plural forms, dates, currency, and timezone-sensitive content.
- Use Telegram date-time entities when localized dates or relative times improve comprehension.
- Treat screen-reader order as message order: title, status, explanation, next action.
- Keep commands usable for people who do not interact with the decorative menu.

## Quality checklist

Before calling a bot interface finished, verify:

- `/start` explains the value and presents a clear first action;
- the main menu has no more top-level destinations than users can scan quickly;
- every visible button works and every callback is acknowledged;
- Back and Home behavior is consistent;
- navigation does not flood private chat with duplicate screens;
- text and captions remain within Bot API limits after entity parsing;
- dynamic HTML or MarkdownV2 content is escaped;
- UTF-16 entity offsets are correct;
- custom emoji eligibility and fallback behavior are handled;
- every screen has loading, empty, error, and expired-state behavior where applicable;
- destructive and paid actions require an explicit confirmation;
- images share a coherent visual system and essential information remains textual;
- the interface works with custom emoji disabled and media unavailable;
- layouts were inspected in Telegram on a narrow phone and desktop client;
- the bot can recover if its stored menu message was deleted.

## Official reference map

Consult these bundled files for implementation details:

- `../../../docs/bot-api/formatting-options.md`
- `../../../docs/bot-api/replyparameters.md`
- `../../../docs/bot-api/sendphoto.md`
- `../../../docs/bot-api/editmessagecaption.md`
- `../../../docs/bot-api/editmessagemedia.md`
- `../../../docs/bot-api/editmessagereplymarkup.md`
- `../../../docs/bot-api/inlinekeyboardbutton.md`
- `../../../docs/bot-api/callbackquery.md`
- `../../../docs/bot-api/linkpreviewoptions.md`
- `../../../docs/bot-api/sendrichmessage.md`
- `../../../docs/bot-api/rich-message-formatting-options.md`
- `../../../docs/bot-api/webappinfo.md`
