# TDLib: starSubscriptions Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Represents a list of Telegram Star subscriptions.

|  |  |
| --- | --- |
| Public Fields | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > | [star_amount_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#a2496222fd9e2f511abe81e45e4873989) |
|  | The amount of owned Telegram Stars. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starSubscription](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscription.html) > > | [subscriptions_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#af891377e669ca6fa664e43f4f5e729d4) |
|  | List of subscriptions for Telegram Stars. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [required_star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#a372015b4130692166b3516e152146632) |
|  | The number of Telegram Stars required to buy to extend subscriptions expiring soon. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [next_offset_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#a33570080057f7258ad9aac6e86cfbd84) |
|  | The offset for the next request. If empty, then there are no more results. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [starSubscriptions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#aff11b71b98094852a562079eede85e85) () |
|  | |
|  | [starSubscriptions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#a264e8d66f7a2f90efe103e450b8ab370) ([object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > &&[star_amount_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#a2496222fd9e2f511abe81e45e4873989), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starSubscription](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscription.html) >> &&[subscriptions_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#af891377e669ca6fa664e43f4f5e729d4), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [required_star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#a372015b4130692166b3516e152146632), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[next_offset_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#a33570080057f7258ad9aac6e86cfbd84)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 151169395 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#aff11b71b98094852a562079eede85e85)starSubscriptions() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [starSubscriptions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html) | ( |  | ) |  |

Represents a list of Telegram Star subscriptions.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#a264e8d66f7a2f90efe103e450b8ab370)starSubscriptions() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [starSubscriptions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html) | ( | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > && | *star_amount_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starSubscription](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscription.html) >> && | *subscriptions_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *required_star_count_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *next_offset_* |
|  | ) |  |  |

Represents a list of Telegram Star subscriptions.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | star_amount_ | The amount of owned Telegram Stars. |
    | [in] | subscriptions_ | List of subscriptions for Telegram Stars. |
    | [in] | required_star_count_ | The number of Telegram Stars required to buy to extend subscriptions expiring soon. |
    | [in] | next_offset_ | The offset for the next request. If empty, then there are no more results. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_subscriptions.html#a8044dab2ba3c75066745014259c050c7)store()

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