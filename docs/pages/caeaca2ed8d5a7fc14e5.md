# TDLib: storyInteraction Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Represents interaction with a story.

|  |  |
| --- | --- |
| Public Fields | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > | [actor_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#a522bf2b4dace5631a59b962b8e840618) |
|  | Identifier of the user or chat that made the interaction. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [interaction_date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#aeab862aa2d8e6dacc52dc103dbc2cbcb) |
|  | Approximate point in time (Unix timestamp) when the interaction happened. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [BlockList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_block_list.html) > | [block_list_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#a6c204c912ab0ecb43b85ea2e033b89cf) |
|  | Block list to which the actor is added; may be null if none or for chat stories. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StoryInteractionType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_story_interaction_type.html) > | [type_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#aedf9e4b5f647f505038d084a50fc2c8a) |
|  | Type of the interaction. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [storyInteraction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#aa4769cba7ec84b230b0b1aa494e1a031) () |
|  | |
|  | [storyInteraction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#a72648d64518730b0d8f5767389428f7c) ([object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > &&[actor_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#a522bf2b4dace5631a59b962b8e840618), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [interaction_date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#aeab862aa2d8e6dacc52dc103dbc2cbcb), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [BlockList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_block_list.html) > &&[block_list_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#a6c204c912ab0ecb43b85ea2e033b89cf), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StoryInteractionType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_story_interaction_type.html) > &&[type_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#aedf9e4b5f647f505038d084a50fc2c8a)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -702229982 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#aa4769cba7ec84b230b0b1aa494e1a031)storyInteraction() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [storyInteraction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html) | ( |  | ) |  |

Represents interaction with a story.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#a72648d64518730b0d8f5767389428f7c)storyInteraction() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [storyInteraction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html) | ( | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > && | *actor_id_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *interaction_date_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [BlockList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_block_list.html) > && | *block_list_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StoryInteractionType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_story_interaction_type.html) > && | *type_* |
|  | ) |  |  |

Represents interaction with a story.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | actor_id_ | Identifier of the user or chat that made the interaction. |
    | [in] | interaction_date_ | Approximate point in time (Unix timestamp) when the interaction happened. |
    | [in] | block_list_ | Block list to which the actor is added; may be null if none or for chat stories. |
    | [in] | type_ | Type of the interaction. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction.html#a8044dab2ba3c75066745014259c050c7)store()

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