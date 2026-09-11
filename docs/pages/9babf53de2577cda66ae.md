# TDLib: scopeAutosaveSettings Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Contains autosave settings for an autosave settings scope.

|  |  |
| --- | --- |
| Public Fields | |
| bool | [autosave\_photos\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html#ad9c37e666b2e41200772384eef18181b) |
|  | True, if photo autosave is enabled. |
|  | |
| bool | [autosave\_videos\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html#aef11b334b3bb9ec8ab6757a39a6cbc80) |
|  | True, if video autosave is enabled. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [max\_video\_file\_size\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html#aa1774ab02fcc66260cbbb1f3899f8f76) |
|  | The maximum size of a video file to be autosaved, in bytes; 512 KB - 4000 MB. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [scopeAutosaveSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html#a84296bb14bbce1f4bef6b71afa9d8ed8) () |
|  | |
|  | [scopeAutosaveSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html#a8df680969a37870ea86dc9c7189a45ca) (bool [autosave\_photos\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html#ad9c37e666b2e41200772384eef18181b), bool [autosave\_videos\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html#aef11b334b3bb9ec8ab6757a39a6cbc80), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [max\_video\_file\_size\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html#aa1774ab02fcc66260cbbb1f3899f8f76)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1546821427 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html#a84296bb14bbce1f4bef6b71afa9d8ed8)scopeAutosaveSettings() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [scopeAutosaveSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html) | ( |  | ) |  |

Contains autosave settings for an autosave settings scope.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html#a8df680969a37870ea86dc9c7189a45ca)scopeAutosaveSettings() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [scopeAutosaveSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html) | ( | bool | *autosave\_photos\_*, |
|  |  | bool | *autosave\_videos\_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *max\_video\_file\_size\_* |
|  | ) |  |  |

Contains autosave settings for an autosave settings scope.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | autosave\_photos\_ | True, if photo autosave is enabled. |
    | [in] | autosave\_videos\_ | True, if video autosave is enabled. |
    | [in] | max\_video\_file\_size\_ | The maximum size of a video file to be autosaved, in bytes; 512 KB - 4000 MB. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1scope_autosave_settings.html#a8044dab2ba3c75066745014259c050c7)store()

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