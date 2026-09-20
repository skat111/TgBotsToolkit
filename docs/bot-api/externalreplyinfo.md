Source: https://core.telegram.org/bots/api#externalreplyinfo
Snapshot: 2026-09-20T08:38:20Z

#### ExternalReplyInfo

This object contains information about a message that is being replied to, which may come from another chat or forum topic.

| Field | Type | Description |
| --- | --- | --- |
| origin | [MessageOrigin](https://core.telegram.org/bots/api#messageorigin) | Origin of the message replied to by the given message |
| chat | [Chat](https://core.telegram.org/bots/api#chat) | *Optional*. Chat the original message belongs to. Available only if the chat is a supergroup or a channel. |
| message_id | Integer | *Optional*. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel. |
| link_preview_options | [LinkPreviewOptions](https://core.telegram.org/bots/api#linkpreviewoptions) | *Optional*. Options used for link preview generation for the original message, if it is a text message |
| animation | [Animation](https://core.telegram.org/bots/api#animation) | *Optional*. Message is an animation, information about the animation |
| audio | [Audio](https://core.telegram.org/bots/api#audio) | *Optional*. Message is an audio file, information about the file |
| document | [Document](https://core.telegram.org/bots/api#document) | *Optional*. Message is a general file, information about the file |
| live_photo | [LivePhoto](https://core.telegram.org/bots/api#livephoto) | *Optional*. Message is a live photo, information about the live photo |
| paid_media | [PaidMediaInfo](https://core.telegram.org/bots/api#paidmediainfo) | *Optional*. Message contains paid media; information about the paid media |
| photo | Array of [PhotoSize](https://core.telegram.org/bots/api#photosize) | *Optional*. Message is a photo, available sizes of the photo |
| sticker | [Sticker](https://core.telegram.org/bots/api#sticker) | *Optional*. Message is a sticker, information about the sticker |
| story | [Story](https://core.telegram.org/bots/api#story) | *Optional*. Message is a forwarded story |
| video | [Video](https://core.telegram.org/bots/api#video) | *Optional*. Message is a video, information about the video |
| video_note | [VideoNote](https://core.telegram.org/bots/api#videonote) | *Optional*. Message is a [video note](https://telegram.org/blog/video-messages-and-telescope), information about the video message |
| voice | [Voice](https://core.telegram.org/bots/api#voice) | *Optional*. Message is a voice message, information about the file |
| has_media_spoiler | True | *Optional*. *True*, if the message media is covered by a spoiler animation |
| checklist | [Checklist](https://core.telegram.org/bots/api#checklist) | *Optional*. Message is a checklist |
| contact | [Contact](https://core.telegram.org/bots/api#contact) | *Optional*. Message is a shared contact, information about the contact |
| dice | [Dice](https://core.telegram.org/bots/api#dice) | *Optional*. Message is a dice with random value |
| game | [Game](https://core.telegram.org/bots/api#game) | *Optional*. Message is a game, information about the game. [More about games »](https://core.telegram.org/bots/api#games) |
| giveaway | [Giveaway](https://core.telegram.org/bots/api#giveaway) | *Optional*. Message is a scheduled giveaway, information about the giveaway |
| giveaway_winners | [GiveawayWinners](https://core.telegram.org/bots/api#giveawaywinners) | *Optional*. A giveaway with public winners was completed |
| invoice | [Invoice](https://core.telegram.org/bots/api#invoice) | *Optional*. Message is an invoice for a [payment](https://core.telegram.org/bots/api#payments), information about the invoice. [More about payments »](https://core.telegram.org/bots/api#payments) |
| location | [Location](https://core.telegram.org/bots/api#location) | *Optional*. Message is a shared location, information about the location |
| poll | [Poll](https://core.telegram.org/bots/api#poll) | *Optional*. Message is a native poll, information about the poll |
| venue | [Venue](https://core.telegram.org/bots/api#venue) | *Optional*. Message is a venue, information about the venue |