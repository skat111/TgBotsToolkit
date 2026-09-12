# TDLib: getGiftAuctionAcquiredGifts Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_gift_auction_acquired_gifts.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Returns the gifts that were acquired by the current user on a gift auction.

Returns object_ptr<GiftAuctionAcquiredGifts>.

|  |  |
| --- | --- |
| Public Fields | |
| [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | [gift_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_gift_auction_acquired_gifts.html#ad8fa083fdde8772552ac42adae3befa1) |
|  | Identifier of the auctioned gift. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_gift_auction_acquired_gifts.html#a2d835c98e2d95a40a67cf09c00ebddcb) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [giftAuctionAcquiredGifts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_acquired_gifts.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [getGiftAuctionAcquiredGifts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_gift_auction_acquired_gifts.html#a5dedc9b77ab33992612d97ab50145a5b) () |
|  | |
|  | [getGiftAuctionAcquiredGifts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_gift_auction_acquired_gifts.html#a77c79b79c05e302f1fd0b7232fe63dc4) ([int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) [gift_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_gift_auction_acquired_gifts.html#ad8fa083fdde8772552ac42adae3befa1)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_gift_auction_acquired_gifts.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_gift_auction_acquired_gifts.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -937975215 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_gift_auction_acquired_gifts.html#a5dedc9b77ab33992612d97ab50145a5b)getGiftAuctionAcquiredGifts() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [getGiftAuctionAcquiredGifts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_gift_auction_acquired_gifts.html) | ( |  | ) |  |

Default constructor for a function, which returns the gifts that were acquired by the current user on a gift auction.

Returns object_ptr<GiftAuctionAcquiredGifts>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_gift_auction_acquired_gifts.html#a77c79b79c05e302f1fd0b7232fe63dc4)getGiftAuctionAcquiredGifts() [2/2]

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [getGiftAuctionAcquiredGifts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_gift_auction_acquired_gifts.html) | ( | [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | *gift_id_* | ) |  | | explicit |

Creates a function, which returns the gifts that were acquired by the current user on a gift auction.

Returns object_ptr<GiftAuctionAcquiredGifts>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | gift_id_ | Identifier of the auctioned gift. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_gift_auction_acquired_gifts.html#a8044dab2ba3c75066745014259c050c7)store()

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