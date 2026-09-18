Source: https://core.telegram.org/bots/api#ephemeral-messages-and-commands
Snapshot: 2026-09-18T08:17:54Z

#### Ephemeral Messages and Commands

Ephemeral interactions allow a bot and an individual member of a group or supergroup chat to communicate privately on the public timeline without cluttering the chat for other members. They may disappear automatically after some time, or if the app is restarted.

**Ephemeral Commands (User to Bot)**  
Bots can declare ephemeral commands by setting the *is_ephemeral* field to *True* in the [BotCommand](https://core.telegram.org/bots/api#botcommand) class. A user can then send an ephemeral command that is received by the target bot but remains invisible to all members of the chat, including both users and other bots.

**Ephemeral Messages**  
Bots can send an ephemeral message response back to a specific user designated by the *receiver_user_id* parameter. Other members of the group or supergroup chat will not see the message.

> It is **not guaranteed** that the ephemeral message will be received, especially if the user is offline.

**Reply Targets and Conditions**

* Any bot can send an ephemeral message to a user within **15 seconds** of the incoming eligible action. The message will be sent to the exact client application that triggered the action. For this the bot must provide either:

  + The *callback_query_id* from a received callback query, or
  + The *reply_parameters.ephemeral_message_id* from an incoming ephemeral message.
* If the bot is a chat administrator, it can send an ephemeral message to any non-bot member of the chat at any time without needing to specify a *callback_query_id* or *reply_parameters.ephemeral_message_id*. In this case, the message may be delivered across multiple active client applications of the user, but is regardless not guaranteed to be delivered to any of them.