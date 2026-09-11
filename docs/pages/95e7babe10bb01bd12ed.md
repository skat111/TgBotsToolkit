# TDLib: updateInstalledStickerSets Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_installed_sticker_sets.html

Inherits [Update](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_update.html).

## Description

The list of installed sticker sets was updated.

|  |  |
| --- | --- |
| Public Fields | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StickerType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_sticker_type.html) > | [sticker\_type\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_installed_sticker_sets.html#a2f8e737beec0bf3fb900885c1f8273b6) |
|  | Type of the affected stickers. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) > | [sticker\_set\_ids\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_installed_sticker_sets.html#a40b5d02c7a6e184b842d7facac08106f) |
|  | The new list of installed ordinary sticker sets. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [updateInstalledStickerSets](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_installed_sticker_sets.html#aa1c02deb25822396d605e265a3ca07d1) () |
|  | |
|  | [updateInstalledStickerSets](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_installed_sticker_sets.html#ae3eabe1280b471b14b4282af7ce2c18a) ([object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StickerType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_sticker_type.html) > &&[sticker\_type\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_installed_sticker_sets.html#a2f8e737beec0bf3fb900885c1f8273b6), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) > &&[sticker\_set\_ids\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_installed_sticker_sets.html#a40b5d02c7a6e184b842d7facac08106f)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_installed_sticker_sets.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_installed_sticker_sets.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1735084182 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_installed_sticker_sets.html#aa1c02deb25822396d605e265a3ca07d1)updateInstalledStickerSets() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [updateInstalledStickerSets](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_installed_sticker_sets.html) | ( |  | ) |  |

The list of installed sticker sets was updated.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_installed_sticker_sets.html#ae3eabe1280b471b14b4282af7ce2c18a)updateInstalledStickerSets() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [updateInstalledStickerSets](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_installed_sticker_sets.html) | ( | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StickerType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_sticker_type.html) > && | *sticker\_type\_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) > && | *sticker\_set\_ids\_* |
|  | ) |  |  |

The list of installed sticker sets was updated.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | sticker\_type\_ | Type of the affected stickers. |
    | [in] | sticker\_set\_ids\_ | The new list of installed ordinary sticker sets. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_installed_sticker_sets.html#a8044dab2ba3c75066745014259c050c7)store()

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