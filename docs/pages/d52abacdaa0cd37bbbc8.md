# TDLib: linkPreviewTypeAlbum Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_album.html

Inherits [LinkPreviewType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_link_preview_type.html).

## Description

The link is a link to a media album consisting of photos and videos.

|  |  |
| --- | --- |
| Public Fields | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [LinkPreviewAlbumMedia](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_link_preview_album_media.html) > > | [media_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_album.html#a9a183f6e0d94a4dc649e56803e444b16) |
|  | The list of album media. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [caption_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_album.html#a2beff4dba46ed56156c0c2b3a3665f0a) |
|  | Album caption. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [linkPreviewTypeAlbum](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_album.html#afb19de808eb210f37886520eb697e3fd) () |
|  | |
|  | [linkPreviewTypeAlbum](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_album.html#aa39a960f52888568013c32da82c49514) ([array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [LinkPreviewAlbumMedia](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_link_preview_album_media.html) >> &&[media_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_album.html#a9a183f6e0d94a4dc649e56803e444b16), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[caption_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_album.html#a2beff4dba46ed56156c0c2b3a3665f0a)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_album.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_album.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -919156671 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_album.html#afb19de808eb210f37886520eb697e3fd)linkPreviewTypeAlbum() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [linkPreviewTypeAlbum](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_album.html) | ( |  | ) |  |

The link is a link to a media album consisting of photos and videos.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_album.html#aa39a960f52888568013c32da82c49514)linkPreviewTypeAlbum() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [linkPreviewTypeAlbum](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_album.html) | ( | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [LinkPreviewAlbumMedia](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_link_preview_album_media.html) >> && | *media_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *caption_* |
|  | ) |  |  |

The link is a link to a media album consisting of photos and videos.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | media_ | The list of album media. |
    | [in] | caption_ | Album caption. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_album.html#a8044dab2ba3c75066745014259c050c7)store()

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