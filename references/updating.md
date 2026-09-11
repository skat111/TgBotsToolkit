# Keeping the toolkit current

The updater checks the latest GitHub Release before bot work. Releases contain `telegram-bot-toolkit.zip` and its `.sha256` file. The installer validates archive paths, plugin name, and checksum, then creates a backup in the sibling `<plugin>.backups` directory before replacing the plugin.

Configure the repository with `TELEGRAM_BOT_TOOLKIT_REPO=owner/repo`, or add a GitHub `origin` to the plugin checkout. The scheduled workflow in `.github/workflows/refresh-telegram-docs.yml` checks Telegram sources, refreshes the snapshot when their hashes change, validates it, and publishes a release asset.
