Source: https://core.telegram.org/bots/api#paid-broadcasts
Snapshot: 2026-09-24T08:30:39Z

#### Paid Broadcasts

By default, all bots are able to broadcast up to [30 messages](https://core.telegram.org/bots/faq#my-bot-is-hitting-limits-how-do-i-avoid-this) per second to their users. Developers can increase this limit by enabling *Paid Broadcasts* in [@BotFather](https://t.me/botfather) - allowing their bot to broadcast **up to 1000 messages** per second.

Each message broadcasted over the free amount of 30 messages per second incurs a cost of 0.1 Stars per message, paid with Telegram Stars from the bot's balance. In order to use this feature, a bot must have at least *10,000 Stars* on its balance.

> Bots with increased limits are only charged for messages that are broadcasted successfully.