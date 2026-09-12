# TDLib: reportChat Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if chat.can_be_reported.

Returns object_ptr<ReportChatResult>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Chat identifier. |
|  | |
| [bytes](https://core.telegram.org/tdlib/docs/td__api_8h.html#a124171ebb3663f1cbd4f902257dced87) | [option_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#ab51dcf0eae4bd8f69ec2d04a867a0ab8) |
|  | Option identifier chosen by the user; leave empty for the initial request. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) > | [message_ids_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#a97dd60d3b9e1d263c22016f5e808a9f8) |
|  | Identifiers of reported messages. Use messageProperties.can_report_chat to check whether the message can be reported. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [text_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#a1e07078cd658903987f94f1a39482856) |
|  | Additional report details if asked by the server; 0-1024 characters; leave empty for the initial request. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#a1e6ab624f2bcb6cdf84fb4e97b8aa72f) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReportChatResult](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_report_chat_result.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [reportChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#a5878b62cb14379cef5227bbd78fbc044) () |
|  | |
|  | [reportChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#a24e009b0033f79daa9efd5723fc54cd6) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#aa8a7803161092ff97e60d58707199e1f), [bytes](https://core.telegram.org/tdlib/docs/td__api_8h.html#a124171ebb3663f1cbd4f902257dced87) const &[option_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#ab51dcf0eae4bd8f69ec2d04a867a0ab8), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) > &&[message_ids_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#a97dd60d3b9e1d263c22016f5e808a9f8), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[text_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#a1e07078cd658903987f94f1a39482856)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1058475058 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#a5878b62cb14379cef5227bbd78fbc044)reportChat() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [reportChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html) | ( |  | ) |  |

Default constructor for a function, which reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if chat.can_be_reported.

Returns object_ptr<ReportChatResult>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#a24e009b0033f79daa9efd5723fc54cd6)reportChat() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [reportChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat_id_*, |
|  |  | [bytes](https://core.telegram.org/tdlib/docs/td__api_8h.html#a124171ebb3663f1cbd4f902257dced87) const & | *option_id_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) > && | *message_ids_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *text_* |
|  | ) |  |  |

Creates a function, which reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if chat.can_be_reported.

Returns object_ptr<ReportChatResult>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat_id_ | Chat identifier. |
    | [in] | option_id_ | Option identifier chosen by the user; leave empty for the initial request. |
    | [in] | message_ids_ | Identifiers of reported messages. Use messageProperties.can_report_chat to check whether the message can be reported. |
    | [in] | text_ | Additional report details if asked by the server; 0-1024 characters; leave empty for the initial request. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat.html#a8044dab2ba3c75066745014259c050c7)store()

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