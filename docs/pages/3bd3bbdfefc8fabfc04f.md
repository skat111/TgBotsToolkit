# TDLib: updateActiveLiveLocationMessages Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_live_location_messages.html

Inherits [Update](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_update.html).

## Description

The list of messages with active live location that need to be updated by the application has changed. The list is persistent across application restarts only if the message database is used.

|  |  |
| --- | --- |
| Public Fields | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [message](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html) > > | [messages_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_live_location_messages.html#aba32b0e1752646140e43e7e5f7931466) |
|  | The list of messages with active live locations. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [updateActiveLiveLocationMessages](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_live_location_messages.html#a1f02340f7549d88b2bfe6172a8b0e0be) () |
|  | |
|  | [updateActiveLiveLocationMessages](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_live_location_messages.html#a64f709045c1318e8deafca6eb3512216) ([array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [message](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html) >> &&[messages_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_live_location_messages.html#aba32b0e1752646140e43e7e5f7931466)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_live_location_messages.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_live_location_messages.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1308142440 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_live_location_messages.html#a1f02340f7549d88b2bfe6172a8b0e0be)updateActiveLiveLocationMessages() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [updateActiveLiveLocationMessages](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_live_location_messages.html) | ( |  | ) |  |

The list of messages with active live location that need to be updated by the application has changed. The list is persistent across application restarts only if the message database is used.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_live_location_messages.html#a64f709045c1318e8deafca6eb3512216)updateActiveLiveLocationMessages() [2/2]

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [updateActiveLiveLocationMessages](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_live_location_messages.html) | ( | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [message](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html) >> && | *messages_* | ) |  | | explicit |

The list of messages with active live location that need to be updated by the application has changed. The list is persistent across application restarts only if the message database is used.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | messages_ | The list of messages with active live locations. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_live_location_messages.html#a8044dab2ba3c75066745014259c050c7)store()

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