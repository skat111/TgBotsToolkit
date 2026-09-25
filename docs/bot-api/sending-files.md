Source: https://core.telegram.org/bots/api#sending-files
Snapshot: 2026-09-25T08:52:18Z

#### Sending files

There are three ways to send files (photos, stickers, audio, media, etc.):

1. If the file is already stored somewhere on the Telegram servers, you don't need to reupload it: each file object has a **file_id** field, simply pass this **file_id** as a parameter instead of uploading. There are **no limits** for files sent this way.
2. Provide Telegram with an HTTP URL for the file to be sent. Telegram will download and send the file. 5 MB max size for photos and 20 MB max for other types of content.
3. Post the file using multipart/form-data in the usual way that files are uploaded via the browser. 10 MB max size for photos, 50 MB for other files.

**Sending by file_id**

* It is not possible to change the file type when resending by **file_id**. I.e. a [video](https://core.telegram.org/bots/api#video) can't be [sent as a photo](https://core.telegram.org/bots/api#sendphoto), a [photo](https://core.telegram.org/bots/api#photosize) can't be [sent as a document](https://core.telegram.org/bots/api#senddocument), etc.
* It is not possible to resend thumbnails.
* Resending a photo by **file_id** will send all of its [sizes](https://core.telegram.org/bots/api#photosize).
* **file_id** is unique for each individual bot and **can't** be transferred from one bot to another.
* **file_id** uniquely identifies a file, but a file can have different valid **file_id**s even for the same bot.

**Sending by URL**

* When sending by URL the target file must have the correct MIME type (e.g., audio/mpeg for [sendAudio](https://core.telegram.org/bots/api#sendaudio), etc.).
* In [sendDocument](https://core.telegram.org/bots/api#senddocument), sending by URL will currently only work for **.PDF** and **.ZIP** files.
* To use [sendVoice](https://core.telegram.org/bots/api#sendvoice), the file must have the type audio/ogg and be no more than 1MB in size. 1-20MB voice notes will be sent as files.
* Other configurations may work but we can't guarantee that they will.