# TDLib: callServerTypeWebrtc Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html

Inherits [CallServerType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_call_server_type.html).

## Description

A WebRTC server.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [username\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#a1ee37eaede4098b7d83340cc202963d5) |
|  | Username to be used for authentication. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [password\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#afbc1b6b06e669783ad50b5cfdfbf3e7e) |
|  | Authentication password. |
|  | |
| bool | [supports\_turn\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#ad3f432918ed7097d8fccd9fefcd8d71b) |
|  | True, if the server supports TURN. |
|  | |
| bool | [supports\_stun\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#a5446b9567a0ec4ecdb3df3c61ecb25f9) |
|  | True, if the server supports STUN. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [callServerTypeWebrtc](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#af3c866f1566f773bd2e0d25892511783) () |
|  | |
|  | [callServerTypeWebrtc](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#a8f5921ca27d9a9fdb959fa1037a5daf7) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[username\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#a1ee37eaede4098b7d83340cc202963d5), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[password\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#afbc1b6b06e669783ad50b5cfdfbf3e7e), bool [supports\_turn\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#ad3f432918ed7097d8fccd9fefcd8d71b), bool [supports\_stun\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#a5446b9567a0ec4ecdb3df3c61ecb25f9)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1250622821 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#af3c866f1566f773bd2e0d25892511783)callServerTypeWebrtc() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [callServerTypeWebrtc](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html) | ( |  | ) |  |

A WebRTC server.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#a8f5921ca27d9a9fdb959fa1037a5daf7)callServerTypeWebrtc() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [callServerTypeWebrtc](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *username\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *password\_*, |
|  |  | bool | *supports\_turn\_*, |
|  |  | bool | *supports\_stun\_* |
|  | ) |  |  |

A WebRTC server.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | username\_ | Username to be used for authentication. |
    | [in] | password\_ | Authentication password. |
    | [in] | supports\_turn\_ | True, if the server supports TURN. |
    | [in] | supports\_stun\_ | True, if the server supports STUN. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_server_type_webrtc.html#a8044dab2ba3c75066745014259c050c7)store()

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