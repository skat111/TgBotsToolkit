# TDLib: summarizeMessage Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Summarizes content of the message with non-empty summary_language_code.

Returns object_ptr<FormattedText>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Identifier of the chat to which the message belongs. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [message_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html#a946f46ee90c465619214e056e4d91ce4) |
|  | Identifier of the message. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [translate_to_language_code_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html#a1f647ece5632a8b0d5628b6570d04d07) |
|  | Pass a language code to which the summary will be translated; may be empty if translation isn't needed. See translateText.to_language_code for the list of supported values. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html#a43fca2435d60f452391e676c3bdcede2) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [summarizeMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html#a1ae87b426119ea12d53a5c9c67bb593b) () |
|  | |
|  | [summarizeMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html#a5a936377a05e5b5dc29f46a4c3ec534e) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html#aa8a7803161092ff97e60d58707199e1f), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [message_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html#a946f46ee90c465619214e056e4d91ce4), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[translate_to_language_code_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html#a1f647ece5632a8b0d5628b6570d04d07)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1405194782 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html#a1ae87b426119ea12d53a5c9c67bb593b)summarizeMessage() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [summarizeMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html) | ( |  | ) |  |

Default constructor for a function, which summarizes content of the message with non-empty summary_language_code.

Returns object_ptr<FormattedText>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html#a5a936377a05e5b5dc29f46a4c3ec534e)summarizeMessage() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [summarizeMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat_id_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *message_id_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *translate_to_language_code_* |
|  | ) |  |  |

Creates a function, which summarizes content of the message with non-empty summary_language_code.

Returns object_ptr<FormattedText>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat_id_ | Identifier of the chat to which the message belongs. |
    | [in] | message_id_ | Identifier of the message. |
    | [in] | translate_to_language_code_ | Pass a language code to which the summary will be translated; may be empty if translation isn't needed. See translateText.to_language_code for the list of supported values. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1summarize_message.html#a8044dab2ba3c75066745014259c050c7)store()

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