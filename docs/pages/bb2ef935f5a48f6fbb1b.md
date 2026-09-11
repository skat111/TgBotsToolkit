# TDLib: starPaymentOption Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes an option for buying Telegram Stars. Use [telegramPaymentPurposeStars](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1telegram_payment_purpose_stars.html) for out-of-store payments.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [currency\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#af027d823cea668905ec74448f1099d35) |
|  | ISO 4217 currency code for the payment. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [amount\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#a6b93487a4b387e2bf75ec0604b3d8209) |
|  | The amount to pay, in the smallest units of the currency. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [star\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#ad508b0848e631be2e72f8b8c664b94c4) |
|  | Number of Telegram Stars that will be purchased. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [store\_product\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#ae7f1ae5f9ef309db88e242864dc34604) |
|  | Identifier of the store product associated with the option; may be empty if none. |
|  | |
| bool | [is\_additional\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#a514afe1e6a6fb7359cbf2620d8c9f455) |
|  | True, if the option must be shown only in the full list of payment options. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [starPaymentOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#a238d025fc0a58cce28b8bf65d0f5a322) () |
|  | |
|  | [starPaymentOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#a7dc6f4b1817c95f4a4438f7bc1134139) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[currency\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#af027d823cea668905ec74448f1099d35), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [amount\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#a6b93487a4b387e2bf75ec0604b3d8209), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [star\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#ad508b0848e631be2e72f8b8c664b94c4), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[store\_product\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#ae7f1ae5f9ef309db88e242864dc34604), bool [is\_additional\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#a514afe1e6a6fb7359cbf2620d8c9f455)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1364056047 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#a238d025fc0a58cce28b8bf65d0f5a322)starPaymentOption() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [starPaymentOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html) | ( |  | ) |  |

Describes an option for buying Telegram Stars. Use [telegramPaymentPurposeStars](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1telegram_payment_purpose_stars.html) for out-of-store payments.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#a7dc6f4b1817c95f4a4438f7bc1134139)starPaymentOption() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [starPaymentOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *currency\_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *amount\_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *star\_count\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *store\_product\_id\_*, |
|  |  | bool | *is\_additional\_* |
|  | ) |  |  |

Describes an option for buying Telegram Stars. Use [telegramPaymentPurposeStars](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1telegram_payment_purpose_stars.html) for out-of-store payments.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | currency\_ | ISO 4217 currency code for the payment. |
    | [in] | amount\_ | The amount to pay, in the smallest units of the currency. |
    | [in] | star\_count\_ | Number of Telegram Stars that will be purchased. |
    | [in] | store\_product\_id\_ | Identifier of the store product associated with the option; may be empty if none. |
    | [in] | is\_additional\_ | True, if the option must be shown only in the full list of payment options. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_payment_option.html#a8044dab2ba3c75066745014259c050c7)store()

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