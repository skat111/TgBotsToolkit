# TDLib: thumbnail Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Represents a thumbnail.

|  |  |
| --- | --- |
| Public Fields | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ThumbnailFormat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_thumbnail_format.html) > | [format_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#a986a97950c15038f1903bdd2b3edb407) |
|  | Thumbnail format. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [width_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#ac36a96daaa63a9706f54c0a4fbf8fff3) |
|  | Thumbnail width. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [height_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#aebff872d03cf6a5c75c5156d148dbe28) |
|  | Thumbnail height. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [file](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1file.html) > | [file_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#a0bc31bd7127575c6691f1451a60ddba5) |
|  | The thumbnail. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [thumbnail](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#a79f6dc83f3d9087da00bad562c200c79) () |
|  | |
|  | [thumbnail](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#a6c107fdbbdea8218733e39d9b0604995) ([object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ThumbnailFormat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_thumbnail_format.html) > &&[format_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#a986a97950c15038f1903bdd2b3edb407), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [width_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#ac36a96daaa63a9706f54c0a4fbf8fff3), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [height_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#aebff872d03cf6a5c75c5156d148dbe28), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [file](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1file.html) > &&[file_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#a0bc31bd7127575c6691f1451a60ddba5)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1243275371 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#a79f6dc83f3d9087da00bad562c200c79)thumbnail() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [thumbnail](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html) | ( |  | ) |  |

Represents a thumbnail.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#a6c107fdbbdea8218733e39d9b0604995)thumbnail() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [thumbnail](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html) | ( | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ThumbnailFormat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_thumbnail_format.html) > && | *format_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *width_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *height_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [file](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1file.html) > && | *file_* |
|  | ) |  |  |

Represents a thumbnail.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | format_ | Thumbnail format. |
    | [in] | width_ | Thumbnail width. |
    | [in] | height_ | Thumbnail height. |
    | [in] | file_ | The thumbnail. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1thumbnail.html#a8044dab2ba3c75066745014259c050c7)store()

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