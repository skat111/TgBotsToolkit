# TDLib: updateStoryPostSucceeded Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_story_post_succeeded.html

Inherits [Update](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_update.html).

## Description

A story has been successfully posted.

|  |  |
| --- | --- |
| Public Fields | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [story](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story.html) > | [story_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_story_post_succeeded.html#a8bb52439c39d932213e25fa44068ac37) |
|  | The posted story. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [old_story_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_story_post_succeeded.html#a2b2596c86e87aa72a3019b070b955290) |
|  | The previous temporary story identifier. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [updateStoryPostSucceeded](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_story_post_succeeded.html#aaeed57c55277b3f06fa56f9d2aed0d42) () |
|  | |
|  | [updateStoryPostSucceeded](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_story_post_succeeded.html#a650c8ef6b2ffca7d8e35a841e2741340) ([object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [story](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story.html) > &&[story_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_story_post_succeeded.html#a8bb52439c39d932213e25fa44068ac37), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [old_story_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_story_post_succeeded.html#a2b2596c86e87aa72a3019b070b955290)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_story_post_succeeded.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_story_post_succeeded.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1712432318 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_story_post_succeeded.html#aaeed57c55277b3f06fa56f9d2aed0d42)updateStoryPostSucceeded() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [updateStoryPostSucceeded](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_story_post_succeeded.html) | ( |  | ) |  |

A story has been successfully posted.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_story_post_succeeded.html#a650c8ef6b2ffca7d8e35a841e2741340)updateStoryPostSucceeded() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [updateStoryPostSucceeded](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_story_post_succeeded.html) | ( | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [story](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story.html) > && | *story_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *old_story_id_* |
|  | ) |  |  |

A story has been successfully posted.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | story_ | The posted story. |
    | [in] | old_story_id_ | The previous temporary story identifier. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_story_post_succeeded.html#a8044dab2ba3c75066745014259c050c7)store()

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