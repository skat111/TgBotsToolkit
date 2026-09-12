# TDLib: openWebApp Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Informs TDLib that a Web App is being opened from the attachment menu, a [botMenuButton](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html) button, an [internalLinkTypeAttachmentMenuBot](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_attachment_menu_bot.html) link, or an [inlineKeyboardButtonTypeWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_keyboard_button_type_web_app.html) button. For each bot, a confirmation alert about data sent to the bot must be shown once.

Returns object_ptr<WebAppInfo>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Identifier of the chat in which the Web App is opened. The Web App can't be opened in secret chats. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [bot_user_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#a852a1eecf72791be8eb2633ff5dcaec4) |
|  | Identifier of the bot, providing the Web App. If the bot is restricted for the current user, then show an error instead of calling the method. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [url_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#a541e0f072a74af71d6978eea722fc5fe) |
|  | The URL from an [inlineKeyboardButtonTypeWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_keyboard_button_type_web_app.html) button, a [botMenuButton](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html) button, an [internalLinkTypeAttachmentMenuBot](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_attachment_menu_bot.html) link, or an empty string otherwise. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > | [topic_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#adf6e2906ee2f8b6a06150747aa41f7e0) |
|  | Topic in which the message will be sent; pass null if none. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputMessageReplyTo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_message_reply_to.html) > | [reply_to_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#a53a1a524255604e5260f4c3eb42a19e5) |
|  | Information about the message or story to be replied in the message sent by the Web App; pass null if none. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [webAppOpenParameters](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1web_app_open_parameters.html) > | [parameters_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#af39abd6dbe450aa53cad2723cc084de1) |
|  | Parameters to use to open the Web App. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#a764c0d673a3ca5115a957b9c25c6f925) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [webAppInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1web_app_info.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [openWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#ad7b2987158a04d5d3c79f83412336418) () |
|  | |
|  | [openWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#aec60664bb6e3b510ce1d57352977fe77) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#aa8a7803161092ff97e60d58707199e1f), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [bot_user_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#a852a1eecf72791be8eb2633ff5dcaec4), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[url_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#a541e0f072a74af71d6978eea722fc5fe), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > &&[topic_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#adf6e2906ee2f8b6a06150747aa41f7e0), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputMessageReplyTo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_message_reply_to.html) > &&[reply_to_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#a53a1a524255604e5260f4c3eb42a19e5), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [webAppOpenParameters](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1web_app_open_parameters.html) > &&[parameters_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#af39abd6dbe450aa53cad2723cc084de1)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
|  | |
| - Public Instance Methods inherited from [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) | |
| virtual void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#aed3fac8962d039b3c4827cd013ba8050) (TlStorerUnsafe &s) const |
|  | |
| virtual void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a66f325c1a08459d978fa08dcc4e7a86e) (TlStorerCalcLength &s) const |
|  | |
|  | [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a524843ecda9a59d32e1a1ad83bfdfef5) ()=default |
|  | |
|  | [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#aaf0b851a7d7420da4ccc5d3f875e33f3) (const [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) &)=delete |
|  | |
| [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) & | [operator=](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#ac017d2d18b4840ffec9274cea86cd1d3) (const [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) &)=delete |
|  | |
|  | [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a767dd89c1cf0f6cd9cc776f36d5b1ece) ([TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) &&)=default |
|  | |
| [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) & | [operator=](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a8ae6deb8ded379f394672c85bafeb70b) ([TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) &&)=default |
|  | |
| virtual | [~TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#abfbd857b9bfdc4e3bf31b5d0476b7289) ()=default |
|  | |

|  |  |
| --- | --- |
| Static Public Attributes | |
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -950685122 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#ad7b2987158a04d5d3c79f83412336418)openWebApp() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [openWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html) | ( |  | ) |  |

Default constructor for a function, which informs TDLib that a Web App is being opened from the attachment menu, a [botMenuButton](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html) button, an [internalLinkTypeAttachmentMenuBot](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_attachment_menu_bot.html) link, or an [inlineKeyboardButtonTypeWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_keyboard_button_type_web_app.html) button. For each bot, a confirmation alert about data sent to the bot must be shown once.

Returns object_ptr<WebAppInfo>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#aec60664bb6e3b510ce1d57352977fe77)openWebApp() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [openWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat_id_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *bot_user_id_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *url_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > && | *topic_id_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputMessageReplyTo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_message_reply_to.html) > && | *reply_to_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [webAppOpenParameters](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1web_app_open_parameters.html) > && | *parameters_* |
|  | ) |  |  |

Creates a function, which informs TDLib that a Web App is being opened from the attachment menu, a [botMenuButton](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html) button, an [internalLinkTypeAttachmentMenuBot](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_attachment_menu_bot.html) link, or an [inlineKeyboardButtonTypeWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_keyboard_button_type_web_app.html) button. For each bot, a confirmation alert about data sent to the bot must be shown once.

Returns object_ptr<WebAppInfo>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat_id_ | Identifier of the chat in which the Web App is opened. The Web App can't be opened in secret chats. |
    | [in] | bot_user_id_ | Identifier of the bot, providing the Web App. If the bot is restricted for the current user, then show an error instead of calling the method. |
    | [in] | url_ | The URL from an [inlineKeyboardButtonTypeWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_keyboard_button_type_web_app.html) button, a [botMenuButton](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html) button, an [internalLinkTypeAttachmentMenuBot](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_attachment_menu_bot.html) link, or an empty string otherwise. |
    | [in] | topic_id_ | Topic in which the message will be sent; pass null if none. |
    | [in] | reply_to_ | Information about the message or story to be replied in the message sent by the Web App; pass null if none. |
    | [in] | parameters_ | Parameters to use to open the Web App. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html#a8044dab2ba3c75066745014259c050c7)store()

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  | | --- | --- | --- | --- | | void store | ( | TlStorerToString & | *s*, | |  |  | const char \* | *field_name* | |  | ) |  | const | | finalvirtual |

Helper function for to_string method. Appends string representation of the object to the storer.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | s | Storer to which object string representation will be appended. |
    | [in] | field_name | [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html) field_name if applicable. |

Implements [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a4f1eab7385f340a2ab0aa8751cdcedc6).

---

The documentation for this class was generated from the following file:

* td/generate/auto/td/telegram/[td_api.h](https://core.telegram.org/tdlib/docs/td__api_8h_source.html)