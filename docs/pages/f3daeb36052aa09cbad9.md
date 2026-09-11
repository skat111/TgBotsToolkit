# TDLib: getChats Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Returns an ordered list of chats from the beginning of a chat list. For informational purposes only. Use [loadChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1load_chats.html) and updates processing instead to maintain chat lists in a consistent state.

Returns object\_ptr<Chats>.

|  |  |
| --- | --- |
| Public Fields | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ChatList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_chat_list.html) > | [chat\_list\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html#a212da12e1a4514fa0fc79813c11f9ae2) |
|  | The chat list in which to return chats; pass null to get chats from the main chat list. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [limit\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html#ad5c6852c24b3b39c48321496871a637b) |
|  | The maximum number of chats to be returned. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html#a133dd6ad4d7481cc53bfa19b655e5dde) = [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [chats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chats.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [getChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html#a19f9bbd60e889917944b08e145d2a869) () |
|  | |
|  | [getChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html#a23e7170e38b03e873765f67fa3ba8e9d) ([object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ChatList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_chat_list.html) > &&[chat\_list\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html#a212da12e1a4514fa0fc79813c11f9ae2), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [limit\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html#ad5c6852c24b3b39c48321496871a637b)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -972768574 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html#a19f9bbd60e889917944b08e145d2a869)getChats() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [getChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html) | ( |  | ) |  |

Default constructor for a function, which returns an ordered list of chats from the beginning of a chat list. For informational purposes only. Use [loadChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1load_chats.html) and updates processing instead to maintain chat lists in a consistent state.

Returns object\_ptr<Chats>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html#a23e7170e38b03e873765f67fa3ba8e9d)getChats() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [getChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html) | ( | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ChatList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_chat_list.html) > && | *chat\_list\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *limit\_* |
|  | ) |  |  |

Creates a function, which returns an ordered list of chats from the beginning of a chat list. For informational purposes only. Use [loadChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1load_chats.html) and updates processing instead to maintain chat lists in a consistent state.

Returns object\_ptr<Chats>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat\_list\_ | The chat list in which to return chats; pass null to get chats from the main chat list. |
    | [in] | limit\_ | The maximum number of chats to be returned. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats.html#a8044dab2ba3c75066745014259c050c7)store()

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