# TDLib: supergroup Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Represents a supergroup or channel with zero or more members (subscribers in the case of channels). From the point of view of the system, a channel is a special kind of a supergroup: only administrators can post and see the list of members, and posts from all administrators use the name and photo of the channel instead of individual names and profile photos. Unlike supergroups, channels can have an unlimited number of subscribers.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#ae1eaecac992cac27502334d1cc8bfd8a) |
|  | Supergroup or channel identifier. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [usernames](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1usernames.html) > | [usernames_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#aa6c60205e4a7f459a69c39a491125eda) |
|  | Usernames of the supergroup or channel; may be null. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a003445033faa1e11b1d5e315b59d5e65) |
|  | Point in time (Unix timestamp) when the current user joined, or the point in time when the supergroup or channel was created, in case the user is not a member. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ChatMemberStatus](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_chat_member_status.html) > | [status_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#ae12958c3bb1acc2238bdd55cf3ef8fcf) |
|  | Status of the current user in the supergroup or channel. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [member_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#afb74b89584e6d98dcd5c460fecd6e456) |
|  | Number of members in the supergroup or channel; 0 if unknown. Currently, it is guaranteed to be known only if the supergroup or channel was received through [getChatSimilarChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_similar_chats.html), [getChatsToPostStories](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats_to_post_stories.html), [getCreatedPublicChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_created_public_chats.html), [getGroupsInCommon](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_groups_in_common.html), [getInactiveSupergroupChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_inactive_supergroup_chats.html), [getRecommendedChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_recommended_chats.html), [getSuitableDiscussionChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_suitable_discussion_chats.html), [getUserPrivacySettingRules](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html), [getVideoChatAvailableParticipants](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_video_chat_available_participants.html), [searchPublicChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_public_chats.html), or in chatFolderInviteLinkInfo.missing_chat_ids, or in userFullInfo.personal_chat_id, or for chats with messages or stories from [publicForwards](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1public_forwards.html) and [foundStories](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1found_stories.html). |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [boost_level_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a593c9b0ecab2e66deaeb410153649414) |
|  | Approximate boost level for the chat. |
|  | |
| bool | [has_automatic_translation_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#ac80ecac5ed0a7c6609b266e6c9dcd512) |
|  | True, if automatic translation of messages is enabled in the channel. |
|  | |
| bool | [has_linked_chat_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a272fcaa35af7d09b97269e55192764db) |
|  | True, if the channel has a discussion group, or the supergroup is the designated discussion group for a channel. |
|  | |
| bool | [has_location_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#aa1ec1d684a50df3ca41bdbdd8a9e236d) |
|  | True, if the supergroup is connected to a location, i.e. the supergroup is a location-based supergroup. |
|  | |
| bool | [sign_messages_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#aed283c3fe4d9f4db55f904586ac59786) |
|  | True, if messages sent to the channel contains name of the sender. This field is only applicable to channels. |
|  | |
| bool | [show_message_sender_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a27ee8537ec772ce8d7ee28d216900d26) |
|  | True, if messages sent to the channel have information about the sender user. This field is only applicable to channels. |
|  | |
| bool | [join_to_send_messages_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a5fc65e27dac49cd7f0d364dd8348914a) |
|  | True, if users need to join the supergroup before they can send messages. May be false only for discussion supergroups and channel direct messages groups. |
|  | |
| bool | [join_by_request_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a9467e716be54f53071d24722a23aaf61) |
|  | True, if all users directly joining the supergroup need to be approved by supergroup administrators. May be true only for non-broadcast supergroups with username, location, or a linked chat. |
|  | |
| bool | [is_slow_mode_enabled_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#abaccd7272930ee8a4a0f8463681ca9c8) |
|  | True, if the slow mode is enabled in the supergroup. |
|  | |
| bool | [is_channel_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a03c3ef88b91f79e111f3f015657a06e8) |
|  | True, if the supergroup is a channel. |
|  | |
| bool | [is_broadcast_group_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a8c4a5114a53bf6159274fcfb0b695ee5) |
|  | True, if the supergroup is a broadcast group, i.e. only administrators can send messages and there is no limit on the number of members. |
|  | |
| bool | [is_forum_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a5cc2f692df786d353dabf2a0b978ab7b) |
|  | True, if the supergroup is a forum with topics. |
|  | |
| bool | [is_direct_messages_group_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a15584a2b9155aae7fff26e796fc6157c) |
|  | True, if the supergroup is a direct message group for a channel chat. |
|  | |
| bool | [is_administered_direct_messages_group_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#aae758601e8748f3a6bc1e85966dea22f) |
|  | True, if the supergroup is a direct messages group for a channel chat that is administered by the current user. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [verificationStatus](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1verification_status.html) > | [verification_status_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a19b93695acd570fd7c5c480955dac459) |
|  | Information about verification status of the supergroup or channel; may be null if none. |
|  | |
| bool | [has_direct_messages_group_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#ab73e27694d21b5182d8d10698dbc2994) |
|  | True, if the channel has direct messages group. |
|  | |
| bool | [has_forum_tabs_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#ab8d4622af607ab2cd7925fc71b46a941) |
|  | True, if the supergroup is a forum, which topics are shown in the same way as in channel direct messages groups. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [restrictionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1restriction_info.html) > | [restriction_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a546a254a895e82fd74b4aeacc68def96) |
|  | Information about the restrictions that must be applied to the corresponding supergroup or channel chat; may be null if none. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [paid_message_star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#ab000a89591b96c76c47a53b91c45755f) |
|  | Number of Telegram Stars that must be paid by non-administrator users of the supergroup chat for each sent message. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ActiveStoryState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_active_story_state.html) > | [active_story_state_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a38567b5fb62090751615b02f5db86afa) |
|  | State of active stories of the supergroup or channel; may be null if there are no active stories. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [supergroup](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a96af64304e0c06b829ff4ce564ac9325) () |
|  | |
|  | [supergroup](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#aebdc22aeb823393591ab1a7252964599) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#ae1eaecac992cac27502334d1cc8bfd8a), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [usernames](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1usernames.html) > &&[usernames_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#aa6c60205e4a7f459a69c39a491125eda), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a003445033faa1e11b1d5e315b59d5e65), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ChatMemberStatus](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_chat_member_status.html) > &&[status_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#ae12958c3bb1acc2238bdd55cf3ef8fcf), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [member_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#afb74b89584e6d98dcd5c460fecd6e456), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [boost_level_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a593c9b0ecab2e66deaeb410153649414), bool [has_automatic_translation_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#ac80ecac5ed0a7c6609b266e6c9dcd512), bool [has_linked_chat_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a272fcaa35af7d09b97269e55192764db), bool [has_location_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#aa1ec1d684a50df3ca41bdbdd8a9e236d), bool [sign_messages_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#aed283c3fe4d9f4db55f904586ac59786), bool [show_message_sender_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a27ee8537ec772ce8d7ee28d216900d26), bool [join_to_send_messages_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a5fc65e27dac49cd7f0d364dd8348914a), bool [join_by_request_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a9467e716be54f53071d24722a23aaf61), bool [is_slow_mode_enabled_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#abaccd7272930ee8a4a0f8463681ca9c8), bool [is_channel_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a03c3ef88b91f79e111f3f015657a06e8), bool [is_broadcast_group_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a8c4a5114a53bf6159274fcfb0b695ee5), bool [is_forum_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a5cc2f692df786d353dabf2a0b978ab7b), bool [is_direct_messages_group_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a15584a2b9155aae7fff26e796fc6157c), bool [is_administered_direct_messages_group_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#aae758601e8748f3a6bc1e85966dea22f), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [verificationStatus](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1verification_status.html) > &&[verification_status_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a19b93695acd570fd7c5c480955dac459), bool [has_direct_messages_group_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#ab73e27694d21b5182d8d10698dbc2994), bool [has_forum_tabs_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#ab8d4622af607ab2cd7925fc71b46a941), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [restrictionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1restriction_info.html) > &&[restriction_info_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a546a254a895e82fd74b4aeacc68def96), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [paid_message_star_count_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#ab000a89591b96c76c47a53b91c45755f), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ActiveStoryState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_active_story_state.html) > &&[active_story_state_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a38567b5fb62090751615b02f5db86afa)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1134998957 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a96af64304e0c06b829ff4ce564ac9325)supergroup() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [supergroup](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html) | ( |  | ) |  |

Represents a supergroup or channel with zero or more members (subscribers in the case of channels). From the point of view of the system, a channel is a special kind of a supergroup: only administrators can post and see the list of members, and posts from all administrators use the name and photo of the channel instead of individual names and profile photos. Unlike supergroups, channels can have an unlimited number of subscribers.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#aebdc22aeb823393591ab1a7252964599)supergroup() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [supergroup](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *id_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [usernames](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1usernames.html) > && | *usernames_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *date_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ChatMemberStatus](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_chat_member_status.html) > && | *status_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *member_count_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *boost_level_*, |
|  |  | bool | *has_automatic_translation_*, |
|  |  | bool | *has_linked_chat_*, |
|  |  | bool | *has_location_*, |
|  |  | bool | *sign_messages_*, |
|  |  | bool | *show_message_sender_*, |
|  |  | bool | *join_to_send_messages_*, |
|  |  | bool | *join_by_request_*, |
|  |  | bool | *is_slow_mode_enabled_*, |
|  |  | bool | *is_channel_*, |
|  |  | bool | *is_broadcast_group_*, |
|  |  | bool | *is_forum_*, |
|  |  | bool | *is_direct_messages_group_*, |
|  |  | bool | *is_administered_direct_messages_group_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [verificationStatus](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1verification_status.html) > && | *verification_status_*, |
|  |  | bool | *has_direct_messages_group_*, |
|  |  | bool | *has_forum_tabs_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [restrictionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1restriction_info.html) > && | *restriction_info_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *paid_message_star_count_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ActiveStoryState](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_active_story_state.html) > && | *active_story_state_* |
|  | ) |  |  |

Represents a supergroup or channel with zero or more members (subscribers in the case of channels). From the point of view of the system, a channel is a special kind of a supergroup: only administrators can post and see the list of members, and posts from all administrators use the name and photo of the channel instead of individual names and profile photos. Unlike supergroups, channels can have an unlimited number of subscribers.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | id_ | Supergroup or channel identifier. |
    | [in] | usernames_ | Usernames of the supergroup or channel; may be null. |
    | [in] | date_ | Point in time (Unix timestamp) when the current user joined, or the point in time when the supergroup or channel was created, in case the user is not a member. |
    | [in] | status_ | Status of the current user in the supergroup or channel. |
    | [in] | member_count_ | Number of members in the supergroup or channel; 0 if unknown. Currently, it is guaranteed to be known only if the supergroup or channel was received through [getChatSimilarChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chat_similar_chats.html), [getChatsToPostStories](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_chats_to_post_stories.html), [getCreatedPublicChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_created_public_chats.html), [getGroupsInCommon](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_groups_in_common.html), [getInactiveSupergroupChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_inactive_supergroup_chats.html), [getRecommendedChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_recommended_chats.html), [getSuitableDiscussionChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_suitable_discussion_chats.html), [getUserPrivacySettingRules](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_privacy_setting_rules.html), [getVideoChatAvailableParticipants](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_video_chat_available_participants.html), [searchPublicChats](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1search_public_chats.html), or in chatFolderInviteLinkInfo.missing_chat_ids, or in userFullInfo.personal_chat_id, or for chats with messages or stories from [publicForwards](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1public_forwards.html) and [foundStories](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1found_stories.html). |
    | [in] | boost_level_ | Approximate boost level for the chat. |
    | [in] | has_automatic_translation_ | True, if automatic translation of messages is enabled in the channel. |
    | [in] | has_linked_chat_ | True, if the channel has a discussion group, or the supergroup is the designated discussion group for a channel. |
    | [in] | has_location_ | True, if the supergroup is connected to a location, i.e. the supergroup is a location-based supergroup. |
    | [in] | sign_messages_ | True, if messages sent to the channel contains name of the sender. This field is only applicable to channels. |
    | [in] | show_message_sender_ | True, if messages sent to the channel have information about the sender user. This field is only applicable to channels. |
    | [in] | join_to_send_messages_ | True, if users need to join the supergroup before they can send messages. May be false only for discussion supergroups and channel direct messages groups. |
    | [in] | join_by_request_ | True, if all users directly joining the supergroup need to be approved by supergroup administrators. May be true only for non-broadcast supergroups with username, location, or a linked chat. |
    | [in] | is_slow_mode_enabled_ | True, if the slow mode is enabled in the supergroup. |
    | [in] | is_channel_ | True, if the supergroup is a channel. |
    | [in] | is_broadcast_group_ | True, if the supergroup is a broadcast group, i.e. only administrators can send messages and there is no limit on the number of members. |
    | [in] | is_forum_ | True, if the supergroup is a forum with topics. |
    | [in] | is_direct_messages_group_ | True, if the supergroup is a direct message group for a channel chat. |
    | [in] | is_administered_direct_messages_group_ | True, if the supergroup is a direct messages group for a channel chat that is administered by the current user. |
    | [in] | verification_status_ | Information about verification status of the supergroup or channel; may be null if none. |
    | [in] | has_direct_messages_group_ | True, if the channel has direct messages group. |
    | [in] | has_forum_tabs_ | True, if the supergroup is a forum, which topics are shown in the same way as in channel direct messages groups. |
    | [in] | restriction_info_ | Information about the restrictions that must be applied to the corresponding supergroup or channel chat; may be null if none. |
    | [in] | paid_message_star_count_ | Number of Telegram Stars that must be paid by non-administrator users of the supergroup chat for each sent message. |
    | [in] | active_story_state_ | State of active stories of the supergroup or channel; may be null if there are no active stories. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1supergroup.html#a8044dab2ba3c75066745014259c050c7)store()

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