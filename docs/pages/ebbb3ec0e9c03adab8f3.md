# TDLib: toggleSupergroupHasAutomaticTranslation Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Toggles whether messages are automatically translated in the channel chat; requires can_change_info administrator right in the channel. The chat must have at least chatBoostFeatures.min_automatic_translation_boost_level boost level to enable automatic translation.

Returns object_ptr<Ok>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [supergroup_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html#ab1d701b99064cad4561e1d3e85359ed0) |
|  | The identifier of the channel. |
|  | |
| bool | [has_automatic_translation_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html#ac80ecac5ed0a7c6609b266e6c9dcd512) |
|  | The new value of has_automatic_translation. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html#ab684327f0ee9cbf9afb740503d89f019) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ok](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1ok.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [toggleSupergroupHasAutomaticTranslation](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html#a32e2238dff589d76c1e766d66d970995) () |
|  | |
|  | [toggleSupergroupHasAutomaticTranslation](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html#ab33baf1ead0fc3abf6d4366846a0d9f6) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [supergroup_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html#ab1d701b99064cad4561e1d3e85359ed0), bool [has_automatic_translation_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html#ac80ecac5ed0a7c6609b266e6c9dcd512)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -184993048 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html#a32e2238dff589d76c1e766d66d970995)toggleSupergroupHasAutomaticTranslation() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [toggleSupergroupHasAutomaticTranslation](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html) | ( |  | ) |  |

Default constructor for a function, which toggles whether messages are automatically translated in the channel chat; requires can_change_info administrator right in the channel. The chat must have at least chatBoostFeatures.min_automatic_translation_boost_level boost level to enable automatic translation.

Returns object_ptr<Ok>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html#ab33baf1ead0fc3abf6d4366846a0d9f6)toggleSupergroupHasAutomaticTranslation() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [toggleSupergroupHasAutomaticTranslation](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *supergroup_id_*, |
|  |  | bool | *has_automatic_translation_* |
|  | ) |  |  |

Creates a function, which toggles whether messages are automatically translated in the channel chat; requires can_change_info administrator right in the channel. The chat must have at least chatBoostFeatures.min_automatic_translation_boost_level boost level to enable automatic translation.

Returns object_ptr<Ok>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | supergroup_id_ | The identifier of the channel. |
    | [in] | has_automatic_translation_ | The new value of has_automatic_translation. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_supergroup_has_automatic_translation.html#a8044dab2ba3c75066745014259c050c7)store()

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