# TDLib: inputMessageDice Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_dice.html

Inherits [InputMessageContent](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_message_content.html).

## Description

A dice message.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [emoji_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_dice.html#ac2cc29cb40b3db7cfa663986a1e261bf) |
|  | Emoji on which the dice throw animation is based. |
|  | |
| bool | [clear_draft_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_dice.html#a3bd4c48c0c3d9cd9ac739a4d01e70911) |
|  | True, if the chat message draft must be deleted. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [inputMessageDice](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_dice.html#a66b548919f605823012f5eea4a7b3072) () |
|  | |
|  | [inputMessageDice](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_dice.html#a11c8016a551eb43993298b640402ae78) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[emoji_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_dice.html#ac2cc29cb40b3db7cfa663986a1e261bf), bool [clear_draft_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_dice.html#a3bd4c48c0c3d9cd9ac739a4d01e70911)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_dice.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_dice.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 841574313 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_dice.html#a66b548919f605823012f5eea4a7b3072)inputMessageDice() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [inputMessageDice](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_dice.html) | ( |  | ) |  |

A dice message.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_dice.html#a11c8016a551eb43993298b640402ae78)inputMessageDice() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [inputMessageDice](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_dice.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *emoji_*, |
|  |  | bool | *clear_draft_* |
|  | ) |  |  |

A dice message.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | emoji_ | Emoji on which the dice throw animation is based. |
    | [in] | clear_draft_ | True, if the chat message draft must be deleted. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_dice.html#a8044dab2ba3c75066745014259c050c7)store()

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