# e2e.chain.sharedKey

Source: https://core.telegram.org/constructor/e2e.chain.sharedKey

Encrypted [shared group key material](https://core.telegram.org/api/end-to-end/group-calls#shared-key-encryption) for an E2E conference call.

```
e2e.chain.sharedKey#8a847e7f ek:int256 encrypted_shared_key:string dest_user_id:Vector<long> dest_header:Vector<bytes> = e2e.chain.SharedKey;
```

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| **ek** | [int256](https://core.telegram.org/type/int256) | Ephemeral public key used to derive per-participant secrets for decrypting the shared key. |
| **encrypted_shared_key** | [string](https://core.telegram.org/type/string) | Encrypted raw group shared key. |
| **dest_user_id** | [Vector](https://core.telegram.org/type/Vector%20t)<[long](https://core.telegram.org/type/long)> | Exactly one unique user ID for each participant in the current group state, in any order |
| **dest_header** | [Vector](https://core.telegram.org/type/Vector%20t)<[bytes](https://core.telegram.org/type/bytes)> | Encrypted per-participant headers containing the one-time secret needed to decrypt `encrypted_shared_key`; each entry corresponds to a user ID located under the same key in `dest_user_id`. |

### Type

[e2e.chain.SharedKey](https://core.telegram.org/type/e2e.chain.SharedKey)

### Related pages

#### [E2E Group Calls](https://core.telegram.org/api/end-to-end/group-calls)

End-to-end encryption used for Telegram group voice and video calls, using a blockchain for state management.