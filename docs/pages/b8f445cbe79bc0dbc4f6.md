# TDLib: linkPreviewTypeExternalVideo Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html

Inherits [LinkPreviewType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_link_preview_type.html).

## Description

The link is a link to a video file.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [url\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#a541e0f072a74af71d6978eea722fc5fe) |
|  | URL of the video file. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [mime\_type\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#a09abaeda9535bad28e1a6159c0a3398a) |
|  | MIME type of the video file. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [width\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#ac36a96daaa63a9706f54c0a4fbf8fff3) |
|  | Expected width of the video preview; 0 if unknown. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [height\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#aebff872d03cf6a5c75c5156d148dbe28) |
|  | Expected height of the video preview; 0 if unknown. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [duration\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#a3567eba0049c4d85b34b7183207ca1bf) |
|  | Duration of the video, in seconds; 0 if unknown. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [linkPreviewTypeExternalVideo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#ac8c27f935eada2e205e67bd0dd44b7ae) () |
|  | |
|  | [linkPreviewTypeExternalVideo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#a25236ac1eb621bf066d206255aa97b70) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[url\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#a541e0f072a74af71d6978eea722fc5fe), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[mime\_type\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#a09abaeda9535bad28e1a6159c0a3398a), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [width\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#ac36a96daaa63a9706f54c0a4fbf8fff3), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [height\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#aebff872d03cf6a5c75c5156d148dbe28), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [duration\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#a3567eba0049c4d85b34b7183207ca1bf)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1367198616 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#ac8c27f935eada2e205e67bd0dd44b7ae)linkPreviewTypeExternalVideo() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [linkPreviewTypeExternalVideo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html) | ( |  | ) |  |

The link is a link to a video file.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#a25236ac1eb621bf066d206255aa97b70)linkPreviewTypeExternalVideo() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [linkPreviewTypeExternalVideo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *url\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *mime\_type\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *width\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *height\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *duration\_* |
|  | ) |  |  |

The link is a link to a video file.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | url\_ | URL of the video file. |
    | [in] | mime\_type\_ | MIME type of the video file. |
    | [in] | width\_ | Expected width of the video preview; 0 if unknown. |
    | [in] | height\_ | Expected height of the video preview; 0 if unknown. |
    | [in] | duration\_ | Duration of the video, in seconds; 0 if unknown. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview_type_external_video.html#a8044dab2ba3c75066745014259c050c7)store()

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