Source: https://core.telegram.org/bots/api#upgradegift
Snapshot: 2026-09-17T08:42:18Z

#### upgradeGift

Upgrades a given regular gift to a unique gift. Requires the *can_transfer_and_upgrade_gifts* business bot right. Additionally requires the *can_transfer_stars* business bot right if the upgrade is paid. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business_connection_id | String | Yes | Unique identifier of the business connection |
| owned_gift_id | String | Yes | Unique identifier of the regular gift that should be upgraded to a unique one |
| keep_original_details | Boolean | Optional | Pass *True* to keep the original gift text, sender and receiver in the upgraded gift |
| star_count | Integer | Optional | The amount of Telegram Stars that will be paid for the upgrade from the business account balance. If `gift.prepaid_upgrade_star_count > 0`, then pass 0, otherwise, the *can_transfer_stars* business bot right is required and `gift.upgrade_star_count` must be passed. |