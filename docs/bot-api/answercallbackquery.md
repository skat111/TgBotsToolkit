Source: https://core.telegram.org/bots/api#answercallbackquery
Snapshot: 2026-09-17T08:42:18Z

#### answerCallbackQuery

Use this method to send answers to callback queries sent from [inline keyboards](https://core.telegram.org/bots/features#inline-keyboards). The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, *True* is returned.

> Alternatively, the user can be redirected to the specified Game URL. For this option to work, you must first create a game for your bot via [@BotFather](https://t.me/botfather) and accept the terms. Otherwise, you may use links like `t.me/your_bot?start=XXXX` that open your bot with a parameter.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| callback_query_id | String | Yes | Unique identifier for the query to be answered |
| text | String | Optional | Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters. |
| show_alert | Boolean | Optional | If *True*, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to *False*. |
| url | String | Optional | URL that will be opened by the user's client. If you have created a [Game](https://core.telegram.org/bots/api#game) and accepted the conditions via [@BotFather](https://t.me/botfather), specify the URL that opens your game - note that this will only work if the query comes from a [*callback_game*](https://core.telegram.org/bots/api#inlinekeyboardbutton) button.  Otherwise, you may use links like `t.me/your_bot?start=XXXX` that open your bot with a parameter. |
| cache_time | Integer | Optional | The maximum amount of time in seconds that the result of the callback query may be cached client-side. Defaults to 0. |