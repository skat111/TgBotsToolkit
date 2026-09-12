# TDLib: storyInteractionInfo Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Contains information about interactions with a story.

|  |  |
| --- | --- |
| Public Fields | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [view_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#aedcc00180639068fa0b6d546933146a2) |
|  | Number of times the story was viewed. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [forward_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#a6394f7af320b5ff1246d495b4cefda07) |
|  | Number of times the story was forwarded; 0 if none or unknown. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [reaction_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#a98f60299b8f692d562bd2509550e21e7) |
|  | Number of reactions added to the story; 0 if none or unknown. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) > | [recent_viewer_user_ids_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#a6b4ea4a6e2427fe7baaec939a19029b8) |
|  | Identifiers of at most 3 recent viewers of the story. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [storyInteractionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#a8d104703e88d78822dc967b586f275bc) () |
|  | |
|  | [storyInteractionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#a28ce2c931c618258ba4e4a45c905c726) ([int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [view_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#aedcc00180639068fa0b6d546933146a2), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [forward_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#a6394f7af320b5ff1246d495b4cefda07), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [reaction_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#a98f60299b8f692d562bd2509550e21e7), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) > &&[recent_viewer_user_ids_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#a6b4ea4a6e2427fe7baaec939a19029b8)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -846542065 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#a8d104703e88d78822dc967b586f275bc)storyInteractionInfo() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [storyInteractionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html) | ( |  | ) |  |

Contains information about interactions with a story.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#a28ce2c931c618258ba4e4a45c905c726)storyInteractionInfo() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [storyInteractionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html) | ( | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *view_count_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *forward_count_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *reaction_count_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) > && | *recent_viewer_user_ids_* |
|  | ) |  |  |

Contains information about interactions with a story.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | view_count_ | Number of times the story was viewed. |
    | [in] | forward_count_ | Number of times the story was forwarded; 0 if none or unknown. |
    | [in] | reaction_count_ | Number of reactions added to the story; 0 if none or unknown. |
    | [in] | recent_viewer_user_ids_ | Identifiers of at most 3 recent viewers of the story. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_interaction_info.html#a8044dab2ba3c75066745014259c050c7)store()

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