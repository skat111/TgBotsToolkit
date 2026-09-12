# TDLib: getStarWithdrawalUrl Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Returns a URL for Telegram Star withdrawal.

Returns object_ptr<HttpUrl>.

|  |  |
| --- | --- |
| Public Fields | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > | [owner_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html#a29f1436e40d2ba3e26b064b6f34832da) |
|  | Identifier of the owner of the Telegram Stars; can be identifier of the current user, an owned bot, or an owned supergroup or channel chat. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html#ad508b0848e631be2e72f8b8c664b94c4) |
|  | The number of Telegram Stars to withdraw; must be between [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("star_withdrawal_count_min") and [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("star_withdrawal_count_max"). |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [password_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html#afbc1b6b06e669783ad50b5cfdfbf3e7e) |
|  | The 2-step verification password of the current user. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html#a89600d844008faaad1ecacab98018b81) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [httpUrl](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1http_url.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [getStarWithdrawalUrl](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html#aa035159be8c3aecfd5afb3d9b6ec2aba) () |
|  | |
|  | [getStarWithdrawalUrl](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html#ad7859ea58273ae4ea035a72561e187d1) ([object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > &&[owner_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html#a29f1436e40d2ba3e26b064b6f34832da), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html#ad508b0848e631be2e72f8b8c664b94c4), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[password_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html#afbc1b6b06e669783ad50b5cfdfbf3e7e)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1445841134 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html#aa035159be8c3aecfd5afb3d9b6ec2aba)getStarWithdrawalUrl() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [getStarWithdrawalUrl](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html) | ( |  | ) |  |

Default constructor for a function, which returns a URL for Telegram Star withdrawal.

Returns object_ptr<HttpUrl>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html#ad7859ea58273ae4ea035a72561e187d1)getStarWithdrawalUrl() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [getStarWithdrawalUrl](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html) | ( | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > && | *owner_id_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *star_count_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *password_* |
|  | ) |  |  |

Creates a function, which returns a URL for Telegram Star withdrawal.

Returns object_ptr<HttpUrl>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | owner_id_ | Identifier of the owner of the Telegram Stars; can be identifier of the current user, an owned bot, or an owned supergroup or channel chat. |
    | [in] | star_count_ | The number of Telegram Stars to withdraw; must be between [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("star_withdrawal_count_min") and [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("star_withdrawal_count_max"). |
    | [in] | password_ | The 2-step verification password of the current user. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_star_withdrawal_url.html#a8044dab2ba3c75066745014259c050c7)store()

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