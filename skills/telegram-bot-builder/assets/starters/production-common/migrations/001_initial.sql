CREATE TABLE IF NOT EXISTS bot_users (
    telegram_user_id BIGINT PRIMARY KEY,
    locale TEXT NOT NULL DEFAULT 'ru',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS screen_state (
    telegram_user_id BIGINT PRIMARY KEY REFERENCES bot_users(telegram_user_id) ON DELETE CASCADE,
    chat_id BIGINT NOT NULL,
    message_id BIGINT NOT NULL,
    screen_id TEXT NOT NULL,
    state JSONB NOT NULL DEFAULT '{}'::jsonb,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS processed_updates (
    update_id BIGINT PRIMARY KEY,
    processed_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS screen_state_updated_at_idx ON screen_state(updated_at);
