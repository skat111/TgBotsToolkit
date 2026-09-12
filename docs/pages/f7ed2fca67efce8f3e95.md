# TDLib: sendPaymentForm Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Sends a filled-out payment form to the bot for final verification.

Returns object_ptr<PaymentResult>.

|  |  |
| --- | --- |
| Public Fields | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputInvoice](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_invoice.html) > | [input_invoice_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a2bacdb8ff726adffa5d1441990be0298) |
|  | The invoice. |
|  | |
| [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | [payment_form_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a91365ab431063282dacbe0cb40435baf) |
|  | Payment form identifier returned by [getPaymentForm](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_payment_form.html). |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [order_info_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a13663e568f377c4495bd8a37bba9ed2a) |
|  | Identifier returned by [validateOrderInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1validate_order_info.html), or an empty string. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [shipping_option_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#aab6adc79d2abdcd9f22ef4800188cfec) |
|  | Identifier of a chosen shipping option, if applicable. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputCredentials](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_credentials.html) > | [credentials_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a4ba66aef7e4094899d803e8b5b053cb8) |
|  | The credentials chosen by user for payment; pass null for a payment in Telegram Stars. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [tip_amount_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#ae880048dc0b3ddef071c3a0fa04b00af) |
|  | Chosen by the user amount of tip in the smallest units of the currency. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a572685d8f34a5e9e03056d90e4764492) = [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [paymentResult](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1payment_result.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [sendPaymentForm](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a7076cd1d281651f91347b99e7abdd217) () |
|  | |
|  | [sendPaymentForm](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a9ec271c7f94f486bf57436dd0c16d7c0) ([object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputInvoice](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_invoice.html) > &&[input_invoice_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a2bacdb8ff726adffa5d1441990be0298), [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) [payment_form_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a91365ab431063282dacbe0cb40435baf), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[order_info_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a13663e568f377c4495bd8a37bba9ed2a), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[shipping_option_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#aab6adc79d2abdcd9f22ef4800188cfec), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputCredentials](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_credentials.html) > &&[credentials_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a4ba66aef7e4094899d803e8b5b053cb8), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [tip_amount_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#ae880048dc0b3ddef071c3a0fa04b00af)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -965855094 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a7076cd1d281651f91347b99e7abdd217)sendPaymentForm() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [sendPaymentForm](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html) | ( |  | ) |  |

Default constructor for a function, which sends a filled-out payment form to the bot for final verification.

Returns object_ptr<PaymentResult>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a9ec271c7f94f486bf57436dd0c16d7c0)sendPaymentForm() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [sendPaymentForm](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html) | ( | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputInvoice](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_invoice.html) > && | *input_invoice_*, |
|  |  | [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | *payment_form_id_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *order_info_id_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *shipping_option_id_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputCredentials](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_credentials.html) > && | *credentials_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *tip_amount_* |
|  | ) |  |  |

Creates a function, which sends a filled-out payment form to the bot for final verification.

Returns object_ptr<PaymentResult>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | input_invoice_ | The invoice. |
    | [in] | payment_form_id_ | Payment form identifier returned by [getPaymentForm](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_payment_form.html). |
    | [in] | order_info_id_ | Identifier returned by [validateOrderInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1validate_order_info.html), or an empty string. |
    | [in] | shipping_option_id_ | Identifier of a chosen shipping option, if applicable. |
    | [in] | credentials_ | The credentials chosen by user for payment; pass null for a payment in Telegram Stars. |
    | [in] | tip_amount_ | Chosen by the user amount of tip in the smallest units of the currency. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1send_payment_form.html#a8044dab2ba3c75066745014259c050c7)store()

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