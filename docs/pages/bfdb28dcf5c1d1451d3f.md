# TDLib: pushMessageContentPaidMedia Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_paid_media.html

Inherits [PushMessageContent](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_push_message_content.html).

## Description

A message with paid media.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_paid_media.html#ad508b0848e631be2e72f8b8c664b94c4) |
|  | Number of Telegram Stars needed to buy access to the media in the message; 0 for pinned message. |
|  | |
| bool | [is_pinned_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_paid_media.html#ada3cbd9c3e89da9f894cd2f29725799d) |
|  | True, if the message is a pinned message with the specified content. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [pushMessageContentPaidMedia](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_paid_media.html#a4e911095d0a90e9582b2646194f17a0a) () |
|  | |
|  | [pushMessageContentPaidMedia](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_paid_media.html#a83093b8c6ff0ae14774ba6c8eaa7f10f) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_paid_media.html#ad508b0848e631be2e72f8b8c664b94c4), bool [is_pinned_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_paid_media.html#ada3cbd9c3e89da9f894cd2f29725799d)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_paid_media.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_paid_media.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1252595894 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_paid_media.html#a4e911095d0a90e9582b2646194f17a0a)pushMessageContentPaidMedia() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [pushMessageContentPaidMedia](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_paid_media.html) | ( |  | ) |  |

A message with paid media.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_paid_media.html#a83093b8c6ff0ae14774ba6c8eaa7f10f)pushMessageContentPaidMedia() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [pushMessageContentPaidMedia](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_paid_media.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *star_count_*, |
|  |  | bool | *is_pinned_* |
|  | ) |  |  |

A message with paid media.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | star_count_ | Number of Telegram Stars needed to buy access to the media in the message; 0 for pinned message. |
    | [in] | is_pinned_ | True, if the message is a pinned message with the specified content. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_paid_media.html#a8044dab2ba3c75066745014259c050c7)store()

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