# TDLib: checklistTask Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes a task in a checklist.

|  |  |
| --- | --- |
| Public Fields | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#a083e2bcfb02882e41b8251e766c957f9) |
|  | Unique identifier of the task. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > | [text_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#a82250655835bea3abad039d944dcd788) |
|  | Text of the task; may contain only Bold, Italic, Underline, Strikethrough, Spoiler, CustomEmoji, Url, EmailAddress, Mention, Hashtag, Cashtag and PhoneNumber entities. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > | [completed_by_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#aa7c468271b50f75a1b52fbe11a2f4a79) |
|  | Identifier of the user or chat that completed the task; may be null if the task isn't completed yet. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [completion_date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#a62f79bcd1fb272b30ec676d836ea865c) |
|  | Point in time (Unix timestamp) when the task was completed; 0 if the task isn't completed. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [checklistTask](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#a83caf3ce40a4ce25d71cf4e3369adf2c) () |
|  | |
|  | [checklistTask](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#a7d13069cc9e80a3d633a2bf3d9a03be9) ([int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#a083e2bcfb02882e41b8251e766c957f9), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > &&[text_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#a82250655835bea3abad039d944dcd788), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > &&[completed_by_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#aa7c468271b50f75a1b52fbe11a2f4a79), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [completion_date_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#a62f79bcd1fb272b30ec676d836ea865c)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
|  | |
| - Public Instance Methods inherited from [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) | |
| virtual void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#aed3fac8962d039b3c4827cd013ba8050) (TlStorerUnsafe &s) const |
|  | |
| virtual void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a66f325c1a08459d978fa08dcc4e7a86e) (TlStorerCalcLength &s) const |
|  | |
|  | [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a524843ecda9a59d32e1a1ad83bfdfef5) ()=default |
|  | |
|  | [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#aaf0b851a7d7420da4ccc5d3f875e33f3) (const [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) &)=delete |
|  | |
| [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) & | [operator=](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#ac017d2d18b4840ffec9274cea86cd1d3) (const [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) &)=delete |
|  | |
|  | [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a767dd89c1cf0f6cd9cc776f36d5b1ece) ([TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) &&)=default |
|  | |
| [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) & | [operator=](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a8ae6deb8ded379f394672c85bafeb70b) ([TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html) &&)=default |
|  | |
| virtual | [~TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#abfbd857b9bfdc4e3bf31b5d0476b7289) ()=default |
|  | |

|  |  |
| --- | --- |
| Static Public Attributes | |
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 464950512 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#a83caf3ce40a4ce25d71cf4e3369adf2c)checklistTask() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [checklistTask](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html) | ( |  | ) |  |

Describes a task in a checklist.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#a7d13069cc9e80a3d633a2bf3d9a03be9)checklistTask() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [checklistTask](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html) | ( | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *id_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [formattedText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1formatted_text.html) > && | *text_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [MessageSender](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_sender.html) > && | *completed_by_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *completion_date_* |
|  | ) |  |  |

Describes a task in a checklist.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | id_ | Unique identifier of the task. |
    | [in] | text_ | Text of the task; may contain only Bold, Italic, Underline, Strikethrough, Spoiler, CustomEmoji, Url, EmailAddress, Mention, Hashtag, Cashtag and PhoneNumber entities. |
    | [in] | completed_by_ | Identifier of the user or chat that completed the task; may be null if the task isn't completed yet. |
    | [in] | completion_date_ | Point in time (Unix timestamp) when the task was completed; 0 if the task isn't completed. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1checklist_task.html#a8044dab2ba3c75066745014259c050c7)store()

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  | | --- | --- | --- | --- | | void store | ( | TlStorerToString & | *s*, | |  |  | const char \* | *field_name* | |  | ) |  | const | | finalvirtual |

Helper function for to_string method. Appends string representation of the object to the storer.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | s | Storer to which object string representation will be appended. |
    | [in] | field_name | [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html) field_name if applicable. |

Implements [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a4f1eab7385f340a2ab0aa8751cdcedc6).

---

The documentation for this class was generated from the following file:

* td/generate/auto/td/telegram/[td_api.h](https://core.telegram.org/tdlib/docs/td__api_8h_source.html)