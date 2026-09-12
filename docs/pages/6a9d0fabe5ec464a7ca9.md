# TDLib: getChatMessageCount Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Returns approximate number of messages of the specified type in the chat or its topic.

Returns object_ptr<Count>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Identifier of the chat in which to count messages. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > | [topic_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#adf6e2906ee2f8b6a06150747aa41f7e0) |
|  | Pass topic identifier to get number of messages only in specific topic; pass null to get number of messages in all topics; message threads aren't supported. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [SearchMessagesFilter](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_search_messages_filter.html) > | [filter_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#a7afa6154c3257c83be5fdcc89c747b21) |
|  | Filter for message content; [searchMessagesFilterEmpty](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_messages_filter_empty.html) is unsupported in this function. |
|  | |
| bool | [return_local_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#a0a5c5e660fdff44430fa6811531e10ab) |
|  | Pass true to get the number of messages without sending network requests, or -1 if the number of messages is unknown locally. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#a374f4381635e14b8e131155eb397a4cc) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [count](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1count.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [getChatMessageCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#a8ffa837c161998119634755a99051f6e) () |
|  | |
|  | [getChatMessageCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#acaefe735b09ddf54ab1788be40c3abe0) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#aa8a7803161092ff97e60d58707199e1f), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > &&[topic_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#adf6e2906ee2f8b6a06150747aa41f7e0), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [SearchMessagesFilter](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_search_messages_filter.html) > &&[filter_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#a7afa6154c3257c83be5fdcc89c747b21), bool [return_local_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#a0a5c5e660fdff44430fa6811531e10ab)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1641001101 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#a8ffa837c161998119634755a99051f6e)getChatMessageCount() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [getChatMessageCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html) | ( |  | ) |  |

Default constructor for a function, which returns approximate number of messages of the specified type in the chat or its topic.

Returns object_ptr<Count>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#acaefe735b09ddf54ab1788be40c3abe0)getChatMessageCount() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [getChatMessageCount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat_id_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > && | *topic_id_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [SearchMessagesFilter](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_search_messages_filter.html) > && | *filter_*, |
|  |  | bool | *return_local_* |
|  | ) |  |  |

Creates a function, which returns approximate number of messages of the specified type in the chat or its topic.

Returns object_ptr<Count>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat_id_ | Identifier of the chat in which to count messages. |
    | [in] | topic_id_ | Pass topic identifier to get number of messages only in specific topic; pass null to get number of messages in all topics; message threads aren't supported. |
    | [in] | filter_ | Filter for message content; [searchMessagesFilterEmpty](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_messages_filter_empty.html) is unsupported in this function. |
    | [in] | return_local_ | Pass true to get the number of messages without sending network requests, or -1 if the number of messages is unknown locally. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_message_count.html#a8044dab2ba3c75066745014259c050c7)store()

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