# TDLib: linkPreviewTypeBackground Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_background.html

Inherits [LinkPreviewType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_link_preview_type.html).

## Description

The link is a link to a background. Link preview title and description are available only for filled backgrounds.

|  |  |
| --- | --- |
| Public Fields | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [document](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1document.html) > | [document\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_background.html#a5613fcca3b412b4faf119edfe151e2f1) |
|  | Document with the background; may be null for filled backgrounds. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [BackgroundType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_background_type.html) > | [background\_type\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_background.html#a073353cd33b4baa96f35b41723d49c88) |
|  | Type of the background; may be null if unknown. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [linkPreviewTypeBackground](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_background.html#a71fe4d2529b384f801e9be7a65777ec5) () |
|  | |
|  | [linkPreviewTypeBackground](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_background.html#a0c6688f8853ba1ce56f4b037168a82d9) ([object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [document](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1document.html) > &&[document\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_background.html#a5613fcca3b412b4faf119edfe151e2f1), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [BackgroundType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_background_type.html) > &&[background\_type\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_background.html#a073353cd33b4baa96f35b41723d49c88)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_background.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_background.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 977838560 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_background.html#a71fe4d2529b384f801e9be7a65777ec5)linkPreviewTypeBackground() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [linkPreviewTypeBackground](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_background.html) | ( |  | ) |  |

The link is a link to a background. Link preview title and description are available only for filled backgrounds.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_background.html#a0c6688f8853ba1ce56f4b037168a82d9)linkPreviewTypeBackground() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [linkPreviewTypeBackground](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_background.html) | ( | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [document](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1document.html) > && | *document\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [BackgroundType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_background_type.html) > && | *background\_type\_* |
|  | ) |  |  |

The link is a link to a background. Link preview title and description are available only for filled backgrounds.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | document\_ | Document with the background; may be null for filled backgrounds. |
    | [in] | background\_type\_ | Type of the background; may be null if unknown. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_background.html#a8044dab2ba3c75066745014259c050c7)store()

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