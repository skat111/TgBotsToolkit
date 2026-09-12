# TDLib: pageBlockTableCell Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Represents a cell of a table.

|  |  |
| --- | --- |
| Public Fields | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [RichText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_rich_text.html) > | [text_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#a457d9bf01815fd9f119f7f975060be27) |
|  | Cell text; may be null. If the text is null, then the cell must be invisible. |
|  | |
| bool | [is_header_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#ab96a8ec3f06c9d96b9a2b44bdc9b51f3) |
|  | True, if it is a header cell. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [colspan_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#a74c31c419884427f95f8c13de431c672) |
|  | The number of columns the cell spans. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [rowspan_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#aebac40fb3a098984ba3919110b6c6e45) |
|  | The number of rows the cell spans. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [PageBlockHorizontalAlignment](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_page_block_horizontal_alignment.html) > | [align_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#a7e7bf2d0c3f7d9d3c1bccc6dbc54a52f) |
|  | Horizontal cell content alignment. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [PageBlockVerticalAlignment](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_page_block_vertical_alignment.html) > | [valign_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#a3de52383adb51b3104f29dc0d7afb168) |
|  | Vertical cell content alignment. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [pageBlockTableCell](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#a53b0f322a92a9d95cf928f45760a4fd8) () |
|  | |
|  | [pageBlockTableCell](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#ade2e37509dc3623ce7acaa08e4e8d091) ([object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [RichText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_rich_text.html) > &&[text_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#a457d9bf01815fd9f119f7f975060be27), bool [is_header_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#ab96a8ec3f06c9d96b9a2b44bdc9b51f3), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [colspan_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#a74c31c419884427f95f8c13de431c672), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [rowspan_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#aebac40fb3a098984ba3919110b6c6e45), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [PageBlockHorizontalAlignment](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_page_block_horizontal_alignment.html) > &&[align_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#a7e7bf2d0c3f7d9d3c1bccc6dbc54a52f), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [PageBlockVerticalAlignment](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_page_block_vertical_alignment.html) > &&[valign_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#a3de52383adb51b3104f29dc0d7afb168)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1417658214 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#a53b0f322a92a9d95cf928f45760a4fd8)pageBlockTableCell() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [pageBlockTableCell](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html) | ( |  | ) |  |

Represents a cell of a table.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#ade2e37509dc3623ce7acaa08e4e8d091)pageBlockTableCell() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [pageBlockTableCell](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html) | ( | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [RichText](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_rich_text.html) > && | *text_*, |
|  |  | bool | *is_header_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *colspan_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *rowspan_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [PageBlockHorizontalAlignment](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_page_block_horizontal_alignment.html) > && | *align_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [PageBlockVerticalAlignment](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_page_block_vertical_alignment.html) > && | *valign_* |
|  | ) |  |  |

Represents a cell of a table.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | text_ | Cell text; may be null. If the text is null, then the cell must be invisible. |
    | [in] | is_header_ | True, if it is a header cell. |
    | [in] | colspan_ | The number of columns the cell spans. |
    | [in] | rowspan_ | The number of rows the cell spans. |
    | [in] | align_ | Horizontal cell content alignment. |
    | [in] | valign_ | Vertical cell content alignment. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1page_block_table_cell.html#a8044dab2ba3c75066745014259c050c7)store()

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