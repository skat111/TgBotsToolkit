# TDLib: premiumFeatures Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Contains information about features, available to Premium users.

|  |  |
| --- | --- |
| Public Fields | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [PremiumFeature](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_premium_feature.html) > > | [features\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html#a3f2ac002a7b5ae77ab6dbd7d75bd8f31) |
|  | The list of available features. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [premiumLimit](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_limit.html) > > | [limits\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html#a9693f5033376b8065672a5d15f97d289) |
|  | The list of limits, increased for Premium users. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InternalLinkType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_internal_link_type.html) > | [payment\_link\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html#a351042515e3f7d682ce3bc5bb137ed50) |
|  | An internal link to be opened to pay for Telegram Premium if store payment isn't possible; may be null if direct payment isn't available. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [premiumFeatures](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html#acfbf7e0df0d1a4ac8ea9adb58481e51b) () |
|  | |
|  | [premiumFeatures](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html#a59652268823314ac90251cb5332b5d24) ([array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [PremiumFeature](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_premium_feature.html) >> &&[features\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html#a3f2ac002a7b5ae77ab6dbd7d75bd8f31), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [premiumLimit](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_limit.html) >> &&[limits\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html#a9693f5033376b8065672a5d15f97d289), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InternalLinkType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_internal_link_type.html) > &&[payment\_link\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html#a351042515e3f7d682ce3bc5bb137ed50)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1875162172 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html#acfbf7e0df0d1a4ac8ea9adb58481e51b)premiumFeatures() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [premiumFeatures](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html) | ( |  | ) |  |

Contains information about features, available to Premium users.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html#a59652268823314ac90251cb5332b5d24)premiumFeatures() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [premiumFeatures](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html) | ( | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [PremiumFeature](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_premium_feature.html) >> && | *features\_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [premiumLimit](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_limit.html) >> && | *limits\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InternalLinkType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_internal_link_type.html) > && | *payment\_link\_* |
|  | ) |  |  |

Contains information about features, available to Premium users.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | features\_ | The list of available features. |
    | [in] | limits\_ | The list of limits, increased for Premium users. |
    | [in] | payment\_link\_ | An internal link to be opened to pay for Telegram Premium if store payment isn't possible; may be null if direct payment isn't available. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1premium_features.html#a8044dab2ba3c75066745014259c050c7)store()

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