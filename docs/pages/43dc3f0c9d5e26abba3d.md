# TDLib: botMenuButton Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes a button to be shown instead of bot commands menu button.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [text_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html#a1e07078cd658903987f94f1a39482856) |
|  | Text of the button. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [url_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html#a541e0f072a74af71d6978eea722fc5fe) |
|  | URL of a Web App to open when the button is pressed. If the link is of the type [internalLinkTypeWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_web_app.html), then it must be processed accordingly. Otherwise, the link must be passed to [openWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html). |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [botMenuButton](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html#a506f7c32dd039ed56bbd33934cbc3351) () |
|  | |
|  | [botMenuButton](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html#a80d3fbe976adcfcca61221fec5c9530e) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[text_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html#a1e07078cd658903987f94f1a39482856), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[url_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html#a541e0f072a74af71d6978eea722fc5fe)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -944407322 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html#a506f7c32dd039ed56bbd33934cbc3351)botMenuButton() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [botMenuButton](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html) | ( |  | ) |  |

Describes a button to be shown instead of bot commands menu button.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html#a80d3fbe976adcfcca61221fec5c9530e)botMenuButton() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [botMenuButton](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *text_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *url_* |
|  | ) |  |  |

Describes a button to be shown instead of bot commands menu button.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | text_ | Text of the button. |
    | [in] | url_ | URL of a Web App to open when the button is pressed. If the link is of the type [internalLinkTypeWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_web_app.html), then it must be processed accordingly. Otherwise, the link must be passed to [openWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1open_web_app.html). |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_menu_button.html#a8044dab2ba3c75066745014259c050c7)store()

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