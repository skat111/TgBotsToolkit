# TDLib: discardCall Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Discards a call.

Returns object_ptr<Ok>.

|  |  |
| --- | --- |
| Public Fields | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [call_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a62281cdea7e3d150c18423cfc887e839) |
|  | Call identifier. |
|  | |
| bool | [is_disconnected_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a0c18c10f752d2e3c7120a7d6c3049c46) |
|  | Pass true if the user was disconnected. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [invite_link_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a8837b4bdc197c673d1ea9b7b36ac105b) |
|  | If the call was upgraded to a group call, pass invite link to the group call. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [duration_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a3567eba0049c4d85b34b7183207ca1bf) |
|  | The call duration, in seconds. |
|  | |
| bool | [is_video_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a51862a8ca479038d05362960902b224f) |
|  | Pass true if the call was a video call. |
|  | |
| [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | [connection_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a219614b13eee370cdb1ee569880ff0c2) |
|  | Identifier of the connection used during the call. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#ab684327f0ee9cbf9afb740503d89f019) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ok](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1ok.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [discardCall](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#af617fcc9950ed2b05f3c29be43db3b03) () |
|  | |
|  | [discardCall](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a05465dbd8a629910926fec4e4c70111d) ([int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [call_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a62281cdea7e3d150c18423cfc887e839), bool [is_disconnected_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a0c18c10f752d2e3c7120a7d6c3049c46), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[invite_link_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a8837b4bdc197c673d1ea9b7b36ac105b), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [duration_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a3567eba0049c4d85b34b7183207ca1bf), bool [is_video_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a51862a8ca479038d05362960902b224f), [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) [connection_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a219614b13eee370cdb1ee569880ff0c2)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1545983346 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#af617fcc9950ed2b05f3c29be43db3b03)discardCall() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [discardCall](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html) | ( |  | ) |  |

Default constructor for a function, which discards a call.

Returns object_ptr<Ok>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a05465dbd8a629910926fec4e4c70111d)discardCall() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [discardCall](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html) | ( | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *call_id_*, |
|  |  | bool | *is_disconnected_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *invite_link_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *duration_*, |
|  |  | bool | *is_video_*, |
|  |  | [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | *connection_id_* |
|  | ) |  |  |

Creates a function, which discards a call.

Returns object_ptr<Ok>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | call_id_ | Call identifier. |
    | [in] | is_disconnected_ | Pass true if the user was disconnected. |
    | [in] | invite_link_ | If the call was upgraded to a group call, pass invite link to the group call. |
    | [in] | duration_ | The call duration, in seconds. |
    | [in] | is_video_ | Pass true if the call was a video call. |
    | [in] | connection_id_ | Identifier of the connection used during the call. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1discard_call.html#a8044dab2ba3c75066745014259c050c7)store()

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