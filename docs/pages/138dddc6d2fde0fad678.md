# TDLib: callStateDiscarded Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html

Inherits [CallState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_call_state.html).

## Description

The call has ended successfully.

|  |  |
| --- | --- |
| Public Fields | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [CallDiscardReason](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_call_discard_reason.html) > | [reason_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#a344f700d46f4462915949481d053031a) |
|  | The reason why the call has ended. |
|  | |
| bool | [need_rating_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#a83dd1ac3ac35b49ec63b3dfff7d478fe) |
|  | True, if the call rating must be sent to the server. |
|  | |
| bool | [need_debug_information_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#ad7747a073b90e46e3d4f4f0cf9d5c8aa) |
|  | True, if the call debug information must be sent to the server. |
|  | |
| bool | [need_log_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#ac2b614d1f3a5b88151554ad607c80da1) |
|  | True, if the call log must be sent to the server. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [callStateDiscarded](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#ad6a9bf50751d8bd5e7bceb437141da52) () |
|  | |
|  | [callStateDiscarded](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#a8905a273e40b41a501cceff11549c6bf) ([object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [CallDiscardReason](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_call_discard_reason.html) > &&[reason_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#a344f700d46f4462915949481d053031a), bool [need_rating_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#a83dd1ac3ac35b49ec63b3dfff7d478fe), bool [need_debug_information_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#ad7747a073b90e46e3d4f4f0cf9d5c8aa), bool [need_log_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#ac2b614d1f3a5b88151554ad607c80da1)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1394310213 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#ad6a9bf50751d8bd5e7bceb437141da52)callStateDiscarded() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [callStateDiscarded](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html) | ( |  | ) |  |

The call has ended successfully.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#a8905a273e40b41a501cceff11549c6bf)callStateDiscarded() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [callStateDiscarded](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html) | ( | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [CallDiscardReason](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_call_discard_reason.html) > && | *reason_*, |
|  |  | bool | *need_rating_*, |
|  |  | bool | *need_debug_information_*, |
|  |  | bool | *need_log_* |
|  | ) |  |  |

The call has ended successfully.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | reason_ | The reason why the call has ended. |
    | [in] | need_rating_ | True, if the call rating must be sent to the server. |
    | [in] | need_debug_information_ | True, if the call debug information must be sent to the server. |
    | [in] | need_log_ | True, if the call log must be sent to the server. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1call_state_discarded.html#a8044dab2ba3c75066745014259c050c7)store()

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