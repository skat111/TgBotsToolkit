# TDLib: oauthLinkInfo Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Information about the OAuth authorization.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [user_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a80aca422ea16bbb3ab3b62fafa43af6c) |
|  | Identifier of the user for which the link was generated; may be 0 if unknown. The corresponding user may be unknown. If the user is logged in the app, then they must be chosen for authorization by default. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [url_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a541e0f072a74af71d6978eea722fc5fe) |
|  | An HTTP URL where the user authorizes. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [domain_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a44b9e1f8a26c08c9dcdb84253d703a9c) |
|  | A domain of the URL. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [bot_user_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a852a1eecf72791be8eb2633ff5dcaec4) |
|  | User identifier of a bot linked with the website. |
|  | |
| bool | [request_write_access_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a988c6d54fcdb9d5528dc8e2e5a832b05) |
|  | True, if the user must be asked for the permission to the bot to send them messages. |
|  | |
| bool | [request_phone_number_access_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a83c5c7c1381390a40da992a10535a411) |
|  | True, if the user must be asked for the permission to share their phone number. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [browser_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a759f9a9f2544bb32d90ff2c9ef5ec8ee) |
|  | The version of a browser used for the authorization. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [platform_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#aa81f06ec384ee696ee72c4714d5f6b33) |
|  | Operating system the browser is running on. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [ip_address_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a9b606e23d1355c037e80a6d52b2a0c06) |
|  | IP address from which the authorization is performed, in human-readable format. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [location_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a842286abf4d9cc56561cc2c92cdf5dc2) |
|  | Human-readable description of a country and a region from which the authorization is performed, based on the IP address. |
|  | |
| bool | [match_code_first_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a4d968ac01750130a6588099578ef24a2) |
|  | True, if code matching dialog must be shown first and [checkOauthRequestMatchCode](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1check_oauth_request_match_code.html) must be called before [acceptOauthRequest](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1accept_oauth_request.html). Otherwise, [checkOauthRequestMatchCode](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1check_oauth_request_match_code.html) must not be called. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) > | [match_codes_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#aa166d1fcbd70f0e95c0f0831df3ad399) |
|  | The list of codes to match; may be empty if irrelevant. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [oauthLinkInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a89732a75c9160507f47eac6db44b59e2) () |
|  | |
|  | [oauthLinkInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#ac1a0051d77879ae1fb21a93b42570b76) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [user_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a80aca422ea16bbb3ab3b62fafa43af6c), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[url_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a541e0f072a74af71d6978eea722fc5fe), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[domain_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a44b9e1f8a26c08c9dcdb84253d703a9c), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [bot_user_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a852a1eecf72791be8eb2633ff5dcaec4), bool [request_write_access_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a988c6d54fcdb9d5528dc8e2e5a832b05), bool [request_phone_number_access_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a83c5c7c1381390a40da992a10535a411), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[browser_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a759f9a9f2544bb32d90ff2c9ef5ec8ee), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[platform_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#aa81f06ec384ee696ee72c4714d5f6b33), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[ip_address_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a9b606e23d1355c037e80a6d52b2a0c06), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[location_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a842286abf4d9cc56561cc2c92cdf5dc2), bool [match_code_first_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a4d968ac01750130a6588099578ef24a2), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) > &&[match_codes_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#aa166d1fcbd70f0e95c0f0831df3ad399)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1916199178 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a89732a75c9160507f47eac6db44b59e2)oauthLinkInfo() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [oauthLinkInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html) | ( |  | ) |  |

Information about the OAuth authorization.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#ac1a0051d77879ae1fb21a93b42570b76)oauthLinkInfo() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [oauthLinkInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *user_id_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *url_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *domain_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *bot_user_id_*, |
|  |  | bool | *request_write_access_*, |
|  |  | bool | *request_phone_number_access_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *browser_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *platform_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *ip_address_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *location_*, |
|  |  | bool | *match_code_first_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) > && | *match_codes_* |
|  | ) |  |  |

Information about the OAuth authorization.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | user_id_ | Identifier of the user for which the link was generated; may be 0 if unknown. The corresponding user may be unknown. If the user is logged in the app, then they must be chosen for authorization by default. |
    | [in] | url_ | An HTTP URL where the user authorizes. |
    | [in] | domain_ | A domain of the URL. |
    | [in] | bot_user_id_ | User identifier of a bot linked with the website. |
    | [in] | request_write_access_ | True, if the user must be asked for the permission to the bot to send them messages. |
    | [in] | request_phone_number_access_ | True, if the user must be asked for the permission to share their phone number. |
    | [in] | browser_ | The version of a browser used for the authorization. |
    | [in] | platform_ | Operating system the browser is running on. |
    | [in] | ip_address_ | IP address from which the authorization is performed, in human-readable format. |
    | [in] | location_ | Human-readable description of a country and a region from which the authorization is performed, based on the IP address. |
    | [in] | match_code_first_ | True, if code matching dialog must be shown first and [checkOauthRequestMatchCode](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1check_oauth_request_match_code.html) must be called before [acceptOauthRequest](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1accept_oauth_request.html). Otherwise, [checkOauthRequestMatchCode](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1check_oauth_request_match_code.html) must not be called. |
    | [in] | match_codes_ | The list of codes to match; may be empty if irrelevant. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1oauth_link_info.html#a8044dab2ba3c75066745014259c050c7)store()

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