Source: https://core.telegram.org/bots/api#uniquegift
Snapshot: 2026-09-18T08:17:54Z

#### UniqueGift

This object describes a unique gift that was upgraded from a regular gift.

| Field | Type | Description |
| --- | --- | --- |
| gift_id | String | Identifier of the regular gift from which the gift was upgraded |
| base_name | String | Human-readable name of the regular gift from which this unique gift was upgraded |
| name | String | Unique name of the gift. This name can be used in `https://t.me/nft/...` links and story areas. |
| number | Integer | Unique number of the upgraded gift among gifts upgraded from the same regular gift |
| model | [UniqueGiftModel](https://core.telegram.org/bots/api#uniquegiftmodel) | Model of the gift |
| symbol | [UniqueGiftSymbol](https://core.telegram.org/bots/api#uniquegiftsymbol) | Symbol of the gift |
| backdrop | [UniqueGiftBackdrop](https://core.telegram.org/bots/api#uniquegiftbackdrop) | Backdrop of the gift |
| is_premium | True | *Optional*. *True*, if the original regular gift was exclusively purchaseable by Telegram Premium subscribers |
| is_burned | True | *Optional*. *True*, if the gift was used to craft another gift and isn't available anymore |
| is_from_blockchain | True | *Optional*. *True*, if the gift is assigned from the TON blockchain and can't be resold or transferred in Telegram |
| colors | [UniqueGiftColors](https://core.telegram.org/bots/api#uniquegiftcolors) | *Optional*. The color scheme that can be used by the gift's owner for the chat's name, replies to messages and link previews; for business account gifts and gifts that are currently on sale only |
| publisher_chat | [Chat](https://core.telegram.org/bots/api#chat) | *Optional*. Information about the chat that published the gift |