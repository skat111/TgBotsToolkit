# messages.requestAppWebView

Source: https://core.telegram.org/method/messages.requestAppWebView

Open a [bot mini app](https://core.telegram.org/bots/webapps) from a [direct Mini App deep link](https://core.telegram.org/api/links#direct-mini-app-links), sending over user information after user confirmation.

After calling this method, until the user closes the webview, [messages.prolongWebView](https://core.telegram.org/method/messages.prolongWebView) must be called every 60 seconds.

* [Layer 223](https://core.telegram.org/method/messages.requestAppWebView) 
  + [1 – Base layer](https://core.telegram.org/method/messages.requestAppWebView?layer=1)
  + [2 – New userpic notifications](https://core.telegram.org/method/messages.requestAppWebView?layer=2)
  + [3 – Send message can trigger link change](https://core.telegram.org/method/messages.requestAppWebView?layer=3)
  + [4 – Check-in chats](https://core.telegram.org/method/messages.requestAppWebView?layer=4)
  + [5 – Localized SMS, localized notifications](https://core.telegram.org/method/messages.requestAppWebView?layer=5)
  + [6 – Foursquare integration](https://core.telegram.org/method/messages.requestAppWebView?layer=6)
  + [7 – Added wallPaperSolid](https://core.telegram.org/method/messages.requestAppWebView?layer=7)
  + [8 – Added end-to-end encryption](https://core.telegram.org/method/messages.requestAppWebView?layer=8)
  + [9 – Improved big files upload perfomance](https://core.telegram.org/method/messages.requestAppWebView?layer=9)
  + [10 – Improved chat participants updates](https://core.telegram.org/method/messages.requestAppWebView?layer=10)
  + [11 – Improved secret chats](https://core.telegram.org/method/messages.requestAppWebView?layer=11)
  + [12 – New dynamic support](https://core.telegram.org/method/messages.requestAppWebView?layer=12)
  + [13 – Audio, video MIME; contacts import retry; new secret actions](https://core.telegram.org/method/messages.requestAppWebView?layer=13)
  + [14 – Notify settings sync, blacklist sync](https://core.telegram.org/method/messages.requestAppWebView?layer=14)
  + [15 – Modified getHistory offset behaviour](https://core.telegram.org/method/messages.requestAppWebView?layer=15)
  + [16 – Split sendCode into 2 parts](https://core.telegram.org/method/messages.requestAppWebView?layer=16)
  + [17 – Added custom typing, introduced message flags](https://core.telegram.org/method/messages.requestAppWebView?layer=17)
  + [18 – Added usernames](https://core.telegram.org/method/messages.requestAppWebView?layer=18)
  + [23 – Stickers for secret chats](https://core.telegram.org/method/messages.requestAppWebView?layer=23)
  + [105 – Scheduled messages, Cloud themes](https://core.telegram.org/method/messages.requestAppWebView?layer=105)
  + [108 – Login with QR code](https://core.telegram.org/method/messages.requestAppWebView?layer=108)
  + [109 – Polls v2](https://core.telegram.org/method/messages.requestAppWebView?layer=109)
  + [110 – People Nearby 2.0, Bank card entity](https://core.telegram.org/method/messages.requestAppWebView?layer=110)
  + [111 – Folders, Broadcast Stats](https://core.telegram.org/method/messages.requestAppWebView?layer=111)
  + [112 – Old featured stickers, generic dice, poll timer, poll solution](https://core.telegram.org/method/messages.requestAppWebView?layer=112)
  + [113 – PSA](https://core.telegram.org/method/messages.requestAppWebView?layer=113)
  + [114 – Video thumbs for GIFs](https://core.telegram.org/method/messages.requestAppWebView?layer=114)
  + [115 – Peek Channel Invite](https://core.telegram.org/method/messages.requestAppWebView?layer=115)
  + [116 – Group Stats, Profile Videos](https://core.telegram.org/method/messages.requestAppWebView?layer=116)
  + [117 – WebRTC Phone Calls](https://core.telegram.org/method/messages.requestAppWebView?layer=117)
  + [118 – Callback with 2FA, Countries list](https://core.telegram.org/method/messages.requestAppWebView?layer=118)
  + [119 – Comments in channels, Threads, Anonymous Admins](https://core.telegram.org/method/messages.requestAppWebView?layer=119)
  + [120 – Multipins, Message Stats, GeoLive v2](https://core.telegram.org/method/messages.requestAppWebView?layer=120)
  + [121 – SVG-based Outlines for Stickers](https://core.telegram.org/method/messages.requestAppWebView?layer=121)
  + [122 – Voice Chats](https://core.telegram.org/method/messages.requestAppWebView?layer=122)
  + [123 – Voice Chat improvements](https://core.telegram.org/method/messages.requestAppWebView?layer=123)
  + [124 – Expiring Invite links](https://core.telegram.org/method/messages.requestAppWebView?layer=124)
  + [125 – Voice Chats in Broadcasts](https://core.telegram.org/method/messages.requestAppWebView?layer=125)
  + [126 – Ban channels in channels](https://core.telegram.org/method/messages.requestAppWebView?layer=126)
  + [127 – Payments in channels](https://core.telegram.org/method/messages.requestAppWebView?layer=127)
  + [128 – Microthumbs for User/Chat profile photos](https://core.telegram.org/method/messages.requestAppWebView?layer=128)
  + [129 – Video Chats](https://core.telegram.org/method/messages.requestAppWebView?layer=129)
  + [130 – Custom placeholder for bot reply keyboards](https://core.telegram.org/method/messages.requestAppWebView?layer=130)
  + [131 – Reset 2FA Password after a week](https://core.telegram.org/method/messages.requestAppWebView?layer=131)
  + [132 – Chat themes](https://core.telegram.org/method/messages.requestAppWebView?layer=132)
  + [133 – 64-bit IDs for User/Chat](https://core.telegram.org/method/messages.requestAppWebView?layer=133)
  + [134 – Chat Requests, Shared Media Calendar](https://core.telegram.org/method/messages.requestAppWebView?layer=134)
  + [135 – Send Message As a Channel](https://core.telegram.org/method/messages.requestAppWebView?layer=135)
  + [136 – Reactions](https://core.telegram.org/method/messages.requestAppWebView?layer=136)
  + [137 – Translations](https://core.telegram.org/method/messages.requestAppWebView?layer=137)
  + [138 – GIF Sticker Packs](https://core.telegram.org/method/messages.requestAppWebView?layer=138)
  + [139 – RTMP streaming](https://core.telegram.org/method/messages.requestAppWebView?layer=139)
  + [140 – WebApps, Cloud Ringtones](https://core.telegram.org/method/messages.requestAppWebView?layer=140)
  + [142 – TCP Reflectors](https://core.telegram.org/method/messages.requestAppWebView?layer=142)
  + [143 – Premium Subscription, Cloud Invoices](https://core.telegram.org/method/messages.requestAppWebView?layer=143)
  + [144 – Premium as a Gift, Custom Emoji](https://core.telegram.org/method/messages.requestAppWebView?layer=144)
  + [145 – Custom Reactions, Statuses, Sign In with email](https://core.telegram.org/method/messages.requestAppWebView?layer=145)
  + [147 – Keywords for stickers and emojis](https://core.telegram.org/method/messages.requestAppWebView?layer=147)
  + [148 – Forums, collectible usernames](https://core.telegram.org/method/messages.requestAppWebView?layer=148)
  + [150 – Pinned forum topics, general topic](https://core.telegram.org/method/messages.requestAppWebView?layer=150)
  + [151 – Media spoilers, suggested profile photos](https://core.telegram.org/method/messages.requestAppWebView?layer=151)
  + [152 – Real-time translations, Firebase SMS authentication](https://core.telegram.org/method/messages.requestAppWebView?layer=152)
  + [153 – Modify created stickersets](https://core.telegram.org/method/messages.requestAppWebView?layer=153)
  + [155 – Dates for reactions](https://core.telegram.org/method/messages.requestAppWebView?layer=155)
  + [158 – Shared folders, per-chat wallpapers](https://core.telegram.org/method/messages.requestAppWebView?layer=158)
  + [159 – Anonymous votes](https://core.telegram.org/method/messages.requestAppWebView?layer=159)
  + [160 – Stories](https://core.telegram.org/method/messages.requestAppWebView?layer=160)
  + [164 – Stories in Channels](https://core.telegram.org/method/messages.requestAppWebView?layer=164)
  + [166 – Giveaways in channels](https://core.telegram.org/method/messages.requestAppWebView?layer=166)
  + [167 – Similar channels](https://core.telegram.org/method/messages.requestAppWebView?layer=167)
  + [168 – Channel colors](https://core.telegram.org/method/messages.requestAppWebView?layer=168)
  + [169 – Multiselection of chats for bots](https://core.telegram.org/method/messages.requestAppWebView?layer=169)
  + [170 – Saved Messages 2.0](https://core.telegram.org/method/messages.requestAppWebView?layer=170)
  + [171 – Saved Messages 2.0](https://core.telegram.org/method/messages.requestAppWebView?layer=171)
  + [174 – Group boosts](https://core.telegram.org/method/messages.requestAppWebView?layer=174)
  + [176 – Business](https://core.telegram.org/method/messages.requestAppWebView?layer=176)
  + [177 – Business Bots, Birthdays](https://core.telegram.org/method/messages.requestAppWebView?layer=177)
  + [178 – Saved Personal channel, Reactions notifications](https://core.telegram.org/method/messages.requestAppWebView?layer=178)
  + [179 – Channel revenue stats, phrases in SMS](https://core.telegram.org/method/messages.requestAppWebView?layer=179)
  + [180 – Message Effects, Hashtags](https://core.telegram.org/method/messages.requestAppWebView?layer=180)
  + [181 – Stars](https://core.telegram.org/method/messages.requestAppWebView?layer=181)
  + [182 – Stars Revenue](https://core.telegram.org/method/messages.requestAppWebView?layer=182)
  + [183 – Paid posts](https://core.telegram.org/method/messages.requestAppWebView?layer=183)
  + [184 – Stars Refunds](https://core.telegram.org/method/messages.requestAppWebView?layer=184)
  + [185 – MiniApp Store, Star Gifts](https://core.telegram.org/method/messages.requestAppWebView?layer=185)
  + [186 – Channel Subscriptions for Stars](https://core.telegram.org/method/messages.requestAppWebView?layer=186)
  + [187 – Stars Giveaways](https://core.telegram.org/method/messages.requestAppWebView?layer=187)
  + [189 – Stars Gifts](https://core.telegram.org/method/messages.requestAppWebView?layer=189)
  + [192 – Video Qualities, Ads in bots](https://core.telegram.org/method/messages.requestAppWebView?layer=192)
  + [194 – Stars Subscription for Bots](https://core.telegram.org/method/messages.requestAppWebView?layer=194)
  + [195 – Affiliate Programs for Bots](https://core.telegram.org/method/messages.requestAppWebView?layer=195)
  + [196 – Collectible gifts](https://core.telegram.org/method/messages.requestAppWebView?layer=196)
  + [197 – Similar Bots](https://core.telegram.org/method/messages.requestAppWebView?layer=197)
  + [198 – Collectibles as emoji statuses](https://core.telegram.org/method/messages.requestAppWebView?layer=198)
  + [200 – Paid Messages](https://core.telegram.org/method/messages.requestAppWebView?layer=200)
  + [202 – Conference calls](https://core.telegram.org/method/messages.requestAppWebView?layer=202)
  + [203 – Resell collectible gifts](https://core.telegram.org/method/messages.requestAppWebView?layer=203)
  + [204 – Monoforums](https://core.telegram.org/method/messages.requestAppWebView?layer=204)
  + [205 – TODO lists](https://core.telegram.org/method/messages.requestAppWebView?layer=205)
  + [207 – Suggested channel posts](https://core.telegram.org/method/messages.requestAppWebView?layer=207)
  + [210 – Star gift collections, rating](https://core.telegram.org/method/messages.requestAppWebView?layer=210)
  + [211 – Story Albums](https://core.telegram.org/method/messages.requestAppWebView?layer=211)
  + [212 – Prepaid gift upgrades](https://core.telegram.org/method/messages.requestAppWebView?layer=212)
  + [213 – Music in profile](https://core.telegram.org/method/messages.requestAppWebView?layer=213)
  + [214 – Chat Themes with collectible gifts](https://core.telegram.org/method/messages.requestAppWebView?layer=214)
  + [215 – Chat Gift Themes](https://core.telegram.org/method/messages.requestAppWebView?layer=215)
  + [216 – Threaded view for Bots](https://core.telegram.org/method/messages.requestAppWebView?layer=216)
  + [217 – Live Stories](https://core.telegram.org/method/messages.requestAppWebView?layer=217)
  + [218 – Gift Auctions](https://core.telegram.org/method/messages.requestAppWebView?layer=218)
  + [219 – Passkeys](https://core.telegram.org/method/messages.requestAppWebView?layer=219)
  + [220 – Gift Offers](https://core.telegram.org/method/messages.requestAppWebView?layer=220)
  + [222 – Gift Crafts](https://core.telegram.org/method/messages.requestAppWebView?layer=222)
  + [**223 – User tags in groups**](https://core.telegram.org/method/messages.requestAppWebView?layer=223)
  + [More...](https://core.telegram.org/api/layers)

```
webViewResultUrl#4d22ff98 flags:# fullsize:flags.1?true fullscreen:flags.2?true query_id:flags.0?long url:string = WebViewResult;
---functions---
messages.requestAppWebView#53618bce flags:# write_allowed:flags.0?true compact:flags.7?true fullscreen:flags.8?true peer:InputPeer app:InputBotApp start_param:flags.1?string theme_params:flags.2?DataJSON platform:string = WebViewResult;
```

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| **flags** | [#](https://core.telegram.org/type/%23) | Flags, see [TL conditional fields](https://core.telegram.org/mtproto/TL-combinators#conditional-fields) |
| **write_allowed** | [flags](https://core.telegram.org/mtproto/TL-combinators#conditional-fields).0?[true](https://core.telegram.org/constructor/true) | Set this flag if the bot is asking permission to send messages to the user as specified in the [direct Mini App deep link](https://core.telegram.org/api/links#direct-mini-app-links) docs, and the user agreed. |
| **compact** | [flags](https://core.telegram.org/mtproto/TL-combinators#conditional-fields).7?[true](https://core.telegram.org/constructor/true) | If set, requests to open the mini app in compact mode (as opposed to normal or fullscreen mode). Must be set if the `mode` parameter of the [direct Mini App deep link](https://core.telegram.org/api/links#direct-mini-app-links) is equal to `compact`. |
| **fullscreen** | [flags](https://core.telegram.org/mtproto/TL-combinators#conditional-fields).8?[true](https://core.telegram.org/constructor/true) | If set, requests to open the mini app in fullscreen mode (as opposed to compact or normal mode). Must be set if the `mode` parameter of the [direct Mini App deep link](https://core.telegram.org/api/links#direct-mini-app-links) is equal to `fullscreen`. |
| **peer** | [InputPeer](https://core.telegram.org/type/InputPeer) | If the client has clicked on the link in a Telegram chat, pass the chat's peer information; otherwise pass the bot's peer information, instead. |
| **app** | [InputBotApp](https://core.telegram.org/type/InputBotApp) | The app obtained by invoking [messages.getBotApp](https://core.telegram.org/method/messages.getBotApp) as specified in the [direct Mini App deep link](https://core.telegram.org/api/links#direct-mini-app-links) docs. |
| **start_param** | [flags](https://core.telegram.org/mtproto/TL-combinators#conditional-fields).1?[string](https://core.telegram.org/type/string) | If the `startapp` query string parameter is present in the [direct Mini App deep link](https://core.telegram.org/api/links#direct-mini-app-links), pass it to `start_param`. |
| **theme_params** | [flags](https://core.telegram.org/mtproto/TL-combinators#conditional-fields).2?[DataJSON](https://core.telegram.org/type/DataJSON) | [Theme parameters »](https://core.telegram.org/api/bots/webapps#theme-parameters) |
| **platform** | [string](https://core.telegram.org/type/string) | Short name of the application; 0-64 English letters, digits, and underscores |

### Result

[WebViewResult](https://core.telegram.org/type/WebViewResult)

### Only users can use this method

### Possible errors

| Code | Type | Description |
| --- | --- | --- |
| 400 | BOT_APP_BOT_INVALID | The bot_id passed in the inputBotAppShortName constructor is invalid. |
| 400 | BOT_APP_INVALID | The specified bot app is invalid. |
| 400 | BOT_APP_SHORTNAME_INVALID | The specified bot app short name is invalid. |
| 400 | MSG_ID_INVALID | Invalid message ID provided. |
| 400 | THEME_PARAMS_INVALID | The specified `theme_params` field is invalid. |

### Related pages

#### [Deep links](https://core.telegram.org/api/links)

Telegram clients must handle special tg:// and t.me deep links encountered in messages, link entities and in other apps by registering OS handlers.

#### [messages.getBotApp](https://core.telegram.org/method/messages.getBotApp)

Obtain information about a [direct link Mini App](https://core.telegram.org/api/bots/webapps#direct-link-mini-apps)

#### [Mini Apps on Telegram](https://core.telegram.org/api/bots/webapps)

Bots can offer users interactive HTML5 web apps to completely replace any website.

#### [Telegram Mini Apps](https://core.telegram.org/bots/webapps)

#### [messages.prolongWebView](https://core.telegram.org/method/messages.prolongWebView)

Indicate to the server (from the user side) that the user is still using a web app.

If the method returns a `QUERY_ID_INVALID` error, the webview must be closed.