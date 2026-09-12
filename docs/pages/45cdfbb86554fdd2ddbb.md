# TDLib: messageDirectMessagePriceChanged Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_direct_message_price_changed.html

Inherits [MessageContent](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_content.html).

## Description

A price for direct messages was changed in the channel chat.

|  |  |
| --- | --- |
| Public Fields | |
| bool | [is_enabled_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_direct_message_price_changed.html#a904ff88e97f6e0b311a07c916ad686d8) |
|  | True, if direct messages group was enabled for the channel; false otherwise. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [paid_message_star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_direct_message_price_changed.html#ab000a89591b96c76c47a53b91c45755f) |
|  | The new number of Telegram Stars that must be paid by non-administrator users of the channel chat for each message sent to the direct messages group; 0 if the direct messages group was disabled or the messages are free. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [messageDirectMessagePriceChanged](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_direct_message_price_changed.html#ae59038576f00acb9ebeac1a8ab077edc) () |
|  | |
|  | [messageDirectMessagePriceChanged](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_direct_message_price_changed.html#a13ab4a45a6867d0aef56504da37a86fb) (bool [is_enabled_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_direct_message_price_changed.html#a904ff88e97f6e0b311a07c916ad686d8), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [paid_message_star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_direct_message_price_changed.html#ab000a89591b96c76c47a53b91c45755f)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_direct_message_price_changed.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_direct_message_price_changed.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1320832439 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_direct_message_price_changed.html#ae59038576f00acb9ebeac1a8ab077edc)messageDirectMessagePriceChanged() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [messageDirectMessagePriceChanged](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_direct_message_price_changed.html) | ( |  | ) |  |

A price for direct messages was changed in the channel chat.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_direct_message_price_changed.html#a13ab4a45a6867d0aef56504da37a86fb)messageDirectMessagePriceChanged() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [messageDirectMessagePriceChanged](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_direct_message_price_changed.html) | ( | bool | *is_enabled_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *paid_message_star_count_* |
|  | ) |  |  |

A price for direct messages was changed in the channel chat.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | is_enabled_ | True, if direct messages group was enabled for the channel; false otherwise. |
    | [in] | paid_message_star_count_ | The new number of Telegram Stars that must be paid by non-administrator users of the channel chat for each message sent to the direct messages group; 0 if the direct messages group was disabled or the messages are free. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_direct_message_price_changed.html#a8044dab2ba3c75066745014259c050c7)store()

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