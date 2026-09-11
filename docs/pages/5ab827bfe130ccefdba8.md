# TDLib: chatActiveStories Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Describes active stories posted by a chat.

|  |  |
| --- | --- |
| Public Fields | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#aa8a7803161092ff97e60d58707199e1f) |
|  | Identifier of the chat that posted the stories. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StoryList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_story_list.html) > | [list\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a46cd6c1b7c138e75d02c2190bfb87aca) |
|  | Identifier of the story list in which the stories are shown; may be null if the stories aren't shown in a story list. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [order\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a7a3631038fd8d1ceb733467d6a2264ca) |
|  | A parameter used to determine order of the stories in the story list; 0 if the stories doesn't need to be shown in the story list. Stories must be sorted by the pair (order, story\_poster\_chat\_id) in descending order. |
|  | |
| bool | [can\_be\_archived\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a72457cadb5c3ee4c444613b5b378ac55) |
|  | True, if the stories are shown in the main story list and can be archived; otherwise, the stories can be hidden from the main story list only by calling [removeTopChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1remove_top_chat.html) with [topChatCategoryUsers](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1top_chat_category_users.html) and the chat\_id. Stories of the current user can't be archived nor hidden using [removeTopChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1remove_top_chat.html). |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [max\_read\_story\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a92b8aaba878d4dd59a302a09b6319182) |
|  | Identifier of the last read active story. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [storyInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_info.html) > > | [stories\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a1078955f1e036d8b56eb3f581cf0ffa0) |
|  | Basic information about the stories; use [getStory](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_story.html) to get full information about the stories. The stories are in chronological order (i.e., in order of increasing story identifiers). |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [chatActiveStories](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a34fdfba6fa6fe0af0a34ddd7a50caa12) () |
|  | |
|  | [chatActiveStories](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a290b69e9a36c5d86ebedb896d74066d6) ([int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [chat\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#aa8a7803161092ff97e60d58707199e1f), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StoryList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_story_list.html) > &&[list\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a46cd6c1b7c138e75d02c2190bfb87aca), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [order\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a7a3631038fd8d1ceb733467d6a2264ca), bool [can\_be\_archived\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a72457cadb5c3ee4c444613b5b378ac55), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [max\_read\_story\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a92b8aaba878d4dd59a302a09b6319182), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [storyInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_info.html) >> &&[stories\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a1078955f1e036d8b56eb3f581cf0ffa0)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 396502772 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a34fdfba6fa6fe0af0a34ddd7a50caa12)chatActiveStories() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [chatActiveStories](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html) | ( |  | ) |  |

Describes active stories posted by a chat.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a290b69e9a36c5d86ebedb896d74066d6)chatActiveStories() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [chatActiveStories](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html) | ( | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *chat\_id\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StoryList](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_story_list.html) > && | *list\_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *order\_*, |
|  |  | bool | *can\_be\_archived\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *max\_read\_story\_id\_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [storyInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1story_info.html) >> && | *stories\_* |
|  | ) |  |  |

Describes active stories posted by a chat.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | chat\_id\_ | Identifier of the chat that posted the stories. |
    | [in] | list\_ | Identifier of the story list in which the stories are shown; may be null if the stories aren't shown in a story list. |
    | [in] | order\_ | A parameter used to determine order of the stories in the story list; 0 if the stories doesn't need to be shown in the story list. Stories must be sorted by the pair (order, story\_poster\_chat\_id) in descending order. |
    | [in] | can\_be\_archived\_ | True, if the stories are shown in the main story list and can be archived; otherwise, the stories can be hidden from the main story list only by calling [removeTopChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1remove_top_chat.html) with [topChatCategoryUsers](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1top_chat_category_users.html) and the chat\_id. Stories of the current user can't be archived nor hidden using [removeTopChat](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1remove_top_chat.html). |
    | [in] | max\_read\_story\_id\_ | Identifier of the last read active story. |
    | [in] | stories\_ | Basic information about the stories; use [getStory](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_story.html) to get full information about the stories. The stories are in chronological order (i.e., in order of increasing story identifiers). |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_active_stories.html#a8044dab2ba3c75066745014259c050c7)store()

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