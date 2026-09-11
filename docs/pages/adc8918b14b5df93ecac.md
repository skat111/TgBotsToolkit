# TDLib: chatEventVideoChatParticipantIsMutedToggled Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_video_chat_participant_is_muted_toggled.html

Inherits [ChatEventAction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_chat_event_action.html).

## Description

A video chat participant was muted or unmuted.

|  |  |
| --- | --- |
| Public Fields | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > | [participant\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_video_chat_participant_is_muted_toggled.html#a08f30ba8d2b3b95263bdc7bcd4e2a5f5) |
|  | Identifier of the affected group call participant. |
|  | |
| bool | [is\_muted\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_video_chat_participant_is_muted_toggled.html#a8f5bcb8dea5faf527818800835485af4) |
|  | New value of is\_muted. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [chatEventVideoChatParticipantIsMutedToggled](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_video_chat_participant_is_muted_toggled.html#a8a12ccc62d676143b4415fe4f8402449) () |
|  | |
|  | [chatEventVideoChatParticipantIsMutedToggled](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_video_chat_participant_is_muted_toggled.html#a905920f91bf40dfc7d5b266053e9b35a) ([object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > &&[participant\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_video_chat_participant_is_muted_toggled.html#a08f30ba8d2b3b95263bdc7bcd4e2a5f5), bool [is\_muted\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_video_chat_participant_is_muted_toggled.html#a8f5bcb8dea5faf527818800835485af4)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_video_chat_participant_is_muted_toggled.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_video_chat_participant_is_muted_toggled.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 521165047 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_video_chat_participant_is_muted_toggled.html#a8a12ccc62d676143b4415fe4f8402449)chatEventVideoChatParticipantIsMutedToggled() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [chatEventVideoChatParticipantIsMutedToggled](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_video_chat_participant_is_muted_toggled.html) | ( |  | ) |  |

A video chat participant was muted or unmuted.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_video_chat_participant_is_muted_toggled.html#a905920f91bf40dfc7d5b266053e9b35a)chatEventVideoChatParticipantIsMutedToggled() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [chatEventVideoChatParticipantIsMutedToggled](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_video_chat_participant_is_muted_toggled.html) | ( | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > && | *participant\_id\_*, |
|  |  | bool | *is\_muted\_* |
|  | ) |  |  |

A video chat participant was muted or unmuted.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | participant\_id\_ | Identifier of the affected group call participant. |
    | [in] | is\_muted\_ | New value of is\_muted. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_event_video_chat_participant_is_muted_toggled.html#a8044dab2ba3c75066745014259c050c7)store()

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