# TDLib: messageLinkInfo Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Contains information about a link to a message or a forum topic in a chat.

|  |  |
| --- | --- |
| Public Fields | |
| bool | [is\_public\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#a44c55f49f4b97127352c51fbdba9f659) |
|  | True, if the link is a public link for a message or a forum topic in a chat. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#aa8a7803161092ff97e60d58707199e1f) |
|  | If found, identifier of the chat to which the link points, 0 otherwise. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > | [topic\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#adf6e2906ee2f8b6a06150747aa41f7e0) |
|  | Identifier of the specific topic in which the message must be opened, or a topic to open if the message is missing; may be null if none. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [message](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html) > | [message\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#af1e141be2a42d5bd3c6569b9efa22914) |
|  | If found, the linked message; may be null. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [media\_timestamp\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#ad09b083834fb6c031cdabf0fe26b5ba6) |
|  | Timestamp from which the video/audio/video note/voice note/story playing must start, in seconds; 0 if not specified. The media can be in the message content or in its link preview. |
|  | |
| bool | [for\_album\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#a4055f79bc9a31e7b52576e2284e0c01c) |
|  | True, if the whole media album to which the message belongs is linked. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [messageLinkInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#a2c52ce189c5e1df612de0bb4ae541b65) () |
|  | |
|  | [messageLinkInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#acfaf0a39032de3ef8548a842295ffdd0) (bool [is\_public\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#a44c55f49f4b97127352c51fbdba9f659), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#aa8a7803161092ff97e60d58707199e1f), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > &&[topic\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#adf6e2906ee2f8b6a06150747aa41f7e0), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [message](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html) > &&[message\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#af1e141be2a42d5bd3c6569b9efa22914), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [media\_timestamp\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#ad09b083834fb6c031cdabf0fe26b5ba6), bool [for\_album\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#a4055f79bc9a31e7b52576e2284e0c01c)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 361619055 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#a2c52ce189c5e1df612de0bb4ae541b65)messageLinkInfo() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [messageLinkInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html) | ( |  | ) |  |

Contains information about a link to a message or a forum topic in a chat.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#acfaf0a39032de3ef8548a842295ffdd0)messageLinkInfo() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [messageLinkInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html) | ( | bool | *is\_public\_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat\_id\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > && | *topic\_id\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [message](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html) > && | *message\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *media\_timestamp\_*, |
|  |  | bool | *for\_album\_* |
|  | ) |  |  |

Contains information about a link to a message or a forum topic in a chat.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | is\_public\_ | True, if the link is a public link for a message or a forum topic in a chat. |
    | [in] | chat\_id\_ | If found, identifier of the chat to which the link points, 0 otherwise. |
    | [in] | topic\_id\_ | Identifier of the specific topic in which the message must be opened, or a topic to open if the message is missing; may be null if none. |
    | [in] | message\_ | If found, the linked message; may be null. |
    | [in] | media\_timestamp\_ | Timestamp from which the video/audio/video note/voice note/story playing must start, in seconds; 0 if not specified. The media can be in the message content or in its link preview. |
    | [in] | for\_album\_ | True, if the whole media album to which the message belongs is linked. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_link_info.html#a8044dab2ba3c75066745014259c050c7)store()

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