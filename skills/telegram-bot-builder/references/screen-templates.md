# Reusable Telegram bot screen templates

Use these templates as a starting system, then rewrite the copy, destinations, fields, and visual direction for the actual bot. Do not expose braces or placeholder names to users. The machine-readable companion is `screen-catalog.json`.

## Shared shell

Render screens through one adapter that receives `screen_id`, locale, user data, domain data, and capabilities. Capabilities include media availability, custom emoji eligibility, and framework support for current Bot API features.

For private-chat navigation, keep the current screen's `chat_id`, `message_id`, and media kind. Use edit methods when possible. On an edit failure caused by a missing or incompatible message, send the target screen again and replace the stored ID.

Suggested state flow:

```mermaid
flowchart LR
    Start[/start] --> Home[Main menu]
    Home --> Catalog
    Home --> Profile
    Home --> Settings
    Catalog --> Product[Product card]
    Product --> Checkout[Payment summary]
    Checkout --> Confirm[Payment confirmation]
    Confirm --> Success[Payment success]
    Product --> Catalog
    Profile --> Home
    Settings --> Home
    Catalog --> Home
```

Keep callback data compact and version it only when an actual migration needs it. Resolve authorization and prices from trusted server state, never from callback payloads.

## `/start`

Purpose: explain the bot in one glance and move the user into the primary task.

```html
<b>{product_name}</b>
<blockquote>{one_sentence_value}</blockquote>

{welcome_line}
```

Keyboard:

```text
[{primary_action}]
[{secondary_action}] [{help_action}]
```

For a returning user, replace generic onboarding with useful context: an unfinished action, recent item, balance, next appointment, or other relevant state. Do not repeat a long introduction on every `/start`.

## Main menu

Purpose: provide three to six stable destinations and a clear primary action.

```html
<b>{greeting_or_product_name}</b>
<blockquote>{current_status_or_short_value}</blockquote>

Выберите раздел:
```

Keyboard:

```text
[{primary_action}]
[{catalog}] [{profile}]
[{help}] [{settings}]
```

Use one branded cover for the menu. A live status belongs in the caption, not baked into the image.

## Profile

Purpose: show identity and the few account facts needed for decisions.

```html
<b>{icon.profile} Профиль</b>

{display_name}
ID: <code>{user_id}</code>
{membership_or_plan_line}

<blockquote>{account_summary}</blockquote>
```

Keyboard:

```text
[Редактировать профиль]
[История] [Поддержка]
[← Назад] [Главное меню]
```

Mask sensitive values. Show a Copy button when users regularly need an identifier.

## Settings

Purpose: make current values visible and changes reversible.

```html
<b>{icon.settings} Настройки</b>

Язык: <b>{language}</b>
Уведомления: <b>{notifications_state}</b>
Оформление: <b>{appearance_state}</b>
```

Keyboard:

```text
[Язык · {language_short}]
[Уведомления · {notifications_short}]
[Оформление · {appearance_short}]
[← Назад] [Главное меню]
```

Put the current value in each button or adjacent text. Apply simple toggles immediately and confirm with a callback toast. Open a choice screen for settings with more than two meaningful values.

## Catalog

Purpose: let users scan categories or a short page of items without a keyboard wall.

```html
<b>{icon.catalog} {catalog_title}</b>
<i>{result_count_line}</i>

{short_filter_summary}
<blockquote expandable>{optional_catalog_help}</blockquote>
```

Keyboard:

```text
[{item_1_label}]
[{item_2_label}]
[‹] [{page}/{pages}] [›]
[Фильтры] [Поиск]
[← Назад] [Главное меню]
```

Do not render disabled pagination controls as active callbacks. Use a disabled button when supported, or omit the unavailable direction. Keep prices and distinguishing attributes in labels only when they remain easy to scan.

Empty catalog variant:

