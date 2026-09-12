# TDLib: chatEventUsernameChanged Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_username_changed.html

Inherits [ChatEventAction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_chat_event_action.html).

## Description

The chat editable username was changed.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [old_username_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_username_changed.html#a5adb4a4162061a6313276d3a4154d8ca) |
|  | Previous chat username. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [new_username_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_username_changed.html#ab2df921f2e05dcd184065b6fdb88c2f6) |
|  | New chat username. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [chatEventUsernameChanged](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_username_changed.html#a81e5d843ef2a725dc0d7f9a079d38399) () |
|  | |
|  | [chatEventUsernameChanged](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_username_changed.html#a3b28ec91c4bf34bd69d0b7a37c89321e) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[old_username_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_username_changed.html#a5adb4a4162061a6313276d3a4154d8ca), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[new_username_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_username_changed.html#ab2df921f2e05dcd184065b6fdb88c2f6)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_username_changed.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_username_changed.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1728558443 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_username_changed.html#a81e5d843ef2a725dc0d7f9a079d38399)chatEventUsernameChanged() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [chatEventUsernameChanged](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_username_changed.html) | ( |  | ) |  |

The chat editable username was changed.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_username_changed.html#a3b28ec91c4bf34bd69d0b7a37c89321e)chatEventUsernameChanged() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [chatEventUsernameChanged](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_username_changed.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *old_username_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *new_username_* |
|  | ) |  |  |

The chat editable username was changed.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | old_username_ | Previous chat username. |
    | [in] | new_username_ | New chat username. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_username_changed.html#a8044dab2ba3c75066745014259c050c7)store()

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