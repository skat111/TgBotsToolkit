Source: https://core.telegram.org/bots/api#chatpermissions
Snapshot: 2026-09-13T08:21:39Z

#### ChatPermissions

Describes actions that a non-administrator user is allowed to take in a chat.

| Field | Type | Description |
| --- | --- | --- |
| can_send_messages | Boolean | *Optional*. *True*, if the user is allowed to send text messages, rich messages, contacts, giveaways, giveaway winners, invoices, locations and venues |
| can_send_audios | Boolean | *Optional*. *True*, if the user is allowed to send audios |
| can_send_documents | Boolean | *Optional*. *True*, if the user is allowed to send documents |
| can_send_photos | Boolean | *Optional*. *True*, if the user is allowed to send photos |
| can_send_videos | Boolean | *Optional*. *True*, if the user is allowed to send videos |
| can_send_video_notes | Boolean | *Optional*. *True*, if the user is allowed to send video notes |
| can_send_voice_notes | Boolean | *Optional*. *True*, if the user is allowed to send voice notes |
| can_send_polls | Boolean | *Optional*. *True*, if the user is allowed to send polls and checklists |
| can_send_other_messages | Boolean | *Optional*. *True*, if the user is allowed to send animations, games, stickers and use inline bots |
| can_add_web_page_previews | Boolean | *Optional*. *True*, if the user is allowed to add web page previews to their messages |
| can_react_to_messages | Boolean | *Optional*. *True*, if the user is allowed to react to messages. If omitted, defaults to the value of *can_send_messages*. |
| can_edit_tag | Boolean | *Optional*. *True*, if the user is allowed to edit their own tag. If omitted, defaults to the value of *can_pin_messages*. |
| can_change_info | Boolean | *Optional*. *True*, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups. |
| can_invite_users | Boolean | *Optional*. *True*, if the user is allowed to invite new users to the chat |
| can_pin_messages | Boolean | *Optional*. *True*, if the user is allowed to pin messages. Ignored in public supergroups. |
| can_manage_topics | Boolean | *Optional*. *True*, if the user is allowed to create forum topics. If omitted, defaults to the value of can_pin_messages. |