# TDLib: starRevenueStatus Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Contains information about Telegram Stars earned by a user or a chat.

|  |  |
| --- | --- |
| Public Fields | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > | [total\_amount\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a18f2d9295e7d68ee6808e47c29ba715a) |
|  | Total Telegram Star amount earned. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > | [current\_amount\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a2c5668cbb7d47ce5cff8460596dc86ec) |
|  | The Telegram Star amount that isn't withdrawn yet. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > | [available\_amount\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a1f2320b45da7816d6cf13720ceae7687) |
|  | The Telegram Star amount that is available for withdrawal. |
|  | |
| bool | [withdrawal\_enabled\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#ae602557809411cde222587834241211e) |
|  | True, if Telegram Stars can be withdrawn now or later. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [next\_withdrawal\_in\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#ae383b80b1e4625b38b10a157814df2da) |
|  | Time left before the next withdrawal can be started, in seconds; 0 if withdrawal can be started now. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [starRevenueStatus](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#ad9d968f2e160c4e20f8b21dda6b46fcd) () |
|  | |
|  | [starRevenueStatus](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#acde80cc31ee2c8b66e81c61dc19d12a7) ([object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > &&[total\_amount\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a18f2d9295e7d68ee6808e47c29ba715a), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > &&[current\_amount\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a2c5668cbb7d47ce5cff8460596dc86ec), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > &&[available\_amount\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a1f2320b45da7816d6cf13720ceae7687), bool [withdrawal\_enabled\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#ae602557809411cde222587834241211e), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [next\_withdrawal\_in\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#ae383b80b1e4625b38b10a157814df2da)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 2006266600 |
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
| [starRevenueStatus](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html) | ( | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > && | *total\_amount\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > && | *current\_amount\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > && | *available\_amount\_*, |
|  |  | bool | *withdrawal\_enabled\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *next\_withdrawal\_in\_* |
|  | ) |  |  |

Contains information about Telegram Stars earned by a user or a chat.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | total\_amount\_ | Total Telegram Star amount earned. |
    | [in] | current\_amount\_ | The Telegram Star amount that isn't withdrawn yet. |
    | [in] | available\_amount\_ | The Telegram Star amount that is available for withdrawal. |
    | [in] | withdrawal\_enabled\_ | True, if Telegram Stars can be withdrawn now or later. |
    | [in] | next\_withdrawal\_in\_ | Time left before the next withdrawal can be started, in seconds; 0 if withdrawal can be started now. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_revenue_status.html#a8044dab2ba3c75066745014259c050c7)store()

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