```html
<b>Ничего не найдено</b>
<blockquote>Измените фильтры или сбросьте поиск.</blockquote>
```

## Product or service card

Purpose: make the decision possible from one screen.

```html
<b>{product_title}</b>
{short_description}

<b>{price}</b> {old_price_if_any}
{availability_line}

<blockquote expandable>{details}</blockquote>
```

Keyboard:

```text
[Выбрать · {price}]
[Подробнее] [Поделиться]
[← К списку] [Главное меню]
```

Use a product image when it helps recognition. Do not hide price, availability, delivery terms, or important restrictions inside the expandable section.

## Payment summary

Purpose: show exactly what will be purchased before opening payment.

```html
<b>{icon.wallet} Проверка заказа</b>

{item_name}
Количество: <b>{quantity}</b>
Итого: <b>{total}</b>

<blockquote>{delivery_or_fulfilment_summary}</blockquote>
```

Keyboard:

```text
[Оплатить {total}]
[Изменить заказ]
[Отмена]
```

Use the Bot API payment button rules for invoices. Re-read price, inventory, currency, and entitlement from server state immediately before creating the invoice. Never trust the total embedded in callback data.

## Payment success

Purpose: confirm the outcome and make fulfilment obvious.

```html
<b>{icon.success} Оплата прошла</b>

Заказ: <code>{order_number}</code>
Сумма: <b>{total}</b>
{fulfilment_status}

<blockquote>{what_happens_next}</blockquote>
```

Keyboard:

```text
[Открыть покупку]
[Получить чек]
[Главное меню]
```

Create fulfilment idempotently from the successful payment identifier. A repeated update must not issue the item twice.

## Destructive confirmation

Purpose: prevent accidental irreversible actions.

```html
<b>{icon.warning} Подтвердите действие</b>

Вы собираетесь {action_description}.
<blockquote>{specific_consequence}</blockquote>

Это действие {reversibility_statement}.
```

Keyboard:

```text
[Отмена]
[{explicit_confirm_label}]
```

Place Cancel first. The confirmation label should name the action, such as “Удалить проект”, rather than “Да”. Use the danger style when available.

## Loading

Purpose: acknowledge work that cannot complete immediately.

```html
<b>{icon.loading} {work_title}</b>
<i>{progress_or_expectation}</i>

<blockquote>{safe_to_leave_note}</blockquote>
```

Keyboard when cancellation is supported:

```text
[Отменить]
```

Update only on meaningful progress to avoid flicker and rate-limit pressure. Do not promise a duration unless it is dependable.

## Validation error

Purpose: explain how to correct user input without discarding it.

```html
<b>{icon.error} Проверьте данные</b>

Поле «{field_label}»: {plain_language_problem}
<blockquote>{valid_example_or_constraint}</blockquote>
```

Keyboard:

```text
[Исправить]
[Отмена]
```

Do not expose stack traces, database names, or internal validation codes.

## System error

Purpose: provide recovery without blaming the user.

```html
<b>{icon.error} Не удалось выполнить действие</b>

{plain_language_effect}
<blockquote>{recovery_instruction}</blockquote>

Код обращения: <code>{support_code}</code>
```

Keyboard:
```text
[Повторить]
[Поддержка]
[Главное меню]
```

Generate a non-secret support code that maps to server logs. Show Retry only for operations safe to repeat.

## Expired screen

Purpose: recover from old callback buttons or changed server state.

```html
<b>{icon.info} Экран устарел</b>
<blockquote>Данные изменились с момента открытия этого сообщения.</blockquote>

Обновите экран, чтобы продолжить.
```

Keyboard:

```text
[Обновить]
[Главное меню]
```

## Template adaptation checklist

For every bot, replace generic nouns with domain language, choose one primary action, remove irrelevant screens, and add domain-specific states. Verify that every placeholder is resolved, all callback routes exist, media has a text fallback, custom emoji can be disabled, and all user-visible strings pass through localization.
