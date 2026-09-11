# TDLib: notificationSound Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes a notification sound in MP3 format.

|  |  |
| --- | --- |
| Public Fields | |
| [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | [id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#aaa5141a413185b6008cfbb04a6f9a21d) |
|  | Unique identifier of the notification sound. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [duration\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#a3567eba0049c4d85b34b7183207ca1bf) |
|  | Duration of the sound, in seconds. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [date\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#a003445033faa1e11b1d5e315b59d5e65) |
|  | Point in time (Unix timestamp) when the sound was created. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [title\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#ae49b8c94dab3e85761dd65876260deb9) |
|  | Title of the notification sound. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [data\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#a2f77f4c7fa52e6471dc4c4a59131f625) |
|  | Arbitrary data, defined while the sound was uploaded. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [file](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1file.html) > | [sound\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#ab0863436bcc591b1ea6285ecfe0e0c64) |
|  | File containing the sound. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [notificationSound](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#acbfb54fff30fa1a620b0889f387c3d9b) () |
|  | |
|  | [notificationSound](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#afed590675fb7242ff157225567502c38) ([int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) [id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#aaa5141a413185b6008cfbb04a6f9a21d), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [duration\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#a3567eba0049c4d85b34b7183207ca1bf), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [date\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#a003445033faa1e11b1d5e315b59d5e65), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[title\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#ae49b8c94dab3e85761dd65876260deb9), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[data\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#a2f77f4c7fa52e6471dc4c4a59131f625), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [file](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1file.html) > &&[sound\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#ab0863436bcc591b1ea6285ecfe0e0c64)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -185638601 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#acbfb54fff30fa1a620b0889f387c3d9b)notificationSound() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [notificationSound](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html) | ( |  | ) |  |

Describes a notification sound in MP3 format.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#afed590675fb7242ff157225567502c38)notificationSound() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [notificationSound](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html) | ( | [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | *id\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *duration\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *date\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *title\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *data\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [file](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1file.html) > && | *sound\_* |
|  | ) |  |  |

Describes a notification sound in MP3 format.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | id\_ | Unique identifier of the notification sound. |
    | [in] | duration\_ | Duration of the sound, in seconds. |
    | [in] | date\_ | Point in time (Unix timestamp) when the sound was created. |
    | [in] | title\_ | Title of the notification sound. |
    | [in] | data\_ | Arbitrary data, defined while the sound was uploaded. |
    | [in] | sound\_ | File containing the sound. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1notification_sound.html#a8044dab2ba3c75066745014259c050c7)store()

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