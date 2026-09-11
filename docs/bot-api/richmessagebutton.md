Source: https://core.telegram.org/bots/api#richmessagebutton
Snapshot: 2026-09-11T06:04:42Z

#### RichMessageButton

This object represents a button in a [RichMessage](https://core.telegram.org/bots/api#richmessage). Exactly one of the fields other than *text* and *style* must be used to specify the type of the button.

| Field | Type | Description |
| --- | --- | --- |
| text | [RichText](https://core.telegram.org/bots/api#richtext) | Text of the button. May contain only plain text, [RichTextCustomEmoji](https://core.telegram.org/bots/api#richtextcustomemoji) and [RichTextDateTime](https://core.telegram.org/bots/api#richtextdatetime) entities. |
| style | String | *Optional*. Style of the button. Must be one of “danger”, “success”, “primary”, or “link” (the button is shown as a regular link without borders). Apps may use theme-specific colors for the button background and text based on the style. The style “link” is allowed only for callback buttons. |
| url | String | *Optional*. HTTP or tg:// URL to be opened when the button is pressed. Links `tg://user?id=<user_id>` can be used to mention a user by their identifier without using a username, if this is allowed by their privacy settings. |
| callback_data | String | *Optional*. Data to be sent in a [callback query](https://core.telegram.org/bots/api#callbackquery) to the bot when the button is pressed, 1-64 bytes |
| web_app | [WebAppInfo](https://core.telegram.org/bots/api#webappinfo) | *Optional*. Description of the [Web App](https://core.telegram.org/bots/webapps) that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method [answerWebAppQuery](https://core.telegram.org/bots/api#answerwebappquery). Available only in private chats between a user and the bot. Not supported for messages sent on behalf of a business account. |
| login_url | [LoginUrl](https://core.telegram.org/bots/api#loginurl) | *Optional*. An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the [Telegram Login Widget](https://core.telegram.org/widgets/login). Not supported for ephemeral messages. |
| switch_inline_query | String | *Optional*. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted. Not supported for messages sent in channel direct messages chats and on behalf of a business account. |
| switch_inline_query_current_chat | String | *Optional*. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted. Not supported in channels and for messages sent in channel direct messages chats and on behalf of a business account. |
| switch_inline_query_chosen_chat | [SwitchInlineQueryChosenChat](https://core.telegram.org/bots/api#switchinlinequerychosenchat) | *Optional*. If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot's username and the specified inline query in the input field. Not supported for messages sent in channel direct messages chats and on behalf of a business account. |
| copy_text | [CopyTextButton](https://core.telegram.org/bots/api#copytextbutton) | *Optional*. A button that copies the specified text to the clipboard |
| disabled | [DisabledButton](https://core.telegram.org/bots/api#disabledbutton) | *Optional*. If set, then the button is disabled and does nothing |