# TDLib: passkey Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes a passkey.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#a8315e6b3eb0f25e33fd70bfed8a6ee2a) |
|  | Unique identifier of the passkey. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [name_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#a79cfd788b219a7f48068d0e96e5e8e77) |
|  | Name of the passkey. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [addition_date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#a77a5d6e4c82a86f09fecc6cb0a30b8a6) |
|  | Point in time (Unix timestamp) when the passkey was added. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [last_usage_date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#a1280b3943be03e6a3186207df7228bac) |
|  | Point in time (Unix timestamp) when the passkey was used last time; 0 if never. |
|  | |
| [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | [software_icon_custom_emoji_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#ac28ad5c5eee962b4928fe0d15d379d7f) |
|  | Identifier of the custom emoji that is used as the icon of the software, which created the passkey; 0 if unknown. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [passkey](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#ae4b256f2b7d93dd302304b426b3446b1) () |
|  | |
|  | [passkey](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#a076a5731db94b44e99d877cd22e046dc) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#a8315e6b3eb0f25e33fd70bfed8a6ee2a), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[name_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#a79cfd788b219a7f48068d0e96e5e8e77), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [addition_date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#a77a5d6e4c82a86f09fecc6cb0a30b8a6), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [last_usage_date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#a1280b3943be03e6a3186207df7228bac), [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) [software_icon_custom_emoji_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#ac28ad5c5eee962b4928fe0d15d379d7f)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1200601505 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#ae4b256f2b7d93dd302304b426b3446b1)passkey() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [passkey](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html) | ( |  | ) |  |

Describes a passkey.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#a076a5731db94b44e99d877cd22e046dc)passkey() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [passkey](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *id_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *name_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *addition_date_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *last_usage_date_*, |
|  |  | [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | *software_icon_custom_emoji_id_* |
|  | ) |  |  |

Describes a passkey.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | id_ | Unique identifier of the passkey. |
    | [in] | name_ | Name of the passkey. |
    | [in] | addition_date_ | Point in time (Unix timestamp) when the passkey was added. |
    | [in] | last_usage_date_ | Point in time (Unix timestamp) when the passkey was used last time; 0 if never. |
    | [in] | software_icon_custom_emoji_id_ | Identifier of the custom emoji that is used as the icon of the software, which created the passkey; 0 if unknown. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passkey.html#a8044dab2ba3c75066745014259c050c7)store()

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