Source: https://core.telegram.org/bots/api#logout
Snapshot: 2026-11-27T12:28:14Z

#### logOut

Use this method to log out from the cloud Bot API server before launching the bot locally. You **must** log out the bot before running it locally; otherwise, there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log back in to the cloud Bot API server for 10 minutes. Returns *True* on success. Requires no parameters.