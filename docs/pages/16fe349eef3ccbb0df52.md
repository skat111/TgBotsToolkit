# TDLib: storyFullId Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_full_id.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Contains identifier of a story along with identifier of the chat that posted it.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [poster\_chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_full_id.html#adc5d77b702a1d83c73c34da4bacedef7) |
|  | Identifier of the chat that posted the story. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [story\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_full_id.html#aeaae5cea664e806d0160e4a48b20ee3b) |
|  | Unique story identifier among stories of the chat. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [storyFullId](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_full_id.html#a722eb4a7f8db02d13fbd5a6bfb6d276f) () |
|  | |
|  | [storyFullId](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_full_id.html#acb5f9bd408348b9081566a129d5ea00e) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [poster\_chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_full_id.html#adc5d77b702a1d83c73c34da4bacedef7), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [story\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_full_id.html#aeaae5cea664e806d0160e4a48b20ee3b)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_full_id.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_full_id.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 765952419 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_full_id.html#a722eb4a7f8db02d13fbd5a6bfb6d276f)storyFullId() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [storyFullId](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_full_id.html) | ( |  | ) |  |

Contains identifier of a story along with identifier of the chat that posted it.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_full_id.html#acb5f9bd408348b9081566a129d5ea00e)storyFullId() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [storyFullId](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_full_id.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *poster\_chat\_id\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *story\_id\_* |
|  | ) |  |  |

Contains identifier of a story along with identifier of the chat that posted it.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | poster\_chat\_id\_ | Identifier of the chat that posted the story. |
    | [in] | story\_id\_ | Unique story identifier among stories of the chat. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_full_id.html#a8044dab2ba3c75066745014259c050c7)store()

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