# TDLib: setChatPaidMessageStarCount Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Changes the Telegram Star amount that must be paid to send a message to a supergroup chat; requires can\_restrict\_members administrator right and supergroupFullInfo.can\_enable\_paid\_messages.

Returns object\_ptr<Ok>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Identifier of the supergroup chat. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [paid\_message\_star\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html#ab000a89591b96c76c47a53b91c45755f) |
|  | The new number of Telegram Stars that must be paid for each message that is sent to the supergroup chat unless the sender is an administrator of the chat; 0-[getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("paid\_message\_star\_count\_max"). The supergroup will receive [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("paid\_message\_earnings\_per\_mille") Telegram Stars for each 1000 Telegram Stars paid for message sending. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html#ab684327f0ee9cbf9afb740503d89f019) = [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ok](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1ok.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [setChatPaidMessageStarCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html#aaae2674fcfdf2457e524b29680048875) () |
|  | |
|  | [setChatPaidMessageStarCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html#ac314dcbe57fbef8c21489be2d5a31e2a) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html#aa8a7803161092ff97e60d58707199e1f), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [paid\_message\_star\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html#ab000a89591b96c76c47a53b91c45755f)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1187053289 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html#aaae2674fcfdf2457e524b29680048875)setChatPaidMessageStarCount() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [setChatPaidMessageStarCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html) | ( |  | ) |  |

Default constructor for a function, which changes the Telegram Star amount that must be paid to send a message to a supergroup chat; requires can\_restrict\_members administrator right and supergroupFullInfo.can\_enable\_paid\_messages.

Returns object\_ptr<Ok>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html#ac314dcbe57fbef8c21489be2d5a31e2a)setChatPaidMessageStarCount() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [setChatPaidMessageStarCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat\_id\_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *paid\_message\_star\_count\_* |
|  | ) |  |  |

Creates a function, which changes the Telegram Star amount that must be paid to send a message to a supergroup chat; requires can\_restrict\_members administrator right and supergroupFullInfo.can\_enable\_paid\_messages.

Returns object\_ptr<Ok>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat\_id\_ | Identifier of the supergroup chat. |
    | [in] | paid\_message\_star\_count\_ | The new number of Telegram Stars that must be paid for each message that is sent to the supergroup chat unless the sender is an administrator of the chat; 0-[getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("paid\_message\_star\_count\_max"). The supergroup will receive [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("paid\_message\_earnings\_per\_mille") Telegram Stars for each 1000 Telegram Stars paid for message sending. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_chat_paid_message_star_count.html#a8044dab2ba3c75066745014259c050c7)store()

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