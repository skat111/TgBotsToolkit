# TDLib: setMessageReactions Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Sets reactions on a message; for bots only.

Returns object_ptr<Ok>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Identifier of the chat to which the message belongs. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [message_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#a946f46ee90c465619214e056e4d91ce4) |
|  | Identifier of the message. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReactionType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reaction_type.html) > > | [reaction_types_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#a65bd03104a94f7bc105002c077ae3f00) |
|  | Types of the reaction to set; pass an empty list to remove the reactions. |
|  | |
| bool | [is_big_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#a1d565201919a09a1cba9e76e4a8b8323) |
|  | Pass true if the reactions are added with a big animation. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#ab684327f0ee9cbf9afb740503d89f019) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ok](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1ok.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [setMessageReactions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#a94bd7c7cde367e67049c29d7f7923476) () |
|  | |
|  | [setMessageReactions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#aa3d1ffdab9d5ffdaaa0919eb49c3b4d5) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#aa8a7803161092ff97e60d58707199e1f), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [message_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#a946f46ee90c465619214e056e4d91ce4), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReactionType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reaction_type.html) >> &&[reaction_types_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#a65bd03104a94f7bc105002c077ae3f00), bool [is_big_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#a1d565201919a09a1cba9e76e4a8b8323)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -372524900 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#a94bd7c7cde367e67049c29d7f7923476)setMessageReactions() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [setMessageReactions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html) | ( |  | ) |  |

Default constructor for a function, which sets reactions on a message; for bots only.

Returns object_ptr<Ok>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#aa3d1ffdab9d5ffdaaa0919eb49c3b4d5)setMessageReactions() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [setMessageReactions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat_id_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *message_id_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReactionType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reaction_type.html) >> && | *reaction_types_*, |
|  |  | bool | *is_big_* |
|  | ) |  |  |

Creates a function, which sets reactions on a message; for bots only.

Returns object_ptr<Ok>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat_id_ | Identifier of the chat to which the message belongs. |
    | [in] | message_id_ | Identifier of the message. |
    | [in] | reaction_types_ | Types of the reaction to set; pass an empty list to remove the reactions. |
    | [in] | is_big_ | Pass true if the reactions are added with a big animation. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_message_reactions.html#a8044dab2ba3c75066745014259c050c7)store()

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