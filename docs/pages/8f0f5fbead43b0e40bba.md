# TDLib: toggleBotUsernameIsActive Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Changes active state for a username of a bot. The editable username can be disabled only if there are other active usernames. May return an error with a message "USERNAMES_ACTIVE_TOO_MUCH" if the maximum number of active usernames has been reached. Can be called only if userTypeBot.can_be_edited == true.

Returns object_ptr<Ok>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [bot_user_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html#a852a1eecf72791be8eb2633ff5dcaec4) |
|  | Identifier of the target bot. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [username_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html#a1ee37eaede4098b7d83340cc202963d5) |
|  | The username to change. |
|  | |
| bool | [is_active_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html#a6eaf1abc6903a9ffe52dbde4383a69f1) |
|  | Pass true to activate the username; pass false to disable it. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html#ab684327f0ee9cbf9afb740503d89f019) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ok](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1ok.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [toggleBotUsernameIsActive](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html#a3fe8fd962278755298f2f516de70fbf7) () |
|  | |
|  | [toggleBotUsernameIsActive](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html#a327cdc5f0287d0a2153f75f700bd9597) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [bot_user_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html#a852a1eecf72791be8eb2633ff5dcaec4), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[username_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html#a1ee37eaede4098b7d83340cc202963d5), bool [is_active_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html#a6eaf1abc6903a9ffe52dbde4383a69f1)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 2036569097 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html#a3fe8fd962278755298f2f516de70fbf7)toggleBotUsernameIsActive() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [toggleBotUsernameIsActive](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html) | ( |  | ) |  |

Default constructor for a function, which changes active state for a username of a bot. The editable username can be disabled only if there are other active usernames. May return an error with a message "USERNAMES_ACTIVE_TOO_MUCH" if the maximum number of active usernames has been reached. Can be called only if userTypeBot.can_be_edited == true.

Returns object_ptr<Ok>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html#a327cdc5f0287d0a2153f75f700bd9597)toggleBotUsernameIsActive() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [toggleBotUsernameIsActive](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *bot_user_id_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *username_*, |
|  |  | bool | *is_active_* |
|  | ) |  |  |

Creates a function, which changes active state for a username of a bot. The editable username can be disabled only if there are other active usernames. May return an error with a message "USERNAMES_ACTIVE_TOO_MUCH" if the maximum number of active usernames has been reached. Can be called only if userTypeBot.can_be_edited == true.

Returns object_ptr<Ok>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | bot_user_id_ | Identifier of the target bot. |
    | [in] | username_ | The username to change. |
    | [in] | is_active_ | Pass true to activate the username; pass false to disable it. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_bot_username_is_active.html#a8044dab2ba3c75066745014259c050c7)store()

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