# TDLib: giftAuctionState Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_state.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Represent auction state of a gift.

|  |  |
| --- | --- |
| Public Fields | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [gift](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift.html) > | [gift_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_state.html#a909377734c84e5ce4307952ae2c55b9c) |
|  | The gift. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [AuctionState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_auction_state.html) > | [state_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_state.html#a58206b61f5894263f035a8c68e04c6f5) |
|  | Auction state of the gift. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [giftAuctionState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_state.html#abd791934cd0f1a7802bc96a122b56f3e) () |
|  | |
|  | [giftAuctionState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_state.html#a778ea2af32a5df7573c55c47dac6f6dc) ([object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [gift](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift.html) > &&[gift_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_state.html#a909377734c84e5ce4307952ae2c55b9c), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [AuctionState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_auction_state.html) > &&[state_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_state.html#a58206b61f5894263f035a8c68e04c6f5)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_state.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_state.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1691485529 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_state.html#abd791934cd0f1a7802bc96a122b56f3e)giftAuctionState() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [giftAuctionState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_state.html) | ( |  | ) |  |

Represent auction state of a gift.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_state.html#a778ea2af32a5df7573c55c47dac6f6dc)giftAuctionState() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [giftAuctionState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_state.html) | ( | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [gift](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift.html) > && | *gift_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [AuctionState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_auction_state.html) > && | *state_* |
|  | ) |  |  |

Represent auction state of a gift.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | gift_ | The gift. |
    | [in] | state_ | Auction state of the gift. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_auction_state.html#a8044dab2ba3c75066745014259c050c7)store()

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