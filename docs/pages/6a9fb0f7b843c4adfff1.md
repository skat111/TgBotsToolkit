# TDLib: locationAddress Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes an address of a location.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [country_code_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#a3a1f9992ac15f26c3b22c5e324cbd29f) |
|  | A two-letter ISO 3166-1 alpha-2 country code. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [state_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#a349084d40097e15041918271b8c74f8a) |
|  | State, if applicable; empty if unknown. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [city_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#a7d0cc83e4cf524e70c0d5d12a0849577) |
|  | City; empty if unknown. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [street_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#a678e1801df280ae55417818f9fd43c57) |
|  | The address; empty if unknown. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [locationAddress](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#a819afd41f1cc5a978c960b12034ddd2e) () |
|  | |
|  | [locationAddress](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#adc47178b33282819fb4118bdf6523508) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[country_code_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#a3a1f9992ac15f26c3b22c5e324cbd29f), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[state_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#a349084d40097e15041918271b8c74f8a), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[city_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#a7d0cc83e4cf524e70c0d5d12a0849577), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[street_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#a678e1801df280ae55417818f9fd43c57)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1545940190 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#a819afd41f1cc5a978c960b12034ddd2e)locationAddress() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [locationAddress](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html) | ( |  | ) |  |

Describes an address of a location.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#adc47178b33282819fb4118bdf6523508)locationAddress() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [locationAddress](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *country_code_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *state_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *city_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *street_* |
|  | ) |  |  |

Describes an address of a location.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | country_code_ | A two-letter ISO 3166-1 alpha-2 country code. |
    | [in] | state_ | State, if applicable; empty if unknown. |
    | [in] | city_ | City; empty if unknown. |
    | [in] | street_ | The address; empty if unknown. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1location_address.html#a8044dab2ba3c75066745014259c050c7)store()

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