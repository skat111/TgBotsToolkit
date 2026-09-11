Source: https://core.telegram.org/bots/api#update
Snapshot: 2026-09-11T06:04:42Z

#### Update

This [object](https://core.telegram.org/bots/api#available-types) represents an incoming update.  
At most **one** of the optional fields can be present in any given update.

| Field | Type | Description |
| --- | --- | --- |
| update_id | Integer | The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This identifier becomes especially handy if you're using [webhooks](https://core.telegram.org/bots/api#setwebhook), since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially. |
| message | [Message](https://core.telegram.org/bots/api#message) | *Optional*. New incoming message of any kind - text, photo, sticker, etc. |
| edited_message | [Message](https://core.telegram.org/bots/api#message) | *Optional*. New version of a message that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot. |
| channel_post | [Message](https://core.telegram.org/bots/api#message) | *Optional*. New incoming channel post of any kind - text, photo, sticker, etc. |
| edited_channel_post | [Message](https://core.telegram.org/bots/api#message) | *Optional*. New version of a channel post that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot. |
| business_connection | [BusinessConnection](https://core.telegram.org/bots/api#businessconnection) | *Optional*. The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot |
| business_message | [Message](https://core.telegram.org/bots/api#message) | *Optional*. New message from a connected business account |
| edited_business_message | [Message](https://core.telegram.org/bots/api#message) | *Optional*. New version of a message from a connected business account |
| deleted_business_messages | [BusinessMessagesDeleted](https://core.telegram.org/bots/api#businessmessagesdeleted) | *Optional*. Messages were deleted from a connected business account |
| guest_message | [Message](https://core.telegram.org/bots/api#message) | *Optional*. New guest message. The bot can use the field *Message.guest_query_id* and the method [answerGuestQuery](https://core.telegram.org/bots/api#answerguestquery) to send a message in response. |
| message_reaction | [MessageReactionUpdated](https://core.telegram.org/bots/api#messagereactionupdated) | *Optional*. A reaction to a message was changed by a user. The bot must be an administrator in the chat and must explicitly specify `"message_reaction"` in the list of *allowed_updates* to receive these updates. The update isn't received for reactions set by bots. |
| message_reaction_count | [MessageReactionCountUpdated](https://core.telegram.org/bots/api#messagereactioncountupdated) | *Optional*. Reactions to a message with anonymous reactions were changed. The bot must be an administrator in the chat and must explicitly specify `"message_reaction_count"` in the list of *allowed_updates* to receive these updates. The updates are grouped and can be sent with delay up to a few minutes. |
| inline_query | [InlineQuery](https://core.telegram.org/bots/api#inlinequery) | *Optional*. New incoming [inline](https://core.telegram.org/bots/api#inline-mode) query |
| chosen_inline_result | [ChosenInlineResult](https://core.telegram.org/bots/api#choseninlineresult) | *Optional*. The result of an [inline](https://core.telegram.org/bots/api#inline-mode) query that was chosen by a user and sent to their chat partner. Please see our documentation on the [feedback collecting](https://core.telegram.org/bots/inline#collecting-feedback) for details on how to enable these updates for your bot. |
| callback_query | [CallbackQuery](https://core.telegram.org/bots/api#callbackquery) | *Optional*. New incoming callback query |
| shipping_query | [ShippingQuery](https://core.telegram.org/bots/api#shippingquery) | *Optional*. New incoming shipping query. Only for invoices with flexible price. |
| pre_checkout_query | [PreCheckoutQuery](https://core.telegram.org/bots/api#precheckoutquery) | *Optional*. New incoming pre-checkout query. Contains full information about checkout. |
| purchased_paid_media | [PaidMediaPurchased](https://core.telegram.org/bots/api#paidmediapurchased) | *Optional*. A user purchased paid media with a non-empty payload sent by the bot in a non-channel chat |
| poll | [Poll](https://core.telegram.org/bots/api#poll) | *Optional*. New poll state. Bots receive only updates about manually stopped polls and polls, which are sent by the bot. |
| poll_answer | [PollAnswer](https://core.telegram.org/bots/api#pollanswer) | *Optional*. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself. |
| my_chat_member | [ChatMemberUpdated](https://core.telegram.org/bots/api#chatmemberupdated) | *Optional*. The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user. |
| chat_member | [ChatMemberUpdated](https://core.telegram.org/bots/api#chatmemberupdated) | *Optional*. A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify `"chat_member"` in the list of *allowed_updates* to receive these updates. |
| chat_join_request | [ChatJoinRequest](https://core.telegram.org/bots/api#chatjoinrequest) | *Optional*. A request to join the chat has been sent. The bot must have the *can_invite_users* administrator right in the chat to receive these updates. |
| chat_boost | [ChatBoostUpdated](https://core.telegram.org/bots/api#chatboostupdated) | *Optional*. A chat boost was added or changed. The bot must be an administrator in the chat to receive these updates. |
| removed_chat_boost | [ChatBoostRemoved](https://core.telegram.org/bots/api#chatboostremoved) | *Optional*. A boost was removed from a chat. The bot must be an administrator in the chat to receive these updates. |
| managed_bot | [ManagedBotUpdated](https://core.telegram.org/bots/api#managedbotupdated) | *Optional*. A new bot was created to be managed by the bot, or token or owner of a managed bot was changed |
| subscription | [BotSubscriptionUpdated](https://core.telegram.org/bots/api#botsubscriptionupdated) | *Optional*. User payment subscription has changed |
| stopped_message_generation | [MessageGenerationStopped](https://core.telegram.org/bots/api#messagegenerationstopped) | *Optional*. A user asked the bot to stop the generation of a message |