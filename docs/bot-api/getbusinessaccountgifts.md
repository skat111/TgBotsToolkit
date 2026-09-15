Source: https://core.telegram.org/bots/api#getbusinessaccountgifts
Snapshot: 2026-09-15T08:44:15Z

#### getBusinessAccountGifts

Returns the gifts received and owned by a managed business account. Requires the *can_view_gifts_and_stars* business bot right. Returns [OwnedGifts](https://core.telegram.org/bots/api#ownedgifts) on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Yes | Unique identifier of the business connection |
| exclude_unsaved | Boolean | Optional | Pass *True* to exclude gifts that aren't saved to the account's profile page |
| exclude_saved | Boolean | Optional | Pass *True* to exclude gifts that are saved to the account's profile page |
| exclude_unlimited | Boolean | Optional | Pass *True* to exclude gifts that can be purchased an unlimited number of times |
| exclude_limited_upgradable | Boolean | Optional | Pass *True* to exclude gifts that can be purchased a limited number of times and can be upgraded to unique |
| exclude_limited_non_upgradable | Boolean | Optional | Pass *True* to exclude gifts that can be purchased a limited number of times and can't be upgraded to unique |
| exclude_unique | Boolean | Optional | Pass *True* to exclude unique gifts |
| exclude_from_blockchain | Boolean | Optional | Pass *True* to exclude gifts that were assigned from the TON blockchain and can't be resold or transferred in Telegram |
| sort_by_price | Boolean | Optional | Pass *True* to sort results by gift price instead of send date. Sorting is applied before pagination. |
| offset | String | Optional | Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results |
| limit | Integer | Optional | The maximum number of gifts to be returned; 1-100. Defaults to 100. |