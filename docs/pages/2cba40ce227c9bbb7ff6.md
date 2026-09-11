# TDLib: toggleGroupCallParticipantIsMuted Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Toggles whether a participant of an active group call is muted, unmuted, or allowed to unmute themselves; not supported for live stories.

Returns object\_ptr<Ok>.

|  |  |
| --- | --- |
| Public Fields | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [group\_call\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html#a0ff6dc8f9e94bab61a479c2496722683) |
|  | Group call identifier. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > | [participant\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html#a08f30ba8d2b3b95263bdc7bcd4e2a5f5) |
|  | Participant identifier. |
|  | |
| bool | [is\_muted\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html#a8f5bcb8dea5faf527818800835485af4) |
|  | Pass true to mute the user; pass false to unmute them. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html#ab684327f0ee9cbf9afb740503d89f019) = [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ok](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1ok.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [toggleGroupCallParticipantIsMuted](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html#a7b96fc68184222348010388fb904b2d6) () |
|  | |
|  | [toggleGroupCallParticipantIsMuted](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html#a31b993787dbd79241ef05ae6f539ded2) ([int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [group\_call\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html#a0ff6dc8f9e94bab61a479c2496722683), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > &&[participant\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html#a08f30ba8d2b3b95263bdc7bcd4e2a5f5), bool [is\_muted\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html#a8f5bcb8dea5faf527818800835485af4)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1308093433 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html#a7b96fc68184222348010388fb904b2d6)toggleGroupCallParticipantIsMuted() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [toggleGroupCallParticipantIsMuted](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html) | ( |  | ) |  |

Default constructor for a function, which toggles whether a participant of an active group call is muted, unmuted, or allowed to unmute themselves; not supported for live stories.

Returns object\_ptr<Ok>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html#a31b993787dbd79241ef05ae6f539ded2)toggleGroupCallParticipantIsMuted() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [toggleGroupCallParticipantIsMuted](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html) | ( | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *group\_call\_id\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > && | *participant\_id\_*, |
|  |  | bool | *is\_muted\_* |
|  | ) |  |  |

Creates a function, which toggles whether a participant of an active group call is muted, unmuted, or allowed to unmute themselves; not supported for live stories.

Returns object\_ptr<Ok>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | group\_call\_id\_ | Group call identifier. |
    | [in] | participant\_id\_ | Participant identifier. |
    | [in] | is\_muted\_ | Pass true to mute the user; pass false to unmute them. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1toggle_group_call_participant_is_muted.html#a8044dab2ba3c75066745014259c050c7)store()

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