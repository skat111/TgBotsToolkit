# TDLib: richTextMarked Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1rich_text_marked.html

Inherits [RichText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_rich_text.html).

## Description

A marked rich text.

|  |  |
| --- | --- |
| Public Fields | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [RichText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_rich_text.html) > | [text\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1rich_text_marked.html#a457d9bf01815fd9f119f7f975060be27) |
|  | Text. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [richTextMarked](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1rich_text_marked.html#acd1b89ac8b37559747bb924e1ade5017) () |
|  | |
|  | [richTextMarked](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1rich_text_marked.html#a3af295e8b8751c67545fef1d122e29d6) ([object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [RichText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_rich_text.html) > &&[text\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1rich_text_marked.html#a457d9bf01815fd9f119f7f975060be27)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1rich_text_marked.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1rich_text_marked.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1271999614 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1rich_text_marked.html#acd1b89ac8b37559747bb924e1ade5017)richTextMarked() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [richTextMarked](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1rich_text_marked.html) | ( |  | ) |  |

A marked rich text.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1rich_text_marked.html#a3af295e8b8751c67545fef1d122e29d6)richTextMarked() [2/2]

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [richTextMarked](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1rich_text_marked.html) | ( | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [RichText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_rich_text.html) > && | *text\_* | ) |  | | explicit |

A marked rich text.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | text\_ | Text. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1rich_text_marked.html#a8044dab2ba3c75066745014259c050c7)store()

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