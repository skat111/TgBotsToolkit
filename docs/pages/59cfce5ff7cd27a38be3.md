# TDLib: inlineQueryResultAudio Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_query_result_audio.html

Inherits [InlineQueryResult](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_inline_query_result.html).

## Description

Represents an audio file.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_query_result_audio.html#a8315e6b3eb0f25e33fd70bfed8a6ee2a) |
|  | Unique identifier of the query result. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [audio](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1audio.html) > | [audio\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_query_result_audio.html#ab3564eae37ae39166f9825900a2f5e18) |
|  | Audio file. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [inlineQueryResultAudio](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_query_result_audio.html#a7bb652a92e6214434c707e4d19aa41bd) () |
|  | |
|  | [inlineQueryResultAudio](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_query_result_audio.html#a73db532029eb86b45c18e362e4fbd4bd) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_query_result_audio.html#a8315e6b3eb0f25e33fd70bfed8a6ee2a), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [audio](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1audio.html) > &&[audio\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_query_result_audio.html#ab3564eae37ae39166f9825900a2f5e18)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_query_result_audio.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_query_result_audio.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 842650360 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_query_result_audio.html#a7bb652a92e6214434c707e4d19aa41bd)inlineQueryResultAudio() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [inlineQueryResultAudio](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_query_result_audio.html) | ( |  | ) |  |

Represents an audio file.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_query_result_audio.html#a73db532029eb86b45c18e362e4fbd4bd)inlineQueryResultAudio() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [inlineQueryResultAudio](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_query_result_audio.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *id\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [audio](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1audio.html) > && | *audio\_* |
|  | ) |  |  |

Represents an audio file.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | id\_ | Unique identifier of the query result. |
    | [in] | audio\_ | Audio file. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1inline_query_result_audio.html#a8044dab2ba3c75066745014259c050c7)store()

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