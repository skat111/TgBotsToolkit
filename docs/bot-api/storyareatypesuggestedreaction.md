Source: https://core.telegram.org/bots/api#storyareatypesuggestedreaction
Snapshot: 2026-09-24T08:30:39Z

#### StoryAreaTypeSuggestedReaction

Describes a story area pointing to a suggested reaction. Currently, a story can have up to 5 suggested reaction areas.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the area, always “suggested_reaction” |
| reaction_type | [ReactionType](https://core.telegram.org/bots/api#reactiontype) | Type of the reaction |
| is_dark | Boolean | *Optional*. Pass *True* if the reaction area has a dark background |
| is_flipped | Boolean | *Optional*. Pass *True* if reaction area corner is flipped |