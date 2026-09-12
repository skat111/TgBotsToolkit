# TDLib: starTransactionTypePaidGroupCallReactionReceive Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html

Inherits [StarTransactionType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_star_transaction_type.html).

## Description

The transaction is a receiving of a paid group call reaction; relevant for regular users and channel chats only.

|  |  |
| --- | --- |
| Public Fields | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > | [sender_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html#aa4efedb303e2a085519405e8a018e184) |
|  | Identifier of the sender of the reaction. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [commission_per_mille_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html#ae4a1d59b6deb73dbcd1b09212c9c61dc) |
|  | The number of Telegram Stars received by the Telegram for each 1000 Telegram Stars paid for reaction sending. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > | [commission_star_amount_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html#aaedc798981a0a9faa237905d25a50c64) |
|  | The Telegram Star amount that was received by Telegram; can be negative for refunds. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [starTransactionTypePaidGroupCallReactionReceive](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html#ab1afd486da40611c493c1f765b9c35fb) () |
|  | |
|  | [starTransactionTypePaidGroupCallReactionReceive](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html#a9bc9c85edd9e9620fe3c9f63834908a6) ([object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > &&[sender_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html#aa4efedb303e2a085519405e8a018e184), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [commission_per_mille_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html#ae4a1d59b6deb73dbcd1b09212c9c61dc), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > &&[commission_star_amount_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html#aaedc798981a0a9faa237905d25a50c64)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1410001679 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html#ab1afd486da40611c493c1f765b9c35fb)starTransactionTypePaidGroupCallReactionReceive() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [starTransactionTypePaidGroupCallReactionReceive](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html) | ( |  | ) |  |

The transaction is a receiving of a paid group call reaction; relevant for regular users and channel chats only.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html#a9bc9c85edd9e9620fe3c9f63834908a6)starTransactionTypePaidGroupCallReactionReceive() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [starTransactionTypePaidGroupCallReactionReceive](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html) | ( | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > && | *sender_id_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *commission_per_mille_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [starAmount](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_amount.html) > && | *commission_star_amount_* |
|  | ) |  |  |

The transaction is a receiving of a paid group call reaction; relevant for regular users and channel chats only.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | sender_id_ | Identifier of the sender of the reaction. |
    | [in] | commission_per_mille_ | The number of Telegram Stars received by the Telegram for each 1000 Telegram Stars paid for reaction sending. |
    | [in] | commission_star_amount_ | The Telegram Star amount that was received by Telegram; can be negative for refunds. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1star_transaction_type_paid_group_call_reaction_receive.html#a8044dab2ba3c75066745014259c050c7)store()

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