# TDLib: Client::Request Struct Reference

Source: https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_request.html

## Description

A request to the TDLib.

|  |  |
| --- | --- |
| Public Fields | |
| std::uint64\_t | [id](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_request.html#a3e3507be967a9cec9979b9ab1179b210) |
|  | |
| [td\_api::object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [td\_api::Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html) > | [function](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_request.html#a77f036373636e74bfa54fa5155b4fe76) |
|  | |

## Member Data Documentation

## [◆](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_request.html#a3e3507be967a9cec9979b9ab1179b210)id

|  |
| --- |
| std::uint64\_t id |

[Request](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_request.html) identifier. Responses to TDLib requests will have the same id as the corresponding request. Updates from TDLib will have id == 0, incoming requests are thus disallowed to have id == 0.

## [◆](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_request.html#a77f036373636e74bfa54fa5155b4fe76)function

|  |
| --- |
| [td\_api::object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)<[td\_api::Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html)> function |

TDLib API function representing a request to TDLib.

---

The documentation for this struct was generated from the following file:

* td/telegram/[Client.h](https://core.telegram.org/tdlib/docs/_client_8h_source.html)