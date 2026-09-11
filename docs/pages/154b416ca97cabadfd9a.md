# TDLib: addChatToList Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Adds a chat to a chat list. A chat can't be simultaneously in Main and Archive chat lists, so it is automatically removed from another one if needed.

Returns object\_ptr<Ok>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Chat identifier. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ChatList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_chat_list.html) > | [chat\_list\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html#a212da12e1a4514fa0fc79813c11f9ae2) |
|  | The chat list. Use [getChatListsToAddChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_lists_to_add_chat.html) to get suitable chat lists. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html#ab684327f0ee9cbf9afb740503d89f019) = [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ok](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1ok.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [addChatToList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html#a6f24ebba8d311336d8bb9ff8af3b28f1) () |
|  | |
|  | [addChatToList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html#aad554e105b80aefa0d21cc0f7793d7e9) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html#aa8a7803161092ff97e60d58707199e1f), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ChatList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_chat_list.html) > &&[chat\_list\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html#a212da12e1a4514fa0fc79813c11f9ae2)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -80523595 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html#a6f24ebba8d311336d8bb9ff8af3b28f1)addChatToList() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [addChatToList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html) | ( |  | ) |  |

Default constructor for a function, which adds a chat to a chat list. A chat can't be simultaneously in Main and Archive chat lists, so it is automatically removed from another one if needed.

Returns object\_ptr<Ok>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html#aad554e105b80aefa0d21cc0f7793d7e9)addChatToList() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [addChatToList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat\_id\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ChatList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_chat_list.html) > && | *chat\_list\_* |
|  | ) |  |  |

Creates a function, which adds a chat to a chat list. A chat can't be simultaneously in Main and Archive chat lists, so it is automatically removed from another one if needed.

Returns object\_ptr<Ok>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat\_id\_ | Chat identifier. |
    | [in] | chat\_list\_ | The chat list. Use [getChatListsToAddChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_lists_to_add_chat.html) to get suitable chat lists. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_chat_to_list.html#a8044dab2ba3c75066745014259c050c7)store()

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