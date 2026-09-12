# TDLib: reactionNotificationSettings Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Contains information about notification settings for reactions.

|  |  |
| --- | --- |
| Public Fields | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReactionNotificationSource](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reaction_notification_source.html) > | [message_reaction_source_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#a402a0278f7e5253a440ccbbb768fe4b1) |
|  | Source of message reactions for which notifications are shown. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReactionNotificationSource](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reaction_notification_source.html) > | [story_reaction_source_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#a0cae89a3c810348cc7cf1ee2474afbaf) |
|  | Source of story reactions for which notifications are shown. |
|  | |
| [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | [sound_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#a48669946603d31b500621abb9f8352d6) |
|  | Identifier of the notification sound to be played; 0 if sound is disabled. |
|  | |
| bool | [show_preview_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#acc097b3238ac060c34b44ec40b32497e) |
|  | True, if reaction sender and emoji must be displayed in notifications. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [reactionNotificationSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#a486985335dcb6d80bc799acf53d63390) () |
|  | |
|  | [reactionNotificationSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#a199647e32ee437c3742b4b2f4f29bf0d) ([object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReactionNotificationSource](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reaction_notification_source.html) > &&[message_reaction_source_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#a402a0278f7e5253a440ccbbb768fe4b1), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReactionNotificationSource](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reaction_notification_source.html) > &&[story_reaction_source_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#a0cae89a3c810348cc7cf1ee2474afbaf), [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) [sound_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#a48669946603d31b500621abb9f8352d6), bool [show_preview_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#acc097b3238ac060c34b44ec40b32497e)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 733017684 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#a486985335dcb6d80bc799acf53d63390)reactionNotificationSettings() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [reactionNotificationSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html) | ( |  | ) |  |

Contains information about notification settings for reactions.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#a199647e32ee437c3742b4b2f4f29bf0d)reactionNotificationSettings() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [reactionNotificationSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html) | ( | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReactionNotificationSource](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reaction_notification_source.html) > && | *message_reaction_source_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReactionNotificationSource](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reaction_notification_source.html) > && | *story_reaction_source_*, |
|  |  | [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | *sound_id_*, |
|  |  | bool | *show_preview_* |
|  | ) |  |  |

Contains information about notification settings for reactions.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | message_reaction_source_ | Source of message reactions for which notifications are shown. |
    | [in] | story_reaction_source_ | Source of story reactions for which notifications are shown. |
    | [in] | sound_id_ | Identifier of the notification sound to be played; 0 if sound is disabled. |
    | [in] | show_preview_ | True, if reaction sender and emoji must be displayed in notifications. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1reaction_notification_settings.html#a8044dab2ba3c75066745014259c050c7)store()

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