# TDLib: getUserPrivacySettingRules Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Returns the current privacy settings.

Returns object\_ptr<UserPrivacySettingRules>.

|  |  |
| --- | --- |
| Public Fields | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [UserPrivacySetting](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_user_privacy_setting.html) > | [setting\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html#ae68e5852765ab8a683d1cb9fc6927931) |
|  | The privacy setting. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html#a7b697b92376c06b34103a4f4eea3c9f4) = [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [userPrivacySettingRules](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_privacy_setting_rules.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [getUserPrivacySettingRules](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html#ac5514994c8e7b36c9e1bbedb3ed27830) () |
|  | |
|  | [getUserPrivacySettingRules](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html#a85512e454d0eebda3129549686be9734) ([object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [UserPrivacySetting](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_user_privacy_setting.html) > &&[setting\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html#ae68e5852765ab8a683d1cb9fc6927931)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -2077223311 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html#ac5514994c8e7b36c9e1bbedb3ed27830)getUserPrivacySettingRules() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [getUserPrivacySettingRules](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html) | ( |  | ) |  |

Default constructor for a function, which returns the current privacy settings.

Returns object\_ptr<UserPrivacySettingRules>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html#a85512e454d0eebda3129549686be9734)getUserPrivacySettingRules() [2/2]

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [getUserPrivacySettingRules](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html) | ( | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [UserPrivacySetting](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_user_privacy_setting.html) > && | *setting\_* | ) |  | | explicit |

Creates a function, which returns the current privacy settings.

Returns object\_ptr<UserPrivacySettingRules>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | setting\_ | The privacy setting. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html#a8044dab2ba3c75066745014259c050c7)store()

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