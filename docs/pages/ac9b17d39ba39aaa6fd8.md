# TDLib: localizationTargetInfo Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1localization_target_info.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Contains information about the current localization target.

|  |  |
| --- | --- |
| Public Fields | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [languagePackInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1language_pack_info.html) > > | [language\_packs\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1localization_target_info.html#a0470c6c8f996b488c7cea4f65279d936) |
|  | List of available language packs for this application. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [localizationTargetInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1localization_target_info.html#a6bbaf8bb1c3b58158b8193fa8cfa62d5) () |
|  | |
|  | [localizationTargetInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1localization_target_info.html#a535fdb8afb3b4e1edb5f5c0732cb91d0) ([array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [languagePackInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1language_pack_info.html) >> &&[language\_packs\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1localization_target_info.html#a0470c6c8f996b488c7cea4f65279d936)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1localization_target_info.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1localization_target_info.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -2048670809 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1localization_target_info.html#a6bbaf8bb1c3b58158b8193fa8cfa62d5)localizationTargetInfo() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [localizationTargetInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1localization_target_info.html) | ( |  | ) |  |

Contains information about the current localization target.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1localization_target_info.html#a535fdb8afb3b4e1edb5f5c0732cb91d0)localizationTargetInfo() [2/2]

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [localizationTargetInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1localization_target_info.html) | ( | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [languagePackInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1language_pack_info.html) >> && | *language\_packs\_* | ) |  | | explicit |

Contains information about the current localization target.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | language\_packs\_ | List of available language packs for this application. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1localization_target_info.html#a8044dab2ba3c75066745014259c050c7)store()

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