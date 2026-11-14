Source: https://core.telegram.org/bots/api#november-9-2026
Snapshot: 2026-11-14T10:30:31Z

#### November 9, 2026

**Bot API 10.4**

**Widgets**

* Added the class [Widget](https://core.telegram.org/bots/api#widget) and the field *widget* to the classes [Message](https://core.telegram.org/bots/api#message) and [ExternalReplyInfo](https://core.telegram.org/bots/api#externalreplyinfo) for messages with [HTML widgets](https://core.telegram.org/bots/widgets).
* Added the method [sendWidget](https://core.telegram.org/bots/api#sendwidget), allowing bots to send messages with HTML widgets. Currently, in the production environment, widgets can be sent only to private chats, and sent widgets automatically have protected content and therefore can't be forwarded.
* Added the method [sendSharedWidget](https://core.telegram.org/bots/api#sendsharedwidget), allowing bots to send again shared widgets created by the bot.
* Added the class [WidgetQuery](https://core.telegram.org/bots/api#widgetquery) and the field *widget_query* to the class [Update](https://core.telegram.org/bots/api#update) for queries sent to the bot by widgets in messages sent by the bot or via the bot.
* Added the class [SharedWidgetQuery](https://core.telegram.org/bots/api#sharedwidgetquery) and the field *shared_widget_query* to the class [Update](https://core.telegram.org/bots/api#update) for queries sent to the bot from forwarded messages with shared widgets.
* Added the classes [WidgetQueryType](https://core.telegram.org/bots/api#widgetquerytype), [WidgetQueryTypeData](https://core.telegram.org/bots/api#widgetquerytypedata), [WidgetQueryTypeSignData](https://core.telegram.org/bots/api#widgetquerytypesigndata), [WidgetQueryTypeSentTransaction](https://core.telegram.org/bots/api#widgetquerytypesenttransaction) and [WidgetQueryWallet](https://core.telegram.org/bots/api#widgetquerywallet), describing the type of a query from a widget. A query can contain data for the bot together with the TON wallet card of the user, data signed by a TON wallet of the user, or a notification about a transaction sent from a TON wallet of the user.
* Added the method [answerWidgetQuery](https://core.telegram.org/bots/api#answerwidgetquery), allowing bots to answer queries from widgets.
* Added the method [editMessageWidgetData](https://core.telegram.org/bots/api#editmessagewidgetdata), allowing bots to change data of a widget in a message.
* Added the method [editSharedWidgetData](https://core.telegram.org/bots/api#editsharedwidgetdata), allowing bots to change public data of a shared widget.
* Added the classes [InputWidgetMessageContent](https://core.telegram.org/bots/api#inputwidgetmessagecontent) and [InputSharedWidgetMessageContent](https://core.telegram.org/bots/api#inputsharedwidgetmessagecontent), allowing bots to send widgets in response to inline queries. Currently, widgets can't be sent in response to inline queries in the production environment.
* Widget messages can't be copied using the methods [copyMessage](https://core.telegram.org/bots/api#copymessage) and [copyMessages](https://core.telegram.org/bots/api#copymessages).
* The right *can_send_other_messages* in the classes [ChatPermissions](https://core.telegram.org/bots/api#chatpermissions) and [ChatMemberRestricted](https://core.telegram.org/bots/api#chatmemberrestricted) now also allows sending widgets.

**Ephemeral messages**

* Allowed bots to send ephemeral replies to callback queries in any chat except channel direct messages chats by specifying *callback_query_id* without *receiver_user_id* in the parameter *ephemeral_message_parameters* of the methods [sendMessage](https://core.telegram.org/bots/api#sendmessage), [sendRichMessage](https://core.telegram.org/bots/api#sendrichmessage), [sendAnimation](https://core.telegram.org/bots/api#sendanimation), [sendAudio](https://core.telegram.org/bots/api#sendaudio), [sendContact](https://core.telegram.org/bots/api#sendcontact), [sendDocument](https://core.telegram.org/bots/api#senddocument), [sendLivePhoto](https://core.telegram.org/bots/api#sendlivephoto), [sendLocation](https://core.telegram.org/bots/api#sendlocation), [sendPhoto](https://core.telegram.org/bots/api#sendphoto), [sendSticker](https://core.telegram.org/bots/api#sendsticker), [sendVenue](https://core.telegram.org/bots/api#sendvenue), [sendVideo](https://core.telegram.org/bots/api#sendvideo), [sendVideoNote](https://core.telegram.org/bots/api#sendvideonote) and [sendVoice](https://core.telegram.org/bots/api#sendvoice).
* The field *receiver_user_id* of the class [EphemeralMessageParameters](https://core.telegram.org/bots/api#ephemeralmessageparameters) and the parameter *chat_id* of the mentioned methods are optional now.

**Quotes from rich messages**

* Added the field *rich_texts* to the class [TextQuote](https://core.telegram.org/bots/api#textquote) for quotes chosen from a [RichMessage](https://core.telegram.org/bots/api#richmessage).
* Added the field *quote_rich_texts* to the class [ReplyParameters](https://core.telegram.org/bots/api#replyparameters), allowing bots to quote rich messages.

**TON wallet**

* Added the classes [TonWalletCard](https://core.telegram.org/bots/api#tonwalletcard), [TonWalletCardSticker](https://core.telegram.org/bots/api#tonwalletcardsticker), [TonNft](https://core.telegram.org/bots/api#tonnft) and [TonNftAttribute](https://core.telegram.org/bots/api#tonnftattribute), and the field *ton_wallet_card* to the class [ChatFullInfo](https://core.telegram.org/bots/api#chatfullinfo).
* Added the class [TonWalletTransfer](https://core.telegram.org/bots/api#tonwallettransfer) and the field *ton_wallet_transfer* to the class [Message](https://core.telegram.org/bots/api#message) for service messages about transfers with a TON wallet.
* Renamed the class StoryAreaPosition to [AreaPosition](https://core.telegram.org/bots/api#areaposition), because it is now also used to describe the position of stickers on TON wallet cards.

**Chat share themes**

* Added the classes [ChatShareTheme](https://core.telegram.org/bots/api#chatsharetheme), [ChatShareThemeEmoji](https://core.telegram.org/bots/api#chatsharethemeemoji) and [ChatShareThemeUniqueGift](https://core.telegram.org/bots/api#chatsharethemeuniquegift), and the field *share_theme* to the class [ChatFullInfo](https://core.telegram.org/bots/api#chatfullinfo), describing the theme of the screen for sharing a link to a user or a chat.
* Added the classes [EmojiType](https://core.telegram.org/bots/api#emojitype), [EmojiTypeEmoji](https://core.telegram.org/bots/api#emojitypeemoji) and [EmojiTypeCustomEmoji](https://core.telegram.org/bots/api#emojitypecustomemoji).
* Added the classes [ChatShareThemeBackdrop](https://core.telegram.org/bots/api#chatsharethemebackdrop) and [ChatShareThemeBackdrops](https://core.telegram.org/bots/api#chatsharethemebackdrops) and the method [getChatShareThemeBackdrops](https://core.telegram.org/bots/api#getchatsharethemebackdrops).

**Gifts**

* Added the method [getUniqueGift](https://core.telegram.org/bots/api#getuniquegift), allowing bots to get information about a unique gift by its name.
* Added the method [deleteBusinessAccountGift](https://core.telegram.org/bots/api#deletebusinessaccountgift), allowing bots to delete regular gifts owned by a managed business account without receiving Telegram Stars for them.

**General**

* Allowed users with a Telegram Premium subscription to assign secondary usernames ending with “agent”, “ai”, “app”, “game”, or “gay” to up to 2 owned bots. Such usernames can be suggested in the field *suggested_username* of the class [KeyboardButtonRequestManagedBot](https://core.telegram.org/bots/api#keyboardbuttonrequestmanagedbot).
* Added the class [RichTextTonAddress](https://core.telegram.org/bots/api#richtexttonaddress) representing an address in the TON blockchain in a [RichMessage](https://core.telegram.org/bots/api#richmessage).
* Added the type “ton_address” to the class [MessageEntity](https://core.telegram.org/bots/api#messageentity) for addresses in the TON blockchain.
* Added the type “bank_card_number” to the class [MessageEntity](https://core.telegram.org/bots/api#messageentity) for bank card numbers.
* Added the parameters *custom_description_parse_mode* and *custom_description_entities* to the methods [verifyUser](https://core.telegram.org/bots/api#verifyuser) and [verifyChat](https://core.telegram.org/bots/api#verifychat).
* Added the class [PaidMessagesWaived](https://core.telegram.org/bots/api#paidmessageswaived) and the field *paid_messages_waived* to the class [Message](https://core.telegram.org/bots/api#message) for service messages about the sender using a link which allows sending messages without paying Telegram Stars.
* Added the ability to create links to topics in private chats with the bot in the format `https://t.me/<bot_username>/<message_thread_id>`. Such a link opens the topic only for the user in the private chat with whom the topic exists.