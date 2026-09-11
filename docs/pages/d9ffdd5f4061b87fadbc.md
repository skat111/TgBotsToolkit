# TDLib: inputStoryAreas Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_areas.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Contains a list of story areas to be added.

|  |  |
| --- | --- |
| Public Fields | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [inputStoryArea](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area.html) > > | [areas\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_areas.html#a318d5e4e6dee9ae5de816e29eee50fcf) |
|  | List of input story areas. Currently, a story can have up to 10 [inputStoryAreaTypeLocation](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_location.html), [inputStoryAreaTypeFoundVenue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_found_venue.html), and [inputStoryAreaTypePreviousVenue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_previous_venue.html) areas, up to [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("story\_suggested\_reaction\_area\_count\_max") [inputStoryAreaTypeSuggestedReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_suggested_reaction.html) areas, up to 1 [inputStoryAreaTypeMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_message.html) area, up to [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("story\_link\_area\_count\_max") [inputStoryAreaTypeLink](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_link.html) areas if the current user is a Telegram Premium user, up to 3 [inputStoryAreaTypeWeather](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_weather.html) areas, and up to 1 [inputStoryAreaTypeUpgradedGift](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_upgraded_gift.html) area. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [inputStoryAreas](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_areas.html#aaa97a3b2246860e662d68a6acd5ae707) () |
|  | |
|  | [inputStoryAreas](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_areas.html#a1c6e6f23a259ebd65a6e027e83e988ed) ([array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [inputStoryArea](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area.html) >> &&[areas\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_areas.html#a318d5e4e6dee9ae5de816e29eee50fcf)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_areas.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_areas.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -883247088 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_areas.html#aaa97a3b2246860e662d68a6acd5ae707)inputStoryAreas() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [inputStoryAreas](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_areas.html) | ( |  | ) |  |

Contains a list of story areas to be added.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_areas.html#a1c6e6f23a259ebd65a6e027e83e988ed)inputStoryAreas() [2/2]

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [inputStoryAreas](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_areas.html) | ( | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [inputStoryArea](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area.html) >> && | *areas\_* | ) |  | | explicit |

Contains a list of story areas to be added.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | areas\_ | List of input story areas. Currently, a story can have up to 10 [inputStoryAreaTypeLocation](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_location.html), [inputStoryAreaTypeFoundVenue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_found_venue.html), and [inputStoryAreaTypePreviousVenue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_previous_venue.html) areas, up to [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("story\_suggested\_reaction\_area\_count\_max") [inputStoryAreaTypeSuggestedReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_suggested_reaction.html) areas, up to 1 [inputStoryAreaTypeMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_message.html) area, up to [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("story\_link\_area\_count\_max") [inputStoryAreaTypeLink](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_link.html) areas if the current user is a Telegram Premium user, up to 3 [inputStoryAreaTypeWeather](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_weather.html) areas, and up to 1 [inputStoryAreaTypeUpgradedGift](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_area_type_upgraded_gift.html) area. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_story_areas.html#a8044dab2ba3c75066745014259c050c7)store()

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