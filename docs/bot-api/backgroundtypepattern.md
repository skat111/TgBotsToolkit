Source: https://core.telegram.org/bots/api#backgroundtypepattern
Snapshot: 2026-09-25T08:52:18Z

#### BackgroundTypePattern

The background is a .PNG or .TGV (gzipped subset of SVG with MIME type “application/x-tgwallpattern”) pattern to be combined with the background fill chosen by the user.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the background, always “pattern” |
| document | [Document](https://core.telegram.org/bots/api#document) | Document with the pattern |
| fill | [BackgroundFill](https://core.telegram.org/bots/api#backgroundfill) | The background fill that is combined with the pattern |
| intensity | Integer | Intensity of the pattern when it is shown above the filled background; 0-100 |
| is_inverted | True | *Optional*. *True*, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only. |
| is_moving | True | *Optional*. *True*, if the background moves slightly when the device is tilted |