# TDLib: textEntityTypeTextUrl Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_text_url.html

Inherits [TextEntityType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_text_entity_type.html).

## Description

A text description shown instead of a raw URL.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [url\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_text_url.html#a541e0f072a74af71d6978eea722fc5fe) |
|  | HTTP or tg:// URL to be opened when the link is clicked. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [textEntityTypeTextUrl](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_text_url.html#a361fff37426e25f9de3ccceff567f687) () |
|  | |
|  | [textEntityTypeTextUrl](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_text_url.html#a1a6108d29b1dc99f5ed6a5b83fc84224) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[url\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_text_url.html#a541e0f072a74af71d6978eea722fc5fe)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_text_url.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_text_url.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 445719651 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_text_url.html#a361fff37426e25f9de3ccceff567f687)textEntityTypeTextUrl() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [textEntityTypeTextUrl](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_text_url.html) | ( |  | ) |  |

A text description shown instead of a raw URL.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_text_url.html#a1a6108d29b1dc99f5ed6a5b83fc84224)textEntityTypeTextUrl() [2/2]

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [textEntityTypeTextUrl](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_text_url.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *url\_* | ) |  | | explicit |

A text description shown instead of a raw URL.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | url\_ | HTTP or tg:// URL to be opened when the link is clicked. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_text_url.html#a8044dab2ba3c75066745014259c050c7)store()

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