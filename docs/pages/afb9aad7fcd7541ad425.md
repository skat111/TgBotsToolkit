# Telegram Premium

Source: https://core.telegram.org/api/premium

Telegram Premium is an optional subscription service that unlocks additional exclusive client-side and API-side features, while helping support the development of the app. It is a part of Telegram’s **sustainable monetization** – driven by our users, rather than advertisers or shareholders. This way, Telegram can remain independent and prioritize its users first.

> This page describes how client apps should handle Premium features: for a user-friendly overview of Telegram Premium features, see the [Telegram Premium FAQ](https://telegram.org/faq_premium).

### Telegram Premium users

```
inputUserSelf#f7c1b13f = InputUser;

user#31774388 flags:# self:flags.10?true contact:flags.11?true mutual_contact:flags.12?true deleted:flags.13?true bot:flags.14?true bot_chat_history:flags.15?true bot_nochats:flags.16?true verified:flags.17?true restricted:flags.18?true min:flags.20?true bot_inline_geo:flags.21?true support:flags.23?true scam:flags.24?true apply_min_photo:flags.25?true fake:flags.26?true bot_attach_menu:flags.27?true premium:flags.28?true attach_menu_enabled:flags.29?true flags2:# bot_can_edit:flags2.1?true close_friend:flags2.2?true stories_hidden:flags2.3?true stories_unavailable:flags2.4?true contact_require_premium:flags2.10?true bot_business:flags2.11?true bot_has_main_app:flags2.13?true bot_forum_view:flags2.16?true bot_forum_can_manage_topics:flags2.17?true bot_can_manage_bots:flags2.18?true bot_guestchat:flags2.19?true id:long access_hash:flags.0?long first_name:flags.1?string last_name:flags.2?string username:flags.3?string phone:flags.4?string photo:flags.5?UserProfilePhoto status:flags.6?UserStatus bot_info_version:flags.14?int restriction_reason:flags.18?Vector<RestrictionReason> bot_inline_placeholder:flags.19?string lang_code:flags.22?string emoji_status:flags.30?EmojiStatus usernames:flags2.0?Vector<Username> stories_max_id:flags2.5?RecentStory color:flags2.8?PeerColor profile_color:flags2.9?PeerColor bot_active_users:flags2.12?int bot_verification_icon:flags2.14?long send_paid_messages_stars:flags2.15?long = User;

help.premiumPromo#5334759c status_text:string status_entities:Vector<MessageEntity> video_sections:Vector<string> videos:Vector<Document> period_options:Vector<PremiumSubscriptionOption> users:Vector<User> = help.PremiumPromo;

---functions---

users.getUsers#0d91a548 id:Vector<InputUser> = Vector<User>;
help.getPremiumPromo#b81b93d4 = help.PremiumPromo;
```

Premium users will have the `premium` flag of the [user](https://core.telegram.org/constructor/user) set.

Use [users.getUsers](https://core.telegram.org/method/users.getUsers) with [inputUserSelf](https://core.telegram.org/constructor/inputUserSelf) to fetch info about the current subscription status of the current user.  
You can also directly use [help.getPremiumPromo](https://core.telegram.org/method/help.getPremiumPromo), as it will return info about the current user in the `users` field.

### Telegram Premium features

Telegram Premium offers a set of additional features and raised limits: clients should be aware of the current subscription status to accordingly modify client behavior.

#### Promo page

```
help.premiumPromo#5334759c status_text:string status_entities:Vector<MessageEntity> video_sections:Vector<string> videos:Vector<Document> period_options:Vector<PremiumSubscriptionOption> users:Vector<User> = help.PremiumPromo;

---functions---

help.getPremiumPromo#b81b93d4 = help.PremiumPromo;
help.getAppConfig#61e3f854 hash:int = help.AppConfig;
```

The [help.premiumPromo](https://core.telegram.org/constructor/help.premiumPromo) constructor returned by [help.getPremiumPromo](https://core.telegram.org/method/help.getPremiumPromo) contains various info about the subscription, as described in the [constructor page](https://core.telegram.org/constructor/help.premiumPromo).

Clients should show a Telegram Premium button in the settings.  
Clicking on this button in the settings, clicking on the [badge](https://core.telegram.org/api/premium#badge) of a Premium user or hitting one of the Premium limits listed below should open a Telegram Premium modal.

Call [help.getPremiumPromo](https://core.telegram.org/method/help.getPremiumPromo) and [help.getAppConfig](https://core.telegram.org/method/help.getAppConfig) to fetch info on how to build the premium modal.

[help.getAppConfig](https://core.telegram.org/method/help.getAppConfig) will return a list of Premium feature identifiers in the [`premium_promo_order` appConfig field](https://core.telegram.org/api/config#premium-promo-order): the modal should contain a row for each returned feature, ordered as specified in the returned array.

These feature identifiers must be used when [subscribing to Telegram Premium](https://core.telegram.org/api/premium#subscribing-to-telegram-premium) if the related limit was hit.

Possible feature identifiers:

##### `stories`

[Telegram Premium](https://core.telegram.org/api/premium) adds some [story-related](https://core.telegram.org/api/stories) features.

Story-related Premium features also have certain sub-identifiers, which are used if the user chooses to [subscribe to Telegram Premium](https://core.telegram.org/api/premium#subscribing-to-telegram-premium) after hitting one of the following story-related limitations.

If the user instead signs up simply after reading the promo page for story-related features, pass just `stories` as feature identifier.

Here's the full list of story-related features and their sub-identifiers (contained in the title header):

###### `stories__priority_order`

Stories posted by Premium users are shown first to users when fetching the list of active stories with [stories.getAllStories »](https://core.telegram.org/method/stories.getAllStories).

###### `stories__stealth_mode`

Premium users can activate [stealth mode »](https://core.telegram.org/api/stories#stealth-mode).

###### `stories__permanent_views_history`

Premium users can [fetch the full viewer list of stories, even after they expire »](https://core.telegram.org/api/stories#fetching-the-interaction-list)

###### `stories__expiration_durations`

Premium users can set [custom expiration options when posting stories »](https://core.telegram.org/api/stories)

###### `stories__save_stories_to_gallery`

Premium users can save other users' unprotected stories.

###### `stories__links_and_formatting`

Premium users can use [styled text entities](https://core.telegram.org/api/entities) and links in story captions and [URL media areas](https://core.telegram.org/api/stories#urls), as specified by the [stories\_entities »](https://core.telegram.org/api/config#stories-entities) config key.

###### `stories__quality`

Premium users can view stories in a higher quality.

There are a few more Premium story features that are listed in the [limits »](https://core.telegram.org/api/premium#double-limits) section.

See the [stories documentation »](https://core.telegram.org/api/stories) for more information on stories.

##### `double_limits`

Clicking on this entry should open a secondary popup with a list of the improved Premium limits, as follows.

Limit-related Premium features also have certain sub-identifiers, which are used if the user chooses to [subscribe to Telegram Premium](https://core.telegram.org/api/premium#subscribing-to-telegram-premium) after hitting one of the following limitations.

If the user instead signs up simply after reading the promo page for limits, pass just `double_limits` as feature identifier.

Here's the full list of improved limits and their sub-identifiers (contained in the title header):

###### `double_limits__channels`

Config keys: [channels\_limit\_premium »](https://core.telegram.org/api/config#channels-limit-premium)/[channels\_limit\_default »](https://core.telegram.org/api/config#channels-limit-default)

The maximum number of [channels and supergroups](https://core.telegram.org/api/channel) a [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) user may join (integer)

###### `double_limits__saved_gifs`

Config keys: [saved\_gifs\_limit\_premium »](https://core.telegram.org/api/config#saved-gifs-limit-premium)/[saved\_gifs\_limit\_default »](https://core.telegram.org/api/config#saved-gifs-limit-default)

The maximum number of GIFs a [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) user may save (integer)

###### `double_limits__stickers_faved`

Config keys: [stickers\_faved\_limit\_premium »](https://core.telegram.org/api/config#stickers-faved-limit-premium)/[stickers\_faved\_limit\_default »](https://core.telegram.org/api/config#stickers-faved-limit-default)

The maximum number of stickers a [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) user may [add to Favorites »](https://core.telegram.org/api/stickers#favorite-stickersets) (integer)

###### `double_limits__dialog_filters`

Config keys: [dialog\_filters\_limit\_premium »](https://core.telegram.org/api/config#dialog-filters-limit-premium)/[dialog\_filters\_limit\_default »](https://core.telegram.org/api/config#dialog-filters-limit-default)

The maximum number of [folders](https://core.telegram.org/api/folders) a [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) user may create (integer)

###### `double_limits__dialog_filters_chats`

Config keys: [dialog\_filters\_chats\_limit\_premium »](https://core.telegram.org/api/config#dialog-filters-chats-limit-premium)/[dialog\_filters\_chats\_limit\_default »](https://core.telegram.org/api/config#dialog-filters-chats-limit-default)

The maximum number of chats a [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) user may add to a [folder](https://core.telegram.org/api/folders) (integer)

###### `double_limits__dialogs_pinned`

Config keys: [dialogs\_pinned\_limit\_premium »](https://core.telegram.org/api/config#dialogs-pinned-limit-premium)/[dialogs\_pinned\_limit\_default »](https://core.telegram.org/api/config#dialogs-pinned-limit-default)

The maximum number of chats a [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) user may pin (integer)

###### `double_limits__dialogs_folder_pinned`

Config keys: [dialogs\_folder\_pinned\_limit\_premium »](https://core.telegram.org/api/config#dialogs-folder-pinned-limit-premium)/[dialogs\_folder\_pinned\_limit\_default »](https://core.telegram.org/api/config#dialogs-folder-pinned-limit-default)

The maximum number of chats a [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) user may pin in a folder (integer)

###### `double_limits__channels_public`

Config keys: [channels\_public\_limit\_premium »](https://core.telegram.org/api/config#channels-public-limit-premium)/[channels\_public\_limit\_default »](https://core.telegram.org/api/config#channels-public-limit-default)

The maximum number of public [channels or supergroups](https://core.telegram.org/api/channel) a [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) user may create (integer)

###### `double_limits__caption_length`

Config keys: [caption\_length\_limit\_premium »](https://core.telegram.org/api/config#caption-length-limit-premium)/[caption\_length\_limit\_default »](https://core.telegram.org/api/config#caption-length-limit-default)

The maximum UTF-8 length of media captions sendable by [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) users (integer)

###### `double_limits__about_length`

Config keys: [about\_length\_limit\_premium »](https://core.telegram.org/api/config#about-length-limit-premium)/[about\_length\_limit\_default »](https://core.telegram.org/api/config#about-length-limit-default)

The maximum UTF-8 length of bios of [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) users (integer)

###### `double_limits__chatlist_invites`

Config keys: [chatlist\_invites\_limit\_premium »](https://core.telegram.org/api/config#chatlist-invites-limit-premium)/[chatlist\_invites\_limit\_default »](https://core.telegram.org/api/config#chatlist-invites-limit-default)

Maximum number of per-folder [chat folder deep links »](https://core.telegram.org/api/links#chat-folder-links) that can be created by [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) users. (integer)

###### `double_limits__chatlists_joined`

Config keys: [chatlists\_joined\_limit\_premium »](https://core.telegram.org/api/config#chatlists-joined-limit-premium)/[chatlists\_joined\_limit\_default »](https://core.telegram.org/api/config#chatlists-joined-limit-default)

Maximum number of [shareable folders](https://core.telegram.org/api/links#chat-folder-links) [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) users may have. (integer)

###### `double_limits__story_expiring`

Config keys: [story\_expiring\_limit\_premium »](https://core.telegram.org/api/config#story-expiring-limit-premium)/[story\_expiring\_limit\_default »](https://core.telegram.org/api/config#story-expiring-limit-default)

The maximum number of active [stories](https://core.telegram.org/api/stories) for [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) users (integer).

###### `double_limits__story_caption_length`

Config keys: [story\_caption\_length\_limit\_premium »](https://core.telegram.org/api/config#story-caption-length-limit-premium)/[story\_caption\_length\_limit\_default »](https://core.telegram.org/api/config#story-caption-length-limit-default)

The maximum UTF-8 length of story captions for [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) users. (integer)

###### `double_limits__stories_sent_weekly`

Config keys: [stories\_sent\_weekly\_limit\_premium »](https://core.telegram.org/api/config#stories-sent-weekly-limit-premium)/[stories\_sent\_weekly\_limit\_default »](https://core.telegram.org/api/config#stories-sent-weekly-limit-default)

Maximum number of stories that can be sent in a week by [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) users. (integer)

###### `double_limits__stories_sent_monthly`

Config keys: [stories\_sent\_monthly\_limit\_premium »](https://core.telegram.org/api/config#stories-sent-monthly-limit-premium)/[stories\_sent\_monthly\_limit\_default »](https://core.telegram.org/api/config#stories-sent-monthly-limit-default)

Maximum number of stories that can be sent in a month by [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) users. (integer)

###### `double_limits__stories_suggested_reactions`

Config keys: [stories\_suggested\_reactions\_limit\_premium »](https://core.telegram.org/api/config#stories-suggested-reactions-limit-premium)/[stories\_suggested\_reactions\_limit\_default »](https://core.telegram.org/api/config#stories-suggested-reactions-limit-default)

Maximum number of [story reaction media areas »](https://core.telegram.org/api/stories#media-areas) that can be added to a story by [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) users. (integer)

###### `double_limits__recommended_channels`

Config keys: [recommended\_channels\_limit\_premium »](https://core.telegram.org/api/config#recommended-channels-limit-premium)/[recommended\_channels\_limit\_default »](https://core.telegram.org/api/config#recommended-channels-limit-default)

The maximum number of similar channels that can be recommended by [channels.getChannelRecommendations»](https://core.telegram.org/method/channels.getChannelRecommendations) to [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) users. (integer)

###### `double_limits__saved_dialogs_pinned`

Config keys: [saved\_dialogs\_pinned\_limit\_premium »](https://core.telegram.org/api/config#saved-dialogs-pinned-limit-premium)/[saved\_dialogs\_pinned\_limit\_default »](https://core.telegram.org/api/config#saved-dialogs-pinned-limit-default)

Maximum number of pinned dialogs in [saved messages](https://core.telegram.org/api/saved-messages) for [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) users. (integer)

###### `double_limits__bots_create`

Config keys: [bots\_create\_limit\_default »](https://core.telegram.org/api/config#bots-create-limit-premium)/[bots\_create\_limit\_premium »](https://core.telegram.org/api/config#bots-create-limit-default)

Maximum number of [bots](https://core.telegram.org/api/bots) that can be owned by [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) users. (integer)

###### `double_limits__aicompose_tone_saved`

Config keys: [aicompose\_tone\_saved\_limit\_premium »](https://core.telegram.org/api/config#aicompose-tone-saved-limit-premium)/[aicompose\_tone\_saved\_limit\_default »](https://core.telegram.org/api/config#aicompose-tone-saved-limit-default)

Maximum number of [custom AI composer tones »](https://core.telegram.org/api/ai#ai-compose-tones) that can be installed by [Premium](https://core.telegram.org/api/premium)/non-[Premium](https://core.telegram.org/api/premium) users. (integer)

##### `business`

Premium users currently have access to subscription-gated [Telegram Business features »](https://core.telegram.org/api/business); [connected business bots »](https://core.telegram.org/api/bots/connected-business-bots) are also available to non-Premium users.

##### `last_seen`

Premium users can view the last seen and message read times of other users even if they can't view the last seen or read time for the current user.

##### `message_privacy`

Premium users can disallow incoming voice and video note messages in private chats using [inputPrivacyKeyVoiceMessages](https://core.telegram.org/constructor/inputPrivacyKeyVoiceMessages) and [restrict incoming messages from non-contacts](https://core.telegram.org/api/privacy#require-premium-for-new-non-contact-users).

##### `more_upload`

Premium users can upload bigger files, as specified by the [upload\_max\_fileparts\_default](https://core.telegram.org/api/config#upload-max-fileparts-default) vs [upload\_max\_fileparts\_premium](https://core.telegram.org/api/config#upload-max-fileparts-premium) config keys.

##### `faster_download`

Premium users have no download speed limits (i.e. they can't receive `FLOOD_PREMIUM_WAIT_X` errors when downloading files, see [here »](https://core.telegram.org/api/files) for more info).

##### `wallpapers`

Premium users [can set custom chat wallpapers both for them and the other user in the chat](https://core.telegram.org/api/wallpapers#installing-wallpapers-in-a-specific-chat-or-channel).

##### `peer_colors`

Premium users can [choose a custom color and background emoji for their profile background and messages](https://core.telegram.org/api/colors).

##### `voice_to_text`

Premium users can [transcribe voice messages without limits](https://core.telegram.org/api/transcribe).

##### `translations`

Premium users can enable [real-time chat translation](https://core.telegram.org/api/translation).

##### `no_ads`

Premium users see no [sponsored messages](https://core.telegram.org/api/sponsored-messages).

##### `unique_reactions`

Premium users have access to more [message reactions](https://core.telegram.org/api/reactions).

##### `premium_stickers`

Premium users have access to premium [stickersets](https://core.telegram.org/api/stickers).

##### `animated_emoji`

Premium users can send custom [animated emojis](https://core.telegram.org/api/custom-emoji).

##### `advanced_chat_management`

Premium users can [reorder the default folder](https://core.telegram.org/api/folders), auto-archive and hide new chats from non-contacts.

##### `profile_badge`

Premium users have a [badge](https://core.telegram.org/api/premium#badge) next to their name, showing that they are helping support Telegram.

##### `animated_userpics`

[Animated profile pictures](https://core.telegram.org/api/files#animated-profile-pictures) of Premium users will play in-chat and when browsing the dialog list.

##### `app_icons`

Premium users can change the default icon of the Telegram app.

##### `infinite_reactions`

Premium users can use [custom emojis](https://core.telegram.org/api/custom-emoji) when [reacting to messages](https://core.telegram.org/api/reactions).

##### `emoji_status`

Premium users can set a [status emoji](https://core.telegram.org/api/emoji-status).

##### `saved_tags`

Premium users can use [saved message tags](https://core.telegram.org/api/saved-messages#tags).

##### `effects`

Premium users can use [message effects](https://core.telegram.org/api/effects).

##### `channel_boost`

Premium users can [boost chats and channels](https://core.telegram.org/api/boost).

##### `forum_topic_icon`

Premium users can set a [custom emoji](https://core.telegram.org/api/custom-emoji) as a [forum topic icon](https://core.telegram.org/api/forum)

##### `todo`

Premium users can [post todo lists »](https://core.telegram.org/api/todo)

##### `paid_messages`

Premium users can [require payment in Telegram stars in order to receive messages from new users »](https://core.telegram.org/api/paid-messages).

##### `pm_noforwards`

Premium users can [enable content protection in private chats »](https://core.telegram.org/api/content-protection#for-users).

##### `ai_compose`

Premium users have **50x** more [AI text transformations »](https://core.telegram.org/api/ai#compose-messages) per day.

#### Badge

Users with a Telegram Premium subscription ([user](https://core.telegram.org/constructor/user).`premium` is set) should have a Telegram Premium badge next to their name.

#### Animated profile pictures

The [animated profile pictures](https://core.telegram.org/api/files#animated-profile-pictures) of Premium users should play inside of chats and dialog lists, and not just when opening the profile page.

#### Sticker suggestions

The suggested sticker selection logic is slightly different for Premium users, see [here for more info »](https://core.telegram.org/api/stickers#sticker-suggestions).

### Subscribing to Telegram Premium

Here's how to activate a Telegram Premium subscription, when the user clicks on the subscribe button:

* If the `premium_bot_username` field is set, call [messages.startBot](https://core.telegram.org/method/messages.startBot), specifying the following parameters:
  + `peer` and `bot`: The bot mentioned in `premium_bot_username`
  + `start_param`: One of the following values:
    - If the user clicks on the subscribe button when viewing the promo page for a specific Premium feature, provide the [feature identifier](https://core.telegram.org/api/premium#telegram-premium-features) (or an empty string if opened from the main promo page).
    - If the user clicks on the subscribe button when viewing the promo page for a specific [Telegram Business](https://core.telegram.org/api/business#business-features-promo-page) feature, provide the business [feature identifier](https://core.telegram.org/api/business#business-features-promo-page) (or `business` if opened from the main business promo page).
    - If the user clicks on the subscribe button after hitting a limit that Telegram Premium raises, provide one of the [limit identifiers](https://core.telegram.org/api/premium#double-limits)
    - If the user clicks on the subscribe button after hitting a [story-related](https://core.telegram.org/api/stories) limit that Telegram Premium raises, provide one of the [story feature identifiers](https://core.telegram.org/api/premium#stories)
    - If the user clicks on the subscribe button from the Telegram Premium button in the settings, provide `settings`
    - If the user clicks on the subscribe button from the Telegram Premium star in a profile page, provide `profile`
    - If the user opened a [premium referrer link](https://core.telegram.org/api/links#premium-referrer-links), provide `deeplink` if the `referrer` is empty, and `deeplink_$referrer` if non-empty.
      Then, when the user clicks on the subscribe button in the sent invoice, follow the [usual payment flow for message invoices](https://core.telegram.org/api/payments).
* Otherwise, if the `premium_invoice_slug` field is set, handle the payment as you would handle a `t.me/$premium_invoice_slug` [invoice deep link](https://core.telegram.org/api/links#invoice-links).

There is also a store-based subscription flow based on [payments.assignAppStoreTransaction](https://core.telegram.org/method/payments.assignAppStoreTransaction)/[payments.assignPlayMarketTransaction](https://core.telegram.org/method/payments.assignPlayMarketTransaction), but it's currently not available to third-party apps (unlike the flow described above, which can be used by all clients).

### Gifting Telegram Premium

Note: to gift Premium subscriptions to multiple friends, the alternative payment flow [described here »](https://core.telegram.org/api/giveaways) ([inputStorePaymentPremiumGiftCode](https://core.telegram.org/constructor/inputStorePaymentPremiumGiftCode) without setting `boost_peer`) must be used, instead.

```
premiumGiftCodeOption#257e962b flags:# users:int months:int store_product:flags.0?string store_quantity:flags.1?int currency:string amount:long = PremiumGiftCodeOption;

inputInvoicePremiumGiftStars#dabab2ef flags:# user_id:InputUser months:int message:flags.0?TextWithEntities = InputInvoice;

messageActionGiftPremium#48e91302 flags:# currency:string amount:long days:int crypto_currency:flags.0?string crypto_amount:flags.0?long message:flags.1?TextWithEntities = MessageAction;

inputStickerSetPremiumGifts#c88b3b02 = InputStickerSet;

---functions---

payments.getPremiumGiftCodeOptions#2757ba54 flags:# boost_peer:flags.0?InputPeer = Vector<PremiumGiftCodeOption>;
```

If the other user in a private chat doesn't have a Premium subscription, we can gift them a non-recurring Telegram Premium subscription.

If the [userFull](https://core.telegram.org/constructor/userFull).`display_gifts_button` flag of both us and another user is set (changed through [globalPrivacySettings](https://core.telegram.org/constructor/globalPrivacySettings)), a gift button should always be displayed in the text field in private chats with the other user: once clicked, the gift UI should be displayed, offering the user options to gift [Telegram Premium »](https://core.telegram.org/api/premium#gifting-telegram-premium) subscriptions or [Telegram Gifts »](https://core.telegram.org/api/gifts).

The same gifting UI should always be (unconditionally) available through a chat picker, activated by a "Send a Gift" entry in the app's settings.

Users may disallow the reception of specific gift types by populating the [globalPrivacySettings](https://core.telegram.org/constructor/globalPrivacySettings).`disallowed_gifts` flag, visible to other users in [userFull](https://core.telegram.org/constructor/userFull).`disallowed_gifts`.

To obtain available gift options for Telegram Premium, invoke [payments.getPremiumGiftCodeOptions](https://core.telegram.org/method/payments.getPremiumGiftCodeOptions).

The returned [premiumGiftCodeOption](https://core.telegram.org/constructor/premiumGiftCodeOption) constructors are an ordered list of Premium gift offers with discounts over the base price, according to the subscription duration.

Filter out only options where `users == 1` (options where `users > 1` are used for [giveaways](https://core.telegram.org/api/giveaways)).

Each `users/months` combo can have up to two options: one in the user's native currency, and the other (optionally) in [Telegram Stars](https://core.telegram.org/api/stars) (`currency == "XTR"`).

Unofficial clients should display and use only the options where `currency`=`XTR`.

To gift a Telegram Premium subscription paying with [Telegram Stars](https://core.telegram.org/api/stars), create an [inputInvoicePremiumGiftStars](https://core.telegram.org/constructor/inputInvoicePremiumGiftStars), then follow the [usual payment flow »](https://core.telegram.org/api/payments#22-getting-invoice-info-about-the-product).

Once the payment is successfully processed, the user to which the gift was sent will automatically receive a [messageService](https://core.telegram.org/constructor/messageService) from the user that sent the gift, containing a [messageActionGiftPremium](https://core.telegram.org/constructor/messageActionGiftPremium) constructor with further info about the price and duration of the gifted Telegram Premium subscription.  
Clients should display this message, along with a sticker from the [inputStickerSetPremiumGifts](https://core.telegram.org/constructor/inputStickerSetPremiumGifts) [stickerset](https://core.telegram.org/api/stickers): here's an [example](https://telegram.org/blog/custom-emoji#gifting-telegram-premium).

Note that if the `premium_gift_attach_menu_icon` [app configuration parameter](https://core.telegram.org/api/config#client-configuration) is `true`, a gift icon should be shown in the attachment menu in private chats with users, offering the current user to gift a [Telegram Premium](https://core.telegram.org/api/premium) subscription to the other user in the chat.

If the `premium_gift_text_field_icon` parameter is also set, a gift icon should be shown in the text bar in private chats with users (i.e. like the `/` icon in chats with bots), offering the current user to gift a [Telegram Premium](https://core.telegram.org/api/premium) subscription to the other user in the chat. Can only be true if `premium_gift_attach_menu_icon` is also true.

Note that even if the `premium_gifts` field is not set, we can still gift one (or more!) Premium subscriptions using the alternative payment flow [described here »](https://core.telegram.org/api/giveaways) ([inputStorePaymentPremiumGiftCode](https://core.telegram.org/constructor/inputStorePaymentPremiumGiftCode) without setting `boost_peer`).

Gifting a [Telegram Premium](https://core.telegram.org/api/premium) subscription to another user will create [boosts\_per\_sent\_gift](https://core.telegram.org/api/config#boosts-per-sent-gift) [boost slots »](https://core.telegram.org/api/boost) for us, and one boost slot for the destination user.

### Blocked Telegram Premium

If the `premium_purchase_blocked` [app configuration parameter](https://core.telegram.org/api/config#client-configuration) is set, the user can't purchase a Premium account, and all Telegram Premium features must be hidden (like the [badges](https://core.telegram.org/api/premium#badge) of Premium users, Telegram Premium purchase buttons, and so on).