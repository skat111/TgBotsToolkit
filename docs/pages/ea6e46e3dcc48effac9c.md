# TDLib: updateNewBusinessMessage Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_business_message.html

Inherits [Update](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_update.html).

## Description

A new message was added to a business account; for bots only.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [connection_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_business_message.html#a1366654baaa112306af93c5660a3a42c) |
|  | Unique identifier of the business connection. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [businessMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_message.html) > | [message_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_business_message.html#a7cff1e738e07be5cddc4df5c48ebe8b4) |
|  | The new message. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [updateNewBusinessMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_business_message.html#a7b0d851e49b8dbe08b25dfeae5473a86) () |
|  | |
|  | [updateNewBusinessMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_business_message.html#a7d39004d649780de89f5d4350c8da5d1) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[connection_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_business_message.html#a1366654baaa112306af93c5660a3a42c), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [businessMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_message.html) > &&[message_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_business_message.html#a7cff1e738e07be5cddc4df5c48ebe8b4)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_business_message.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_business_message.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -2034350524 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_business_message.html#a7b0d851e49b8dbe08b25dfeae5473a86)updateNewBusinessMessage() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [updateNewBusinessMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_business_message.html) | ( |  | ) |  |

A new message was added to a business account; for bots only.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_business_message.html#a7d39004d649780de89f5d4350c8da5d1)updateNewBusinessMessage() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [updateNewBusinessMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_business_message.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *connection_id_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [businessMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_message.html) > && | *message_* |
|  | ) |  |  |

A new message was added to a business account; for bots only.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | connection_id_ | Unique identifier of the business connection. |
    | [in] | message_ | The new message. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_business_message.html#a8044dab2ba3c75066745014259c050c7)store()

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