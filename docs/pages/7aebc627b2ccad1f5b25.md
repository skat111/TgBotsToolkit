# TDLib: messageGiveawayPrizeStars Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html

Inherits [MessageContent](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_content.html).

## Description

A Telegram Stars were received by the current user from a giveaway.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#ad508b0848e631be2e72f8b8c664b94c4) |
|  | Number of Telegram Stars that were received. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [transaction_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#a72bab3e9d416d8a7f8403b884e7f6b67) |
|  | Identifier of the transaction for Telegram Stars credit. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [boosted_chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#ae95fba70af0949e2ab1e5c4798953d7b) |
|  | Identifier of the supergroup or channel chat, which was automatically boosted by the winners of the giveaway. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [giveaway_message_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#a116e1ed78d838b14023fd0ab38285f7f) |
|  | Identifier of the message with the giveaway in the boosted chat; may be 0 or an identifier of a deleted message. |
|  | |
| bool | [is_unclaimed_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#a2a252d6595b8c2b1182aaacd7c4b5524) |
|  | True, if the corresponding winner wasn't chosen and the Telegram Stars were received by the owner of the boosted chat. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [sticker](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sticker.html) > | [sticker_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#a681634f2c1ba6d856402bcb704471cc4) |
|  | A sticker to be shown in the message; may be null if unknown. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [messageGiveawayPrizeStars](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#a15231bdb8cc04780f8836d2c9098cff8) () |
|  | |
|  | [messageGiveawayPrizeStars](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#a427080dfc04cec699058f312257a3850) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#ad508b0848e631be2e72f8b8c664b94c4), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[transaction_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#a72bab3e9d416d8a7f8403b884e7f6b67), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [boosted_chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#ae95fba70af0949e2ab1e5c4798953d7b), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [giveaway_message_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#a116e1ed78d838b14023fd0ab38285f7f), bool [is_unclaimed_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#a2a252d6595b8c2b1182aaacd7c4b5524), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [sticker](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sticker.html) > &&[sticker_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#a681634f2c1ba6d856402bcb704471cc4)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1441833501 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#a15231bdb8cc04780f8836d2c9098cff8)messageGiveawayPrizeStars() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [messageGiveawayPrizeStars](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html) | ( |  | ) |  |

A Telegram Stars were received by the current user from a giveaway.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#a427080dfc04cec699058f312257a3850)messageGiveawayPrizeStars() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [messageGiveawayPrizeStars](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *star_count_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *transaction_id_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *boosted_chat_id_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *giveaway_message_id_*, |
|  |  | bool | *is_unclaimed_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [sticker](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sticker.html) > && | *sticker_* |
|  | ) |  |  |

A Telegram Stars were received by the current user from a giveaway.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | star_count_ | Number of Telegram Stars that were received. |
    | [in] | transaction_id_ | Identifier of the transaction for Telegram Stars credit. |
    | [in] | boosted_chat_id_ | Identifier of the supergroup or channel chat, which was automatically boosted by the winners of the giveaway. |
    | [in] | giveaway_message_id_ | Identifier of the message with the giveaway in the boosted chat; may be 0 or an identifier of a deleted message. |
    | [in] | is_unclaimed_ | True, if the corresponding winner wasn't chosen and the Telegram Stars were received by the owner of the boosted chat. |
    | [in] | sticker_ | A sticker to be shown in the message; may be null if unknown. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_giveaway_prize_stars.html#a8044dab2ba3c75066745014259c050c7)store()

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