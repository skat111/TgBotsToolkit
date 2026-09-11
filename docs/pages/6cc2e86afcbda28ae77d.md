# TDLib: requestQrCodeAuthentication Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1request_qr_code_authentication.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Requests QR code authentication by scanning a QR code on another logged in device. Works only when the current authorization state is [authorizationStateWaitPhoneNumber](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_phone_number.html), or if there is no pending authentication query and the current authorization state is [authorizationStateWaitPremiumPurchase](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_premium_purchase.html), [authorizationStateWaitEmailAddress](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_email_address.html), [authorizationStateWaitEmailCode](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_email_code.html), [authorizationStateWaitCode](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_code.html), [authorizationStateWaitRegistration](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_registration.html), or [authorizationStateWaitPassword](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_password.html).

Returns object\_ptr<Ok>.

|  |  |
| --- | --- |
| Public Fields | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) > | [other\_user\_ids\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1request_qr_code_authentication.html#ac7fa11d1c5dc45d697598f29066d2173) |
|  | List of user identifiers of other users currently using the application. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1request_qr_code_authentication.html#ab684327f0ee9cbf9afb740503d89f019) = [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ok](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1ok.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [requestQrCodeAuthentication](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1request_qr_code_authentication.html#a6e4cfb8deccf3312c4f8999c0a3b47c1) () |
|  | |
|  | [requestQrCodeAuthentication](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1request_qr_code_authentication.html#a2cb31ea1cabe833164eeaa882617ae75) ([array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) > &&[other\_user\_ids\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1request_qr_code_authentication.html#ac7fa11d1c5dc45d697598f29066d2173)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1request_qr_code_authentication.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1request_qr_code_authentication.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1363496527 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1request_qr_code_authentication.html#a6e4cfb8deccf3312c4f8999c0a3b47c1)requestQrCodeAuthentication() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [requestQrCodeAuthentication](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1request_qr_code_authentication.html) | ( |  | ) |  |

Default constructor for a function, which requests QR code authentication by scanning a QR code on another logged in device. Works only when the current authorization state is [authorizationStateWaitPhoneNumber](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_phone_number.html), or if there is no pending authentication query and the current authorization state is [authorizationStateWaitPremiumPurchase](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_premium_purchase.html), [authorizationStateWaitEmailAddress](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_email_address.html), [authorizationStateWaitEmailCode](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_email_code.html), [authorizationStateWaitCode](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_code.html), [authorizationStateWaitRegistration](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_registration.html), or [authorizationStateWaitPassword](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_password.html).

Returns object\_ptr<Ok>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1request_qr_code_authentication.html#a2cb31ea1cabe833164eeaa882617ae75)requestQrCodeAuthentication() [2/2]

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [requestQrCodeAuthentication](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1request_qr_code_authentication.html) | ( | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) > && | *other\_user\_ids\_* | ) |  | | explicit |

Creates a function, which requests QR code authentication by scanning a QR code on another logged in device. Works only when the current authorization state is [authorizationStateWaitPhoneNumber](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_phone_number.html), or if there is no pending authentication query and the current authorization state is [authorizationStateWaitPremiumPurchase](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_premium_purchase.html), [authorizationStateWaitEmailAddress](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_email_address.html), [authorizationStateWaitEmailCode](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_email_code.html), [authorizationStateWaitCode](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_code.html), [authorizationStateWaitRegistration](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_registration.html), or [authorizationStateWaitPassword](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1authorization_state_wait_password.html).

Returns object\_ptr<Ok>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | other\_user\_ids\_ | List of user identifiers of other users currently using the application. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1request_qr_code_authentication.html#a8044dab2ba3c75066745014259c050c7)store()

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