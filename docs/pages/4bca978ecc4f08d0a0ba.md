# TDLib: getWebAppLinkUrl Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Returns an HTTPS URL of a Web App to open after a link of the type [internalLinkTypeWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_web_app.html) is clicked.

Returns object_ptr<HttpUrl>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Identifier of the chat in which the link was clicked; pass 0 if none. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [bot_user_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a852a1eecf72791be8eb2633ff5dcaec4) |
|  | Identifier of the target bot. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [web_app_short_name_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a790983d865ac7a7355db6aad4d84f864) |
|  | Short name of the Web App. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [start_parameter_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a0bb6210f37d63781e256ce994776918c) |
|  | Start parameter from [internalLinkTypeWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_web_app.html). |
|  | |
| bool | [allow_write_access_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a7da6253b54395e4b495a4f7d7c2c8079) |
|  | Pass true if the current user allowed the bot to send them messages. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [webAppOpenParameters](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1web_app_open_parameters.html) > | [parameters_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#af39abd6dbe450aa53cad2723cc084de1) |
|  | Parameters to use to open the Web App. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a89600d844008faaad1ecacab98018b81) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [httpUrl](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1http_url.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [getWebAppLinkUrl](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a9beb47d2920537fc5970b631d4e52a33) () |
|  | |
|  | [getWebAppLinkUrl](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a01fbbf33a0d72ec53aa5520eb32c046f) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#aa8a7803161092ff97e60d58707199e1f), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [bot_user_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a852a1eecf72791be8eb2633ff5dcaec4), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[web_app_short_name_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a790983d865ac7a7355db6aad4d84f864), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[start_parameter_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a0bb6210f37d63781e256ce994776918c), bool [allow_write_access_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a7da6253b54395e4b495a4f7d7c2c8079), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [webAppOpenParameters](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1web_app_open_parameters.html) > &&[parameters_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#af39abd6dbe450aa53cad2723cc084de1)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1627284161 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a9beb47d2920537fc5970b631d4e52a33)getWebAppLinkUrl() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [getWebAppLinkUrl](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html) | ( |  | ) |  |

Default constructor for a function, which returns an HTTPS URL of a Web App to open after a link of the type [internalLinkTypeWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_web_app.html) is clicked.

Returns object_ptr<HttpUrl>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a01fbbf33a0d72ec53aa5520eb32c046f)getWebAppLinkUrl() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [getWebAppLinkUrl](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat_id_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *bot_user_id_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *web_app_short_name_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *start_parameter_*, |
|  |  | bool | *allow_write_access_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [webAppOpenParameters](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1web_app_open_parameters.html) > && | *parameters_* |
|  | ) |  |  |

Creates a function, which returns an HTTPS URL of a Web App to open after a link of the type [internalLinkTypeWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_web_app.html) is clicked.

Returns object_ptr<HttpUrl>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat_id_ | Identifier of the chat in which the link was clicked; pass 0 if none. |
    | [in] | bot_user_id_ | Identifier of the target bot. |
    | [in] | web_app_short_name_ | Short name of the Web App. |
    | [in] | start_parameter_ | Start parameter from [internalLinkTypeWebApp](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1internal_link_type_web_app.html). |
    | [in] | allow_write_access_ | Pass true if the current user allowed the bot to send them messages. |
    | [in] | parameters_ | Parameters to use to open the Web App. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_web_app_link_url.html#a8044dab2ba3c75066745014259c050c7)store()

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