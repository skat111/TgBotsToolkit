Source: https://core.telegram.org/bots/api#chatfullinfo
Snapshot: 2026-09-17T08:42:18Z

#### ChatFullInfo

This object contains full information about a chat.

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. |
| type | String | Type of the chat, can be either “private”, “group”, “supergroup” or “channel” |
| title | String | *Optional*. Title, for supergroups, channels and group chats |
| username | String | *Optional*. Username, for private chats, supergroups and channels if available |
| first_name | String | *Optional*. First name of the other party in a private chat |
| last_name | String | *Optional*. Last name of the other party in a private chat |
| is_forum | True | *Optional*. *True*, if the supergroup chat is a forum (has [topics](https://telegram.org/blog/topics-in-groups-collectible-usernames#topics-in-groups) enabled) |
| is_direct_messages | True | *Optional*. *True*, if the chat is the direct messages chat of a channel |
| accent_color_id | Integer | Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See [accent colors](https://core.telegram.org/bots/api#accent-colors) for more details. |
| max_reaction_count | Integer | The maximum number of reactions that can be set on a message in the chat |
| photo | [ChatPhoto](https://core.telegram.org/bots/api#chatphoto) | *Optional*. Chat photo |
| active_usernames | Array of String | *Optional*. If non-empty, the list of all [active chat usernames](https://telegram.org/blog/topics-in-groups-collectible-usernames#collectible-usernames); for private chats, supergroups and channels |
| birthdate | [Birthdate](https://core.telegram.org/bots/api#birthdate) | *Optional*. For private chats, the date of birth of the user |
| business_intro | [BusinessIntro](https://core.telegram.org/bots/api#businessintro) | *Optional*. For private chats with business accounts, the intro of the business |
| business_location | [BusinessLocation](https://core.telegram.org/bots/api#businesslocation) | *Optional*. For private chats with business accounts, the location of the business |
| business_opening_hours | [BusinessOpeningHours](https://core.telegram.org/bots/api#businessopeninghours) | *Optional*. For private chats with business accounts, the opening hours of the business |
| personal_chat | [Chat](https://core.telegram.org/bots/api#chat) | *Optional*. For private chats, the personal channel of the user |
| parent_chat | [Chat](https://core.telegram.org/bots/api#chat) | *Optional*. Information about the corresponding channel chat; for direct messages chats only |
| available_reactions | Array of [ReactionType](https://core.telegram.org/bots/api#reactiontype) | *Optional*. List of available reactions allowed in the chat. If omitted, then all [emoji reactions](https://core.telegram.org/bots/api#reactiontypeemoji) are allowed. |
| background_custom_emoji_id | String | *Optional*. Custom emoji identifier of the emoji chosen by the chat for the reply header and link preview background |
| profile_accent_color_id | Integer | *Optional*. Identifier of the accent color for the chat's profile background. See [profile accent colors](https://core.telegram.org/bots/api#profile-accent-colors) for more details. |
| profile_background_custom_emoji_id | String | *Optional*. Custom emoji identifier of the emoji chosen by the chat for its profile background |
| emoji_status_custom_emoji_id | String | *Optional*. Custom emoji identifier of the emoji status of the chat or the other party in a private chat |
| emoji_status_expiration_date | Integer | *Optional*. Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any |
| bio | String | *Optional*. Bio of the other party in a private chat |
| has_private_forwards | True | *Optional*. *True*, if privacy settings of the other party in the private chat allows to use `tg://user?id=<user_id>` links only in chats with the user |
| has_restricted_voice_and_video_messages | True | *Optional*. *True*, if the privacy settings of the other party restrict sending voice and video note messages in the private chat |
| join_to_send_messages | True | *Optional*. *True*, if users need to join the supergroup before they can send messages |
| join_by_request | True | *Optional*. *True*, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators |
| description | String | *Optional*. Description, for groups, supergroups and channel chats |
| invite_link | String | *Optional*. Primary invite link, for groups, supergroups and channel chats |
| pinned_message | [Message](https://core.telegram.org/bots/api#message) | *Optional*. The most recent pinned message (by sending date) |
| permissions | [ChatPermissions](https://core.telegram.org/bots/api#chatpermissions) | *Optional*. Default chat member permissions, for groups and supergroups |
| accepted_gift_types | [AcceptedGiftTypes](https://core.telegram.org/bots/api#acceptedgifttypes) | Information about types of gifts that are accepted by the chat or by the corresponding user for private chats |
| can_send_paid_media | True | *Optional*. *True*, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats. |
| slow_mode_delay | Integer | *Optional*. For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds |
| unrestrict_boost_count | Integer | *Optional*. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions |
| message_auto_delete_time | Integer | *Optional*. The time after which all messages sent to the chat will be automatically deleted; in seconds |
| has_aggressive_anti_spam_enabled | True | *Optional*. *True*, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators. |
| has_hidden_members | True | *Optional*. *True*, if non-administrators can only get the list of bots and administrators in the chat |
| has_protected_content | True | *Optional*. *True*, if messages from the chat can't be forwarded to other chats |
| has_visible_history | True | *Optional*. *True*, if new chat members will have access to old messages; available only to chat administrators |
| sticker_set_name | String | *Optional*. For supergroups, name of the group sticker set |
| can_set_sticker_set | True | *Optional*. *True*, if the bot can change the group sticker set |
| custom_emoji_sticker_set_name | String | *Optional*. For supergroups, the name of the group's custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group. |
| linked_chat_id | Integer | *Optional*. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. |
| location | [ChatLocation](https://core.telegram.org/bots/api#chatlocation) | *Optional*. For supergroups, the location to which the supergroup is connected |
| rating | [UserRating](https://core.telegram.org/bots/api#userrating) | *Optional*. For private chats, the rating of the user if any |
| first_profile_audio | [Audio](https://core.telegram.org/bots/api#audio) | *Optional*. For private chats, the first audio added to the profile of the user |
| unique_gift_colors | [UniqueGiftColors](https://core.telegram.org/bots/api#uniquegiftcolors) | *Optional*. The color scheme based on a unique gift that must be used for the chat's name, message replies and link previews |
| paid_message_star_count | Integer | *Optional*. The number of Telegram Stars a general user has to pay to send a message to the chat |
| guard_bot | [User](https://core.telegram.org/bots/api#user) | *Optional*. The bot that processes join request queries in the chat. The field is only available to chat administrators. |
| community | [Community](https://core.telegram.org/bots/api#community) | *Optional*. The [Community](https://core.telegram.org/bots/api#community) to which the chat belongs |