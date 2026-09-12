# TDLib: upgradedGiftValueInfo Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Contains information about value of an upgraded gift.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [currency_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#af027d823cea668905ec74448f1099d35) |
|  | ISO 4217 currency code of the currency in which the prices are represented. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [value_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a505df171d361615f56b8e47d3dbe2c62) |
|  | Estimated value of the gift; in the smallest units of the currency. |
|  | |
| bool | [is_value_average_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#accd559a6e471df619f99013ade9f6d3e) |
|  | True, if the value is calculated as average value of similar sold gifts. Otherwise, it is based on the sale price of the gift. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [initial_sale_date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#aef897ef44941197e15bdd519414d48b4) |
|  | Point in time (Unix timestamp) when the corresponding regular gift was originally purchased. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [initial_sale_star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#ab5353edc29a548fb03eb16b48ac1a7f4) |
|  | The Telegram Star amount that was paid for the gift. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [initial_sale_price_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a48dbd993557ed31f242f63a29f7253e9) |
|  | Initial price of the gift; in the smallest units of the currency. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [last_sale_date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a43cfe2de1a2604dba9155a71684de8a3) |
|  | Point in time (Unix timestamp) when the upgraded gift was purchased last time; 0 if never. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [last_sale_price_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a6b3c41f861360e4a1d65912dd8b19310) |
|  | Last purchase price of the gift; in the smallest units of the currency; 0 if the gift has never been resold. |
|  | |
| bool | [is_last_sale_on_fragment_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a62bcddd9f42d53e997144839744094ca) |
|  | True, if the last sale was completed on Fragment. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [minimum_price_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a16f7c3e28921dfd38d79f212e75b411f) |
|  | The current minimum price of gifts upgraded from the same gift; in the smallest units of the currency; 0 if there are no such gifts. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [average_sale_price_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a0f33e274447af9d26366633cbe9b316c) |
|  | The average sale price in the last month of gifts upgraded from the same gift; in the smallest units of the currency; 0 if there were no such sales. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [telegram_listed_gift_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#ad970d86028c9d64fd1a523a41843ecb2) |
|  | Number of gifts upgraded from the same gift being resold on Telegram. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [fragment_listed_gift_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a8ad6df139f3bd39631c84fd0ed277f3c) |
|  | Number of gifts upgraded from the same gift being resold on Fragment. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [fragment_url_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#af7a909804bac94630581cca517f9fa32) |
|  | The HTTPS link to the Fragment for the gift; may be empty if there are no such gifts being sold on Fragment. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [upgradedGiftValueInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a013e00646863821035e59e44216e255a) () |
|  | |
|  | [upgradedGiftValueInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a8597df831fa882289c34be76745fe8bd) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[currency_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#af027d823cea668905ec74448f1099d35), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [value_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a505df171d361615f56b8e47d3dbe2c62), bool [is_value_average_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#accd559a6e471df619f99013ade9f6d3e), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [initial_sale_date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#aef897ef44941197e15bdd519414d48b4), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [initial_sale_star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#ab5353edc29a548fb03eb16b48ac1a7f4), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [initial_sale_price_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a48dbd993557ed31f242f63a29f7253e9), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [last_sale_date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a43cfe2de1a2604dba9155a71684de8a3), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [last_sale_price_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a6b3c41f861360e4a1d65912dd8b19310), bool [is_last_sale_on_fragment_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a62bcddd9f42d53e997144839744094ca), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [minimum_price_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a16f7c3e28921dfd38d79f212e75b411f), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [average_sale_price_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a0f33e274447af9d26366633cbe9b316c), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [telegram_listed_gift_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#ad970d86028c9d64fd1a523a41843ecb2), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [fragment_listed_gift_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a8ad6df139f3bd39631c84fd0ed277f3c), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[fragment_url_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#af7a909804bac94630581cca517f9fa32)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1729877677 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a013e00646863821035e59e44216e255a)upgradedGiftValueInfo() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [upgradedGiftValueInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html) | ( |  | ) |  |

Contains information about value of an upgraded gift.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a8597df831fa882289c34be76745fe8bd)upgradedGiftValueInfo() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [upgradedGiftValueInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *currency_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *value_*, |
|  |  | bool | *is_value_average_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *initial_sale_date_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *initial_sale_star_count_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *initial_sale_price_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *last_sale_date_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *last_sale_price_*, |
|  |  | bool | *is_last_sale_on_fragment_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *minimum_price_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *average_sale_price_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *telegram_listed_gift_count_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *fragment_listed_gift_count_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *fragment_url_* |
|  | ) |  |  |

Contains information about value of an upgraded gift.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | currency_ | ISO 4217 currency code of the currency in which the prices are represented. |
    | [in] | value_ | Estimated value of the gift; in the smallest units of the currency. |
    | [in] | is_value_average_ | True, if the value is calculated as average value of similar sold gifts. Otherwise, it is based on the sale price of the gift. |
    | [in] | initial_sale_date_ | Point in time (Unix timestamp) when the corresponding regular gift was originally purchased. |
    | [in] | initial_sale_star_count_ | The Telegram Star amount that was paid for the gift. |
    | [in] | initial_sale_price_ | Initial price of the gift; in the smallest units of the currency. |
    | [in] | last_sale_date_ | Point in time (Unix timestamp) when the upgraded gift was purchased last time; 0 if never. |
    | [in] | last_sale_price_ | Last purchase price of the gift; in the smallest units of the currency; 0 if the gift has never been resold. |
    | [in] | is_last_sale_on_fragment_ | True, if the last sale was completed on Fragment. |
    | [in] | minimum_price_ | The current minimum price of gifts upgraded from the same gift; in the smallest units of the currency; 0 if there are no such gifts. |
    | [in] | average_sale_price_ | The average sale price in the last month of gifts upgraded from the same gift; in the smallest units of the currency; 0 if there were no such sales. |
    | [in] | telegram_listed_gift_count_ | Number of gifts upgraded from the same gift being resold on Telegram. |
    | [in] | fragment_listed_gift_count_ | Number of gifts upgraded from the same gift being resold on Fragment. |
    | [in] | fragment_url_ | The HTTPS link to the Fragment for the gift; may be empty if there are no such gifts being sold on Fragment. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_value_info.html#a8044dab2ba3c75066745014259c050c7)store()

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