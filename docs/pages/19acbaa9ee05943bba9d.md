# TDLib: loginUrlInfoOpen Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1login_url_info_open.html

Inherits [LoginUrlInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_login_url_info.html).

## Description

An HTTP URL needs to be open.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [url_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1login_url_info_open.html#a541e0f072a74af71d6978eea722fc5fe) |
|  | The URL to open. |
|  | |
| bool | [skip_confirmation_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1login_url_info_open.html#a608b250eae67060ba62cfaf3635e5b38) |
|  | True, if there is no need to show an ordinary open URL confirmation. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [loginUrlInfoOpen](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1login_url_info_open.html#a188855d28aaa2b919abf87d889787939) () |
|  | |
|  | [loginUrlInfoOpen](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1login_url_info_open.html#a6e9c891cda327a0ad633d81f15bf02b3) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[url_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1login_url_info_open.html#a541e0f072a74af71d6978eea722fc5fe), bool [skip_confirmation_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1login_url_info_open.html#a608b250eae67060ba62cfaf3635e5b38)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1login_url_info_open.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1login_url_info_open.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 837282306 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1login_url_info_open.html#a188855d28aaa2b919abf87d889787939)loginUrlInfoOpen() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [loginUrlInfoOpen](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1login_url_info_open.html) | ( |  | ) |  |

An HTTP URL needs to be open.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1login_url_info_open.html#a6e9c891cda327a0ad633d81f15bf02b3)loginUrlInfoOpen() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [loginUrlInfoOpen](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1login_url_info_open.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *url_*, |
|  |  | bool | *skip_confirmation_* |
|  | ) |  |  |

An HTTP URL needs to be open.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | url_ | The URL to open. |
    | [in] | skip_confirmation_ | True, if there is no need to show an ordinary open URL confirmation. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1login_url_info_open.html#a8044dab2ba3c75066745014259c050c7)store()

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