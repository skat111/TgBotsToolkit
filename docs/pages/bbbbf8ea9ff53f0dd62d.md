# TDLib: linkPreview Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes a link preview.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [url\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a541e0f072a74af71d6978eea722fc5fe) |
|  | Original URL of the link. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [display\_url\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a51eed740b62e1a678ea9da833d6bb154) |
|  | URL to display. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [site\_name\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#aea2aa264a7d743543ed01a4d947d821d) |
|  | Short name of the site (e.g., Google Docs, App Store). |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [title\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#ae49b8c94dab3e85761dd65876260deb9) |
|  | Title of the content. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > | [description\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#aec954a3260430e8fdc17f9a82dd7e8aa) |
|  | Description of the content. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [author\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a1a43939226448d9f70ce934a25d926de) |
|  | Author of the content. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [LinkPreviewType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_link_preview_type.html) > | [type\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#ad640f99bf8655184dcbf2a383a91f004) |
|  | Type of the link preview. |
|  | |
| bool | [has\_large\_media\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a79328937c1b3d4dc983e85e39fa1e56d) |
|  | True, if size of media in the preview can be changed. |
|  | |
| bool | [show\_large\_media\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a6cc9ecc486f2dd70744a2a5354bf3f59) |
|  | True, if large media preview must be shown; otherwise, the media preview must be shown small and only the first frame must be shown for videos. |
|  | |
| bool | [show\_media\_above\_description\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a326a5001979c280740fa904bfa7e0c5c) |
|  | True, if media must be shown above link preview description; otherwise, the media must be shown below the description. |
|  | |
| bool | [skip\_confirmation\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a608b250eae67060ba62cfaf3635e5b38) |
|  | True, if there is no need to show an ordinary open URL confirmation, when opening the URL from the preview, because the URL is shown in the message text in clear. |
|  | |
| bool | [show\_above\_text\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a1f92bfaf0c1adcaec3aeb9de1f57a923) |
|  | True, if the link preview must be shown above message text; otherwise, the link preview must be shown below the message text. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [instant\_view\_version\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a0f3ded3e809c93ba5611bcd81747009a) |
|  | Version of instant view (currently, can be 1 or 2) for the web page; 0 if none. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [linkPreview](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a2fccd941d91d570c9e6353fcc418ae6a) () |
|  | |
|  | [linkPreview](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a2cb00eeb4182a1ba9c94634bf89292d8) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[url\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a541e0f072a74af71d6978eea722fc5fe), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[display\_url\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a51eed740b62e1a678ea9da833d6bb154), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[site\_name\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#aea2aa264a7d743543ed01a4d947d821d), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[title\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#ae49b8c94dab3e85761dd65876260deb9), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > &&[description\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#aec954a3260430e8fdc17f9a82dd7e8aa), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[author\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a1a43939226448d9f70ce934a25d926de), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [LinkPreviewType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_link_preview_type.html) > &&[type\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#ad640f99bf8655184dcbf2a383a91f004), bool [has\_large\_media\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a79328937c1b3d4dc983e85e39fa1e56d), bool [show\_large\_media\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a6cc9ecc486f2dd70744a2a5354bf3f59), bool [show\_media\_above\_description\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a326a5001979c280740fa904bfa7e0c5c), bool [skip\_confirmation\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a608b250eae67060ba62cfaf3635e5b38), bool [show\_above\_text\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a1f92bfaf0c1adcaec3aeb9de1f57a923), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [instant\_view\_version\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a0f3ded3e809c93ba5611bcd81747009a)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1729417714 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a2fccd941d91d570c9e6353fcc418ae6a)linkPreview() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [linkPreview](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html) | ( |  | ) |  |

Describes a link preview.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a2cb00eeb4182a1ba9c94634bf89292d8)linkPreview() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [linkPreview](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *url\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *display\_url\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *site\_name\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *title\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > && | *description\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *author\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [LinkPreviewType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_link_preview_type.html) > && | *type\_*, |
|  |  | bool | *has\_large\_media\_*, |
|  |  | bool | *show\_large\_media\_*, |
|  |  | bool | *show\_media\_above\_description\_*, |
|  |  | bool | *skip\_confirmation\_*, |
|  |  | bool | *show\_above\_text\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *instant\_view\_version\_* |
|  | ) |  |  |

Describes a link preview.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | url\_ | Original URL of the link. |
    | [in] | display\_url\_ | URL to display. |
    | [in] | site\_name\_ | Short name of the site (e.g., Google Docs, App Store). |
    | [in] | title\_ | Title of the content. |
    | [in] | description\_ | Description of the content. |
    | [in] | author\_ | Author of the content. |
    | [in] | type\_ | Type of the link preview. |
    | [in] | has\_large\_media\_ | True, if size of media in the preview can be changed. |
    | [in] | show\_large\_media\_ | True, if large media preview must be shown; otherwise, the media preview must be shown small and only the first frame must be shown for videos. |
    | [in] | show\_media\_above\_description\_ | True, if media must be shown above link preview description; otherwise, the media must be shown below the description. |
    | [in] | skip\_confirmation\_ | True, if there is no need to show an ordinary open URL confirmation, when opening the URL from the preview, because the URL is shown in the message text in clear. |
    | [in] | show\_above\_text\_ | True, if the link preview must be shown above message text; otherwise, the link preview must be shown below the message text. |
    | [in] | instant\_view\_version\_ | Version of instant view (currently, can be 1 or 2) for the web page; 0 if none. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1link_preview.html#a8044dab2ba3c75066745014259c050c7)store()

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