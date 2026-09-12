# TDLib: availableReactions Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Represents a list of reactions that can be added to a message.

|  |  |
| --- | --- |
| Public Fields | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [availableReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reaction.html) > > | [top_reactions_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#a108d619ff6a006bd8b4e63ed6ef08be9) |
|  | List of reactions to be shown at the top. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [availableReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reaction.html) > > | [recent_reactions_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#a42d9d6ec74632a49e868872413df7c5e) |
|  | List of recently used reactions. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [availableReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reaction.html) > > | [popular_reactions_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#ad25ed4aea432740821a51557f3fb75d8) |
|  | List of popular reactions. |
|  | |
| bool | [allow_custom_emoji_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#aa8baf441d878271a46577604035cf1ad) |
|  | True, if any custom emoji reaction can be added by Telegram Premium subscribers. |
|  | |
| bool | [are_tags_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#af6c632b322beadfaa0c2798b120a330e) |
|  | True, if the reactions will be tags and the message can be found by them. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReactionUnavailabilityReason](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reaction_unavailability_reason.html) > | [unavailability_reason_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#ace870af89f4a57693048a819d928b0d8) |
|  | The reason why the current user can't add reactions to the message, despite some other users can; may be null if none. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [availableReactions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#ab1648716859f23048c29d003646720ca) () |
|  | |
|  | [availableReactions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#a45e7c650997c5a278a759b8e1bab88e4) ([array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [availableReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reaction.html) >> &&[top_reactions_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#a108d619ff6a006bd8b4e63ed6ef08be9), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [availableReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reaction.html) >> &&[recent_reactions_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#a42d9d6ec74632a49e868872413df7c5e), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [availableReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reaction.html) >> &&[popular_reactions_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#ad25ed4aea432740821a51557f3fb75d8), bool [allow_custom_emoji_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#aa8baf441d878271a46577604035cf1ad), bool [are_tags_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#af6c632b322beadfaa0c2798b120a330e), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReactionUnavailabilityReason](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reaction_unavailability_reason.html) > &&[unavailability_reason_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#ace870af89f4a57693048a819d928b0d8)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 912529522 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#ab1648716859f23048c29d003646720ca)availableReactions() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [availableReactions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html) | ( |  | ) |  |

Represents a list of reactions that can be added to a message.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#a45e7c650997c5a278a759b8e1bab88e4)availableReactions() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [availableReactions](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html) | ( | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [availableReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reaction.html) >> && | *top_reactions_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [availableReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reaction.html) >> && | *recent_reactions_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [availableReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reaction.html) >> && | *popular_reactions_*, |
|  |  | bool | *allow_custom_emoji_*, |
|  |  | bool | *are_tags_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReactionUnavailabilityReason](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reaction_unavailability_reason.html) > && | *unavailability_reason_* |
|  | ) |  |  |

Represents a list of reactions that can be added to a message.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | top_reactions_ | List of reactions to be shown at the top. |
    | [in] | recent_reactions_ | List of recently used reactions. |
    | [in] | popular_reactions_ | List of popular reactions. |
    | [in] | allow_custom_emoji_ | True, if any custom emoji reaction can be added by Telegram Premium subscribers. |
    | [in] | are_tags_ | True, if the reactions will be tags and the message can be found by them. |
    | [in] | unavailability_reason_ | The reason why the current user can't add reactions to the message, despite some other users can; may be null if none. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1available_reactions.html#a8044dab2ba3c75066745014259c050c7)store()

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