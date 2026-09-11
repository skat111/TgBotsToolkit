# TDLib: userFullInfo Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Contains full information about a user.

|  |  |
| --- | --- |
| Public Fields | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [chatPhoto](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_photo.html) > | [personal\_photo\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#ac7780a9743c6056a6a5fb1a8d3516580) |
|  | User profile photo set by the current user for the contact; may be null. If null and user.profile\_photo is null, then the photo is empty; otherwise, it is unknown. If non-null, then it is the same photo as in user.profile\_photo and chat.photo. This photo isn't returned in the list of user photos. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [chatPhoto](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_photo.html) > | [photo\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#aabefbf5dc83795382e2b6bf1ded1e2ac) |
|  | User profile photo; may be null. If null and user.profile\_photo is null, then the photo is empty; otherwise, it is unknown. If non-null and personal\_photo is null, then it is the same photo as in user.profile\_photo and chat.photo. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [chatPhoto](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_photo.html) > | [public\_photo\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a3f738e672014396e3385c66a6f1afd70) |
|  | User profile photo visible if the main photo is hidden by privacy settings; may be null. If null and user.profile\_photo is null, then the photo is empty; otherwise, it is unknown. If non-null and both photo and personal\_photo are null, then it is the same photo as in user.profile\_photo and chat.photo. This photo isn't returned in the list of user photos. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [BlockList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_block_list.html) > | [block\_list\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a6c204c912ab0ecb43b85ea2e033b89cf) |
|  | Block list to which the user is added; may be null if none. |
|  | |
| bool | [can\_be\_called\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a0695b6b93c34a2309e349dbe44ae3833) |
|  | True, if the user can be called. |
|  | |
| bool | [supports\_video\_calls\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a91d8ad0c50502d57f97fb4c1490b8e1f) |
|  | True, if a video call can be created with the user. |
|  | |
| bool | [has\_private\_calls\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a9b228334284f23134bbb3e6afcd64fff) |
|  | True, if the user can't be called due to their privacy settings. |
|  | |
| bool | [has\_private\_forwards\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a78e7981880c822b18c35ed756ca982aa) |
|  | True, if the user can't be linked in forwarded messages due to their privacy settings. |
|  | |
| bool | [has\_restricted\_voice\_and\_video\_note\_messages\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#afd3e1270876dca9356bf88c1e9a76f0d) |
|  | True, if voice and video notes can't be sent or forwarded to the user. |
|  | |
| bool | [has\_posted\_to\_profile\_stories\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a9e32d83cd6148518a9db0251a5b825dc) |
|  | True, if the user has posted to profile stories. |
|  | |
| bool | [has\_sponsored\_messages\_enabled\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#ad575905a8f3504933ac8a7a3d06d0e0f) |
|  | True, if the user always enabled sponsored messages; known only for the current user. |
|  | |
| bool | [need\_phone\_number\_privacy\_exception\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#aac68c60783c2797b69ed296934034d32) |
|  | True, if the current user needs to explicitly allow to share their phone number with the user when the method [addContact](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_contact.html) is used. |
|  | |
| bool | [set\_chat\_background\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#aa7612566ff7af5d300ac4828c9df75f0) |
|  | True, if the user set chat background for both chat users and it wasn't reverted yet. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > | [bio\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a0e7ef9d5190badba8aa525aaac5fa6c0) |
|  | A short user bio; may be null for bots. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [birthdate](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1birthdate.html) > | [birthdate\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a5fe2c39d3c9714f53d985d648fa1932f) |
|  | Birthdate of the user; may be null if unknown. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [personal\_chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a94182133475748b410c941eab3ce5a8c) |
|  | Identifier of the personal chat of the user; 0 if none. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [gift\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#af45c11f20ed5a094793bd02984eeeab6) |
|  | Number of saved to profile gifts for other users or the total number of received gifts for the current user. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [group\_in\_common\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a32d901c751a6bfeabe23b6c5d8dac7fe) |
|  | Number of group chats where both the other user and the current user are a member; 0 for the current user. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [incoming\_paid\_message\_star\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#ab4754eeaa5e16e633a735b22b10ba07f) |
|  | Number of Telegram Stars that must be paid by the user for each sent message to the current user. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [outgoing\_paid\_message\_star\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a91bbd63f55ca7c13f47b883f0963adba) |
|  | Number of Telegram Stars that must be paid by the current user for each sent message to the user. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [giftSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html) > | [gift\_settings\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#aced8bc8dea2970dccc0e3b0c344bf9ea) |
|  | Settings for gift receiving for the user. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [botVerification](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_verification.html) > | [bot\_verification\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#aa1b971c7184b5caca06b36b9180a7c75) |
|  | Information about verification status of the user provided by a bot; may be null if none or unknown. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ProfileTab](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_profile_tab.html) > | [main\_profile\_tab\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a4fd35ee71cf02bcc27a29191b72d265c) |
|  | The main tab chosen by the user; may be null if not chosen manually. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [audio](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1audio.html) > | [first\_profile\_audio\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a02030850a133b0427d15ef417d48706b) |
|  | The first audio file added to the user's profile; may be null if none. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [userRating](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_rating.html) > | [rating\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a319c2fe31e75ae377117ab955bc6a6de) |
|  | The current rating of the user; may be null if none. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [userRating](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_rating.html) > | [pending\_rating\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#aa853d7a4e45f1d3a52f3bddd100a6275) |
|  | The rating of the user after the next change; may be null if the user isn't the current user or there are no pending rating changes. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [pending\_rating\_date\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a5c952e221835fb118169917f87244e36) |
|  | Unix timestamp when rating of the user will change to pending\_rating; 0 if the user isn't the current user or there are no pending rating changes. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > | [note\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a364a2582c68ee504231d2a01bbfd1f59) |
|  | Note added to the user's contact; may be null if none. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [businessInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_info.html) > | [business\_info\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a628850d367d853b88cc43b81465be7e3) |
|  | Information about business settings for Telegram Business accounts; may be null if none. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [botInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_info.html) > | [bot\_info\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#af3f5137d09c18460d5627889b746711e) |
|  | For bots, information about the bot; may be null if the user isn't a bot. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [userFullInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a286771810ddabd516717c7096256738d) () |
|  | |
|  | [userFullInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#adf566f03aaf614e4ff38ef12b5b1480c) ([object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [chatPhoto](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_photo.html) > &&[personal\_photo\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#ac7780a9743c6056a6a5fb1a8d3516580), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [chatPhoto](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_photo.html) > &&[photo\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#aabefbf5dc83795382e2b6bf1ded1e2ac), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [chatPhoto](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_photo.html) > &&[public\_photo\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a3f738e672014396e3385c66a6f1afd70), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [BlockList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_block_list.html) > &&[block\_list\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a6c204c912ab0ecb43b85ea2e033b89cf), bool [can\_be\_called\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a0695b6b93c34a2309e349dbe44ae3833), bool [supports\_video\_calls\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a91d8ad0c50502d57f97fb4c1490b8e1f), bool [has\_private\_calls\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a9b228334284f23134bbb3e6afcd64fff), bool [has\_private\_forwards\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a78e7981880c822b18c35ed756ca982aa), bool [has\_restricted\_voice\_and\_video\_note\_messages\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#afd3e1270876dca9356bf88c1e9a76f0d), bool [has\_posted\_to\_profile\_stories\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a9e32d83cd6148518a9db0251a5b825dc), bool [has\_sponsored\_messages\_enabled\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#ad575905a8f3504933ac8a7a3d06d0e0f), bool [need\_phone\_number\_privacy\_exception\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#aac68c60783c2797b69ed296934034d32), bool [set\_chat\_background\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#aa7612566ff7af5d300ac4828c9df75f0), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > &&[bio\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a0e7ef9d5190badba8aa525aaac5fa6c0), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [birthdate](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1birthdate.html) > &&[birthdate\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a5fe2c39d3c9714f53d985d648fa1932f), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [personal\_chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a94182133475748b410c941eab3ce5a8c), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [gift\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#af45c11f20ed5a094793bd02984eeeab6), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [group\_in\_common\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a32d901c751a6bfeabe23b6c5d8dac7fe), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [incoming\_paid\_message\_star\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#ab4754eeaa5e16e633a735b22b10ba07f), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [outgoing\_paid\_message\_star\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a91bbd63f55ca7c13f47b883f0963adba), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [giftSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html) > &&[gift\_settings\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#aced8bc8dea2970dccc0e3b0c344bf9ea), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [botVerification](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_verification.html) > &&[bot\_verification\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#aa1b971c7184b5caca06b36b9180a7c75), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ProfileTab](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_profile_tab.html) > &&[main\_profile\_tab\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a4fd35ee71cf02bcc27a29191b72d265c), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [audio](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1audio.html) > &&[first\_profile\_audio\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a02030850a133b0427d15ef417d48706b), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [userRating](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_rating.html) > &&[rating\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a319c2fe31e75ae377117ab955bc6a6de), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [userRating](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_rating.html) > &&[pending\_rating\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#aa853d7a4e45f1d3a52f3bddd100a6275), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [pending\_rating\_date\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a5c952e221835fb118169917f87244e36), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > &&[note\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a364a2582c68ee504231d2a01bbfd1f59), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [businessInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_info.html) > &&[business\_info\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a628850d367d853b88cc43b81465be7e3), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [botInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_info.html) > &&[bot\_info\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#af3f5137d09c18460d5627889b746711e)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 2128551190 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a286771810ddabd516717c7096256738d)userFullInfo() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [userFullInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html) | ( |  | ) |  |

Contains full information about a user.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#adf566f03aaf614e4ff38ef12b5b1480c)userFullInfo() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [userFullInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html) | ( | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [chatPhoto](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_photo.html) > && | *personal\_photo\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [chatPhoto](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_photo.html) > && | *photo\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [chatPhoto](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_photo.html) > && | *public\_photo\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [BlockList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_block_list.html) > && | *block\_list\_*, |
|  |  | bool | *can\_be\_called\_*, |
|  |  | bool | *supports\_video\_calls\_*, |
|  |  | bool | *has\_private\_calls\_*, |
|  |  | bool | *has\_private\_forwards\_*, |
|  |  | bool | *has\_restricted\_voice\_and\_video\_note\_messages\_*, |
|  |  | bool | *has\_posted\_to\_profile\_stories\_*, |
|  |  | bool | *has\_sponsored\_messages\_enabled\_*, |
|  |  | bool | *need\_phone\_number\_privacy\_exception\_*, |
|  |  | bool | *set\_chat\_background\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > && | *bio\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [birthdate](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1birthdate.html) > && | *birthdate\_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *personal\_chat\_id\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *gift\_count\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *group\_in\_common\_count\_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *incoming\_paid\_message\_star\_count\_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *outgoing\_paid\_message\_star\_count\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [giftSettings](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1gift_settings.html) > && | *gift\_settings\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [botVerification](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_verification.html) > && | *bot\_verification\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ProfileTab](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_profile_tab.html) > && | *main\_profile\_tab\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [audio](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1audio.html) > && | *first\_profile\_audio\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [userRating](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_rating.html) > && | *rating\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [userRating](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_rating.html) > && | *pending\_rating\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *pending\_rating\_date\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > && | *note\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [businessInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1business_info.html) > && | *business\_info\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [botInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1bot_info.html) > && | *bot\_info\_* |
|  | ) |  |  |

Contains full information about a user.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | personal\_photo\_ | User profile photo set by the current user for the contact; may be null. If null and user.profile\_photo is null, then the photo is empty; otherwise, it is unknown. If non-null, then it is the same photo as in user.profile\_photo and chat.photo. This photo isn't returned in the list of user photos. |
    | [in] | photo\_ | User profile photo; may be null. If null and user.profile\_photo is null, then the photo is empty; otherwise, it is unknown. If non-null and personal\_photo is null, then it is the same photo as in user.profile\_photo and chat.photo. |
    | [in] | public\_photo\_ | User profile photo visible if the main photo is hidden by privacy settings; may be null. If null and user.profile\_photo is null, then the photo is empty; otherwise, it is unknown. If non-null and both photo and personal\_photo are null, then it is the same photo as in user.profile\_photo and chat.photo. This photo isn't returned in the list of user photos. |
    | [in] | block\_list\_ | Block list to which the user is added; may be null if none. |
    | [in] | can\_be\_called\_ | True, if the user can be called. |
    | [in] | supports\_video\_calls\_ | True, if a video call can be created with the user. |
    | [in] | has\_private\_calls\_ | True, if the user can't be called due to their privacy settings. |
    | [in] | has\_private\_forwards\_ | True, if the user can't be linked in forwarded messages due to their privacy settings. |
    | [in] | has\_restricted\_voice\_and\_video\_note\_messages\_ | True, if voice and video notes can't be sent or forwarded to the user. |
    | [in] | has\_posted\_to\_profile\_stories\_ | True, if the user has posted to profile stories. |
    | [in] | has\_sponsored\_messages\_enabled\_ | True, if the user always enabled sponsored messages; known only for the current user. |
    | [in] | need\_phone\_number\_privacy\_exception\_ | True, if the current user needs to explicitly allow to share their phone number with the user when the method [addContact](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1add_contact.html) is used. |
    | [in] | set\_chat\_background\_ | True, if the user set chat background for both chat users and it wasn't reverted yet. |
    | [in] | bio\_ | A short user bio; may be null for bots. |
    | [in] | birthdate\_ | Birthdate of the user; may be null if unknown. |
    | [in] | personal\_chat\_id\_ | Identifier of the personal chat of the user; 0 if none. |
    | [in] | gift\_count\_ | Number of saved to profile gifts for other users or the total number of received gifts for the current user. |
    | [in] | group\_in\_common\_count\_ | Number of group chats where both the other user and the current user are a member; 0 for the current user. |
    | [in] | incoming\_paid\_message\_star\_count\_ | Number of Telegram Stars that must be paid by the user for each sent message to the current user. |
    | [in] | outgoing\_paid\_message\_star\_count\_ | Number of Telegram Stars that must be paid by the current user for each sent message to the user. |
    | [in] | gift\_settings\_ | Settings for gift receiving for the user. |
    | [in] | bot\_verification\_ | Information about verification status of the user provided by a bot; may be null if none or unknown. |
    | [in] | main\_profile\_tab\_ | The main tab chosen by the user; may be null if not chosen manually. |
    | [in] | first\_profile\_audio\_ | The first audio file added to the user's profile; may be null if none. |
    | [in] | rating\_ | The current rating of the user; may be null if none. |
    | [in] | pending\_rating\_ | The rating of the user after the next change; may be null if the user isn't the current user or there are no pending rating changes. |
    | [in] | pending\_rating\_date\_ | Unix timestamp when rating of the user will change to pending\_rating; 0 if the user isn't the current user or there are no pending rating changes. |
    | [in] | note\_ | Note added to the user's contact; may be null if none. |
    | [in] | business\_info\_ | Information about business settings for Telegram Business accounts; may be null if none. |
    | [in] | bot\_info\_ | For bots, information about the bot; may be null if the user isn't a bot. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html#a8044dab2ba3c75066745014259c050c7)store()

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