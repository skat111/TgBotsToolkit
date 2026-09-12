Source: https://core.telegram.org/bots/api#backgroundtypewallpaper
Snapshot: 2026-09-12T07:57:24Z

#### BackgroundTypeWallpaper

The background is a wallpaper in the JPEG format.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the background, always “wallpaper” |
| document | [Document](https://core.telegram.org/bots/api#document) | Document with the wallpaper |
| dark_theme_dimming | Integer | Dimming of the background in dark themes, as a percentage; 0-100 |
| is_blurred | True | *Optional*. *True*, if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred with radius 12 |
| is_moving | True | *Optional*. *True*, if the background moves slightly when the device is tilted |