# TDLib: photoSize Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes an image in JPEG format.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [type\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#a76462a38d118ce274a53920aa60094a4) |
|  | Image type (see <https://core.telegram.org/constructor/photoSize>). |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [file](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1file.html) > | [photo\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#a87bcb71f12c089acbc848b1aa258577d) |
|  | Information about the image file. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [width\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#ac36a96daaa63a9706f54c0a4fbf8fff3) |
|  | Image width. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [height\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#aebff872d03cf6a5c75c5156d148dbe28) |
|  | Image height. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > | [progressive\_sizes\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#a712f64c472cc20a2c823660746fb6aef) |
|  | Sizes of progressive JPEG file prefixes, which can be used to preliminarily show the image; in bytes. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [photoSize](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#aabec0cc049b7294bfe2d1e11d5c79061) () |
|  | |
|  | [photoSize](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#a23d0f01376bef9d877acf4b6dd19b1c6) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[type\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#a76462a38d118ce274a53920aa60094a4), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [file](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1file.html) > &&[photo\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#a87bcb71f12c089acbc848b1aa258577d), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [width\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#ac36a96daaa63a9706f54c0a4fbf8fff3), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [height\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#aebff872d03cf6a5c75c5156d148dbe28), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > &&[progressive\_sizes\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#a712f64c472cc20a2c823660746fb6aef)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1609182352 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#aabec0cc049b7294bfe2d1e11d5c79061)photoSize() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [photoSize](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html) | ( |  | ) |  |

Describes an image in JPEG format.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#a23d0f01376bef9d877acf4b6dd19b1c6)photoSize() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [photoSize](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *type\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [file](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1file.html) > && | *photo\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *width\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *height\_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > && | *progressive\_sizes\_* |
|  | ) |  |  |

Describes an image in JPEG format.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | type\_ | Image type (see <https://core.telegram.org/constructor/photoSize>). |
    | [in] | photo\_ | Information about the image file. |
    | [in] | width\_ | Image width. |
    | [in] | height\_ | Image height. |
    | [in] | progressive\_sizes\_ | Sizes of progressive JPEG file prefixes, which can be used to preliminarily show the image; in bytes. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html#a8044dab2ba3c75066745014259c050c7)store()

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