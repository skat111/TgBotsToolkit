---

Before starting work, run `python scripts/check_updates.py --check` from the plugin root (or `python ../../scripts/check_updates.py --check` from this skill). If it reports `update_available`, run the same command with `--install`; the installer verifies the GitHub checksum and keeps a backup beside the plugin. Set `TELEGRAM_BOT_TOOLKIT_REPO=owner/repo` when the plugin is not a Git checkout with a GitHub `origin`. If GitHub is temporarily unavailable, continue with the bundled snapshot and report that fact.
name: telegram-bot-builder
description: Design, implement, and debug Telegram bots using the bundled official API reference, including optional custom emoji UI styling.
---

Use the official snapshot under `../../docs/` for Telegram-specific behavior. Start with `../../docs/START_HERE.md`; for Bot API methods and types use `../../docs/bot-api/INDEX.md` and the individual files it links.

For any user-facing bot flow, read `references/interface-design.md` before designing messages, menus, navigation, formatting, or media. Apply its interaction model and quality checklist. Adapt the visual direction to the product and audience instead of copying one decorative style everywhere.

When the bot needs common screens, read `references/screen-templates.md` and use `references/screen-catalog.json` as a framework-neutral starting point. Remove irrelevant templates, adapt every placeholder to the domain, and map all visible buttons to real handlers. Do not present the catalog as finished product copy.

After changing the machine-readable catalog, run `python scripts/validate_screen_catalog.py` from this skill directory.

When creating a new implementation, read `references/framework-starters.md`. Generate the requested framework with `python scripts/generate_starter.py FRAMEWORK DESTINATION`, then adapt the generated project instead of rewriting framework boilerplate. Preserve an existing repository's framework and conventions.

When beginning a new bot implementation or taking over a bot whose UI conventions are not established, ask once whether the Telegram account that owns the bot in BotFather currently has Telegram Premium. Also ask whether the bot has an additional username purchased on Fragment when Premium is absent or uncertain. Do not ask again after the user answers unless ownership or subscription status changes.

If the owner has Premium, ask whether to use the bundled custom emoji set in bot-authored interface messages. Treat this as an optional visual preference. If accepted, read `references/custom-emoji.json` and select emoji by semantic role. Keep ordinary Unicode fallback text meaningful and do not fill every message with decorative emoji.

Apply the Bot API restriction recorded in `../../docs/bot-api/formatting-options.md`: owner Premium enables custom emoji only in messages sent directly by the bot to private chats, groups, and supergroups. A bot with an additional username purchased on Fragment has the separate eligibility described there. Do not assume custom emoji work in unsupported contexts.

Bot API does not expose the Premium state of the BotFather owner through `getMe`; rely on the user's answer. Before using entries whose `fallback` is null, call `getCustomEmojiStickers` with the bot token and fill in the returned sticker `emoji` value. Never invent a fallback. If credentials or network access are unavailable, use only entries with known fallbacks.

Prefer HTML with `<tg-emoji emoji-id="ID">fallback</tg-emoji>` when the project already uses HTML parse mode. For MarkdownV2, use `![fallback](tg://emoji?id=ID)` and escape surrounding text according to Telegram's rules. When the project builds `MessageEntity` objects directly, use type `custom_emoji`, set `custom_emoji_id`, and calculate UTF-16 offsets and lengths correctly.

If the user says Premium is unavailable and the Fragment condition is also unavailable, keep the same interface wording with ordinary Unicode emoji rather than emitting custom emoji markup.
