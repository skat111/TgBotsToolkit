# TDLib: pushMessageContentChatSetTheme Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_chat_set_theme.html

Inherits [PushMessageContent](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_push_message_content.html).

## Description

A chat theme was edited.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [name_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_chat_set_theme.html#a79cfd788b219a7f48068d0e96e5e8e77) |
|  | If non-empty, human-readable name of the new theme. Otherwise, the chat theme was reset to the default one. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [pushMessageContentChatSetTheme](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_chat_set_theme.html#a5f3cc3cbe707a6928e3734fb838a2c3a) () |
|  | |
|  | [pushMessageContentChatSetTheme](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_chat_set_theme.html#a7932ed38906859ee2b47673c218fd6ad) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[name_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_chat_set_theme.html#a79cfd788b219a7f48068d0e96e5e8e77)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_chat_set_theme.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_chat_set_theme.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1605251024 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_chat_set_theme.html#a5f3cc3cbe707a6928e3734fb838a2c3a)pushMessageContentChatSetTheme() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [pushMessageContentChatSetTheme](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_chat_set_theme.html) | ( |  | ) |  |

A chat theme was edited.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_chat_set_theme.html#a7932ed38906859ee2b47673c218fd6ad)pushMessageContentChatSetTheme() [2/2]

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [pushMessageContentChatSetTheme](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_chat_set_theme.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *name_* | ) |  | | explicit |

A chat theme was edited.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | name_ | If non-empty, human-readable name of the new theme. Otherwise, the chat theme was reset to the default one. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1push_message_content_chat_set_theme.html#a8044dab2ba3c75066745014259c050c7)store()

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