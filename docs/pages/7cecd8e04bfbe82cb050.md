# TDLib: updateFileRemovedFromDownloads Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_file_removed_from_downloads.html

Inherits [Update](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_update.html).

## Description

A file was removed from the file download list. This update is sent only after file download list is loaded for the first time.

|  |  |
| --- | --- |
| Public Fields | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [file_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_file_removed_from_downloads.html#ac1aebf3d9d209699b87093ecff110b52) |
|  | File identifier. |
|  | |
| [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [downloadedFileCounts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1downloaded_file_counts.html) > | [counts_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_file_removed_from_downloads.html#a41111a1663d7a262dff0affb18b265fb) |
|  | New number of being downloaded and recently downloaded files found. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [updateFileRemovedFromDownloads](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_file_removed_from_downloads.html#a0b00c7f2cd01286819eabe395582864a) () |
|  | |
|  | [updateFileRemovedFromDownloads](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_file_removed_from_downloads.html#ace691dfd55dcce88b52814985d464589) ([int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [file_id_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_file_removed_from_downloads.html#ac1aebf3d9d209699b87093ecff110b52), [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [downloadedFileCounts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1downloaded_file_counts.html) > &&[counts_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_file_removed_from_downloads.html#a41111a1663d7a262dff0affb18b265fb)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_file_removed_from_downloads.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field_name) const final |
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
| static const std::int32_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_file_removed_from_downloads.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1853625576 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_file_removed_from_downloads.html#a0b00c7f2cd01286819eabe395582864a)updateFileRemovedFromDownloads() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [updateFileRemovedFromDownloads](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_file_removed_from_downloads.html) | ( |  | ) |  |

A file was removed from the file download list. This update is sent only after file download list is loaded for the first time.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_file_removed_from_downloads.html#ace691dfd55dcce88b52814985d464589)updateFileRemovedFromDownloads() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [updateFileRemovedFromDownloads](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_file_removed_from_downloads.html) | ( | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *file_id_*, |
|  |  | [object_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [downloadedFileCounts](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1downloaded_file_counts.html) > && | *counts_* |
|  | ) |  |  |

A file was removed from the file download list. This update is sent only after file download list is loaded for the first time.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | file_id_ | File identifier. |
    | [in] | counts_ | New number of being downloaded and recently downloaded files found. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_file_removed_from_downloads.html#a8044dab2ba3c75066745014259c050c7)store()

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