# TDLib: Client Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1_client.html

## Description

Old native C++ interface for interaction with TDLib to be removed in TDLib 2.0.0.

The TDLib instance is created for the lifetime of the [Client](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html) object. Requests to TDLib can be sent using the [Client::send](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#ab445ac5feeb53f638da3f617a9bef9ec) method from any thread. New updates and responses to requests can be received using the [Client::receive](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#a95ed6da3afd8b605b3bf94f1f8915aff) method from any thread, this function must not be called simultaneously from two different threads. Also, note that all updates and responses to requests should be applied in the same order as they were received, to ensure consistency. Given this information, it's advisable to call this function from a dedicated thread. Some service TDLib requests can be executed synchronously from any thread using the [Client::execute](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#a05d77816ef3c9e1038260295c4e18f1b) method.

General pattern of usage:

std::shared_ptr<td::Client> client = std::make_shared<td::Client>();

// somehow share the client with other threads, which will be able to send requests via client->send

const double WAIT_TIMEOUT = 10.0; // seconds

bool is_closed = false; // should be set to true, when updateAuthorizationState with

// authorizationStateClosed is received

while (!is_closed) {

auto response = client->[receive](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#a95ed6da3afd8b605b3bf94f1f8915aff)(WAIT_TIMEOUT);

if (response.object == nullptr) {

continue;

}

if (response.id == 0) {

// process response.object as an incoming update of type td_api::Update

} else {

// process response.object as an answer to a sent request with identifier response.id

}

}

|  |  |
| --- | --- |
| Classes | |
| struct | [Request](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_request.html) |
|  | |
| struct | [Response](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_response.html) |
|  | |

|  |  |
| --- | --- |
| Public Class Methods | |
| static [Response](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_response.html) | [execute](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#a05d77816ef3c9e1038260295c4e18f1b) ([Request](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_request.html) &&request) |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [Client](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#aa5777bac2de54b388226a381a4174ff0) () |
|  | |
| void | [send](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#ab445ac5feeb53f638da3f617a9bef9ec) ([Request](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_request.html) &&request) |
|  | |
| [Response](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_response.html) | [receive](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#a95ed6da3afd8b605b3bf94f1f8915aff) (double timeout) |
|  | |
|  | [~Client](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#a37731a8f5dd5caca4cc2ddb8b556cd6c) () |
|  | |
|  | [Client](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#a98c358a0982927cd083b447c8fab9b58) ([Client](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html) &&other) noexcept |
|  | |
| [Client](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html) & | [operator=](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#a028f95a4ece503e01ccf31f37763af21) ([Client](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html) &&other) noexcept |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#aa5777bac2de54b388226a381a4174ff0)Client() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Client](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html) | ( |  | ) |  |

Creates a new TDLib client.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#a37731a8f5dd5caca4cc2ddb8b556cd6c)~Client()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ~[Client](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html) | ( |  | ) |  |

Destroys the client and TDLib instance.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#a98c358a0982927cd083b447c8fab9b58)Client() [2/2]

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [Client](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html) | ( | [Client](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html) && | *other* | ) |  | | noexcept |

Move constructor.

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#ab445ac5feeb53f638da3f617a9bef9ec)send()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void send | ( | [Request](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_request.html) && | *request* | ) |  |

Sends request to TDLib. May be called from any thread.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | request | [Request](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_request.html) to TDLib. |

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#a95ed6da3afd8b605b3bf94f1f8915aff)receive()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| [Response](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_response.html) receive | ( | double | *timeout* | ) |  |

Receives incoming updates and request responses from TDLib. May be called from any thread, but shouldn't be called simultaneously from two different threads.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | timeout | The maximum number of seconds allowed for this function to wait for new data. |

Returns
:   An incoming update or request response. The object returned in the response may be a nullptr if the timeout expires.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#a05d77816ef3c9e1038260295c4e18f1b)execute()

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | static [Response](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_response.html) execute | ( | [Request](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_request.html) && | *request* | ) |  | | static |

Synchronously executes TDLib requests. Only a few requests can be executed synchronously. May be called from any thread.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | request | [Request](https://core.telegram.org/tdlib/docs/structtd_1_1_client_1_1_request.html) to the TDLib. |

Returns
:   The request response.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html#a028f95a4ece503e01ccf31f37763af21)operator=()

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [Client](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html)& operator= | ( | [Client](https://core.telegram.org/tdlib/docs/classtd_1_1_client.html) && | *other* | ) |  | | noexcept |

Move assignment operator.

---

The documentation for this class was generated from the following file:

* td/telegram/[Client.h](https://core.telegram.org/tdlib/docs/_client_8h_source.html)