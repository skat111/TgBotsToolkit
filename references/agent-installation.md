# Установка в AI-агенты

Плагин хранит документацию и инструкции в одной папке, а `scripts/install_agents.py` создаёт маленькие адаптеры под конкретные среды. Это экономит место и позволяет всем агентам использовать один обновляемый снимок Telegram API.

Из корня плагина:

```powershell
python scripts/install_agents.py --target all --project C:\path\to\your\bot
```

Доступны цели `codex`, `claude`, `cursor`, `gemini`, `cline`, `roo`, `continue`, `windsurf`, `opencode` и `aider`. Для уже существующего файла установщик ничего не перезаписывает; `--force` создаёт `.telegram-toolkit.bak` рядом с ним.

Для Cursor создаётся `.cursor/rules/telegram-bot-toolkit.mdc`, для Gemini — `GEMINI.md`, для Claude — глобальный skill в `~/.claude/skills/`, для Cline/Roo/Continue/Windsurf — их project rules, для OpenCode — `AGENTS.md`, для Aider — `CONVENTIONS.md`. Codex использует официальный `.codex-plugin` и получает только установочную памятку.

GLM-агенты, которые поддерживают формат `AGENTS.md`, подключаются через цель `opencode`; если конкретный клиент использует собственный каталог правил, передайте его адаптеру вручную, сохранив ссылку на этот toolkit.
