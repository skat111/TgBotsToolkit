# TDLib: connectedWebsite Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html

Inherits [Object](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_object.html).

## Description

Contains information about one website the current user is logged in with Telegram.

|  |  |
| --- | --- |
| Public Fields | |
| [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | [id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#aaa5141a413185b6008cfbb04a6f9a21d) |
|  | Website identifier. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [domain\_name\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a9ed0618f55c0e7a6408ae7b8044700fc) |
|  | The domain name of the website. |
|  | |
| [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | [bot\_user\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a852a1eecf72791be8eb2633ff5dcaec4) |
|  | User identifier of a bot linked with the website. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [browser\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a759f9a9f2544bb32d90ff2c9ef5ec8ee) |
|  | The version of a browser used to log in. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [platform\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#aa81f06ec384ee696ee72c4714d5f6b33) |
|  | Operating system the browser is running on. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [log\_in\_date\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#ad1039437fc114c48094f7b73860e0f61) |
|  | Point in time (Unix timestamp) when the user was logged in. |
|  | |
| [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | [last\_active\_date\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a73ba6b7cf411ddde2cda6df0a8536a92) |
|  | Point in time (Unix timestamp) when obtained authorization was last used. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [ip\_address\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a9b606e23d1355c037e80a6d52b2a0c06) |
|  | IP address from which the user was logged in, in human-readable format. |
|  | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [location\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a842286abf4d9cc56561cc2c92cdf5dc2) |
|  | Human-readable description of a country and a region from which the user was logged in, based on the IP address. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [connectedWebsite](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#ac6bf50a9557e6d308ea3c31db29df60b) () |
|  | |
|  | [connectedWebsite](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a5941651676d3683438b01579c02a92e2) ([int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) [id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#aaa5141a413185b6008cfbb04a6f9a21d), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[domain\_name\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a9ed0618f55c0e7a6408ae7b8044700fc), [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) [bot\_user\_id\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a852a1eecf72791be8eb2633ff5dcaec4), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[browser\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a759f9a9f2544bb32d90ff2c9ef5ec8ee), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[platform\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#aa81f06ec384ee696ee72c4714d5f6b33), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [log\_in\_date\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#ad1039437fc114c48094f7b73860e0f61), [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) [last\_active\_date\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a73ba6b7cf411ddde2cda6df0a8536a92), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[ip\_address\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a9b606e23d1355c037e80a6d52b2a0c06), [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[location\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a842286abf4d9cc56561cc2c92cdf5dc2)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = 1978115978 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#ac6bf50a9557e6d308ea3c31db29df60b)connectedWebsite() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [connectedWebsite](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html) | ( |  | ) |  |

Contains information about one website the current user is logged in with Telegram.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a5941651676d3683438b01579c02a92e2)connectedWebsite() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [connectedWebsite](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html) | ( | [int64](https://core.telegram.org/tdlib/docs/td__api_8h.html#a552928ab323811c9694f5b7c9f53d0fb) | *id\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *domain\_name\_*, |
|  |  | [int53](https://core.telegram.org/tdlib/docs/td__api_8h.html#a6f57ab89c6371535f0fb7fec2d770126) | *bot\_user\_id\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *browser\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *platform\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *log\_in\_date\_*, |
|  |  | [int32](https://core.telegram.org/tdlib/docs/td__api_8h.html#a3d594eb72953c94a18a03d929ebd9167) | *last\_active\_date\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *ip\_address\_*, |
|  |  | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *location\_* |
|  | ) |  |  |

Contains information about one website the current user is logged in with Telegram.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | id\_ | Website identifier. |
    | [in] | domain\_name\_ | The domain name of the website. |
    | [in] | bot\_user\_id\_ | User identifier of a bot linked with the website. |
    | [in] | browser\_ | The version of a browser used to log in. |
    | [in] | platform\_ | Operating system the browser is running on. |
    | [in] | log\_in\_date\_ | Point in time (Unix timestamp) when the user was logged in. |
    | [in] | last\_active\_date\_ | Point in time (Unix timestamp) when obtained authorization was last used. |
    | [in] | ip\_address\_ | IP address from which the user was logged in, in human-readable format. |
    | [in] | location\_ | Human-readable description of a country and a region from which the user was logged in, based on the IP address. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1connected_website.html#a8044dab2ba3c75066745014259c050c7)store()

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