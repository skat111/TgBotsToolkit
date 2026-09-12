# TDLib: starRevenueStatus Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Contains information about Telegram Stars earned by a user or a chat.

|  |  |
| --- | --- |
| Public Fields | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > | [total_amount_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a18f2d9295e7d68ee6808e47c29ba715a) |
|  | Total Telegram Star amount earned. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > | [current_amount_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a2c5668cbb7d47ce5cff8460596dc86ec) |
|  | The Telegram Star amount that isn't withdrawn yet. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > | [available_amount_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a1f2320b45da7816d6cf13720ceae7687) |
|  | The Telegram Star amount that is available for withdrawal. |
|  | |
| bool | [withdrawal_enabled_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#ae602557809411cde222587834241211e) |
|  | True, if Telegram Stars can be withdrawn now or later. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [next_withdrawal_in_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#ae383b80b1e4625b38b10a157814df2da) |
|  | Time left before the next withdrawal can be started, in seconds; 0 if withdrawal can be started now. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [starRevenueStatus](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#ad9d968f2e160c4e20f8b21dda6b46fcd) () |
|  | |
|  | [starRevenueStatus](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#acde80cc31ee2c8b66e81c61dc19d12a7) ([object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > &&[total_amount_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a18f2d9295e7d68ee6808e47c29ba715a), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > &&[current_amount_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a2c5668cbb7d47ce5cff8460596dc86ec), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > &&[available_amount_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a1f2320b45da7816d6cf13720ceae7687), bool [withdrawal_enabled_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#ae602557809411cde222587834241211e), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [next_withdrawal_in_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#ae383b80b1e4625b38b10a157814df2da)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 2006266600 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#ad9d968f2e160c4e20f8b21dda6b46fcd)starRevenueStatus() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [starRevenueStatus](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html) | ( |  | ) |  |

Contains information about Telegram Stars earned by a user or a chat.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#acde80cc31ee2c8b66e81c61dc19d12a7)starRevenueStatus() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [starRevenueStatus](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html) | ( | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > && | *total_amount_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > && | *current_amount_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > && | *available_amount_*, |
|  |  | bool | *withdrawal_enabled_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *next_withdrawal_in_* |
|  | ) |  |  |

Contains information about Telegram Stars earned by a user or a chat.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | total_amount_ | Total Telegram Star amount earned. |
    | [in] | current_amount_ | The Telegram Star amount that isn't withdrawn yet. |
    | [in] | available_amount_ | The Telegram Star amount that is available for withdrawal. |
    | [in] | withdrawal_enabled_ | True, if Telegram Stars can be withdrawn now or later. |
    | [in] | next_withdrawal_in_ | Time left before the next withdrawal can be started, in seconds; 0 if withdrawal can be started now. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a8044dab2ba3c75066745014259c050c7)store()

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