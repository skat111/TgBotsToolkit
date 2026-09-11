# TDLib: chatActionBarJoinRequest Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html

Inherits [ChatActionBar](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_chat_action_bar.html).

## Description

The chat is a private chat with an administrator of a chat to which the user sent join request.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [title\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html#ae49b8c94dab3e85761dd65876260deb9) |
|  | Title of the chat to which the join request was sent. |
|  | |
| bool | [is\_channel\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html#a03c3ef88b91f79e111f3f015657a06e8) |
|  | True, if the join request was sent to a channel chat. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [request\_date\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html#af108bd54d0b9e49fda8f21839c59a1b9) |
|  | Point in time (Unix timestamp) when the join request was sent. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [chatActionBarJoinRequest](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html#afdb834b8b2f46f5c9f0a3bf7cc25ab9c) () |
|  | |
|  | [chatActionBarJoinRequest](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html#af0c87ffda5e746150eca870f0deb6dbe) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[title\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html#ae49b8c94dab3e85761dd65876260deb9), bool [is\_channel\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html#a03c3ef88b91f79e111f3f015657a06e8), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [request\_date\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html#af108bd54d0b9e49fda8f21839c59a1b9)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1037140744 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html#afdb834b8b2f46f5c9f0a3bf7cc25ab9c)chatActionBarJoinRequest() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [chatActionBarJoinRequest](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html) | ( |  | ) |  |

The chat is a private chat with an administrator of a chat to which the user sent join request.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html#af0c87ffda5e746150eca870f0deb6dbe)chatActionBarJoinRequest() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [chatActionBarJoinRequest](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *title\_*, |
|  |  | bool | *is\_channel\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *request\_date\_* |
|  | ) |  |  |

The chat is a private chat with an administrator of a chat to which the user sent join request.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | title\_ | Title of the chat to which the join request was sent. |
    | [in] | is\_channel\_ | True, if the join request was sent to a channel chat. |
    | [in] | request\_date\_ | Point in time (Unix timestamp) when the join request was sent. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_action_bar_join_request.html#a8044dab2ba3c75066745014259c050c7)store()

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