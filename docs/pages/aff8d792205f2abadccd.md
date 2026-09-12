# TDLib: sponsoredMessage Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes a sponsored message.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [message_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#a946f46ee90c465619214e056e4d91ce4) |
|  | Message identifier; unique for the chat to which the sponsored message belongs among both ordinary and sponsored messages. |
|  | |
| bool | [is_recommended_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#a6a892fa683cf5f179afc67b0a0f9f2a7) |
|  | True, if the message needs to be labeled as "recommended" instead of "sponsored". |
|  | |
| bool | [can_be_reported_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#a249bba2bdd2d041fcfd646df89cc2e16) |
|  | True, if the message can be reported to Telegram moderators through [reportChatSponsoredMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat_sponsored_message.html). |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageContent](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_content.html) > | [content_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#a0baa307e8b895334e20b3247b07103d6) |
|  | Content of the message. Currently, can be only of the types [messageText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_text.html), [messageAnimation](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_animation.html), [messagePhoto](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_photo.html), or [messageVideo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_video.html). Video messages can be viewed fullscreen. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [advertisementSponsor](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1advertisement_sponsor.html) > | [sponsor_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#aa716c8cf4f42e9622ad65ff0fd0fc72d) |
|  | Information about the sponsor of the message. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [title_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#ae49b8c94dab3e85761dd65876260deb9) |
|  | Title of the sponsored message. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [button_text_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#af6a36c2ef2ca564be926cd0256441130) |
|  | Text for the message action button. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [accent_color_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#afbb46ea2c6615c4f33f4251471f83f5e) |
|  | Identifier of the accent color for title, button text and message background. |
|  | |
| [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | [background_custom_emoji_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#aed33ded6defeed4fc21a9ae7b0601475) |
|  | Identifier of a custom emoji to be shown on the message background; 0 if none. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [additional_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#ae880f199b97a1170dd86963bf47e0eb7) |
|  | If non-empty, additional information about the sponsored message to be shown along with the message. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [sponsoredMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#a8f5ecc91c42fc5a1f8e2770988ea0f3a) () |
|  | |
|  | [sponsoredMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#a87dcfe4708bcc2f19227c9c2bcb6ffd3) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [message_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#a946f46ee90c465619214e056e4d91ce4), bool [is_recommended_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#a6a892fa683cf5f179afc67b0a0f9f2a7), bool [can_be_reported_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#a249bba2bdd2d041fcfd646df89cc2e16), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageContent](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_content.html) > &&[content_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#a0baa307e8b895334e20b3247b07103d6), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [advertisementSponsor](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1advertisement_sponsor.html) > &&[sponsor_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#aa716c8cf4f42e9622ad65ff0fd0fc72d), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[title_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#ae49b8c94dab3e85761dd65876260deb9), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[button_text_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#af6a36c2ef2ca564be926cd0256441130), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [accent_color_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#afbb46ea2c6615c4f33f4251471f83f5e), [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) [background_custom_emoji_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#aed33ded6defeed4fc21a9ae7b0601475), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[additional_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#ae880f199b97a1170dd86963bf47e0eb7)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1521782216 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#a8f5ecc91c42fc5a1f8e2770988ea0f3a)sponsoredMessage() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [sponsoredMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html) | ( |  | ) |  |

Describes a sponsored message.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#a87dcfe4708bcc2f19227c9c2bcb6ffd3)sponsoredMessage() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [sponsoredMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *message_id_*, |
|  |  | bool | *is_recommended_*, |
|  |  | bool | *can_be_reported_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageContent](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_content.html) > && | *content_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [advertisementSponsor](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1advertisement_sponsor.html) > && | *sponsor_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *title_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *button_text_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *accent_color_id_*, |
|  |  | [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | *background_custom_emoji_id_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *additional_info_* |
|  | ) |  |  |

Describes a sponsored message.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | message_id_ | Message identifier; unique for the chat to which the sponsored message belongs among both ordinary and sponsored messages. |
    | [in] | is_recommended_ | True, if the message needs to be labeled as "recommended" instead of "sponsored". |
    | [in] | can_be_reported_ | True, if the message can be reported to Telegram moderators through [reportChatSponsoredMessage](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1report_chat_sponsored_message.html). |
    | [in] | content_ | Content of the message. Currently, can be only of the types [messageText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_text.html), [messageAnimation](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_animation.html), [messagePhoto](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_photo.html), or [messageVideo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_video.html). Video messages can be viewed fullscreen. |
    | [in] | sponsor_ | Information about the sponsor of the message. |
    | [in] | title_ | Title of the sponsored message. |
    | [in] | button_text_ | Text for the message action button. |
    | [in] | accent_color_id_ | Identifier of the accent color for title, button text and message background. |
    | [in] | background_custom_emoji_id_ | Identifier of a custom emoji to be shown on the message background; 0 if none. |
    | [in] | additional_info_ | If non-empty, additional information about the sponsored message to be shown along with the message. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1sponsored_message.html#a8044dab2ba3c75066745014259c050c7)store()

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