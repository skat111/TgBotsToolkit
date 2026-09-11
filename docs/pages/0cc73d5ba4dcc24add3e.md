# TDLib: setChatProfileAccentColor Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Changes accent color and background custom emoji for profile of a supergroup or channel chat. Requires can\_change\_info administrator right.

Returns object\_ptr<Ok>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Chat identifier. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [profile\_accent\_color\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html#ab7ee910d75b05e9ef2b095b8565a7270) |
|  | Identifier of the accent color to use for profile; pass -1 if none. The chat must have at least profileAccentColor.min\_supergroup\_chat\_boost\_level for supergroups or profileAccentColor.min\_channel\_chat\_boost\_level for channels boost level to pass the corresponding color. |
|  | |
| [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | [profile\_background\_custom\_emoji\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html#aadc51056e1e24e119689091632776caa) |
|  | Identifier of a custom emoji to be shown on the chat's profile photo background; 0 if none. Use chatBoostLevelFeatures.can\_set\_profile\_background\_custom\_emoji to check whether a custom emoji can be set. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html#ab684327f0ee9cbf9afb740503d89f019) = [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ok](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1ok.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [setChatProfileAccentColor](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html#a07b8d524ec928c29f2f5372aafc59457) () |
|  | |
|  | [setChatProfileAccentColor](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html#a190fc8423baa2de2a1bbc9626826b755) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html#aa8a7803161092ff97e60d58707199e1f), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [profile\_accent\_color\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html#ab7ee910d75b05e9ef2b095b8565a7270), [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) [profile\_background\_custom\_emoji\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html#aadc51056e1e24e119689091632776caa)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1109896826 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html#a07b8d524ec928c29f2f5372aafc59457)setChatProfileAccentColor() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [setChatProfileAccentColor](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html) | ( |  | ) |  |

Default constructor for a function, which changes accent color and background custom emoji for profile of a supergroup or channel chat. Requires can\_change\_info administrator right.

Returns object\_ptr<Ok>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html#a190fc8423baa2de2a1bbc9626826b755)setChatProfileAccentColor() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [setChatProfileAccentColor](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat\_id\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *profile\_accent\_color\_id\_*, |
|  |  | [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | *profile\_background\_custom\_emoji\_id\_* |
|  | ) |  |  |

Creates a function, which changes accent color and background custom emoji for profile of a supergroup or channel chat. Requires can\_change\_info administrator right.

Returns object\_ptr<Ok>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat\_id\_ | Chat identifier. |
    | [in] | profile\_accent\_color\_id\_ | Identifier of the accent color to use for profile; pass -1 if none. The chat must have at least profileAccentColor.min\_supergroup\_chat\_boost\_level for supergroups or profileAccentColor.min\_channel\_chat\_boost\_level for channels boost level to pass the corresponding color. |
    | [in] | profile\_background\_custom\_emoji\_id\_ | Identifier of a custom emoji to be shown on the chat's profile photo background; 0 if none. Use chatBoostLevelFeatures.can\_set\_profile\_background\_custom\_emoji to check whether a custom emoji can be set. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_profile_accent_color.html#a8044dab2ba3c75066745014259c050c7)store()

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