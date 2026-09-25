Source: https://core.telegram.org/bots/api#messageentity
Snapshot: 2026-09-25T08:52:18Z

#### MessageEntity

This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the entity. Currently, can be “mention” (`@username`), “hashtag” (`#hashtag` or `#hashtag@chatusername`), “cashtag” (`$USD` or `$USD@chatusername`), “bot_command” (`/start@jobs_bot`), “url” (`https://telegram.org`), “email” (`do-not-reply@telegram.org`), “phone_number” (`+1-212-555-0123`), “bold” (**bold text**), “italic” (*italic text*), “underline” (underlined text), “strikethrough” (strikethrough text), “spoiler” (spoiler message), “blockquote” (block quotation), “expandable_blockquote” (collapsed-by-default block quotation), “code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs), “text_mention” (for users [without usernames](https://telegram.org/blog/edit#new-mentions)), “custom_emoji” (for inline custom emoji stickers), or “date_time” (for formatted date and time). |
| offset | Integer | Offset in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length) to the start of the entity |
| length | Integer | Length of the entity in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length) |
| url | String | *Optional*. For “text_link” only, URL that will be opened after user taps on the text |
| user | [User](https://core.telegram.org/bots/api#user) | *Optional*. For “text_mention” only, the mentioned user |
| language | String | *Optional*. For “pre” only, the programming language of the entity text |
| custom_emoji_id | String | *Optional*. For “custom_emoji” only, unique identifier of the custom emoji. Use [getCustomEmojiStickers](https://core.telegram.org/bots/api#getcustomemojistickers) to get full information about the sticker. |
| unix_time | Integer | *Optional*. For “date_time” only, the Unix time associated with the entity |
| date_time_format | String | *Optional*. For “date_time” only, the string that defines the formatting of the date and time. See [date-time entity formatting](https://core.telegram.org/bots/api#date-time-entity-formatting) for more details. |