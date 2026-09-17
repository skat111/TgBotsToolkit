Source: https://core.telegram.org/bots/api#giftinfo
Snapshot: 2026-09-17T08:42:18Z

#### GiftInfo

Describes a service message about a regular gift that was sent or received.

| Field | Type | Description |
| --- | --- | --- |
| gift | [Gift](https://core.telegram.org/bots/api#gift) | Information about the gift |
| owned_gift_id | String | *Optional*. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts |
| convert_star_count | Integer | *Optional*. Number of Telegram Stars that can be claimed by the receiver by converting the gift; omitted if conversion to Telegram Stars is impossible |
| prepaid_upgrade_star_count | Integer | *Optional*. Number of Telegram Stars that were prepaid for the ability to upgrade the gift |
| is_upgrade_separate | True | *Optional*. *True*, if the gift's upgrade was purchased after the gift was sent |
| can_be_upgraded | True | *Optional*. *True*, if the gift can be upgraded to a unique gift |
| text | String | *Optional*. Text of the message that was added to the gift |
| entities | Array of [MessageEntity](https://core.telegram.org/bots/api#messageentity) | *Optional*. Special entities that appear in the text |
| is_private | True | *Optional*. *True*, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them |
| unique_gift_number | Integer | *Optional*. Unique number reserved for this gift when upgraded. See the *number* field in [UniqueGift](https://core.telegram.org/bots/api#uniquegift). |