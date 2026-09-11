# TDLib options

Source: https://core.telegram.org/tdlib/options

[TDLib](https://core.telegram.org/tdlib) has many options that affect the behavior of the library. Each option has a **name** and a **value**. **Value** may be of one of the following types:

|  |  |  |
| --- | --- | --- |
| **Type of value** | **Default value** | **Value range** |
| Integer | 0 | 64-bit integer |
| Boolean | false | True or false |
| String |  | Any Unicode string |

# List of options supported by TDLib

Options not mentioned in this list may be safely ignored.

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Writable** | **Description** |
| always\_parse\_markdown | Boolean | Yes | If true, text entities will be automatically parsed in all `inputMessageText` objects |
| disable\_animated\_emoji | Boolean | Yes | If true, animated emoji will be disabled and shown as plain emoji |
| disable\_contact\_registered\_notifications | Boolean | Yes | If true, notifications about the user's contacts who have joined Telegram will be disabled. User will still receive the corresponding message in the private chat. `getOption` needs to be called explicitly to fetch the latest value of the option, changed from another device |
| disable\_network\_statistics | Boolean | Yes | *Since TDLib 1.8.24*. If true, then network statistics will be completely disabled |
| disable\_persistent\_network\_statistics | Boolean | Yes | If true, persistent network statistics will be disabled, which significantly reduces disk usage |
| disable\_sent\_scheduled\_message\_notifications | Boolean | Yes | If true, notifications about outgoing scheduled messages that were sent will be disabled |
| disable\_time\_adjustment\_protection | Boolean | Yes | If true, protection from external time adjustment will be disabled, which significantly reduces disk usage |
| disable\_top\_chats | Boolean | Yes | If true, support for top chats and statistics collection is disabled |
| ignore\_background\_updates | Boolean | Yes | If true, allows to skip all updates received while the TDLib instance was not running. The option does nothing if the database or secret chats are used |
| ignore\_default\_disable\_notification | Boolean | Yes | If true, the `disable_notification` value specified in the request will be always used instead of the default value |
| ignore\_file\_names | Boolean | Yes | *Since TDLib 1.8.24*. If true, document file names will be ignored and numerical names will be used instead |
| ignore\_inline\_thumbnails | Boolean | Yes | If true, prevents file thumbnails sent by the server along with messages from being saved on the disk |
| ignore\_platform\_restrictions | Boolean | Yes | If true, chat and message restrictions specific to the currently used operating system will be ignored |
| ignore\_sensitive\_content\_restrictions | Boolean | Yes | If true, sensitive content will be shown on all user devices. `getOption` needs to be called explicitly to fetch the latest value of the option, changed from another device |
| is\_paid\_reaction\_anonymous | Boolean | Yes | *TDLib 1.8.36-1.8.44*. If true, added paid reactions are anonymous by default. If false, they are non-anonymous. |
| language\_pack\_database\_path | String | Yes | Path to a database for storing language pack strings, so that this database can be shared between different accounts. By default, language pack strings are stored only in memory. Changes of value of this option will be applied only after TDLib restart, so it should be set before call to `setTdlibParameters`. |
| language\_pack\_id | String | Yes | Identifier of the currently used language pack from the current localization target |
| localization\_target | String | Yes | Name for the current localization target (for example, “android”, “android\_x”, “ios”, “macos”, “tdesktop”, “unigram”, “web”, “webz”) |
| message\_unload\_delay | Integer | Yes | The maximum time messages are stored in memory before they are unloaded, 60-86400; in seconds. Defaults to 60 for users and 1800 for bots |
| notification\_group\_count\_max | Integer | Yes | The maximum number of notification groups to be shown simultaneously, 0-25 |
| notification\_group\_size\_max | Integer | Yes | The maximum number of simultaneously shown notifications in a group, 1-25. Defaults to 10 |
| online | Boolean | Yes | Online status of the current user |
| prefer\_ipv6 | Boolean | Yes | If true, IPv6 addresses will be preferred over IPv4 addresses |
| process\_pinned\_messages\_as\_mentions | Boolean | Yes | *Since TDLib 1.8.24*. If true, then all pinned messages will be treated as mentions even posted without notification of chat members |
| use\_pfs | Boolean | Yes | If true, Perfect Forward Secrecy will be enabled for interaction with the Telegram servers for cloud chats |
| use\_quick\_ack | Boolean | Yes | If true, quick acknowledgement will be enabled for outgoing messages |
| use\_storage\_optimizer | Boolean | Yes | If true, the background storage optimizer will be enabled |
| utc\_time\_offset | Integer | Yes | A UTC time offset used for splitting messages by days. The option is reset automatically on each TDLib instance launch, so it needs to be set manually only if the time offset is changed during execution. |
| active\_story\_count\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of active stories posted by the current user |
| added\_shareable\_chat\_folder\_count\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of added shareable chat folders for the current user |
| added\_text\_composition\_style\_count\_max | Integer | No | *Since TDLib 1.8.65*. The maximum number of added custom text composition styles |
| affiliate\_program\_commission\_per\_mille\_max | Integer | No | *Since TDLib 1.8.41*. The maximum commission that can be used for an affiliate program |
| affiliate\_program\_commission\_per\_mille\_min | Integer | No | *Since TDLib 1.8.41*. The minimum commission that can be used for an affiliate program |
| animation\_search\_bot\_username | String | No | Username of a bot which can be used in inline mode for animations search |
| anti\_spam\_bot\_user\_id | Integer | No | *Since TDLib 1.8.24*. User identifier of the Telegram Anti-Spam bot |
| authentication\_token | String | No | An authentication token to be used on subsequent authorizations |
| authorization\_date | Integer | No | Point in time (Unix timestamp) when authorization was received |
| basic\_group\_size\_max | Integer | No | The maximum number of members in a basic group |
| bio\_length\_max | Integer | No | *Since TDLib 1.8.24*. The maximum allowed length of the current user's bio |
| bot\_media\_preview\_count\_max | Integer | No | *Since TDLib 1.8.34*. The maximum number of media previews that can be added for a bot |
| bot\_verification\_custom\_description\_length\_max | Integer | No | *Since TDLib 1.8.42*. The maximum length of custom description for verification provided by a third-party organization |
| business\_chat\_link\_count\_max | Integer | No | *Since TDLib 1.8.28*. The maximum number of created short chat links by a Telegram Business account |
| business\_start\_page\_message\_length\_max | Integer | No | *Since TDLib 1.8.28*. The maximum allowed length of the start page message of a Telegram Business account |
| business\_start\_page\_title\_length\_max | Integer | No | *Since TDLib 1.8.28*. The maximum allowed length of the start page title of a Telegram Business account |
| call\_connect\_timeout\_ms | Integer | No | The maximum time to wait for call connection creation to be passed to tgcalls |
| call\_packet\_timeout\_ms | Integer | No | The maximum time to wait for call packet delivery to be passed to tgcalls |
| can\_accept\_calls | Boolean | No | *Since TDLib 1.8.48*. If true, the user can accept calls from this device |
| can\_archive\_and\_mute\_new\_chats\_from\_unknown\_users | Boolean | No | If true, new chats from unknown users can be automatically archived and muted via `archiveChatListSettings` |
| can\_enable\_paid\_messages | Boolean | No | *Since TDLib 1.8.46*. If true, the user can enable paid messages |
| can\_gift\_stars | Boolean | No | *Since TDLib 1.8.34*. If true, Telegram Stars can be gifted to other users |
| can\_ignore\_sensitive\_content\_restrictions | Boolean | No | If true, the option “ignore\_sensitive\_content\_restrictions” can be changed |
| can\_preload\_weather | Boolean | No | *Since TDLib 1.8.34*. If true, the current weather must be preloaded before adding the media area to the story. Otherwise, weather must be loaded only after the user has chosen weather media area. |
| can\_set\_new\_chat\_privacy\_settings | Boolean | No | *Since TDLib 1.8.28*. If true, then the current user can change privacy settings for new chats |
| can\_use\_login\_passkey | Boolean | No | *Since TDLib 1.8.59*. If true, then passkey can be used to log in and new passkeys can be added |
| can\_use\_text\_entities\_in\_story\_caption | Boolean | No | *Since TDLib 1.8.24*. If true, then the current user can use text entities in story captions |
| can\_withdraw\_chat\_revenue | Boolean | No | *Since TDLib 1.8.28*. If true, then revenue from sponsored messages in chats can be withdrawn |
| channel\_bot\_user\_id | Integer | No | Identifier of the bot which is shown as the sender of messages sent on behalf of channels when viewed from an outdated client |
| chat\_available\_reaction\_count\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of manually chosen reactions for a chat |
| chat\_boost\_level\_max | Integer | No | *Since TDLib 1.8.24*. The maximum boost level available to a chat |
| chat\_folder\_chosen\_chat\_count\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of always included or excluded chats in a chat folder for the current user |
| chat\_folder\_count\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of chat folders that the current user can have |
| chat\_folder\_invite\_link\_count\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of shareable chat folders with owned invite links |
| chat\_folder\_new\_chats\_update\_period | Integer | No | *Since TDLib 1.8.24*. The minimum interval between calls to getChatFolderNewChats in shareable chat folders |
| checklist\_task\_count\_max | Integer | No | *Since TDLib 1.8.51*. The maximum number of tasks in a checklist |
| checklist\_task\_text\_length\_max | Integer | No | *Since TDLib 1.8.51*. The maximum length of text of a task in a checklist |
| checklist\_title\_length\_max | Integer | No | *Since TDLib 1.8.51*. The maximum length of title of a checklist |
| commit\_hash | String | No | *Since TDLib 1.8.24*. If known, the hash of the source code commit that was used to build TDLib. Can be received synchronously. |
| community\_bot\_count\_max | Integer | No | *Since TDLib 1.8.67*. The maximum number of bots that can be added to a community |
| community\_chat\_count\_max | Integer | No | *Since TDLib 1.8.67*. The maximum number of supergroups and channels that can be added to a community |
| direct\_channel\_message\_star\_count\_default | Integer | No | *Since TDLib 1.8.50*. Default value for the price of incoming messages in direct channels |
| enabled\_proxy\_id | Integer | No | Identifier of the enabled proxy |
| expect\_blocking | Boolean | No | If true, access to Telegram is likely blocked for the user |
| fact\_check\_length\_max | Integer | No | *Since TDLib 1.8.30*. The maximum allowed length of a fact-check |
| favorite\_stickers\_limit | Integer | No | The maximum number of favorite stickers |
| forwarded\_message\_count\_max | Integer | No | The maximum number of forwarded messages per one request |
| gift\_collection\_count\_max | Integer | No | *Since TDLib 1.8.53*. The maximum number of gift collections |
| gift\_collection\_size\_max | Integer | No | *Since TDLib 1.8.54*. The maximum number of gifts in a gift collection |
| gift\_premium\_from\_attachment\_menu | Boolean | No | *Since TDLib 1.8.24*. If true, then a suggestion to gift Telegram Premium needs to be shown in the attachment menu if appropriate |
| gift\_premium\_from\_input\_field | Boolean | No | *Since TDLib 1.8.24*. If true, then a suggestion to gift Telegram Premium needs to be shown in the input field if appropriate |
| gift\_resale\_earnings\_per\_mille | Integer | No | *TDLib 1.8.49-1.8.52*. The amount of Telegram Stars received by the user for each 1000 Telegram Stars paid for gifts bought from them |
| gift\_resale\_gram\_cent\_count\_max | Integer | No | *Since TDLib 1.8.65*. The maximum price in 1/100 of TON Gram for a gift that is available for resale |
| gift\_resale\_gram\_cent\_count\_min | Integer | No | *Since TDLib 1.8.65*. The minimum price in 1/100 of TON Gram for a gift that is available for resale |
| gift\_resale\_gram\_earnings\_per\_mille | Integer | No | *Since TDLib 1.8.65*. The amount of TON Grams received by the user for each 1000 Grams paid for gifts bought from them |
| gift\_resale\_star\_count\_max | Integer | No | *Since TDLib 1.8.49*. The maximum price in Telegram Stars for a gift that is available for resale |
| gift\_resale\_star\_count\_min | Integer | No | *Since TDLib 1.8.49*. The minimum price in Telegram Stars for a gift that is available for resale |
| gift\_resale\_star\_earnings\_per\_mille | Integer | No | *Since TDLib 1.8.53*. The amount of Telegram Stars received by the user for each 1000 Telegram Stars paid for gifts bought from them |
| gift\_resale\_toncoin\_cent\_count\_max | Integer | No | *TDLib 1.8.53-1.8.64*. The maximum price in 1/100 of TON Gram for a gift that is available for resale |
| gift\_resale\_toncoin\_cent\_count\_min | Integer | No | *TDLib 1.8.53-1.8.64*. The minimum price in 1/100 of TON Gram for a gift that is available for resale |
| gift\_resale\_toncoin\_earnings\_per\_mille | Integer | No | *TDLib 1.8.53-1.8.64*. The amount of TON Grams received by the user for each 1000 Grams paid for gifts bought from them |
| gift\_sell\_period | Integer | No | *Since TDLib 1.8.38*. The number of seconds after gift receiving for which it can be sold for Telegram Stars |
| gift\_text\_length\_max | Integer | No | *Since TDLib 1.8.37*. The maximum length of a message added to a sent gift |
| giveaway\_additional\_chat\_count\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of additional chats that can be added to a giveaway |
| giveaway\_boost\_count\_per\_premium | Integer | No | *Since TDLib 1.8.24*. The number of boosts that received by the channel for each giveaway prize |
| giveaway\_country\_count\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of countries that can be added to a giveaway |
| giveaway\_duration\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of additional chats that can be added to a giveaway |
| gram\_top\_up\_url | String | No | *Since TDLib 1.8.65*. The URL that can be used to top up TON Gram balance of the current user |
| group\_anonymous\_bot\_user\_id | Integer | No | Identifier of the bot which is shown as the sender of anonymous messages in groups when viewed from an outdated client |
| group\_call\_message\_text\_length\_max | Integer | No | *Since TDLib 1.8.56*. The maximum length of a message text in a group call that isn't a live story |
| group\_call\_participant\_count\_max | Integer | No | *Since TDLib 1.8.48*. The maximum number of participants in a group call that is not bound to a chat |
| is\_premium | Boolean | No | *Since TDLib 1.8.24*. If true, then the current user subscribed to Telegram Premium |
| is\_premium\_available | Boolean | No | *Since TDLib 1.8.24*. If true, then the current user can subscribe to Telegram Premium. Otherwise, all premium-related features must be hidden |
| login\_passkey\_count\_max | Integer | No | *Since TDLib 1.8.59*. The maximum number of login passkeys that can be added |
| message\_caption\_length\_max | Integer | No | The maximum length of a message caption |
| message\_reply\_quote\_length\_max | Integer | No | *Since TDLib 1.8.24*. The maximum length of quote from the replied message |
| message\_text\_length\_max | Integer | No | The maximum length of a message text |
| million\_gram\_to\_usd\_rate | Integer | No | *Since TDLib 1.8.65*. The number of US dollars that can be received by selling 1000000 TON Grams on a third-party exchange |
| million\_toncoin\_to\_usd\_rate | Integer | No | *TDLib 1.8.52-1.8.64*. The number of US dollars that can be received by selling 1000000 TON Grams on a third-party exchange |
| monthly\_sent\_story\_count\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of stories that can be posted per month by the current user |
| my\_id | Integer | No | Identifier of the current user |
| notification\_sound\_count\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of saved notification sounds |
| notification\_sound\_duration\_max | Integer | No | *Since TDLib 1.8.24*. The maximum duration of an audio that can be used as a notification sound |
| notification\_sound\_size\_max | Integer | No | *Since TDLib 1.8.24*. The maximum size of the audio file that can be used as a notification sound |
| owned\_bot\_count\_max | Integer | No | *Since TDLib 1.8.63*. The maximum number of bots that can be owned by the current user |
| paid\_group\_call\_message\_star\_count\_max | Integer | No | *Since TDLib 1.8.57*. The maximum number of Telegram Stars that can be set as the price for paid group call messages |
| paid\_media\_message\_star\_count\_max | Integer | No | *Since TDLib 1.8.32*. The maximum price of a paid post in Telegram Stars |
| paid\_message\_earnings\_per\_mille | Integer | No | *Since TDLib 1.8.46*. The amount of Telegram Stars received by the user or the supergroup for each 1000 Telegram Stars paid for their incoming messages |
| paid\_message\_star\_count\_max | Integer | No | *Since TDLib 1.8.46*. The maximum number of Telegram Stars that can be set as the price for paid messages |
| paid\_reaction\_star\_count\_max | Integer | No | *Since TDLib 1.8.35*. The maximum number of Telegram Stars that can be added as paid reaction to a message in one request |
| pending\_text\_message\_period | Integer | No | *Since TDLib 1.8.56*. The maximum number of seconds to show a pending message from a bot |
| photo\_search\_bot\_username | String | No | Username of a bot which can be used in inline mode for photos search |
| pinned\_archived\_chat\_count\_max | Integer | No | The maximum number of pinned cloud chats in the Archive chat list for the current user. The same amount of secret chats can be pinned locally |
| pinned\_chat\_count\_max | Integer | No | The maximum number of pinned cloud chats in the Main chat list for the current user. The same amount of secret chats can be pinned locally |
| pinned\_forum\_topic\_count\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of pinned forum topics |
| pinned\_gift\_count\_max | Integer | No | *Since TDLib 1.8.46*. The maximum number of pinned unique gifts |
| pinned\_saved\_messages\_topic\_count\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of pinned topics in Saved Messages for the current user |
| pinned\_story\_count\_max | Integer | No | *Since TDLib 1.8.29*. The maximum number of pinned stories on a chat page |
| poll\_answer\_count\_max | Integer | No | *Since TDLib 1.8.50*. The maximum number of options in a poll message |
| poll\_country\_count\_max | Integer | No | *Since TDLib 1.8.63*. The maximum number of countries for which a poll can be restricted |
| poll\_open\_period\_max | Integer | No | *Since TDLib 1.8.63*. The maximum amount of time after which the poll may be automatically closed; in seconds |
| premium\_download\_speedup | Integer | No | *Since TDLib 1.8.28*. Approximate number of times file download speed will increase if the user subscribes to Telegram Premium |
| premium\_gift\_boost\_count | Integer | No | *Since TDLib 1.8.24*. The number of boosts that is obtained by gifting Telegram Premium to another user |
| premium\_upload\_speedup | Integer | No | *Since TDLib 1.8.28*. Approximate number of times file upload speed will increase if the user subscribes to Telegram Premium |
| quick\_reply\_shortcut\_count\_max | Integer | No | *Since TDLib 1.8.28*. The maximum number of quick reply shortcuts that can be created by a Telegram Business account |
| quick\_reply\_shortcut\_message\_count\_max | Integer | No | *Since TDLib 1.8.28*. The maximum number of messages that can be added to a quick reply shortcut by a Telegram Business account |
| replies\_bot\_chat\_id | Integer | No | Identifier of the @replies bot |
| rich\_message\_block\_count\_max | Integer | No | *Since TDLib 1.8.65*. The maximum number of blocks in a rich message |
| rich\_message\_depth\_max | Integer | No | *Since TDLib 1.8.65*. The maximum depth of nested blocks in a rich message |
| rich\_message\_media\_count\_max | Integer | No | *Since TDLib 1.8.65*. The maximum number of media files in a rich message |
| rich\_message\_table\_column\_count\_max | Integer | No | *Since TDLib 1.8.65*. The maximum number of columns in a table of a rich message |
| rich\_message\_text\_length\_max | Integer | No | *Since TDLib 1.8.65*. The maximum length of a rich message text |
| show\_message\_edit\_date\_by\_default | Boolean | No | If true, then message edit date must be shown along the message instead of the message send date |
| stake\_dice\_stake\_amount\_max | Integer | No | *Since TDLib 1.8.60*. The maximum amount of TON Grams that can be staked for a roll in nanograms |
| stake\_dice\_stake\_amount\_min | Integer | No | *Since TDLib 1.8.60*. The minimum amount of TON Grams that can be staked for a roll in nanograms |
| star\_withdrawal\_count\_max | Integer | No | *Since TDLib 1.8.52*. The maximum number of Telegram Stars that can be withdrawn |
| star\_withdrawal\_count\_min | Integer | No | *Since TDLib 1.8.31*. The minimum number of Telegram Stars that can be withdrawn |
| story\_album\_count\_max | Integer | No | *Since TDLib 1.8.53*. The maximum number of story albums |
| story\_album\_size\_max | Integer | No | *Since TDLib 1.8.54*. The maximum number of stories in a story album |
| story\_caption\_length\_max | Integer | No | *Since TDLib 1.8.24*. The maximum length of story caption for the current user |
| story\_link\_area\_count\_max | Integer | No | *Since TDLib 1.8.31*. The maximum number of link areas that can be added to a story by Telegram Premium users |
| story\_stealth\_mode\_cooldown\_period | Integer | No | *Since TDLib 1.8.24*. The number of seconds that must pass between before Stealth Mode can be enabled again |
| story\_stealth\_mode\_future\_period | Integer | No | *Since TDLib 1.8.24*. The number of seconds in the future the Stealth Mode will last |
| story\_stealth\_mode\_past\_period | Integer | No | *Since TDLib 1.8.24*. The number of seconds in the past during which all views of stories from the current user will be hidden if Stealth Mode is enabled |
| story\_suggested\_reaction\_area\_count\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of suggested reaction areas that can be added to a story |
| story\_viewers\_expiration\_delay | Integer | No | *Since TDLib 1.8.24*. The number of seconds after story expiration date for which story viewers still can be received |
| subscription\_star\_count\_max | Integer | No | *Since TDLib 1.8.35*. The maximum number of Telegram Stars that can be asked for monthly subscription to a chat |
| suggested\_language\_pack\_id | String | No | Identifier of the language pack, suggested for the user by the server |
| suggested\_post\_gram\_cent\_count\_max | Integer | No | *Since TDLib 1.8.65*. The maximum price of a suggested post in TON Gram cents |
| suggested\_post\_gram\_cent\_count\_min | Integer | No | *Since TDLib 1.8.65*. The minimum price of a suggested post in TON Gram cents |
| suggested\_post\_gram\_earnings\_per\_mille | Integer | No | *Since TDLib 1.8.65*. The amount of TON Grams received by a channel for each 1000 Grams paid for suggested post publication in the channel |
| suggested\_post\_lifetime\_min | Integer | No | *Since TDLib 1.8.52*. The minimum amount of time for which a suggested post must be published in a channel to receive payment for the post; in seconds |
| suggested\_post\_send\_delay\_max | Integer | No | *Since TDLib 1.8.52*. The maximum delay for suggested post publish date; in seconds |
| suggested\_post\_send\_delay\_min | Integer | No | *Since TDLib 1.8.52*. The minimum delay for suggested post publish date; in seconds |
| suggested\_post\_star\_count\_max | Integer | No | *Since TDLib 1.8.52*. The maximum price of a suggested post in Telegram Stars |
| suggested\_post\_star\_count\_min | Integer | No | *Since TDLib 1.8.52*. The minimum price of a suggested post in Telegram Stars |
| suggested\_post\_star\_earnings\_per\_mille | Integer | No | *Since TDLib 1.8.52*. The amount of Telegram Stars received by a channel for each 1000 Telegram Stars paid for suggested post publication in the channel |
| suggested\_post\_toncoin\_cent\_count\_max | Integer | No | *TDLib 1.8.52-1.8.64*. The maximum price of a suggested post in TON Gram cents |
| suggested\_post\_toncoin\_cent\_count\_min | Integer | No | *TDLib 1.8.52-1.8.64*. The minimum price of a suggested post in TON Gram cents |
| suggested\_post\_toncoin\_earnings\_per\_mille | Integer | No | *TDLib 1.8.52-1.8.64*. The amount of TON Grams received by a channel for each 1000 Grams paid for suggested post publication in the channel |
| suggested\_video\_note\_audio\_bitrate | Integer | No | Suggested bit rate for audio encoding in video notes, in kbit/s |
| suggested\_video\_note\_length | Integer | No | Suggested width and height of the video in video notes |
| suggested\_video\_note\_video\_bitrate | Integer | No | Suggested bit rate for video encoding in video notes, in kbit/s |
| supergroup\_size\_max | Integer | No | The maximum number of members in a supergroup |
| t\_me\_url | String | No | Current value of t.me URL, i.e. `https://t.me/` |
| telegram\_service\_notifications\_chat\_id | Integer | No | Identifier of the Telegram Service Notifications chat |
| test\_mode | Boolean | No | If true, the test environment is being used instead of the production environment |
| text\_composition\_style\_example\_count | Integer | No | *Since TDLib 1.8.64*. The number of examples that are available for each text composition style |
| text\_composition\_style\_prompt\_length\_max | Integer | No | *Since TDLib 1.8.64*. The maximum allowed length of the text composition style prompt |
| text\_composition\_style\_title\_length\_max | Integer | No | *Since TDLib 1.8.64*. The maximum allowed length of the text composition style title |
| thousand\_star\_to\_usd\_rate | Integer | No | *Since TDLib 1.8.35*. The number of US dollars that can be received by withdrawing 1000 Telegram Stars |
| ton\_blockchain\_explorer\_url | String | No | *Since TDLib 1.8.45*. A prefix of the URL that can be used to get information about a TON blockchain address |
| toncoin\_top\_up\_url | String | No | *TDLib 1.8.52-1.8.64*. The URL that can be used to top up TON Gram balance of the current user |
| unix\_time | Integer | No | An estimation of the current Unix timestamp. The option will not be updated automatically unless the difference between the previous estimation and the locally available monotonic clocks changes significantly |
| usd\_to\_thousand\_star\_rate | Integer | No | *Since TDLib 1.8.35*. The number of US dollars needed to buy 1000 Telegram Stars |
| user\_note\_text\_length\_max | Integer | No | *Since TDLib 1.8.56*. The maximum length of text of a user note |
| venue\_search\_bot\_username | String | No | Username of a bot which can be used in inline mode for venues search |
| verification\_codes\_bot\_chat\_id | Integer | No | *Since TDLib 1.8.37*. Identifier of the Verification Codes chat with codes from Telegram Gateway |
| version | String | No | TDLib version. This options is guaranteed to come before all other updates. Can be received synchronously. |
| web\_app\_allowed\_protocols | String | No | *Since TDLib 1.8.32*. A space-separated list of URL protocols that are allowed to be open by the call to `web_app_open_link` from Web Apps. |
| weekly\_sent\_story\_count\_max | Integer | No | *Since TDLib 1.8.24*. The maximum number of stories that can be posted per week by the current user |
| welcome\_message\_count\_max | Integer | No | *Since TDLib 1.8.67*. The maximum number of welcome messages that can be added for a chat |

Additionally any option beginning with 'x' or 'X' is writeable and can be safely used by the application to persistently store some small amount of data.