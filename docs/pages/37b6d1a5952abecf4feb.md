# TDLib: PassportElementType Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_passport_element_type.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

Inherited by [passportElementTypeAddress](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passport_element_type_address.html), [passportElementTypeBankStatement](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passport_element_type_bank_statement.html), [passportElementTypeDriverLicense](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passport_element_type_driver_license.html), [passportElementTypeEmailAddress](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passport_element_type_email_address.html), [passportElementTypeIdentityCard](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passport_element_type_identity_card.html), [passportElementTypeInternalPassport](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passport_element_type_internal_passport.html), [passportElementTypePassport](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passport_element_type_passport.html), [passportElementTypePassportRegistration](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passport_element_type_passport_registration.html), [passportElementTypePersonalDetails](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passport_element_type_personal_details.html), [passportElementTypePhoneNumber](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passport_element_type_phone_number.html), [passportElementTypeRentalAgreement](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passport_element_type_rental_agreement.html), [passportElementTypeTemporaryRegistration](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passport_element_type_temporary_registration.html), and [passportElementTypeUtilityBill](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1passport_element_type_utility_bill.html).

## Description

This class is an abstract base class. Contains the type of Telegram Passport element.

|  |  |
| --- | --- |
| Additional Inherited Members | |
| - Public Instance Methods inherited from [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) | |
| virtual std::int32\_t | [get\_id](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a19a85e75f450a2d07f0cf57c7e32076b) () const =0 |
|  | |
| virtual void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#aed3fac8962d039b3c4827cd013ba8050) (TlStorerUnsafe &s) const |
|  | |
| virtual void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a66f325c1a08459d978fa08dcc4e7a86e) (TlStorerCalcLength &s) const |
|  | |
| virtual void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a4f1eab7385f340a2ab0aa8751cdcedc6) (TlStorerToString &s, const char \*field\_name) const =0 |
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

---

The documentation for this class was generated from the following file:

* td/generate/auto/td/telegram/[td\_api.h](https://core.telegram.org/tdlib/docs/td__api_8h_source.html)