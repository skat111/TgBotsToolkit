# TDLib: photo Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes a photo.

|  |  |
| --- | --- |
| Public Fields | |
| bool | [has_stickers_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html#a6c887138da2637604d7f46c5d11ee877) |
|  | True, if stickers were added to the photo. The list of corresponding sticker sets can be received using [getAttachedStickerSets](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_attached_sticker_sets.html). |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [minithumbnail](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1minithumbnail.html) > | [minithumbnail_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html#ad35ff870510ffb26f83ef6c749870646) |
|  | Photo minithumbnail; may be null. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [photoSize](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html) > > | [sizes_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html#af7b5cb13981a8f90d70e3a1197d66504) |
|  | Available variants of the photo, in different sizes. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [photo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html#ab352eaa046e4c09b64354907a53eefce) () |
|  | |
|  | [photo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html#ac7c8abfda80735d3cd986826bd1ec438) (bool [has_stickers_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html#a6c887138da2637604d7f46c5d11ee877), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [minithumbnail](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1minithumbnail.html) > &&[minithumbnail_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html#ad35ff870510ffb26f83ef6c749870646), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [photoSize](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html) >> &&[sizes_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html#af7b5cb13981a8f90d70e3a1197d66504)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -2022871583 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html#ab352eaa046e4c09b64354907a53eefce)photo() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [photo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html) | ( |  | ) |  |

Describes a photo.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html#ac7c8abfda80735d3cd986826bd1ec438)photo() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [photo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html) | ( | bool | *has_stickers_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [minithumbnail](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1minithumbnail.html) > && | *minithumbnail_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [photoSize](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html) >> && | *sizes_* |
|  | ) |  |  |

Describes a photo.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | has_stickers_ | True, if stickers were added to the photo. The list of corresponding sticker sets can be received using [getAttachedStickerSets](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_attached_sticker_sets.html). |
    | [in] | minithumbnail_ | Photo minithumbnail; may be null. |
    | [in] | sizes_ | Available variants of the photo, in different sizes. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html#a8044dab2ba3c75066745014259c050c7)store()

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