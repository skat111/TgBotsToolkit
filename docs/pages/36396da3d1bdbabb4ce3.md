# TDLib: giftSettings Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Contains settings for gift receiving for a user.

|  |  |
| --- | --- |
| Public Fields | |
| bool | [show\_gift\_button\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html#adf63152bc30bc200657e6a2ac0e3cb07) |
|  | True, if a button for sending a gift to the user or by the user must always be shown in the input field. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [acceptedGiftTypes](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1accepted_gift_types.html) > | [accepted\_gift\_types\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html#a594340c2b82e401a468ffe366a3c363e) |
|  | Types of gifts accepted by the user; for Telegram Premium users only. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [giftSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html#a40002b7a33769c68f8ca937b1764c8ef) () |
|  | |
|  | [giftSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html#a9183853c9faeeb40fe68703869b21684) (bool [show\_gift\_button\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html#adf63152bc30bc200657e6a2ac0e3cb07), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [acceptedGiftTypes](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1accepted_gift_types.html) > &&[accepted\_gift\_types\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html#a594340c2b82e401a468ffe366a3c363e)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 45783168 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html#a40002b7a33769c68f8ca937b1764c8ef)giftSettings() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [giftSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html) | ( |  | ) |  |

Contains settings for gift receiving for a user.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html#a9183853c9faeeb40fe68703869b21684)giftSettings() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [giftSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html) | ( | bool | *show\_gift\_button\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [acceptedGiftTypes](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1accepted_gift_types.html) > && | *accepted\_gift\_types\_* |
|  | ) |  |  |

Contains settings for gift receiving for a user.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | show\_gift\_button\_ | True, if a button for sending a gift to the user or by the user must always be shown in the input field. |
    | [in] | accepted\_gift\_types\_ | Types of gifts accepted by the user; for Telegram Premium users only. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html#a8044dab2ba3c75066745014259c050c7)store()

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