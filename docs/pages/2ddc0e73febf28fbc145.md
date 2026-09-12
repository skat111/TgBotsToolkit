# TDLib: updateSavedMessagesTopic Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_saved_messages_topic.html

Inherits [Update](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_update.html).

## Description

Basic information about a Saved Messages topic has changed. This update is guaranteed to come before the topic identifier is returned to the application.

|  |  |
| --- | --- |
| Public Fields | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [savedMessagesTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1saved_messages_topic.html) > | [topic_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_saved_messages_topic.html#a69c4eba576bd6a769581af27779b7424) |
|  | New data about the topic. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [updateSavedMessagesTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_saved_messages_topic.html#a7f7d9dd71bb9d1a8e68c945a0a6b4352) () |
|  | |
|  | [updateSavedMessagesTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_saved_messages_topic.html#a29d558baef19954505eb3b8dedf9427c) ([object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [savedMessagesTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1saved_messages_topic.html) > &&[topic_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_saved_messages_topic.html#a69c4eba576bd6a769581af27779b7424)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_saved_messages_topic.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_saved_messages_topic.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1618855120 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_saved_messages_topic.html#a7f7d9dd71bb9d1a8e68c945a0a6b4352)updateSavedMessagesTopic() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [updateSavedMessagesTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_saved_messages_topic.html) | ( |  | ) |  |

Basic information about a Saved Messages topic has changed. This update is guaranteed to come before the topic identifier is returned to the application.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_saved_messages_topic.html#a29d558baef19954505eb3b8dedf9427c)updateSavedMessagesTopic() [2/2]

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [updateSavedMessagesTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_saved_messages_topic.html) | ( | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [savedMessagesTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1saved_messages_topic.html) > && | *topic_* | ) |  | | explicit |

Basic information about a Saved Messages topic has changed. This update is guaranteed to come before the topic identifier is returned to the application.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | topic_ | New data about the topic. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_saved_messages_topic.html#a8044dab2ba3c75066745014259c050c7)store()

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