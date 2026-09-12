# TDLib: getChatRevenueStatistics Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Returns detailed revenue statistics about a chat. Currently, this method can be used only for channels if supergroupFullInfo.can_get_revenue_statistics == true or bots if userFullInfo.bot_info.can_get_revenue_statistics == true.

Returns object_ptr<ChatRevenueStatistics>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Chat identifier. |
|  | |
| bool | [is_dark_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html#a2d8bc30dcdffdaa08bd361027e115141) |
|  | Pass true if a dark theme is used by the application. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html#a75d18fb1574a534e1b3d5d47a5bb5140) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [chatRevenueStatistics](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_revenue_statistics.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [getChatRevenueStatistics](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html#a27a752c7f5df54c921f21f99220e8e32) () |
|  | |
|  | [getChatRevenueStatistics](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html#a58328acbfa7c0a27282c8b9b319232c2) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html#aa8a7803161092ff97e60d58707199e1f), bool [is_dark_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html#a2d8bc30dcdffdaa08bd361027e115141)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 701995836 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html#a27a752c7f5df54c921f21f99220e8e32)getChatRevenueStatistics() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [getChatRevenueStatistics](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html) | ( |  | ) |  |

Default constructor for a function, which returns detailed revenue statistics about a chat. Currently, this method can be used only for channels if supergroupFullInfo.can_get_revenue_statistics == true or bots if userFullInfo.bot_info.can_get_revenue_statistics == true.

Returns object_ptr<ChatRevenueStatistics>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html#a58328acbfa7c0a27282c8b9b319232c2)getChatRevenueStatistics() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [getChatRevenueStatistics](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat_id_*, |
|  |  | bool | *is_dark_* |
|  | ) |  |  |

Creates a function, which returns detailed revenue statistics about a chat. Currently, this method can be used only for channels if supergroupFullInfo.can_get_revenue_statistics == true or bots if userFullInfo.bot_info.can_get_revenue_statistics == true.

Returns object_ptr<ChatRevenueStatistics>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat_id_ | Chat identifier. |
    | [in] | is_dark_ | Pass true if a dark theme is used by the application. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_revenue_statistics.html#a8044dab2ba3c75066745014259c050c7)store()

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