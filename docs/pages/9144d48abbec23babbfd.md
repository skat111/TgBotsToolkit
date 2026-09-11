# TDLib: updateAnimationSearchParameters Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_animation_search_parameters.html

Inherits [Update](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_update.html).

## Description

The parameters of animation search through [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("animation\_search\_bot\_username") bot has changed.

|  |  |
| --- | --- |
| Public Fields | |
| [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) | [provider\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_animation_search_parameters.html#a2ac689b1b349726c7b2158a8049b81a5) |
|  | Name of the animation search provider. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) > | [emojis\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_animation_search_parameters.html#ade19609f127f3e0fc8c6a2860723b517) |
|  | The new list of emojis suggested for searching. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [updateAnimationSearchParameters](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_animation_search_parameters.html#a80e1610297f24fa7b5da87c33961bc34) () |
|  | |
|  | [updateAnimationSearchParameters](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_animation_search_parameters.html#a34137d4238133af4d55861bdb8928e1f) ([string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const &[provider\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_animation_search_parameters.html#a2ac689b1b349726c7b2158a8049b81a5), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) > &&[emojis\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_animation_search_parameters.html#ade19609f127f3e0fc8c6a2860723b517)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_animation_search_parameters.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_animation_search_parameters.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1144983202 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_animation_search_parameters.html#a80e1610297f24fa7b5da87c33961bc34)updateAnimationSearchParameters() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [updateAnimationSearchParameters](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_animation_search_parameters.html) | ( |  | ) |  |

The parameters of animation search through [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("animation\_search\_bot\_username") bot has changed.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_animation_search_parameters.html#a34137d4238133af4d55861bdb8928e1f)updateAnimationSearchParameters() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [updateAnimationSearchParameters](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_animation_search_parameters.html) | ( | [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) const & | *provider\_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [string](https://core.telegram.org/tdlib/docs/td__api_8h.html#aca454f84dd198a937af6499dd758aa3d) > && | *emojis\_* |
|  | ) |  |  |

The parameters of animation search through [getOption](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_option.html)("animation\_search\_bot\_username") bot has changed.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | provider\_ | Name of the animation search provider. |
    | [in] | emojis\_ | The new list of emojis suggested for searching. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_animation_search_parameters.html#a8044dab2ba3c75066745014259c050c7)store()

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