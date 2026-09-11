# TDLib: setChatPinnedStories Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Changes the list of pinned stories on a chat page; requires can\_edit\_stories administrator right in the chat.

Returns object\_ptr<Ok>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Identifier of the chat that posted the stories. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > | [story\_ids\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html#ae9df04013ac4402a2d58aa6fe492a196) |
|  | New list of pinned stories. All stories must be posted to the chat page first. There can be up to [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("pinned\_story\_count\_max") pinned stories on a chat page. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html#ab684327f0ee9cbf9afb740503d89f019) = [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ok](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1ok.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [setChatPinnedStories](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html#a01f4605d162632cd19be0291e9c01b36) () |
|  | |
|  | [setChatPinnedStories](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html#acd787c25d1b4b676d5435511e9e20d40) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html#aa8a7803161092ff97e60d58707199e1f), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > &&[story\_ids\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html#ae9df04013ac4402a2d58aa6fe492a196)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -669062355 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html#a01f4605d162632cd19be0291e9c01b36)setChatPinnedStories() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [setChatPinnedStories](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html) | ( |  | ) |  |

Default constructor for a function, which changes the list of pinned stories on a chat page; requires can\_edit\_stories administrator right in the chat.

Returns object\_ptr<Ok>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html#acd787c25d1b4b676d5435511e9e20d40)setChatPinnedStories() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [setChatPinnedStories](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat\_id\_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > && | *story\_ids\_* |
|  | ) |  |  |

Creates a function, which changes the list of pinned stories on a chat page; requires can\_edit\_stories administrator right in the chat.

Returns object\_ptr<Ok>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat\_id\_ | Identifier of the chat that posted the stories. |
    | [in] | story\_ids\_ | New list of pinned stories. All stories must be posted to the chat page first. There can be up to [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("pinned\_story\_count\_max") pinned stories on a chat page. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_pinned_stories.html#a8044dab2ba3c75066745014259c050c7)store()

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