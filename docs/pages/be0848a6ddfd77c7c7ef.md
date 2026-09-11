# TDLib: updateActiveNotifications Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_notifications.html

Inherits [Update](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_update.html).

## Description

Contains active notifications that were shown on previous application launches. This update is sent only if the message database is used. In that case it comes once before any [updateNotification](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_notification.html) and [updateNotificationGroup](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_notification_group.html) update.

|  |  |
| --- | --- |
| Public Fields | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [notificationGroup](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_group.html) > > | [groups\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_notifications.html#a2ac711ec82a9be522a315a33c8a55a63) |
|  | Lists of active notification groups. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [updateActiveNotifications](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_notifications.html#a014f15c9a34fa0dd50209451948ac1a5) () |
|  | |
|  | [updateActiveNotifications](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_notifications.html#a7e25fe51f0a6d3bebcbe5901390e74f1) ([array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [notificationGroup](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_group.html) >> &&[groups\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_notifications.html#a2ac711ec82a9be522a315a33c8a55a63)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_notifications.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_notifications.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1306672221 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_notifications.html#a014f15c9a34fa0dd50209451948ac1a5)updateActiveNotifications() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [updateActiveNotifications](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_notifications.html) | ( |  | ) |  |

Contains active notifications that were shown on previous application launches. This update is sent only if the message database is used. In that case it comes once before any [updateNotification](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_notification.html) and [updateNotificationGroup](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_notification_group.html) update.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_notifications.html#a7e25fe51f0a6d3bebcbe5901390e74f1)updateActiveNotifications() [2/2]

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [updateActiveNotifications](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_notifications.html) | ( | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [notificationGroup](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_group.html) >> && | *groups\_* | ) |  | | explicit |

Contains active notifications that were shown on previous application launches. This update is sent only if the message database is used. In that case it comes once before any [updateNotification](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_notification.html) and [updateNotificationGroup](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_notification_group.html) update.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | groups\_ | Lists of active notification groups. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_active_notifications.html#a8044dab2ba3c75066745014259c050c7)store()

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