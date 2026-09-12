# TDLib: pageBlockCollage Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_collage.html

Inherits [PageBlock](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_page_block.html).

## Description

A collage.

|  |  |
| --- | --- |
| Public Fields | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [PageBlock](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_page_block.html) > > | [page_blocks_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_collage.html#a7301a4aebdcceac12b5e058b29927dbe) |
|  | Collage item contents. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [pageBlockCaption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_caption.html) > | [caption_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_collage.html#ac739d621ada24d66043dc18122e37114) |
|  | Block caption. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [pageBlockCollage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_collage.html#a7a70a7a694cdf66d6fc30d2a2188767c) () |
|  | |
|  | [pageBlockCollage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_collage.html#a3461aa07734040de3bfc7b5914bb3f96) ([array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [PageBlock](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_page_block.html) >> &&[page_blocks_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_collage.html#a7301a4aebdcceac12b5e058b29927dbe), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [pageBlockCaption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_caption.html) > &&[caption_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_collage.html#ac739d621ada24d66043dc18122e37114)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_collage.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_collage.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1163760110 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_collage.html#a7a70a7a694cdf66d6fc30d2a2188767c)pageBlockCollage() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [pageBlockCollage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_collage.html) | ( |  | ) |  |

A collage.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_collage.html#a3461aa07734040de3bfc7b5914bb3f96)pageBlockCollage() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [pageBlockCollage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_collage.html) | ( | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [PageBlock](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_page_block.html) >> && | *page_blocks_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [pageBlockCaption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_caption.html) > && | *caption_* |
|  | ) |  |  |

A collage.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | page_blocks_ | Collage item contents. |
    | [in] | caption_ | Block caption. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_collage.html#a8044dab2ba3c75066745014259c050c7)store()

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