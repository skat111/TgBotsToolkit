# TDLib: getChatBoosts Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Returns the list of boosts applied to a chat; requires administrator rights in the chat.

Returns object_ptr<FoundChatBoosts>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Identifier of the chat. |
|  | |
| bool | [only_gift_codes_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#af027e09493a329752009f035dd2eacc8) |
|  | Pass true to receive only boosts received from gift codes and giveaways created by the chat. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [offset_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#ac90d045c5303dffca956fcf036e11d39) |
|  | Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [limit_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#ad5c6852c24b3b39c48321496871a637b) |
|  | The maximum number of boosts to be returned; up to 100. For optimal performance, the number of returned boosts can be smaller than the specified limit. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#a540d127589bda423beadac1ef280b0e9) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [foundChatBoosts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1found_chat_boosts.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [getChatBoosts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#af038060752beb6f0838c4d4666bddfda) () |
|  | |
|  | [getChatBoosts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#a3669c16c6be1f6079691c482c16d3f41) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#aa8a7803161092ff97e60d58707199e1f), bool [only_gift_codes_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#af027e09493a329752009f035dd2eacc8), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[offset_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#ac90d045c5303dffca956fcf036e11d39), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [limit_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#ad5c6852c24b3b39c48321496871a637b)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1419859400 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#af038060752beb6f0838c4d4666bddfda)getChatBoosts() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [getChatBoosts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html) | ( |  | ) |  |

Default constructor for a function, which returns the list of boosts applied to a chat; requires administrator rights in the chat.

Returns object_ptr<FoundChatBoosts>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#a3669c16c6be1f6079691c482c16d3f41)getChatBoosts() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [getChatBoosts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat_id_*, |
|  |  | bool | *only_gift_codes_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *offset_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *limit_* |
|  | ) |  |  |

Creates a function, which returns the list of boosts applied to a chat; requires administrator rights in the chat.

Returns object_ptr<FoundChatBoosts>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat_id_ | Identifier of the chat. |
    | [in] | only_gift_codes_ | Pass true to receive only boosts received from gift codes and giveaways created by the chat. |
    | [in] | offset_ | Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results. |
    | [in] | limit_ | The maximum number of boosts to be returned; up to 100. For optimal performance, the number of returned boosts can be smaller than the specified limit. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_boosts.html#a8044dab2ba3c75066745014259c050c7)store()

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