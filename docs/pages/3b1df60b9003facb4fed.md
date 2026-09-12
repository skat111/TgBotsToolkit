# TDLib: messageOriginChannel Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html

Inherits [MessageOrigin](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_origin.html).

## Description

The message was originally a post in a channel.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Identifier of the channel chat to which the message was originally sent. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [message_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html#a946f46ee90c465619214e056e4d91ce4) |
|  | Message identifier of the original message. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [author_signature_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html#adab596c616a042fe957a271ef2c5d17e) |
|  | Original post author signature. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [messageOriginChannel](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html#ad8028ca8591e3f2580dab6755f1303c1) () |
|  | |
|  | [messageOriginChannel](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html#a01ef17ec8a4bff20b31dd8658c819646) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html#aa8a7803161092ff97e60d58707199e1f), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [message_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html#a946f46ee90c465619214e056e4d91ce4), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[author_signature_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html#adab596c616a042fe957a271ef2c5d17e)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1451535938 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html#ad8028ca8591e3f2580dab6755f1303c1)messageOriginChannel() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [messageOriginChannel](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html) | ( |  | ) |  |

The message was originally a post in a channel.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html#a01ef17ec8a4bff20b31dd8658c819646)messageOriginChannel() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [messageOriginChannel](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat_id_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *message_id_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *author_signature_* |
|  | ) |  |  |

The message was originally a post in a channel.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat_id_ | Identifier of the channel chat to which the message was originally sent. |
    | [in] | message_id_ | Message identifier of the original message. |
    | [in] | author_signature_ | Original post author signature. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_origin_channel.html#a8044dab2ba3c75066745014259c050c7)store()

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