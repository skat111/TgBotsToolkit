Source: https://core.telegram.org/bots/api#getusergifts
Snapshot: 2026-09-18T08:17:54Z

#### getUserGifts

Returns the gifts owned and hosted by a user. Returns [OwnedGifts](https://core.telegram.org/bots/api#ownedgifts) on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | Integer | Yes | Unique identifier of the user |
| exclude_unlimited | Boolean | Optional | Pass *True* to exclude gifts that can be purchased an unlimited number of times |
| exclude_limited_upgradable | Boolean | Optional | Pass *True* to exclude gifts that can be purchased a limited number of times and can be upgraded to unique |
| exclude_limited_non_upgradable | Boolean | Optional | Pass *True* to exclude gifts that can be purchased a limited number of times and can't be upgraded to unique |
| exclude_from_blockchain | Boolean | Optional | Pass *True* to exclude gifts that were assigned from the TON blockchain and can't be resold or transferred in Telegram |
| exclude_unique | Boolean | Optional | Pass *True* to exclude unique gifts |
| sort_by_price | Boolean | Optional | Pass *True* to sort results by gift price instead of send date. Sorting is applied before pagination. |
| offset | String | Optional | Offset of the first entry to return as received from the previous request; use an empty string to get the first chunk of results |
| limit | Integer | Optional | The maximum number of gifts to be returned; 1-100. Defaults to 100. |