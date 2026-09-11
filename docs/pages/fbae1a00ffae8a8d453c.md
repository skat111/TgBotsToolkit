# TDLib: sendInlineQueryResultMessage Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Sends the result of an inline query as a message. Returns the sent message. Always clears a chat draft message.

Returns object\_ptr<Message>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Target chat. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > | [topic\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#adf6e2906ee2f8b6a06150747aa41f7e0) |
|  | Topic in which the message will be sent; pass null if none. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputMessageReplyTo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_message_reply_to.html) > | [reply\_to\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#a53a1a524255604e5260f4c3eb42a19e5) |
|  | Information about the message or story to be replied; pass null if none. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [messageSendOptions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_send_options.html) > | [options\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#a24117df785245c138fc22bbc2a0cd56e) |
|  | Options to be used to send the message; pass null to use default options. |
|  | |
| [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | [query\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#aa046f0554eb0a0469f67efab71158a7d) |
|  | Identifier of the inline query. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [result\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#a164f0ec26810ae270522cc39fe76e0f9) |
|  | Identifier of the inline query result. |
|  | |
| bool | [hide\_via\_bot\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#a119a190778555fb67acf462804e3e8dc) |
|  | Pass true to hide the bot, via which the message is sent. Can be used only for bots [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("animation\_search\_bot\_username"), [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("photo\_search\_bot\_username"), and [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("venue\_search\_bot\_username"). |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#afc091f71bd2c2eb207a0fd621a8260b3) = [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [message](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [sendInlineQueryResultMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#a9877c1c310aa11219c1b01db467daab4) () |
|  | |
|  | [sendInlineQueryResultMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#a205b8b204b84721173cf6ab8f7c2c08b) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#aa8a7803161092ff97e60d58707199e1f), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > &&[topic\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#adf6e2906ee2f8b6a06150747aa41f7e0), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputMessageReplyTo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_message_reply_to.html) > &&[reply\_to\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#a53a1a524255604e5260f4c3eb42a19e5), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [messageSendOptions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_send_options.html) > &&[options\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#a24117df785245c138fc22bbc2a0cd56e), [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) [query\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#aa046f0554eb0a0469f67efab71158a7d), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[result\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#a164f0ec26810ae270522cc39fe76e0f9), bool [hide\_via\_bot\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#a119a190778555fb67acf462804e3e8dc)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1445935970 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#a9877c1c310aa11219c1b01db467daab4)sendInlineQueryResultMessage() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [sendInlineQueryResultMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html) | ( |  | ) |  |

Default constructor for a function, which sends the result of an inline query as a message. Returns the sent message. Always clears a chat draft message.

Returns object\_ptr<Message>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#a205b8b204b84721173cf6ab8f7c2c08b)sendInlineQueryResultMessage() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [sendInlineQueryResultMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat\_id\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > && | *topic\_id\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputMessageReplyTo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_message_reply_to.html) > && | *reply\_to\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [messageSendOptions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_send_options.html) > && | *options\_*, |
|  |  | [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | *query\_id\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *result\_id\_*, |
|  |  | bool | *hide\_via\_bot\_* |
|  | ) |  |  |

Creates a function, which sends the result of an inline query as a message. Returns the sent message. Always clears a chat draft message.

Returns object\_ptr<Message>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat\_id\_ | Target chat. |
    | [in] | topic\_id\_ | Topic in which the message will be sent; pass null if none. |
    | [in] | reply\_to\_ | Information about the message or story to be replied; pass null if none. |
    | [in] | options\_ | Options to be used to send the message; pass null to use default options. |
    | [in] | query\_id\_ | Identifier of the inline query. |
    | [in] | result\_id\_ | Identifier of the inline query result. |
    | [in] | hide\_via\_bot\_ | Pass true to hide the bot, via which the message is sent. Can be used only for bots [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("animation\_search\_bot\_username"), [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("photo\_search\_bot\_username"), and [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("venue\_search\_bot\_username"). |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_inline_query_result_message.html#a8044dab2ba3c75066745014259c050c7)store()

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  | | --- | --- | --- | --- | | void store | ( | TlStorerToString & | *s*, | |  |  | const char \* | *field\_name* | |  | ) |  | const | | finalvirtual |

Helper function for to\_string method. Appends string representation of the object to the storer.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | s | Storer to which object string representation will be appended. |
    | [in] | field\_name | [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html) field\_name if applicable. |

Implements [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a4f1eab7385f340a2ab0aa8751cdcedc6).

---

The documentation for this class was generated from the following file:

* td/generate/auto/td/telegram/[td\_api.h](https://core.telegram.org/tdlib/docs/td__api_8h_source.html)