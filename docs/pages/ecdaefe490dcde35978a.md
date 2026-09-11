# TDLib: getChatMessagePosition Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Returns approximate 1-based position of a message among messages, which can be found by the specified filter in the chat and topic. Cannot be used in secret chats.

Returns object\_ptr<Count>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Identifier of the chat in which to find message position. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > | [topic\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#adf6e2906ee2f8b6a06150747aa41f7e0) |
|  | Pass topic identifier to get position among messages only in specific topic; pass null to get position among all chat messages; message threads aren't supported. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [SearchMessagesFilter](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_search_messages_filter.html) > | [filter\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#a7afa6154c3257c83be5fdcc89c747b21) |
|  | Filter for message content; [searchMessagesFilterEmpty](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_messages_filter_empty.html), [searchMessagesFilterUnreadMention](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_messages_filter_unread_mention.html), [searchMessagesFilterUnreadReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_messages_filter_unread_reaction.html), and [searchMessagesFilterFailedToSend](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_messages_filter_failed_to_send.html) are unsupported in this function. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [message\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#a946f46ee90c465619214e056e4d91ce4) |
|  | Message identifier. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#a374f4381635e14b8e131155eb397a4cc) = [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [count](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1count.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [getChatMessagePosition](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#a5707b267775e9b97831fbb267b50348a) () |
|  | |
|  | [getChatMessagePosition](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#a0cfaff76398687da4ed983ff28ee4bb6) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#aa8a7803161092ff97e60d58707199e1f), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > &&[topic\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#adf6e2906ee2f8b6a06150747aa41f7e0), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [SearchMessagesFilter](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_search_messages_filter.html) > &&[filter\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#a7afa6154c3257c83be5fdcc89c747b21), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [message\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#a946f46ee90c465619214e056e4d91ce4)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1468174577 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#a5707b267775e9b97831fbb267b50348a)getChatMessagePosition() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [getChatMessagePosition](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html) | ( |  | ) |  |

Default constructor for a function, which returns approximate 1-based position of a message among messages, which can be found by the specified filter in the chat and topic. Cannot be used in secret chats.

Returns object\_ptr<Count>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#a0cfaff76398687da4ed983ff28ee4bb6)getChatMessagePosition() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [getChatMessagePosition](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat\_id\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > && | *topic\_id\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [SearchMessagesFilter](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_search_messages_filter.html) > && | *filter\_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *message\_id\_* |
|  | ) |  |  |

Creates a function, which returns approximate 1-based position of a message among messages, which can be found by the specified filter in the chat and topic. Cannot be used in secret chats.

Returns object\_ptr<Count>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat\_id\_ | Identifier of the chat in which to find message position. |
    | [in] | topic\_id\_ | Pass topic identifier to get position among messages only in specific topic; pass null to get position among all chat messages; message threads aren't supported. |
    | [in] | filter\_ | Filter for message content; [searchMessagesFilterEmpty](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_messages_filter_empty.html), [searchMessagesFilterUnreadMention](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_messages_filter_unread_mention.html), [searchMessagesFilterUnreadReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_messages_filter_unread_reaction.html), and [searchMessagesFilterFailedToSend](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_messages_filter_failed_to_send.html) are unsupported in this function. |
    | [in] | message\_id\_ | Message identifier. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_position.html#a8044dab2ba3c75066745014259c050c7)store()

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