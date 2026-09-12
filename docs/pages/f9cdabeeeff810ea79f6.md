# DocumentAttribute

Source: https://core.telegram.org/type/DocumentAttribute

Various possible attributes of a document (used to define if it's a sticker, a GIF, a video, a mask sticker, an image, an audio, and so on)

#### [End-to-end schema](https://core.telegram.org/schema/end-to-end)

```
===23===
documentAttributeAnimated#11b58939 = DocumentAttribute;
documentAttributeAudio#051448e5 duration:int = DocumentAttribute;
documentAttributeFilename#15590068 file_name:string = DocumentAttribute;
documentAttributeImageSize#6c37c15c w:int h:int = DocumentAttribute;
documentAttributeSticker#fb0a5727 = DocumentAttribute;
documentAttributeVideo#5910cccb duration:int w:int h:int = DocumentAttribute;

===45===
documentAttributeAudio#ded218e0 duration:int title:string performer:string = DocumentAttribute;
documentAttributeSticker#3a556302 alt:string stickerset:InputStickerSet = DocumentAttribute;

===46===
documentAttributeAudio#9852f9c6 flags:# duration:int title:flags.0?string performer:flags.1?string waveform:flags.2?bytes = DocumentAttribute;

===66===
documentAttributeVideo#0ef02ce6 flags:# duration:int w:int h:int = DocumentAttribute;
```

API schema:

* [Layer 223](https://core.telegram.org/type/DocumentAttribute) 
  + [1 – Base layer](https://core.telegram.org/type/DocumentAttribute?layer=1)
  + [2 – New userpic notifications](https://core.telegram.org/type/DocumentAttribute?layer=2)
  + [3 – Send message can trigger link change](https://core.telegram.org/type/DocumentAttribute?layer=3)
  + [4 – Check-in chats](https://core.telegram.org/type/DocumentAttribute?layer=4)
  + [5 – Localized SMS, localized notifications](https://core.telegram.org/type/DocumentAttribute?layer=5)
  + [6 – Foursquare integration](https://core.telegram.org/type/DocumentAttribute?layer=6)
  + [7 – Added wallPaperSolid](https://core.telegram.org/type/DocumentAttribute?layer=7)
  + [8 – Added end-to-end encryption](https://core.telegram.org/type/DocumentAttribute?layer=8)
  + [9 – Improved big files upload perfomance](https://core.telegram.org/type/DocumentAttribute?layer=9)
  + [10 – Improved chat participants updates](https://core.telegram.org/type/DocumentAttribute?layer=10)
  + [11 – Improved secret chats](https://core.telegram.org/type/DocumentAttribute?layer=11)
  + [12 – New dynamic support](https://core.telegram.org/type/DocumentAttribute?layer=12)
  + [13 – Audio, video MIME; contacts import retry; new secret actions](https://core.telegram.org/type/DocumentAttribute?layer=13)
  + [14 – Notify settings sync, blacklist sync](https://core.telegram.org/type/DocumentAttribute?layer=14)
  + [15 – Modified getHistory offset behaviour](https://core.telegram.org/type/DocumentAttribute?layer=15)
  + [16 – Split sendCode into 2 parts](https://core.telegram.org/type/DocumentAttribute?layer=16)
  + [17 – Added custom typing, introduced message flags](https://core.telegram.org/type/DocumentAttribute?layer=17)
  + [18 – Added usernames](https://core.telegram.org/type/DocumentAttribute?layer=18)
  + [23 – Stickers for secret chats](https://core.telegram.org/type/DocumentAttribute?layer=23)
  + [105 – Scheduled messages, Cloud themes](https://core.telegram.org/type/DocumentAttribute?layer=105)
  + [108 – Login with QR code](https://core.telegram.org/type/DocumentAttribute?layer=108)
  + [109 – Polls v2](https://core.telegram.org/type/DocumentAttribute?layer=109)
  + [110 – People Nearby 2.0, Bank card entity](https://core.telegram.org/type/DocumentAttribute?layer=110)
  + [111 – Folders, Broadcast Stats](https://core.telegram.org/type/DocumentAttribute?layer=111)
  + [112 – Old featured stickers, generic dice, poll timer, poll solution](https://core.telegram.org/type/DocumentAttribute?layer=112)
  + [113 – PSA](https://core.telegram.org/type/DocumentAttribute?layer=113)
  + [114 – Video thumbs for GIFs](https://core.telegram.org/type/DocumentAttribute?layer=114)
  + [115 – Peek Channel Invite](https://core.telegram.org/type/DocumentAttribute?layer=115)
  + [116 – Group Stats, Profile Videos](https://core.telegram.org/type/DocumentAttribute?layer=116)
  + [117 – WebRTC Phone Calls](https://core.telegram.org/type/DocumentAttribute?layer=117)
  + [118 – Callback with 2FA, Countries list](https://core.telegram.org/type/DocumentAttribute?layer=118)
  + [119 – Comments in channels, Threads, Anonymous Admins](https://core.telegram.org/type/DocumentAttribute?layer=119)
  + [120 – Multipins, Message Stats, GeoLive v2](https://core.telegram.org/type/DocumentAttribute?layer=120)
  + [121 – SVG-based Outlines for Stickers](https://core.telegram.org/type/DocumentAttribute?layer=121)
  + [122 – Voice Chats](https://core.telegram.org/type/DocumentAttribute?layer=122)
  + [123 – Voice Chat improvements](https://core.telegram.org/type/DocumentAttribute?layer=123)
  + [124 – Expiring Invite links](https://core.telegram.org/type/DocumentAttribute?layer=124)
  + [125 – Voice Chats in Broadcasts](https://core.telegram.org/type/DocumentAttribute?layer=125)
  + [126 – Ban channels in channels](https://core.telegram.org/type/DocumentAttribute?layer=126)
  + [127 – Payments in channels](https://core.telegram.org/type/DocumentAttribute?layer=127)
  + [128 – Microthumbs for User/Chat profile photos](https://core.telegram.org/type/DocumentAttribute?layer=128)
  + [129 – Video Chats](https://core.telegram.org/type/DocumentAttribute?layer=129)
  + [130 – Custom placeholder for bot reply keyboards](https://core.telegram.org/type/DocumentAttribute?layer=130)
  + [131 – Reset 2FA Password after a week](https://core.telegram.org/type/DocumentAttribute?layer=131)
  + [132 – Chat themes](https://core.telegram.org/type/DocumentAttribute?layer=132)
  + [133 – 64-bit IDs for User/Chat](https://core.telegram.org/type/DocumentAttribute?layer=133)
  + [134 – Chat Requests, Shared Media Calendar](https://core.telegram.org/type/DocumentAttribute?layer=134)
  + [135 – Send Message As a Channel](https://core.telegram.org/type/DocumentAttribute?layer=135)
  + [136 – Reactions](https://core.telegram.org/type/DocumentAttribute?layer=136)
  + [137 – Translations](https://core.telegram.org/type/DocumentAttribute?layer=137)
  + [138 – GIF Sticker Packs](https://core.telegram.org/type/DocumentAttribute?layer=138)
  + [139 – RTMP streaming](https://core.telegram.org/type/DocumentAttribute?layer=139)
  + [140 – WebApps, Cloud Ringtones](https://core.telegram.org/type/DocumentAttribute?layer=140)
  + [142 – TCP Reflectors](https://core.telegram.org/type/DocumentAttribute?layer=142)
  + [143 – Premium Subscription, Cloud Invoices](https://core.telegram.org/type/DocumentAttribute?layer=143)
  + [144 – Premium as a Gift, Custom Emoji](https://core.telegram.org/type/DocumentAttribute?layer=144)
  + [145 – Custom Reactions, Statuses, Sign In with email](https://core.telegram.org/type/DocumentAttribute?layer=145)
  + [147 – Keywords for stickers and emojis](https://core.telegram.org/type/DocumentAttribute?layer=147)
  + [148 – Forums, collectible usernames](https://core.telegram.org/type/DocumentAttribute?layer=148)
  + [150 – Pinned forum topics, general topic](https://core.telegram.org/type/DocumentAttribute?layer=150)
  + [151 – Media spoilers, suggested profile photos](https://core.telegram.org/type/DocumentAttribute?layer=151)
  + [152 – Real-time translations, Firebase SMS authentication](https://core.telegram.org/type/DocumentAttribute?layer=152)
  + [153 – Modify created stickersets](https://core.telegram.org/type/DocumentAttribute?layer=153)
  + [155 – Dates for reactions](https://core.telegram.org/type/DocumentAttribute?layer=155)
  + [158 – Shared folders, per-chat wallpapers](https://core.telegram.org/type/DocumentAttribute?layer=158)
  + [159 – Anonymous votes](https://core.telegram.org/type/DocumentAttribute?layer=159)
  + [160 – Stories](https://core.telegram.org/type/DocumentAttribute?layer=160)
  + [164 – Stories in Channels](https://core.telegram.org/type/DocumentAttribute?layer=164)
  + [166 – Giveaways in channels](https://core.telegram.org/type/DocumentAttribute?layer=166)
  + [167 – Similar channels](https://core.telegram.org/type/DocumentAttribute?layer=167)
  + [168 – Channel colors](https://core.telegram.org/type/DocumentAttribute?layer=168)
  + [169 – Multiselection of chats for bots](https://core.telegram.org/type/DocumentAttribute?layer=169)
  + [170 – Saved Messages 2.0](https://core.telegram.org/type/DocumentAttribute?layer=170)
  + [171 – Saved Messages 2.0](https://core.telegram.org/type/DocumentAttribute?layer=171)
  + [174 – Group boosts](https://core.telegram.org/type/DocumentAttribute?layer=174)
  + [176 – Business](https://core.telegram.org/type/DocumentAttribute?layer=176)
  + [177 – Business Bots, Birthdays](https://core.telegram.org/type/DocumentAttribute?layer=177)
  + [178 – Saved Personal channel, Reactions notifications](https://core.telegram.org/type/DocumentAttribute?layer=178)
  + [179 – Channel revenue stats, phrases in SMS](https://core.telegram.org/type/DocumentAttribute?layer=179)
  + [180 – Message Effects, Hashtags](https://core.telegram.org/type/DocumentAttribute?layer=180)
  + [181 – Stars](https://core.telegram.org/type/DocumentAttribute?layer=181)
  + [182 – Stars Revenue](https://core.telegram.org/type/DocumentAttribute?layer=182)
  + [183 – Paid posts](https://core.telegram.org/type/DocumentAttribute?layer=183)
  + [184 – Stars Refunds](https://core.telegram.org/type/DocumentAttribute?layer=184)
  + [185 – MiniApp Store, Star Gifts](https://core.telegram.org/type/DocumentAttribute?layer=185)
  + [186 – Channel Subscriptions for Stars](https://core.telegram.org/type/DocumentAttribute?layer=186)
  + [187 – Stars Giveaways](https://core.telegram.org/type/DocumentAttribute?layer=187)
  + [189 – Stars Gifts](https://core.telegram.org/type/DocumentAttribute?layer=189)
  + [192 – Video Qualities, Ads in bots](https://core.telegram.org/type/DocumentAttribute?layer=192)
  + [194 – Stars Subscription for Bots](https://core.telegram.org/type/DocumentAttribute?layer=194)
  + [195 – Affiliate Programs for Bots](https://core.telegram.org/type/DocumentAttribute?layer=195)
  + [196 – Collectible gifts](https://core.telegram.org/type/DocumentAttribute?layer=196)
  + [197 – Similar Bots](https://core.telegram.org/type/DocumentAttribute?layer=197)
  + [198 – Collectibles as emoji statuses](https://core.telegram.org/type/DocumentAttribute?layer=198)
  + [200 – Paid Messages](https://core.telegram.org/type/DocumentAttribute?layer=200)
  + [202 – Conference calls](https://core.telegram.org/type/DocumentAttribute?layer=202)
  + [203 – Resell collectible gifts](https://core.telegram.org/type/DocumentAttribute?layer=203)
  + [204 – Monoforums](https://core.telegram.org/type/DocumentAttribute?layer=204)
  + [205 – TODO lists](https://core.telegram.org/type/DocumentAttribute?layer=205)
  + [207 – Suggested channel posts](https://core.telegram.org/type/DocumentAttribute?layer=207)
  + [210 – Star gift collections, rating](https://core.telegram.org/type/DocumentAttribute?layer=210)
  + [211 – Story Albums](https://core.telegram.org/type/DocumentAttribute?layer=211)
  + [212 – Prepaid gift upgrades](https://core.telegram.org/type/DocumentAttribute?layer=212)
  + [213 – Music in profile](https://core.telegram.org/type/DocumentAttribute?layer=213)
  + [214 – Chat Themes with collectible gifts](https://core.telegram.org/type/DocumentAttribute?layer=214)
  + [215 – Chat Gift Themes](https://core.telegram.org/type/DocumentAttribute?layer=215)
  + [216 – Threaded view for Bots](https://core.telegram.org/type/DocumentAttribute?layer=216)
  + [217 – Live Stories](https://core.telegram.org/type/DocumentAttribute?layer=217)
  + [218 – Gift Auctions](https://core.telegram.org/type/DocumentAttribute?layer=218)
  + [219 – Passkeys](https://core.telegram.org/type/DocumentAttribute?layer=219)
  + [220 – Gift Offers](https://core.telegram.org/type/DocumentAttribute?layer=220)
  + [222 – Gift Crafts](https://core.telegram.org/type/DocumentAttribute?layer=222)
  + [**223 – User tags in groups**](https://core.telegram.org/type/DocumentAttribute?layer=223)
  + [More...](https://core.telegram.org/api/layers)

```
documentAttributeImageSize#6c37c15c w:int h:int = DocumentAttribute;
documentAttributeAnimated#11b58939 = DocumentAttribute;
documentAttributeSticker#6319d612 flags:# mask:flags.1?true alt:string stickerset:InputStickerSet mask_coords:flags.0?MaskCoords = DocumentAttribute;
documentAttributeVideo#43c57c48 flags:# round_message:flags.0?true supports_streaming:flags.1?true nosound:flags.3?true duration:double w:int h:int preload_prefix_size:flags.2?int video_start_ts:flags.4?double video_codec:flags.5?string = DocumentAttribute;
documentAttributeAudio#9852f9c6 flags:# voice:flags.10?true duration:int title:flags.0?string performer:flags.1?string waveform:flags.2?bytes = DocumentAttribute;
documentAttributeFilename#15590068 file_name:string = DocumentAttribute;
documentAttributeHasStickers#9801d2f7 = DocumentAttribute;
documentAttributeCustomEmoji#fd149899 flags:# free:flags.0?true text_color:flags.1?true alt:string stickerset:InputStickerSet = DocumentAttribute;
```

### Constructors

| Constructor | Description |
| --- | --- |
| [documentAttributeImageSize](https://core.telegram.org/constructor/documentAttributeImageSize) | Defines the width and height of an image uploaded as document |
| [documentAttributeAnimated](https://core.telegram.org/constructor/documentAttributeAnimated) | Defines an animated GIF |
| [documentAttributeSticker](https://core.telegram.org/constructor/documentAttributeSticker) | Defines a sticker |
| [documentAttributeVideo](https://core.telegram.org/constructor/documentAttributeVideo) | Defines a video |
| [documentAttributeAudio](https://core.telegram.org/constructor/documentAttributeAudio) | Represents an audio file |
| [documentAttributeFilename](https://core.telegram.org/constructor/documentAttributeFilename) | A simple document with a file name |
| [documentAttributeHasStickers](https://core.telegram.org/constructor/documentAttributeHasStickers) | Whether the current document has stickers attached |
| [documentAttributeCustomEmoji](https://core.telegram.org/constructor/documentAttributeCustomEmoji) | Info about a custom emoji |