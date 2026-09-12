# TDLib: message Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes a message.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ae1eaecac992cac27502334d1cc8bfd8a) |
|  | Message identifier; unique for the chat to which the message belongs. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > | [sender_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#aa4efedb303e2a085519405e8a018e184) |
|  | Identifier of the sender of the message. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Chat identifier. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSendingState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sending_state.html) > | [sending_state_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#accbb4f1c1aca998b5ec10e0a2e7e8f92) |
|  | The sending state of the message; may be null if the message isn't being sent and didn't fail to be sent. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSchedulingState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_scheduling_state.html) > | [scheduling_state_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a31a595cb539d928495a60f352cf8813a) |
|  | The scheduling state of the message; may be null if the message isn't scheduled. |
|  | |
| bool | [is_outgoing_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#af1fa053641f5a505dad2f81a168fdbe8) |
|  | True, if the message is outgoing. |
|  | |
| bool | [is_pinned_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ada3cbd9c3e89da9f894cd2f29725799d) |
|  | True, if the message is pinned. |
|  | |
| bool | [is_from_offline_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a7569eed6de11628c16a9bd30c617fb86) |
|  | True, if the message was sent because of a scheduled action by the message sender, for example, as away, or greeting service message. |
|  | |
| bool | [can_be_saved_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ae3c6abfc97d19936bb0f1ebbf19e15b2) |
|  | True, if content of the message can be saved locally. |
|  | |
| bool | [has_timestamped_media_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ad919989fe8d95e1a1ef8157bdc4918f6) |
|  | True, if media timestamp entities refers to a media in this message as opposed to a media in the replied message. |
|  | |
| bool | [is_channel_post_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#af7163adcfcbfe4e76be93fc406cbefa6) |
|  | True, if the message is a channel post. All messages to channels are channel posts, all other messages are not channel posts. |
|  | |
| bool | [is_paid_star_suggested_post_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#aa59bbae9b9de8a0818d803c3c6be7a4c) |
|  | True, if the message is a suggested channel post which was paid in Telegram Stars; a warning must be shown if the message is deleted in less than [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("suggested_post_lifetime_min") seconds after sending. |
|  | |
| bool | [is_paid_ton_suggested_post_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a628e1ed87c6b58ed7030bafd67dc9452) |
|  | True, if the message is a suggested channel post which was paid in Toncoins; a warning must be shown if the message is deleted in less than [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("suggested_post_lifetime_min") seconds after sending. |
|  | |
| bool | [contains_unread_mention_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#af65aa7d805c3ffc2e6b3f2a091250eff) |
|  | True, if the message contains an unread mention for the current user. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a003445033faa1e11b1d5e315b59d5e65) |
|  | Point in time (Unix timestamp) when the message was sent; 0 for scheduled messages. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [edit_date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a73880b9514e2e63e3511b5fb67975c85) |
|  | Point in time (Unix timestamp) when the message was last edited; 0 for scheduled messages. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [messageForwardInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_forward_info.html) > | [forward_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#aadd4f38730eddecb5d1284d70c8e27ba) |
|  | Information about the initial message sender; may be null if none or unknown. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [messageImportInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_import_info.html) > | [import_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a3e33511928eb839c48f0ef64c92d57a7) |
|  | Information about the initial message for messages created with [importMessages](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1import_messages.html); may be null if the message isn't imported. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [messageInteractionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_interaction_info.html) > | [interaction_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a6e70e19837857441e9ecd5a505655e8e) |
|  | Information about interactions with the message; may be null if none. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [unreadReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1unread_reaction.html) > > | [unread_reactions_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a79a73d4be55fe31d8bcbe372b5e03066) |
|  | Information about unread reactions added to the message. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [factCheck](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1fact_check.html) > | [fact_check_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a3f616859f4b3427d5469cda28c60ee81) |
|  | Information about fact-check added to the message; may be null if none. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [suggestedPostInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1suggested_post_info.html) > | [suggested_post_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ac7133a26df3cf6ca5e7e40afa87332e8) |
|  | Information about the suggested post; may be null if the message isn't a suggested post. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageReplyTo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_reply_to.html) > | [reply_to_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a0fa880b88cc45ead6ed2454e70c1cb98) |
|  | Information about the message or the story this message is replying to; may be null if none. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > | [topic_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#adf6e2906ee2f8b6a06150747aa41f7e0) |
|  | Identifier of the topic within the chat to which the message belongs; may be null if none; may change when the chat is converted to a forum or back. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSelfDestructType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_self_destruct_type.html) > | [self_destruct_type_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a30b79307f0ad983e2a8e01ac6c3eeabd) |
|  | The message's self-destruct type; may be null if none. |
|  | |
| double | [self_destruct_in_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ac3954f1acb7a56f583edbba792020191) |
|  | Time left before the message self-destruct timer expires, in seconds; 0 if self-destruction isn't scheduled yet. |
|  | |
| double | [auto_delete_in_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a30a94de0da5272ddd2876c341f202021) |
|  | Time left before the message will be automatically deleted by message_auto_delete_time setting of the chat, in seconds; 0 if never. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [via_bot_user_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a1cd697fb7c5f04c3e5779bdcff96829f) |
|  | If non-zero, the user identifier of the inline bot through which this message was sent. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [sender_business_bot_user_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ae81d56fefdb0db54e728a6537b4876f6) |
|  | If non-zero, the user identifier of the business bot that sent this message. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [sender_boost_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a12cc749bf5a4dba2971e39cdb9cba376) |
|  | Number of times the sender of the message boosted the supergroup at the time the message was sent; 0 if none or unknown. For messages sent by the current user, supergroupFullInfo.my_boost_count must be used instead. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [sender_tag_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a716b548040d0206ba34c28a83fb880ba) |
|  | Tag of the sender of the message in the supergroup at the time the message was sent; may be empty if none or unknown. For messages sent in basic groups or supergroup administrators, the current custom title or tag must be used instead. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [paid_message_star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ab000a89591b96c76c47a53b91c45755f) |
|  | The number of Telegram Stars the sender paid to send the message. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [author_signature_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#adab596c616a042fe957a271ef2c5d17e) |
|  | For channel posts and anonymous group messages, optional author signature. |
|  | |
| [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | [media_album_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#af0bd3a46ae4b528dfa155ad34eef0267) |
|  | Unique identifier of an album this message belongs to; 0 if none. Only audios, documents, photos and videos can be grouped together in albums. |
|  | |
| [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | [effect_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#aeb43b1badf8ef38f52582f4a66c77df9) |
|  | Unique identifier of the effect added to the message; 0 if none. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [restrictionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1restriction_info.html) > | [restriction_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a546a254a895e82fd74b4aeacc68def96) |
|  | Information about the restrictions that must be applied to the message content; may be null if none. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [summary_language_code_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a029eb909b87f8ef654c96500a2734d00) |
|  | IETF language tag of the message language on which it can be summarized; empty if summary isn't available for the message. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageContent](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_content.html) > | [content_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a0baa307e8b895334e20b3247b07103d6) |
|  | Content of the message. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReplyMarkup](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reply_markup.html) > | [reply_markup_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#aa660f2adb85f042b68f5bb3c0a96e336) |
|  | Reply markup for the message; may be null if none. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [message](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#aba502b8bb024cc38b45756fdf581f915) () |
|  | |
|  | [message](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a43beefdfb8e51e399b32ba6ef298b31f) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ae1eaecac992cac27502334d1cc8bfd8a), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > &&[sender_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#aa4efedb303e2a085519405e8a018e184), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#aa8a7803161092ff97e60d58707199e1f), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSendingState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sending_state.html) > &&[sending_state_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#accbb4f1c1aca998b5ec10e0a2e7e8f92), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSchedulingState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_scheduling_state.html) > &&[scheduling_state_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a31a595cb539d928495a60f352cf8813a), bool [is_outgoing_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#af1fa053641f5a505dad2f81a168fdbe8), bool [is_pinned_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ada3cbd9c3e89da9f894cd2f29725799d), bool [is_from_offline_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a7569eed6de11628c16a9bd30c617fb86), bool [can_be_saved_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ae3c6abfc97d19936bb0f1ebbf19e15b2), bool [has_timestamped_media_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ad919989fe8d95e1a1ef8157bdc4918f6), bool [is_channel_post_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#af7163adcfcbfe4e76be93fc406cbefa6), bool [is_paid_star_suggested_post_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#aa59bbae9b9de8a0818d803c3c6be7a4c), bool [is_paid_ton_suggested_post_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a628e1ed87c6b58ed7030bafd67dc9452), bool [contains_unread_mention_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#af65aa7d805c3ffc2e6b3f2a091250eff), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a003445033faa1e11b1d5e315b59d5e65), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [edit_date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a73880b9514e2e63e3511b5fb67975c85), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [messageForwardInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_forward_info.html) > &&[forward_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#aadd4f38730eddecb5d1284d70c8e27ba), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [messageImportInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_import_info.html) > &&[import_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a3e33511928eb839c48f0ef64c92d57a7), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [messageInteractionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_interaction_info.html) > &&[interaction_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a6e70e19837857441e9ecd5a505655e8e), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [unreadReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1unread_reaction.html) >> &&[unread_reactions_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a79a73d4be55fe31d8bcbe372b5e03066), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [factCheck](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1fact_check.html) > &&[fact_check_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a3f616859f4b3427d5469cda28c60ee81), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [suggestedPostInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1suggested_post_info.html) > &&[suggested_post_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ac7133a26df3cf6ca5e7e40afa87332e8), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageReplyTo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_reply_to.html) > &&[reply_to_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a0fa880b88cc45ead6ed2454e70c1cb98), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > &&[topic_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#adf6e2906ee2f8b6a06150747aa41f7e0), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSelfDestructType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_self_destruct_type.html) > &&[self_destruct_type_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a30b79307f0ad983e2a8e01ac6c3eeabd), double [self_destruct_in_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ac3954f1acb7a56f583edbba792020191), double [auto_delete_in_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a30a94de0da5272ddd2876c341f202021), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [via_bot_user_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a1cd697fb7c5f04c3e5779bdcff96829f), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [sender_business_bot_user_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ae81d56fefdb0db54e728a6537b4876f6), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [sender_boost_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a12cc749bf5a4dba2971e39cdb9cba376), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[sender_tag_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a716b548040d0206ba34c28a83fb880ba), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [paid_message_star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ab000a89591b96c76c47a53b91c45755f), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[author_signature_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#adab596c616a042fe957a271ef2c5d17e), [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) [media_album_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#af0bd3a46ae4b528dfa155ad34eef0267), [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) [effect_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#aeb43b1badf8ef38f52582f4a66c77df9), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [restrictionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1restriction_info.html) > &&[restriction_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a546a254a895e82fd74b4aeacc68def96), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[summary_language_code_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a029eb909b87f8ef654c96500a2734d00), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageContent](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_content.html) > &&[content_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a0baa307e8b895334e20b3247b07103d6), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReplyMarkup](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reply_markup.html) > &&[reply_markup_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#aa660f2adb85f042b68f5bb3c0a96e336)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 284850729 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#aba502b8bb024cc38b45756fdf581f915)message() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [message](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html) | ( |  | ) |  |

Describes a message.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a43beefdfb8e51e399b32ba6ef298b31f)message() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [message](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *id_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > && | *sender_id_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat_id_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSendingState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sending_state.html) > && | *sending_state_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSchedulingState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_scheduling_state.html) > && | *scheduling_state_*, |
|  |  | bool | *is_outgoing_*, |
|  |  | bool | *is_pinned_*, |
|  |  | bool | *is_from_offline_*, |
|  |  | bool | *can_be_saved_*, |
|  |  | bool | *has_timestamped_media_*, |
|  |  | bool | *is_channel_post_*, |
|  |  | bool | *is_paid_star_suggested_post_*, |
|  |  | bool | *is_paid_ton_suggested_post_*, |
|  |  | bool | *contains_unread_mention_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *date_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *edit_date_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [messageForwardInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_forward_info.html) > && | *forward_info_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [messageImportInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_import_info.html) > && | *import_info_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [messageInteractionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_interaction_info.html) > && | *interaction_info_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [unreadReaction](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1unread_reaction.html) >> && | *unread_reactions_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [factCheck](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1fact_check.html) > && | *fact_check_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [suggestedPostInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1suggested_post_info.html) > && | *suggested_post_info_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageReplyTo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_reply_to.html) > && | *reply_to_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageTopic](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_topic.html) > && | *topic_id_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSelfDestructType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_self_destruct_type.html) > && | *self_destruct_type_*, |
|  |  | double | *self_destruct_in_*, |
|  |  | double | *auto_delete_in_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *via_bot_user_id_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *sender_business_bot_user_id_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *sender_boost_count_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *sender_tag_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *paid_message_star_count_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *author_signature_*, |
|  |  | [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | *media_album_id_*, |
|  |  | [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | *effect_id_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [restrictionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1restriction_info.html) > && | *restriction_info_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *summary_language_code_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageContent](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_content.html) > && | *content_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ReplyMarkup](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_reply_markup.html) > && | *reply_markup_* |
|  | ) |  |  |

Describes a message.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | id_ | Message identifier; unique for the chat to which the message belongs. |
    | [in] | sender_id_ | Identifier of the sender of the message. |
    | [in] | chat_id_ | Chat identifier. |
    | [in] | sending_state_ | The sending state of the message; may be null if the message isn't being sent and didn't fail to be sent. |
    | [in] | scheduling_state_ | The scheduling state of the message; may be null if the message isn't scheduled. |
    | [in] | is_outgoing_ | True, if the message is outgoing. |
    | [in] | is_pinned_ | True, if the message is pinned. |
    | [in] | is_from_offline_ | True, if the message was sent because of a scheduled action by the message sender, for example, as away, or greeting service message. |
    | [in] | can_be_saved_ | True, if content of the message can be saved locally. |
    | [in] | has_timestamped_media_ | True, if media timestamp entities refers to a media in this message as opposed to a media in the replied message. |
    | [in] | is_channel_post_ | True, if the message is a channel post. All messages to channels are channel posts, all other messages are not channel posts. |
    | [in] | is_paid_star_suggested_post_ | True, if the message is a suggested channel post which was paid in Telegram Stars; a warning must be shown if the message is deleted in less than [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("suggested_post_lifetime_min") seconds after sending. |
    | [in] | is_paid_ton_suggested_post_ | True, if the message is a suggested channel post which was paid in Toncoins; a warning must be shown if the message is deleted in less than [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("suggested_post_lifetime_min") seconds after sending. |
    | [in] | contains_unread_mention_ | True, if the message contains an unread mention for the current user. |
    | [in] | date_ | Point in time (Unix timestamp) when the message was sent; 0 for scheduled messages. |
    | [in] | edit_date_ | Point in time (Unix timestamp) when the message was last edited; 0 for scheduled messages. |
    | [in] | forward_info_ | Information about the initial message sender; may be null if none or unknown. |
    | [in] | import_info_ | Information about the initial message for messages created with [importMessages](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1import_messages.html); may be null if the message isn't imported. |
    | [in] | interaction_info_ | Information about interactions with the message; may be null if none. |
    | [in] | unread_reactions_ | Information about unread reactions added to the message. |
    | [in] | fact_check_ | Information about fact-check added to the message; may be null if none. |
    | [in] | suggested_post_info_ | Information about the suggested post; may be null if the message isn't a suggested post. |
    | [in] | reply_to_ | Information about the message or the story this message is replying to; may be null if none. |
    | [in] | topic_id_ | Identifier of the topic within the chat to which the message belongs; may be null if none; may change when the chat is converted to a forum or back. |
    | [in] | self_destruct_type_ | The message's self-destruct type; may be null if none. |
    | [in] | self_destruct_in_ | Time left before the message self-destruct timer expires, in seconds; 0 if self-destruction isn't scheduled yet. |
    | [in] | auto_delete_in_ | Time left before the message will be automatically deleted by message_auto_delete_time setting of the chat, in seconds; 0 if never. |
    | [in] | via_bot_user_id_ | If non-zero, the user identifier of the inline bot through which this message was sent. |
    | [in] | sender_business_bot_user_id_ | If non-zero, the user identifier of the business bot that sent this message. |
    | [in] | sender_boost_count_ | Number of times the sender of the message boosted the supergroup at the time the message was sent; 0 if none or unknown. For messages sent by the current user, supergroupFullInfo.my_boost_count must be used instead. |
    | [in] | sender_tag_ | Tag of the sender of the message in the supergroup at the time the message was sent; may be empty if none or unknown. For messages sent in basic groups or supergroup administrators, the current custom title or tag must be used instead. |
    | [in] | paid_message_star_count_ | The number of Telegram Stars the sender paid to send the message. |
    | [in] | author_signature_ | For channel posts and anonymous group messages, optional author signature. |
    | [in] | media_album_id_ | Unique identifier of an album this message belongs to; 0 if none. Only audios, documents, photos and videos can be grouped together in albums. |
    | [in] | effect_id_ | Unique identifier of the effect added to the message; 0 if none. |
    | [in] | restriction_info_ | Information about the restrictions that must be applied to the message content; may be null if none. |
    | [in] | summary_language_code_ | IETF language tag of the message language on which it can be summarized; empty if summary isn't available for the message. |
    | [in] | content_ | Content of the message. |
    | [in] | reply_markup_ | Reply markup for the message; may be null if none. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html#a8044dab2ba3c75066745014259c050c7)store()

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