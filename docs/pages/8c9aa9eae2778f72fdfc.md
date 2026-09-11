# TDLib: markChecklistTasksAsDone Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html

Inherits [Function](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_function.html).

## Description

Adds tasks of a checklist in a message as done or not done.

Returns object\_ptr<Ok>.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Identifier of the chat with the message. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [message\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#a946f46ee90c465619214e056e4d91ce4) |
|  | Identifier of the message containing the checklist. Use messageProperties.can\_mark\_tasks\_as\_done to check whether the tasks can be marked as done or not done. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > | [marked\_as\_done\_task\_ids\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#a85432f179a1274eac8ca4f4f5af3be48) |
|  | Identifiers of tasks that were marked as done. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > | [marked\_as\_not\_done\_task\_ids\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#a78c28b4581649190b13dcc104e4591e1) |
|  | Identifiers of tasks that were marked as not done. |
|  | |

|  |  |
| --- | --- |
| Public Types | |
| using | [ReturnType](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#ab684327f0ee9cbf9afb740503d89f019) = [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [ok](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1ok.html) > |
|  | Typedef for the type returned by the function. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [markChecklistTasksAsDone](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#adba68bcc540a7f9be67625d7493fd6c4) () |
|  | |
|  | [markChecklistTasksAsDone](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#a958ac67239ffc7a8a8a66de11b3e0b14) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#aa8a7803161092ff97e60d58707199e1f), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [message\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#a946f46ee90c465619214e056e4d91ce4), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > &&[marked\_as\_done\_task\_ids\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#a85432f179a1274eac8ca4f4f5af3be48), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > &&[marked\_as\_not\_done\_task\_ids\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#a78c28b4581649190b13dcc104e4591e1)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 386950739 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#adba68bcc540a7f9be67625d7493fd6c4)markChecklistTasksAsDone() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [markChecklistTasksAsDone](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html) | ( |  | ) |  |

Default constructor for a function, which adds tasks of a checklist in a message as done or not done.

Returns object\_ptr<Ok>.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#a958ac67239ffc7a8a8a66de11b3e0b14)markChecklistTasksAsDone() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [markChecklistTasksAsDone](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat\_id\_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *message\_id\_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > && | *marked\_as\_done\_task\_ids\_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) > && | *marked\_as\_not\_done\_task\_ids\_* |
|  | ) |  |  |

Creates a function, which adds tasks of a checklist in a message as done or not done.

Returns object\_ptr<Ok>.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat\_id\_ | Identifier of the chat with the message. |
    | [in] | message\_id\_ | Identifier of the message containing the checklist. Use messageProperties.can\_mark\_tasks\_as\_done to check whether the tasks can be marked as done or not done. |
    | [in] | marked\_as\_done\_task\_ids\_ | Identifiers of tasks that were marked as done. |
    | [in] | marked\_as\_not\_done\_task\_ids\_ | Identifiers of tasks that were marked as not done. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1mark_checklist_tasks_as_done.html#a8044dab2ba3c75066745014259c050c7)store()

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  | | --- | --- | --- | --- | | void store | ( | TlStorerToString & | *s*, | |  |  | const char \* | *field\_name* | |  | ) |  | const | | finalvirtual |

Helper function for to\_string method. Appends string representation of the object to the storer.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | s | Storer to which object string representation will be appended. |
    | [in] | field\_name | [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html) field\_name if applicable. |

Implements [TlObject](https://core.telegram.org/tdlib/docs/classtd_1_1_tl_object.html#a4f1eab7385f340a2ab0aa8751cdcedc6).

---

The documentation for this class was generated from the following file:

* td/generate/auto/td/telegram/[td\_api.h](https://core.telegram.org/tdlib/docs/td__api_8h_source.html)