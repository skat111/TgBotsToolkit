# TDLib: recoverAuthenticationPassword Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Recovers the 2-step verification password with a password recovery code sent to an email address that was previously set up. Works only when the current authorization state is [authorizationStateWaitPassword](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_password.html).

Returns object_ptr<Ok>.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [recovery_code_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html#aa4659c1d80e67a22747677ab5c6761ce) |
|  | Recovery code to check. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [new_password_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html#a78488f4dfec18b8e647571c2f49d7976) |
|  | New 2-step verification password of the user; may be empty to remove the password. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [new_hint_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html#ad8b63067fcb0711256be8fbe9de1af43) |
|  | New password hint; may be empty. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html#ab684327f0ee9cbf9afb740503d89f019) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ok](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1ok.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [recoverAuthenticationPassword](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html#a98c9306db1ea2987f919d3b5254d098d) () |
|  | |
|  | [recoverAuthenticationPassword](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html#aba1d69223bcd3ad50667e79e7d6c12ea) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[recovery_code_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html#aa4659c1d80e67a22747677ab5c6761ce), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[new_password_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html#a78488f4dfec18b8e647571c2f49d7976), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[new_hint_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html#ad8b63067fcb0711256be8fbe9de1af43)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -131001053 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html#a98c9306db1ea2987f919d3b5254d098d)recoverAuthenticationPassword() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [recoverAuthenticationPassword](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html) | ( |  | ) |  |

Default constructor for a function, which recovers the 2-step verification password with a password recovery code sent to an email address that was previously set up. Works only when the current authorization state is [authorizationStateWaitPassword](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_password.html).

Returns object_ptr<Ok>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html#aba1d69223bcd3ad50667e79e7d6c12ea)recoverAuthenticationPassword() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [recoverAuthenticationPassword](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *recovery_code_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *new_password_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *new_hint_* |
|  | ) |  |  |

Creates a function, which recovers the 2-step verification password with a password recovery code sent to an email address that was previously set up. Works only when the current authorization state is [authorizationStateWaitPassword](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_password.html).

Returns object_ptr<Ok>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | recovery_code_ | Recovery code to check. |
    | [in] | new_password_ | New 2-step verification password of the user; may be empty to remove the password. |
    | [in] | new_hint_ | New password hint; may be empty. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1recover_authentication_password.html#a8044dab2ba3c75066745014259c050c7)store()

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