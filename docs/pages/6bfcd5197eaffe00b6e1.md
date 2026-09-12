# TDLib: premiumGiftPaymentOption Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes an option for gifting Telegram Premium to a user. Use [telegramPaymentPurposePremiumGift](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1telegram_payment_purpose_premium_gift.html) for out-of-store payments or payments in Telegram Stars.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [currency_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#af027d823cea668905ec74448f1099d35) |
|  | ISO 4217 currency code for the payment. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [amount_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#a6b93487a4b387e2bf75ec0604b3d8209) |
|  | The amount to pay, in the smallest units of the currency. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#ad508b0848e631be2e72f8b8c664b94c4) |
|  | The alternative Telegram Star amount to pay; 0 if payment in Telegram Stars is not possible. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [discount_percentage_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#a43553d06339f2925ebadf4d46eea8442) |
|  | The discount associated with this option, as a percentage. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [month_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#a7650c5c484689e444d76aec30eff15cd) |
|  | Number of months the Telegram Premium subscription will be active. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [store_product_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#ae7f1ae5f9ef309db88e242864dc34604) |
|  | Identifier of the store product associated with the option. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [sticker](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sticker.html) > | [sticker_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#a681634f2c1ba6d856402bcb704471cc4) |
|  | A sticker to be shown along with the option; may be null if unknown. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [premiumGiftPaymentOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#ae9de93c8045bb4fcf3c2fe7659fb59a9) () |
|  | |
|  | [premiumGiftPaymentOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#adb535d575870876574f705399c2bcf0b) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[currency_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#af027d823cea668905ec74448f1099d35), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [amount_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#a6b93487a4b387e2bf75ec0604b3d8209), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#ad508b0848e631be2e72f8b8c664b94c4), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [discount_percentage_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#a43553d06339f2925ebadf4d46eea8442), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [month_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#a7650c5c484689e444d76aec30eff15cd), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[store_product_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#ae7f1ae5f9ef309db88e242864dc34604), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [sticker](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sticker.html) > &&[sticker_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#a681634f2c1ba6d856402bcb704471cc4)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -338085027 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#ae9de93c8045bb4fcf3c2fe7659fb59a9)premiumGiftPaymentOption() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [premiumGiftPaymentOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html) | ( |  | ) |  |

Describes an option for gifting Telegram Premium to a user. Use [telegramPaymentPurposePremiumGift](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1telegram_payment_purpose_premium_gift.html) for out-of-store payments or payments in Telegram Stars.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#adb535d575870876574f705399c2bcf0b)premiumGiftPaymentOption() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [premiumGiftPaymentOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *currency_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *amount_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *star_count_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *discount_percentage_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *month_count_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *store_product_id_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [sticker](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sticker.html) > && | *sticker_* |
|  | ) |  |  |

Describes an option for gifting Telegram Premium to a user. Use [telegramPaymentPurposePremiumGift](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1telegram_payment_purpose_premium_gift.html) for out-of-store payments or payments in Telegram Stars.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | currency_ | ISO 4217 currency code for the payment. |
    | [in] | amount_ | The amount to pay, in the smallest units of the currency. |
    | [in] | star_count_ | The alternative Telegram Star amount to pay; 0 if payment in Telegram Stars is not possible. |
    | [in] | discount_percentage_ | The discount associated with this option, as a percentage. |
    | [in] | month_count_ | Number of months the Telegram Premium subscription will be active. |
    | [in] | store_product_id_ | Identifier of the store product associated with the option. |
    | [in] | sticker_ | A sticker to be shown along with the option; may be null if unknown. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_gift_payment_option.html#a8044dab2ba3c75066745014259c050c7)store()

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