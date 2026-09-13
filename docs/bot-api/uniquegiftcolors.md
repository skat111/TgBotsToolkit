Source: https://core.telegram.org/bots/api#uniquegiftcolors
Snapshot: 2026-09-13T08:21:39Z

#### UniqueGiftColors

This object contains information about the color scheme for a user's name, message replies and link previews based on a unique gift.

| Field | Type | Description |
| --- | --- | --- |
| model_custom_emoji_id | String | Custom emoji identifier of the unique gift's model |
| symbol_custom_emoji_id | String | Custom emoji identifier of the unique gift's symbol |
| light_theme_main_color | Integer | Main color used in light themes; RGB format |
| light_theme_other_colors | Array of Integer | List of 1-3 additional colors used in light themes; RGB format |
| dark_theme_main_color | Integer | Main color used in dark themes; RGB format |
| dark_theme_other_colors | Array of Integer | List of 1-3 additional colors used in dark themes; RGB format |