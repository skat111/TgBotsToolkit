# messages.getSearchResultsPositions

Source: https://core.telegram.org/method/messages.getSearchResultsPositions

Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation.

Returns the results in reverse chronological order (i.e., in order of decreasing message_id).

* [Layer 225](https://core.telegram.org/method/messages.getSearchResultsPositions) 
  + [1 – Base layer](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=1)
  + [2 – New userpic notifications](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=2)
  + [3 – Send message can trigger link change](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=3)
  + [4 – Check-in chats](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=4)
  + [5 – Localized SMS, localized notifications](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=5)
  + [6 – Foursquare integration](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=6)
  + [7 – Added wallPaperSolid](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=7)
  + [8 – Added end-to-end encryption](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=8)
  + [9 – Improved big files upload perfomance](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=9)
  + [10 – Improved chat participants updates](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=10)
  + [11 – Improved secret chats](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=11)
  + [12 – New dynamic support](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=12)
  + [13 – Audio, video MIME; contacts import retry; new secret actions](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=13)
  + [14 – Notify settings sync, blacklist sync](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=14)
  + [15 – Modified getHistory offset behaviour](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=15)
  + [16 – Split sendCode into 2 parts](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=16)
  + [17 – Added custom typing, introduced message flags](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=17)
  + [18 – Added usernames](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=18)
  + [23 – Stickers for secret chats](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=23)
  + [105 – Scheduled messages, Cloud themes](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=105)
  + [108 – Login with QR code](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=108)
  + [109 – Polls v2](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=109)
  + [110 – People Nearby 2.0, Bank card entity](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=110)
  + [111 – Folders, Broadcast Stats](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=111)
  + [112 – Old featured stickers, generic dice, poll timer, poll solution](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=112)
  + [113 – PSA](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=113)
  + [114 – Video thumbs for GIFs](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=114)
  + [115 – Peek Channel Invite](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=115)
  + [116 – Group Stats, Profile Videos](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=116)
  + [117 – WebRTC Phone Calls](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=117)
  + [118 – Callback with 2FA, Countries list](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=118)
  + [119 – Comments in channels, Threads, Anonymous Admins](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=119)
  + [120 – Multipins, Message Stats, GeoLive v2](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=120)
  + [121 – SVG-based Outlines for Stickers](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=121)
  + [122 – Voice Chats](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=122)
  + [123 – Voice Chat improvements](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=123)
  + [124 – Expiring Invite links](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=124)
  + [125 – Voice Chats in Broadcasts](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=125)
  + [126 – Ban channels in channels](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=126)
  + [127 – Payments in channels](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=127)
  + [128 – Microthumbs for User/Chat profile photos](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=128)
  + [129 – Video Chats](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=129)
  + [130 – Custom placeholder for bot reply keyboards](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=130)
  + [131 – Reset 2FA Password after a week](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=131)
  + [132 – Chat themes](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=132)
  + [133 – 64-bit IDs for User/Chat](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=133)
  + [134 – Chat Requests, Shared Media Calendar](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=134)
  + [135 – Send Message As a Channel](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=135)
  + [136 – Reactions](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=136)
  + [137 – Translations](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=137)
  + [138 – GIF Sticker Packs](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=138)
  + [139 – RTMP streaming](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=139)
  + [140 – WebApps, Cloud Ringtones](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=140)
  + [142 – TCP Reflectors](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=142)
  + [143 – Premium Subscription, Cloud Invoices](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=143)
  + [144 – Premium as a Gift, Custom Emoji](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=144)
  + [145 – Custom Reactions, Statuses, Sign In with email](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=145)
  + [147 – Keywords for stickers and emojis](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=147)
  + [148 – Forums, collectible usernames](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=148)
  + [150 – Pinned forum topics, general topic](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=150)
  + [151 – Media spoilers, suggested profile photos](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=151)
  + [152 – Real-time translations, Firebase SMS authentication](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=152)
  + [153 – Modify created stickersets](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=153)
  + [155 – Dates for reactions](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=155)
  + [158 – Shared folders, per-chat wallpapers](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=158)
  + [159 – Anonymous votes](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=159)
  + [160 – Stories](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=160)
  + [164 – Stories in Channels](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=164)
  + [166 – Giveaways in channels](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=166)
  + [167 – Similar channels](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=167)
  + [168 – Channel colors](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=168)
  + [169 – Multiselection of chats for bots](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=169)
  + [170 – Saved Messages 2.0](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=170)
  + [171 – Saved Messages 2.0](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=171)
  + [174 – Group boosts](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=174)
  + [176 – Business](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=176)
  + [177 – Business Bots, Birthdays](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=177)
  + [178 – Saved Personal channel, Reactions notifications](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=178)
  + [179 – Channel revenue stats, phrases in SMS](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=179)
  + [180 – Message Effects, Hashtags](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=180)
  + [181 – Stars](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=181)
  + [182 – Stars Revenue](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=182)
  + [183 – Paid posts](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=183)
  + [184 – Stars Refunds](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=184)
  + [185 – MiniApp Store, Star Gifts](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=185)
  + [186 – Channel Subscriptions for Stars](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=186)
  + [187 – Stars Giveaways](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=187)
  + [189 – Stars Gifts](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=189)
  + [192 – Video Qualities, Ads in bots](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=192)
  + [194 – Stars Subscription for Bots](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=194)
  + [195 – Affiliate Programs for Bots](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=195)
  + [196 – Collectible gifts](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=196)
  + [197 – Similar Bots](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=197)
  + [198 – Collectibles as emoji statuses](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=198)
  + [200 – Paid Messages](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=200)
  + [202 – Conference calls](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=202)
  + [203 – Resell collectible gifts](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=203)
  + [204 – Monoforums](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=204)
  + [205 – TODO lists](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=205)
  + [207 – Suggested channel posts](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=207)
  + [210 – Star gift collections, rating](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=210)
  + [211 – Story Albums](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=211)
  + [212 – Prepaid gift upgrades](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=212)
  + [213 – Music in profile](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=213)
  + [214 – Chat Themes with collectible gifts](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=214)
  + [215 – Chat Gift Themes](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=215)
  + [216 – Threaded view for Bots](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=216)
  + [217 – Live Stories](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=217)
  + [218 – Gift Auctions](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=218)
  + [219 – Passkeys](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=219)
  + [220 – Gift Offers](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=220)
  + [222 – Gift Crafts](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=222)
  + [223 – User tags in groups](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=223)
  + [224 – AI Editor, Live photos](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=224)
  + [**225 – Guest mode, Custom AI compose tones**](https://core.telegram.org/method/messages.getSearchResultsPositions?layer=225)
  + [More...](https://core.telegram.org/api/layers)

```
messages.searchResultsPositions#53b22baf count:int positions:Vector<SearchResultsPosition> = messages.SearchResultsPositions;
---functions---
messages.getSearchResultsPositions#9c7f2f10 flags:# peer:InputPeer saved_peer_id:flags.2?InputPeer filter:MessagesFilter offset_id:int limit:int = messages.SearchResultsPositions;
```

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| **flags** | [#](https://core.telegram.org/type/%23) | Flags, see [TL conditional fields](https://core.telegram.org/mtproto/TL-combinators#conditional-fields) |
| **peer** | [InputPeer](https://core.telegram.org/type/InputPeer) | Peer where to search |
| **saved_peer_id** | [flags](https://core.telegram.org/mtproto/TL-combinators#conditional-fields).2?[InputPeer](https://core.telegram.org/type/InputPeer) | Search within the [saved message dialog »](https://core.telegram.org/api/saved-messages) with this ID. |
| **filter** | [MessagesFilter](https://core.telegram.org/type/MessagesFilter) | Message filter, [inputMessagesFilterEmpty](https://core.telegram.org/constructor/inputMessagesFilterEmpty), [inputMessagesFilterMyMentions](https://core.telegram.org/constructor/inputMessagesFilterMyMentions) filters are not supported by this method. |
| **offset_id** | [int](https://core.telegram.org/type/int) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) |
| **limit** | [int](https://core.telegram.org/type/int) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) |

### Result

[messages.SearchResultsPositions](https://core.telegram.org/type/messages.SearchResultsPositions)

### Only users can use this method

### Possible errors

| Code | Type | Description |
| --- | --- | --- |
| 400 | PEER_ID_INVALID | The provided peer id is invalid. |

### Related pages

#### [Saved messages](https://core.telegram.org/api/saved-messages)

The Saved Messages chat allows users to bookmark messages and media: it's a personal cloud storage for any messages or media you may want to send or forward there.

#### [inputMessagesFilterEmpty](https://core.telegram.org/constructor/inputMessagesFilterEmpty)

Filter is absent.

#### [inputMessagesFilterMyMentions](https://core.telegram.org/constructor/inputMessagesFilterMyMentions)

Return only messages where the current user was [mentioned](https://core.telegram.org/api/mentions).

#### [Pagination in the API](https://core.telegram.org/api/offsets)

How to fetch results from large lists of objects.