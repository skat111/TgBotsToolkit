Source: https://core.telegram.org/bots/api#deletebusinessaccountgift
Snapshot: 2026-11-12T11:19:03Z

#### deleteBusinessAccountGift

Deletes a regular gift owned by a managed business account without receiving Telegram Stars for it. Requires the *can_convert_gifts_to_stars* business bot right. The gift can be deleted only if it isn't limited (the field *total_count* of the [Gift](https://core.telegram.org/bots/api#gift) is omitted) and wasn't refunded. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Yes | Unique identifier of the business connection |
| owned_gift_id | String | Yes | Unique identifier of the regular gift that should be deleted |