Source: https://core.telegram.org/bots/api#november-22-2026
Snapshot: 2026-11-22T11:29:57Z

#### November 22, 2026

**Bot API 10.5**

**Bot Settings**

* Added the method [setMySettings](https://core.telegram.org/bots/api#setmysettings), allowing bots to change their settings, including inline mode settings, privacy mode, the ability to be added to groups, forum topic mode in private chats, and the mode of receiving callback queries.
* Added the ability to receive callback queries from buttons in messages sent by the bot with the field *inline_message_id* instead of the field *message* in the class [CallbackQuery](https://core.telegram.org/bots/api#callbackquery), depending on the parameter *callback_query_mode* of the method [setMySettings](https://core.telegram.org/bots/api#setmysettings).
* Added the ability for bots to show the list of topics in a sidebar in private chats with the bot using the parameter *has_topic_sidebar* of the method [setMySettings](https://core.telegram.org/bots/api#setmysettings).
* Split out the class [BotFullInfo](https://core.telegram.org/bots/api#botfullinfo) from the class [User](https://core.telegram.org/bots/api#user) and changed the return type of the method [getMe](https://core.telegram.org/bots/api#getme) to *BotFullInfo*. The fields that were returned only in [getMe](https://core.telegram.org/bots/api#getme) were removed from the class [User](https://core.telegram.org/bots/api#user).
* Added the field *active_usernames* to the class [BotFullInfo](https://core.telegram.org/bots/api#botfullinfo), allowing the bot to get the list of all its active usernames.
* Added the field *inline_query_placeholder* to the class [BotFullInfo](https://core.telegram.org/bots/api#botfullinfo), allowing the bot to get its placeholder for inline queries.
* Added the field *needs_inline_query_location* to the class [BotFullInfo](https://core.telegram.org/bots/api#botfullinfo), allowing the bot to check whether it requests the location of the user with every inline query.
* Added the field *has_topic_sidebar* to the class [BotFullInfo](https://core.telegram.org/bots/api#botfullinfo), allowing the bot to check whether topics in private chats with the bot are shown in a sidebar.

**General**

* Added the ability for bot owners to invite up to 10 users at once to private chats with the bot by pressing the link `https://t.me/botinvite/<bot_username>`. The bot can send messages to the invited users.
* Added the field *inviter* to the class [WriteAccessAllowed](https://core.telegram.org/bots/api#writeaccessallowed) for service messages about users invited to the private chat with the bot by the owner of the bot.
* Replaced the field *text* with the field *blocks* in the classes [RichBlockExpandableBlockQuotation](https://core.telegram.org/bots/api#richblockexpandableblockquotation) and [InputRichBlockExpandableBlockQuotation](https://core.telegram.org/bots/api#inputrichblockexpandableblockquotation), allowing expandable block quotations to contain arbitrary blocks.