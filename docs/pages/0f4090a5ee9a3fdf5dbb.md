# messages.summarizeText

Source: https://core.telegram.org/method/messages.summarizeText

Summarize the contents of a message with AI, see [here »](https://core.telegram.org/api/ai#summarize-messages) for more info.

Clients should use [message](https://core.telegram.org/constructor/message).`summary_from_language` as a hint for showing a summarization button; its absence does not forbid invoking this method.

* [Layer 223](https://core.telegram.org/method/messages.summarizeText#) 
  + [1 – Base layer](https://core.telegram.org/method/messages.summarizeText?layer=1)
  + [2 – New userpic notifications](https://core.telegram.org/method/messages.summarizeText?layer=2)
  + [3 – Send message can trigger link change](https://core.telegram.org/method/messages.summarizeText?layer=3)
  + [4 – Check-in chats](https://core.telegram.org/method/messages.summarizeText?layer=4)
  + [5 – Localized SMS, localized notifications](https://core.telegram.org/method/messages.summarizeText?layer=5)
  + [6 – Foursquare integration](https://core.telegram.org/method/messages.summarizeText?layer=6)
  + [7 – Added wallPaperSolid](https://core.telegram.org/method/messages.summarizeText?layer=7)
  + [8 – Added end-to-end encryption](https://core.telegram.org/method/messages.summarizeText?layer=8)
  + [9 – Improved big files upload perfomance](https://core.telegram.org/method/messages.summarizeText?layer=9)
  + [10 – Improved chat participants updates](https://core.telegram.org/method/messages.summarizeText?layer=10)
  + [11 – Improved secret chats](https://core.telegram.org/method/messages.summarizeText?layer=11)
  + [12 – New dynamic support](https://core.telegram.org/method/messages.summarizeText?layer=12)
  + [13 – Audio, video MIME; contacts import retry; new secret actions](https://core.telegram.org/method/messages.summarizeText?layer=13)
  + [14 – Notify settings sync, blacklist sync](https://core.telegram.org/method/messages.summarizeText?layer=14)
  + [15 – Modified getHistory offset behaviour](https://core.telegram.org/method/messages.summarizeText?layer=15)
  + [16 – Split sendCode into 2 parts](https://core.telegram.org/method/messages.summarizeText?layer=16)
  + [17 – Added custom typing, introduced message flags](https://core.telegram.org/method/messages.summarizeText?layer=17)
  + [18 – Added usernames](https://core.telegram.org/method/messages.summarizeText?layer=18)
  + [23 – Stickers for secret chats](https://core.telegram.org/method/messages.summarizeText?layer=23)
  + [105 – Scheduled messages, Cloud themes](https://core.telegram.org/method/messages.summarizeText?layer=105)
  + [108 – Login with QR code](https://core.telegram.org/method/messages.summarizeText?layer=108)
  + [109 – Polls v2](https://core.telegram.org/method/messages.summarizeText?layer=109)
  + [110 – People Nearby 2.0, Bank card entity](https://core.telegram.org/method/messages.summarizeText?layer=110)
  + [111 – Folders, Broadcast Stats](https://core.telegram.org/method/messages.summarizeText?layer=111)
  + [112 – Old featured stickers, generic dice, poll timer, poll solution](https://core.telegram.org/method/messages.summarizeText?layer=112)
  + [113 – PSA](https://core.telegram.org/method/messages.summarizeText?layer=113)
  + [114 – Video thumbs for GIFs](https://core.telegram.org/method/messages.summarizeText?layer=114)
  + [115 – Peek Channel Invite](https://core.telegram.org/method/messages.summarizeText?layer=115)
  + [116 – Group Stats, Profile Videos](https://core.telegram.org/method/messages.summarizeText?layer=116)
  + [117 – WebRTC Phone Calls](https://core.telegram.org/method/messages.summarizeText?layer=117)
  + [118 – Callback with 2FA, Countries list](https://core.telegram.org/method/messages.summarizeText?layer=118)
  + [119 – Comments in channels, Threads, Anonymous Admins](https://core.telegram.org/method/messages.summarizeText?layer=119)
  + [120 – Multipins, Message Stats, GeoLive v2](https://core.telegram.org/method/messages.summarizeText?layer=120)
  + [121 – SVG-based Outlines for Stickers](https://core.telegram.org/method/messages.summarizeText?layer=121)
  + [122 – Voice Chats](https://core.telegram.org/method/messages.summarizeText?layer=122)
  + [123 – Voice Chat improvements](https://core.telegram.org/method/messages.summarizeText?layer=123)
  + [124 – Expiring Invite links](https://core.telegram.org/method/messages.summarizeText?layer=124)
  + [125 – Voice Chats in Broadcasts](https://core.telegram.org/method/messages.summarizeText?layer=125)
  + [126 – Ban channels in channels](https://core.telegram.org/method/messages.summarizeText?layer=126)
  + [127 – Payments in channels](https://core.telegram.org/method/messages.summarizeText?layer=127)
  + [128 – Microthumbs for User/Chat profile photos](https://core.telegram.org/method/messages.summarizeText?layer=128)
  + [129 – Video Chats](https://core.telegram.org/method/messages.summarizeText?layer=129)
  + [130 – Custom placeholder for bot reply keyboards](https://core.telegram.org/method/messages.summarizeText?layer=130)
  + [131 – Reset 2FA Password after a week](https://core.telegram.org/method/messages.summarizeText?layer=131)
  + [132 – Chat themes](https://core.telegram.org/method/messages.summarizeText?layer=132)
  + [133 – 64-bit IDs for User/Chat](https://core.telegram.org/method/messages.summarizeText?layer=133)
  + [134 – Chat Requests, Shared Media Calendar](https://core.telegram.org/method/messages.summarizeText?layer=134)
  + [135 – Send Message As a Channel](https://core.telegram.org/method/messages.summarizeText?layer=135)
  + [136 – Reactions](https://core.telegram.org/method/messages.summarizeText?layer=136)
  + [137 – Translations](https://core.telegram.org/method/messages.summarizeText?layer=137)
  + [138 – GIF Sticker Packs](https://core.telegram.org/method/messages.summarizeText?layer=138)
  + [139 – RTMP streaming](https://core.telegram.org/method/messages.summarizeText?layer=139)
  + [140 – WebApps, Cloud Ringtones](https://core.telegram.org/method/messages.summarizeText?layer=140)
  + [142 – TCP Reflectors](https://core.telegram.org/method/messages.summarizeText?layer=142)
  + [143 – Premium Subscription, Cloud Invoices](https://core.telegram.org/method/messages.summarizeText?layer=143)
  + [144 – Premium as a Gift, Custom Emoji](https://core.telegram.org/method/messages.summarizeText?layer=144)
  + [145 – Custom Reactions, Statuses, Sign In with email](https://core.telegram.org/method/messages.summarizeText?layer=145)
  + [147 – Keywords for stickers and emojis](https://core.telegram.org/method/messages.summarizeText?layer=147)
  + [148 – Forums, collectible usernames](https://core.telegram.org/method/messages.summarizeText?layer=148)
  + [150 – Pinned forum topics, general topic](https://core.telegram.org/method/messages.summarizeText?layer=150)
  + [151 – Media spoilers, suggested profile photos](https://core.telegram.org/method/messages.summarizeText?layer=151)
  + [152 – Real-time translations, Firebase SMS authentication](https://core.telegram.org/method/messages.summarizeText?layer=152)
  + [153 – Modify created stickersets](https://core.telegram.org/method/messages.summarizeText?layer=153)
  + [155 – Dates for reactions](https://core.telegram.org/method/messages.summarizeText?layer=155)
  + [158 – Shared folders, per-chat wallpapers](https://core.telegram.org/method/messages.summarizeText?layer=158)
  + [159 – Anonymous votes](https://core.telegram.org/method/messages.summarizeText?layer=159)
  + [160 – Stories](https://core.telegram.org/method/messages.summarizeText?layer=160)
  + [164 – Stories in Channels](https://core.telegram.org/method/messages.summarizeText?layer=164)
  + [166 – Giveaways in channels](https://core.telegram.org/method/messages.summarizeText?layer=166)
  + [167 – Similar channels](https://core.telegram.org/method/messages.summarizeText?layer=167)
  + [168 – Channel colors](https://core.telegram.org/method/messages.summarizeText?layer=168)
  + [169 – Multiselection of chats for bots](https://core.telegram.org/method/messages.summarizeText?layer=169)
  + [170 – Saved Messages 2.0](https://core.telegram.org/method/messages.summarizeText?layer=170)
  + [171 – Saved Messages 2.0](https://core.telegram.org/method/messages.summarizeText?layer=171)
  + [174 – Group boosts](https://core.telegram.org/method/messages.summarizeText?layer=174)
  + [176 – Business](https://core.telegram.org/method/messages.summarizeText?layer=176)
  + [177 – Business Bots, Birthdays](https://core.telegram.org/method/messages.summarizeText?layer=177)
  + [178 – Saved Personal channel, Reactions notifications](https://core.telegram.org/method/messages.summarizeText?layer=178)
  + [179 – Channel revenue stats, phrases in SMS](https://core.telegram.org/method/messages.summarizeText?layer=179)
  + [180 – Message Effects, Hashtags](https://core.telegram.org/method/messages.summarizeText?layer=180)
  + [181 – Stars](https://core.telegram.org/method/messages.summarizeText?layer=181)
  + [182 – Stars Revenue](https://core.telegram.org/method/messages.summarizeText?layer=182)
  + [183 – Paid posts](https://core.telegram.org/method/messages.summarizeText?layer=183)
  + [184 – Stars Refunds](https://core.telegram.org/method/messages.summarizeText?layer=184)
  + [185 – MiniApp Store, Star Gifts](https://core.telegram.org/method/messages.summarizeText?layer=185)
  + [186 – Channel Subscriptions for Stars](https://core.telegram.org/method/messages.summarizeText?layer=186)
  + [187 – Stars Giveaways](https://core.telegram.org/method/messages.summarizeText?layer=187)
  + [189 – Stars Gifts](https://core.telegram.org/method/messages.summarizeText?layer=189)
  + [192 – Video Qualities, Ads in bots](https://core.telegram.org/method/messages.summarizeText?layer=192)
  + [194 – Stars Subscription for Bots](https://core.telegram.org/method/messages.summarizeText?layer=194)
  + [195 – Affiliate Programs for Bots](https://core.telegram.org/method/messages.summarizeText?layer=195)
  + [196 – Collectible gifts](https://core.telegram.org/method/messages.summarizeText?layer=196)
  + [197 – Similar Bots](https://core.telegram.org/method/messages.summarizeText?layer=197)
  + [198 – Collectibles as emoji statuses](https://core.telegram.org/method/messages.summarizeText?layer=198)
  + [200 – Paid Messages](https://core.telegram.org/method/messages.summarizeText?layer=200)
  + [202 – Conference calls](https://core.telegram.org/method/messages.summarizeText?layer=202)
  + [203 – Resell collectible gifts](https://core.telegram.org/method/messages.summarizeText?layer=203)
  + [204 – Monoforums](https://core.telegram.org/method/messages.summarizeText?layer=204)
  + [205 – TODO lists](https://core.telegram.org/method/messages.summarizeText?layer=205)
  + [207 – Suggested channel posts](https://core.telegram.org/method/messages.summarizeText?layer=207)
  + [210 – Star gift collections, rating](https://core.telegram.org/method/messages.summarizeText?layer=210)
  + [211 – Story Albums](https://core.telegram.org/method/messages.summarizeText?layer=211)
  + [212 – Prepaid gift upgrades](https://core.telegram.org/method/messages.summarizeText?layer=212)
  + [213 – Music in profile](https://core.telegram.org/method/messages.summarizeText?layer=213)
  + [214 – Chat Themes with collectible gifts](https://core.telegram.org/method/messages.summarizeText?layer=214)
  + [215 – Chat Gift Themes](https://core.telegram.org/method/messages.summarizeText?layer=215)
  + [216 – Threaded view for Bots](https://core.telegram.org/method/messages.summarizeText?layer=216)
  + [217 – Live Stories](https://core.telegram.org/method/messages.summarizeText?layer=217)
  + [218 – Gift Auctions](https://core.telegram.org/method/messages.summarizeText?layer=218)
  + [219 – Passkeys](https://core.telegram.org/method/messages.summarizeText?layer=219)
  + [220 – Gift Offers](https://core.telegram.org/method/messages.summarizeText?layer=220)
  + [222 – Gift Crafts](https://core.telegram.org/method/messages.summarizeText?layer=222)
  + [**223 – User tags in groups**](https://core.telegram.org/method/messages.summarizeText?layer=223)
  + [More...](https://core.telegram.org/api/layers)

```
textWithEntities#751f3146 text:string entities:Vector<MessageEntity> = TextWithEntities;
---functions---
messages.summarizeText#9d4104e2 flags:# peer:InputPeer id:int to_lang:flags.0?string = TextWithEntities;
```

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| **flags** | [#](https://core.telegram.org/type/%23) | Flags, see [TL conditional fields](https://core.telegram.org/mtproto/TL-combinators#conditional-fields) |
| **peer** | [InputPeer](https://core.telegram.org/type/InputPeer) | The peer where the message is located. |
| **id** | [int](https://core.telegram.org/type/int) | Message ID. |
| **to\_lang** | [flags](https://core.telegram.org/mtproto/TL-combinators#conditional-fields).0?[string](https://core.telegram.org/type/string) | If set, generates the summary in the specified target language (two-letter ISO 639-1 language code) instead of the message's language. |
| **tone** | [flags](https://core.telegram.org/mtproto/TL-combinators#conditional-fields).2?[string](https://core.telegram.org/type/string) | If set, rephrases the summary using the specified [AI composer tone »](https://core.telegram.org/api/ai#ai-compose-tones) (pass the tone identifier) |

### Result

[TextWithEntities](https://core.telegram.org/type/TextWithEntities)

### Only users can use this method

### Possible errors

| Code | Type | Description |
| --- | --- | --- |
| 400 | INPUT\_TEXT\_TOO\_LONG | The specified text is too long. |
| 400 | MSG\_ID\_INVALID | Invalid message ID provided. |
| 400 | PEER\_ID\_INVALID | The provided peer id is invalid. |

### Related pages

#### [AI features](https://core.telegram.org/api/ai)

Telegram offers many AI features powered by Cocoon — a decentralized network designed to maximize privacy.

#### [message](https://core.telegram.org/constructor/message)

A message