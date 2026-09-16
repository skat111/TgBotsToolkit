Source: https://core.telegram.org/bots/api#inlinequeryresultcontact
Snapshot: 2026-09-16T08:38:32Z

#### InlineQueryResultContact

Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use *input_message_content* to send a message with the specified content instead of the contact.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *contact* |
| id | String | Unique identifier for this result, 1-64 Bytes |
| phone_number | String | Contact's phone number |
| first_name | String | Contact's first name |
| last_name | String | *Optional*. Contact's last name |
| vcard | String | *Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes |
| reply_markup | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input_message_content | [InputMessageContent](https://core.telegram.org/bots/api#inputmessagecontent) | *Optional*. Content of the message to be sent instead of the contact |
| thumbnail_url | String | *Optional*. Url of the thumbnail for the result |
| thumbnail_width | Integer | *Optional*. Thumbnail width |
| thumbnail_height | Integer | *Optional*. Thumbnail height |