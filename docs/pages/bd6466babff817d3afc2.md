# TDLib: pushMessageContentGiveaway Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html

Inherits [PushMessageContent](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_push_message_content.html).

## Description

A message with a giveaway.

|  |  |
| --- | --- |
| Public Fields | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [winner\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html#aefb4b5f6a67e068d822b931abdb54722) |
|  | Number of users which will receive giveaway prizes; 0 for pinned message. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [GiveawayPrize](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_giveaway_prize.html) > | [prize\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html#aa361944b63696cf8539d0da8dd8e98e4) |
|  | Prize of the giveaway; may be null for pinned message. |
|  | |
| bool | [is\_pinned\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html#ada3cbd9c3e89da9f894cd2f29725799d) |
|  | True, if the message is a pinned message with the specified content. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [pushMessageContentGiveaway](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html#a6d4839f0c79d08c461736d38d5dde66d) () |
|  | |
|  | [pushMessageContentGiveaway](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html#a2bc36a469cdb3a9a7ead0be6b2b6f639) ([int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [winner\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html#aefb4b5f6a67e068d822b931abdb54722), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [GiveawayPrize](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_giveaway_prize.html) > &&[prize\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html#aa361944b63696cf8539d0da8dd8e98e4), bool [is\_pinned\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html#ada3cbd9c3e89da9f894cd2f29725799d)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -700547186 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html#a6d4839f0c79d08c461736d38d5dde66d)pushMessageContentGiveaway() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [pushMessageContentGiveaway](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html) | ( |  | ) |  |

A message with a giveaway.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html#a2bc36a469cdb3a9a7ead0be6b2b6f639)pushMessageContentGiveaway() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [pushMessageContentGiveaway](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html) | ( | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *winner\_count\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [GiveawayPrize](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_giveaway_prize.html) > && | *prize\_*, |
|  |  | bool | *is\_pinned\_* |
|  | ) |  |  |

A message with a giveaway.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | winner\_count\_ | Number of users which will receive giveaway prizes; 0 for pinned message. |
    | [in] | prize\_ | Prize of the giveaway; may be null for pinned message. |
    | [in] | is\_pinned\_ | True, if the message is a pinned message with the specified content. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_giveaway.html#a8044dab2ba3c75066745014259c050c7)store()

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