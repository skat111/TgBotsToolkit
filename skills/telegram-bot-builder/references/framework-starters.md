# Framework starters

Generate a project from the skill directory:

```sh
python scripts/generate_starter.py aiogram ./my-bot
python scripts/generate_starter.py python-telegram-bot ./my-bot
python scripts/generate_starter.py telegraf ./my-bot
python scripts/generate_starter.py grammy ./my-bot
```

Add the production stack with `--production`:

```sh
python scripts/generate_starter.py aiogram ./my-bot --production
```

Production mode adds Docker, PostgreSQL, Redis, an initial SQL migration, RU/EN locale catalogs, webhook environment variables, health checks, and framework-specific tests. Read the generated `PRODUCTION.md` before deployment.

Choose the framework requested by the user. If none is requested, prefer aiogram for an async Python project, python-telegram-bot for an established Python codebase already using it, Telegraf for a Node.js project using its middleware ecosystem, and grammY for a TypeScript-oriented or composable Node.js project. Do not replace a framework already present in a repository.

Each starter includes `/start`, an editable main-menu message, profile, settings, catalog, product, and destructive-confirmation screens. It supports a shared photo through `MENU_PHOTO` and optional custom emoji through `CUSTOM_EMOJI_ENABLED`.

The generated code is a clean starting point, not a complete production architecture. Adapt copy and routes using `screen-templates.md`. Add persistence before relying on navigation state, and add webhook deployment, authorization, localization, payment verification, structured logging, and domain services only when the product needs them.

Never place a real bot token in generated source, `.env.example`, logs, tests, or commits. Keep `BOT_TOKEN` in the deployment environment or a local ignored `.env` file.

Official framework documentation used for these starters:

- aiogram: https://docs.aiogram.dev/en/latest/quick_start.html
- python-telegram-bot: https://docs.python-telegram-bot.org/en/stable/examples.inlinekeyboard2.html
- Telegraf: https://telegraf.js.org/
- grammY: https://grammy.dev/guide/getting-started
