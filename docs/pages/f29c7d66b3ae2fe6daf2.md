# TDLib: sponsoredChat Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes a sponsored chat.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [unique_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#a3d44aabdec5fcc61f449a52b2bc6e3f3) |
|  | Unique identifier of this result. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Chat identifier. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [sponsor_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#a1aa5f2b4d9eb8d7fe75224abf80b330c) |
|  | Additional optional information about the sponsor to be shown along with the chat. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [additional_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#ae880f199b97a1170dd86963bf47e0eb7) |
|  | If non-empty, additional information about the sponsored chat to be shown along with the chat. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [sponsoredChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#af51e5150ac5ec89afc84d954f6095c39) () |
|  | |
|  | [sponsoredChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#a7e853321cf34e061000af0b6c6f9bf80) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [unique_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#a3d44aabdec5fcc61f449a52b2bc6e3f3), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#aa8a7803161092ff97e60d58707199e1f), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[sponsor_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#a1aa5f2b4d9eb8d7fe75224abf80b330c), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[additional_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#ae880f199b97a1170dd86963bf47e0eb7)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -325763489 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#af51e5150ac5ec89afc84d954f6095c39)sponsoredChat() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [sponsoredChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html) | ( |  | ) |  |

Describes a sponsored chat.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#a7e853321cf34e061000af0b6c6f9bf80)sponsoredChat() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [sponsoredChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *unique_id_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat_id_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *sponsor_info_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *additional_info_* |
|  | ) |  |  |

Describes a sponsored chat.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | unique_id_ | Unique identifier of this result. |
    | [in] | chat_id_ | Chat identifier. |
    | [in] | sponsor_info_ | Additional optional information about the sponsor to be shown along with the chat. |
    | [in] | additional_info_ | If non-empty, additional information about the sponsored chat to be shown along with the chat. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_chat.html#a8044dab2ba3c75066745014259c050c7)store()

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