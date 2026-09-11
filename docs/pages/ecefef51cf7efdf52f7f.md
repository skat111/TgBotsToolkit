# TDLib: businessConnectedBot Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes a bot connected to a business account.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [bot\_user\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html#a852a1eecf72791be8eb2633ff5dcaec4) |
|  | User identifier of the bot. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [businessRecipients](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_recipients.html) > | [recipients\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html#aede87aedb97da792dfeacfdb64770d91) |
|  | Private chats that will be accessible to the bot. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [businessBotRights](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_bot_rights.html) > | [rights\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html#a1cfe939b78ccc03b0f013aeed74fa258) |
|  | Rights of the bot. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [businessConnectedBot](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html#a4a2dc54a34cc0288b9d3faea5123193b) () |
|  | |
|  | [businessConnectedBot](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html#aadf65ddf67bcb7e09bc6929101c014b3) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [bot\_user\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html#a852a1eecf72791be8eb2633ff5dcaec4), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [businessRecipients](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_recipients.html) > &&[recipients\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html#aede87aedb97da792dfeacfdb64770d91), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [businessBotRights](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_bot_rights.html) > &&[rights\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html#a1cfe939b78ccc03b0f013aeed74fa258)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1815439021 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html#a4a2dc54a34cc0288b9d3faea5123193b)businessConnectedBot() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [businessConnectedBot](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html) | ( |  | ) |  |

Describes a bot connected to a business account.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html#aadf65ddf67bcb7e09bc6929101c014b3)businessConnectedBot() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [businessConnectedBot](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *bot\_user\_id\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [businessRecipients](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_recipients.html) > && | *recipients\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [businessBotRights](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_bot_rights.html) > && | *rights\_* |
|  | ) |  |  |

Describes a bot connected to a business account.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | bot\_user\_id\_ | User identifier of the bot. |
    | [in] | recipients\_ | Private chats that will be accessible to the bot. |
    | [in] | rights\_ | Rights of the bot. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_connected_bot.html#a8044dab2ba3c75066745014259c050c7)store()

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