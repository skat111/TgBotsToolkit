# Production setup

The stack includes the bot, PostgreSQL, Redis, an initial idempotent SQL migration, RU/EN locale catalogs, webhook configuration, container health checks, and starter tests.

Set a public HTTPS `WEBHOOK_BASE_URL`, a random `WEBHOOK_SECRET` containing only letters, digits, `_` or `-`, a strong `POSTGRES_PASSWORD`, and the bot token. `WEBHOOK_PATH` defaults to `/telegram/webhook` and `PORT` to `8080`.

```sh
docker compose up --build
```

The SQL in `migrations/` is applied automatically only when PostgreSQL initializes an empty data volume. Use a migration runner such as Alembic, Flyway, or node-pg-migrate before changing an existing production database.

Redis and PostgreSQL are provisioned for durable screen state, idempotency, caching, locks, and jobs. Connect them in domain services as those features are implemented; do not add database calls directly to Telegram handlers.

Terminate TLS at the hosting platform or reverse proxy and forward webhook traffic to the bot container. Never expose PostgreSQL or Redis ports publicly. Rotate `WEBHOOK_SECRET` and the BotFather token if either leaks.
