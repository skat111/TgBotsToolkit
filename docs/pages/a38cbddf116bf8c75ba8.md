# TDLib: premiumSourceLink Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_source_link.html

Inherits [PremiumSource](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_premium_source.html).

## Description

A user opened an internal link of the type [internalLinkTypePremiumFeaturesPage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_premium_features_page.html).

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [referrer_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_source_link.html#ad43593ca1828b4e3cec333cd11c2cb94) |
|  | The referrer from the link. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [premiumSourceLink](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_source_link.html#a453cdf5495e61e6e5b06c2b362f02471) () |
|  | |
|  | [premiumSourceLink](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_source_link.html#a69d08cbcb03722f86eff1bbeb4b88151) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[referrer_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_source_link.html#ad43593ca1828b4e3cec333cd11c2cb94)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_source_link.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_source_link.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 2135071132 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_source_link.html#a453cdf5495e61e6e5b06c2b362f02471)premiumSourceLink() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [premiumSourceLink](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_source_link.html) | ( |  | ) |  |

A user opened an internal link of the type [internalLinkTypePremiumFeaturesPage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_premium_features_page.html).

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_source_link.html#a69d08cbcb03722f86eff1bbeb4b88151)premiumSourceLink() [2/2]

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [premiumSourceLink](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_source_link.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *referrer_* | ) |  | | explicit |

A user opened an internal link of the type [internalLinkTypePremiumFeaturesPage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_premium_features_page.html).

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | referrer_ | The referrer from the link. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_source_link.html#a8044dab2ba3c75066745014259c050c7)store()

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