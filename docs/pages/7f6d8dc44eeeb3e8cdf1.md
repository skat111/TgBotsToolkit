# TDLib: inputMessageAnimation Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html

Inherits [InputMessageContent](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_message_content.html).

## Description

An animation message (GIF-style).

|  |  |
| --- | --- |
| Public Fields | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputFile](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_file.html) > | [animation_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#aafb963d46c45b478f627d5d4209a2937) |
|  | Animation file to be sent. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [inputThumbnail](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_thumbnail.html) > | [thumbnail_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#a9ef9afaa278fe91f763bbcb79d80f4ba) |
|  | Animation thumbnail; pass null to skip thumbnail uploading. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > | [added_sticker_file_ids_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#ab3e99358921691b38509e54cb63fdd1c) |
|  | File identifiers of the stickers added to the animation, if applicable. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [duration_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#a3567eba0049c4d85b34b7183207ca1bf) |
|  | Duration of the animation, in seconds. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [width_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#ac36a96daaa63a9706f54c0a4fbf8fff3) |
|  | Width of the animation; may be replaced by the server. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [height_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#aebff872d03cf6a5c75c5156d148dbe28) |
|  | Height of the animation; may be replaced by the server. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > | [caption_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#a08705c09fec60dac112d4935015895af) |
|  | Animation caption; pass null to use an empty caption; 0-[getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("message_caption_length_max") characters. |
|  | |
| bool | [show_caption_above_media_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#a23420332e42ccf007c59ffd02df37f4e) |
|  | True, if the caption must be shown above the animation; otherwise, the caption must be shown below the animation; not supported in secret chats. |
|  | |
| bool | [has_spoiler_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#a1c3a7faba5317bc5e19eb15bd17a697e) |
|  | True, if the animation preview must be covered by a spoiler animation; not supported in secret chats. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [inputMessageAnimation](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#a31f014971bd6e6726e46ae0edf80d3bc) () |
|  | |
|  | [inputMessageAnimation](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#ad267474f077fe148171cb79b2030e4f6) ([object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputFile](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_file.html) > &&[animation_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#aafb963d46c45b478f627d5d4209a2937), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [inputThumbnail](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_thumbnail.html) > &&[thumbnail_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#a9ef9afaa278fe91f763bbcb79d80f4ba), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > &&[added_sticker_file_ids_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#ab3e99358921691b38509e54cb63fdd1c), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [duration_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#a3567eba0049c4d85b34b7183207ca1bf), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [width_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#ac36a96daaa63a9706f54c0a4fbf8fff3), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [height_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#aebff872d03cf6a5c75c5156d148dbe28), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > &&[caption_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#a08705c09fec60dac112d4935015895af), bool [show_caption_above_media_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#a23420332e42ccf007c59ffd02df37f4e), bool [has_spoiler_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#a1c3a7faba5317bc5e19eb15bd17a697e)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -210404059 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#a31f014971bd6e6726e46ae0edf80d3bc)inputMessageAnimation() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [inputMessageAnimation](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html) | ( |  | ) |  |

An animation message (GIF-style).

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#ad267474f077fe148171cb79b2030e4f6)inputMessageAnimation() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [inputMessageAnimation](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html) | ( | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [InputFile](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_input_file.html) > && | *animation_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [inputThumbnail](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_thumbnail.html) > && | *thumbnail_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > && | *added_sticker_file_ids_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *duration_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *width_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *height_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > && | *caption_*, |
|  |  | bool | *show_caption_above_media_*, |
|  |  | bool | *has_spoiler_* |
|  | ) |  |  |

An animation message (GIF-style).

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | animation_ | Animation file to be sent. |
    | [in] | thumbnail_ | Animation thumbnail; pass null to skip thumbnail uploading. |
    | [in] | added_sticker_file_ids_ | File identifiers of the stickers added to the animation, if applicable. |
    | [in] | duration_ | Duration of the animation, in seconds. |
    | [in] | width_ | Width of the animation; may be replaced by the server. |
    | [in] | height_ | Height of the animation; may be replaced by the server. |
    | [in] | caption_ | Animation caption; pass null to use an empty caption; 0-[getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("message_caption_length_max") characters. |
    | [in] | show_caption_above_media_ | True, if the caption must be shown above the animation; otherwise, the caption must be shown below the animation; not supported in secret chats. |
    | [in] | has_spoiler_ | True, if the animation preview must be covered by a spoiler animation; not supported in secret chats. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1input_message_animation.html#a8044dab2ba3c75066745014259c050c7)store()

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