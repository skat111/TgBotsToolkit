# TDLib: giftsForResale Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes gifts available for resale.

|  |  |
| --- | --- |
| Public Fields | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [total_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#ad3e9b02d2b339bc59630382c38d07e68) |
|  | Total number of gifts found. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [giftForResale](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_for_resale.html) > > | [gifts_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#a475257a97526e5ed0dc21a1ff9012629) |
|  | The gifts. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [upgradedGiftModelCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_model_count.html) > > | [models_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#a10b766218d78922525a8f85f207feac9) |
|  | Available models; for [searchGiftsForResale](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_gifts_for_resale.html) requests without offset and attributes only. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [upgradedGiftSymbolCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_symbol_count.html) > > | [symbols_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#ae4478f9e80441e034ba6c6380ab026df) |
|  | Available symbols; for [searchGiftsForResale](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_gifts_for_resale.html) requests without offset and attributes only. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [upgradedGiftBackdropCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_backdrop_count.html) > > | [backdrops_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#a2ff7f368925e1479e45a43dea9f476c1) |
|  | Available backdrops; for [searchGiftsForResale](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_gifts_for_resale.html) requests without offset and attributes only. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [next_offset_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#a33570080057f7258ad9aac6e86cfbd84) |
|  | The offset for the next request. If empty, then there are no more results. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [giftsForResale](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#a01b60c308a1684f99dc10652319527a2) () |
|  | |
|  | [giftsForResale](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#aba278645c825fb6a0966e72676e71806) ([int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [total_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#ad3e9b02d2b339bc59630382c38d07e68), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [giftForResale](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_for_resale.html) >> &&[gifts_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#a475257a97526e5ed0dc21a1ff9012629), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [upgradedGiftModelCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_model_count.html) >> &&[models_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#a10b766218d78922525a8f85f207feac9), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [upgradedGiftSymbolCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_symbol_count.html) >> &&[symbols_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#ae4478f9e80441e034ba6c6380ab026df), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [upgradedGiftBackdropCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_backdrop_count.html) >> &&[backdrops_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#a2ff7f368925e1479e45a43dea9f476c1), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[next_offset_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#a33570080057f7258ad9aac6e86cfbd84)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 35082425 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#a01b60c308a1684f99dc10652319527a2)giftsForResale() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [giftsForResale](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html) | ( |  | ) |  |

Describes gifts available for resale.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#aba278645c825fb6a0966e72676e71806)giftsForResale() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [giftsForResale](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html) | ( | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *total_count_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [giftForResale](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_for_resale.html) >> && | *gifts_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [upgradedGiftModelCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_model_count.html) >> && | *models_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [upgradedGiftSymbolCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_symbol_count.html) >> && | *symbols_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [upgradedGiftBackdropCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1upgraded_gift_backdrop_count.html) >> && | *backdrops_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *next_offset_* |
|  | ) |  |  |

Describes gifts available for resale.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | total_count_ | Total number of gifts found. |
    | [in] | gifts_ | The gifts. |
    | [in] | models_ | Available models; for [searchGiftsForResale](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_gifts_for_resale.html) requests without offset and attributes only. |
    | [in] | symbols_ | Available symbols; for [searchGiftsForResale](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_gifts_for_resale.html) requests without offset and attributes only. |
    | [in] | backdrops_ | Available backdrops; for [searchGiftsForResale](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_gifts_for_resale.html) requests without offset and attributes only. |
    | [in] | next_offset_ | The offset for the next request. If empty, then there are no more results. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gifts_for_resale.html#a8044dab2ba3c75066745014259c050c7)store()

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