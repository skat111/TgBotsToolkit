Source: https://core.telegram.org/bots/api#making-requests-when-getting-updates
Snapshot: 2026-09-15T08:44:15Z

#### Making requests when getting updates

If you're using [**webhooks**](https://core.telegram.org/bots/api#getting-updates), you can perform a request to the Bot API while sending an answer to the webhook. Use either *application/json* or *application/x-www-form-urlencoded* or *multipart/form-data* response content type for passing parameters. Specify the method to be invoked in the *method* parameter of the request. It's not possible to know that such a request was successful or get its result.

> Please see our [FAQ](https://core.telegram.org/bots/faq#how-can-i-make-requests-in-response-to-updates) for examples.