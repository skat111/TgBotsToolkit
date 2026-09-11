# TDLib: ClientManager::Response Struct Reference

Source: https://core.telegram.org/tdlib/docs/structtd_1_1_client_manager_1_1_response.html

## Description

A response to a request, or an incoming update from TDLib.

|  |  |
| --- | --- |
| Public Fields | |
| [ClientId](https://core.telegram.org/tdlib/docs/classtd_1_1_client_manager.html#a7c00e91c9a898ef7b0d5df0d30bae316) | [client\_id](https://core.telegram.org/tdlib/docs/structtd_1_1_client_manager_1_1_response.html#aa15f0c7a1e48252aa5f2a5cd0c4bd6f5) |
|  | |
| [RequestId](https://core.telegram.org/tdlib/docs/classtd_1_1_client_manager.html#af977e0c4b3a6e7886c42d276bceb0bd1) | [request\_id](https://core.telegram.org/tdlib/docs/structtd_1_1_client_manager_1_1_response.html#a33a5cce7ed27c77beb037b83d38cd173) |
|  | |
| [td\_api::object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [td\_api::Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html) > | [object](https://core.telegram.org/tdlib/docs/structtd_1_1_client_manager_1_1_response.html#a17487d4a1e5c5d8b0c1ec7706eb0ced3) |
|  | |

## Member Data Documentation

## [◆](https://core.telegram.org/tdlib/docs/structtd_1_1_client_manager_1_1_response.html#aa15f0c7a1e48252aa5f2a5cd0c4bd6f5)client\_id

|  |
| --- |
| [ClientId](https://core.telegram.org/tdlib/docs/classtd_1_1_client_manager.html#a7c00e91c9a898ef7b0d5df0d30bae316) client\_id |

TDLib client instance identifier, for which the response was received.

## [◆](https://core.telegram.org/tdlib/docs/structtd_1_1_client_manager_1_1_response.html#a33a5cce7ed27c77beb037b83d38cd173)request\_id

|  |
| --- |
| [RequestId](https://core.telegram.org/tdlib/docs/classtd_1_1_client_manager.html#af977e0c4b3a6e7886c42d276bceb0bd1) request\_id |

Request identifier to which the response corresponds, or 0 for incoming updates from TDLib.

## [◆](https://core.telegram.org/tdlib/docs/structtd_1_1_client_manager_1_1_response.html#a17487d4a1e5c5d8b0c1ec7706eb0ced3)object

|  |
| --- |
| [td\_api::object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)<[td\_api::Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html)> object |

TDLib API object representing a response to a TDLib request or an incoming update.

---

The documentation for this struct was generated from the following file:

* td/telegram/[Client.h](https://core.telegram.org/tdlib/docs/_client_8h_source.html)