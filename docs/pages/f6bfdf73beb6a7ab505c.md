# TDLib: internalLinkTypeGiftCollection Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_gift_collection.html

Inherits [InternalLinkType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_internal_link_type.html).

## Description

The link is a link to a gift collection. Call [searchPublicChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_public_chat.html) with the given username, then call [getReceivedGifts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_received_gifts.html) with the received gift owner identifier and the given collection identifier, then show the collection if received.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [gift\_owner\_username\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_gift_collection.html#a2f45759e3d78e57b2b79142b44866120) |
|  | Username of the owner of the gift collection. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [collection\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_gift_collection.html#a4f7a01c11b02cebd4a2b2b2cf87f44ce) |
|  | Gift collection identifier. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [internalLinkTypeGiftCollection](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_gift_collection.html#a75506f1bbd95ceb2042086f06a9620cd) () |
|  | |
|  | [internalLinkTypeGiftCollection](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_gift_collection.html#a582d9397813d4d8775c12062464aba08) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[gift\_owner\_username\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_gift_collection.html#a2f45759e3d78e57b2b79142b44866120), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [collection\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_gift_collection.html#a4f7a01c11b02cebd4a2b2b2cf87f44ce)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_gift_collection.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_gift_collection.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -812480347 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_gift_collection.html#a75506f1bbd95ceb2042086f06a9620cd)internalLinkTypeGiftCollection() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [internalLinkTypeGiftCollection](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_gift_collection.html) | ( |  | ) |  |

The link is a link to a gift collection. Call [searchPublicChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_public_chat.html) with the given username, then call [getReceivedGifts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_received_gifts.html) with the received gift owner identifier and the given collection identifier, then show the collection if received.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_gift_collection.html#a582d9397813d4d8775c12062464aba08)internalLinkTypeGiftCollection() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [internalLinkTypeGiftCollection](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_gift_collection.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *gift\_owner\_username\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *collection\_id\_* |
|  | ) |  |  |

The link is a link to a gift collection. Call [searchPublicChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_public_chat.html) with the given username, then call [getReceivedGifts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_received_gifts.html) with the received gift owner identifier and the given collection identifier, then show the collection if received.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | gift\_owner\_username\_ | Username of the owner of the gift collection. |
    | [in] | collection\_id\_ | Gift collection identifier. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_gift_collection.html#a8044dab2ba3c75066745014259c050c7)store()

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