# TDLib: chatStatisticsChannel Class Reference

Source: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html

Inherits [ChatStatistics](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_chat_statistics.html).

## Description

A detailed statistics about a channel chat.

|  |  |
| --- | --- |
| Public Fields | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [dateRange](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1date_range.html) > | [period\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a77b85a479137349a4e31e717c0ff5865) |
|  | A period to which the statistics applies. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > | [member\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a3fc294fb1c072f9135797c21f7740f2f) |
|  | Number of members in the chat. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > | [mean\_message\_view\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a2e8b287d9706aefab34715ea386098b8) |
|  | Mean number of times the recently sent messages were viewed. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > | [mean\_message\_share\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#aef79a3d4a16149c36b21d93e1b06b051) |
|  | Mean number of times the recently sent messages were shared. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > | [mean\_message\_reaction\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a0c33f67d79615216b79aea760adfef4c) |
|  | Mean number of times reactions were added to the recently sent messages. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > | [mean\_story\_view\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a11797d36fa07dc5a47438ad87ccab4e8) |
|  | Mean number of times the recently posted stories were viewed. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > | [mean\_story\_share\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#ac8b3d006bc9e2c4835f62ba43c2f725b) |
|  | Mean number of times the recently posted stories were shared. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > | [mean\_story\_reaction\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a9cde679c516173da9cf94bd43f2dc571) |
|  | Mean number of times reactions were added to the recently posted stories. |
|  | |
| double | [enabled\_notifications\_percentage\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a1e7064957b5a84daf6893a78e8c80dbf) |
|  | A percentage of users with enabled notifications for the chat; 0-100. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > | [member\_count\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a0d51856f0374e6592972e66c48610fe8) |
|  | A graph containing number of members in the chat. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > | [join\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a8628734e71b6b29fd024215c7ac0addc) |
|  | A graph containing number of members joined and left the chat. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > | [mute\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#ac49c522800e7ec4aa94f0dbdb6feb165) |
|  | A graph containing number of members muted and unmuted the chat. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > | [view\_count\_by\_hour\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a5b164108b1c256ce2498662760c15aa3) |
|  | A graph containing number of message views in a given hour in the last two weeks. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > | [view\_count\_by\_source\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a031c8fe266ff1efe051f4f47551dc853) |
|  | A graph containing number of message views per source. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > | [join\_by\_source\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#aef0553b31f6f92498f845fde99555d88) |
|  | A graph containing number of new member joins per source. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > | [language\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a9f699034b73f92699a5ce2f37afb4017) |
|  | A graph containing number of users viewed chat messages per language. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > | [message\_interaction\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a6df69eb883cca1024a43bd8f7834c933) |
|  | A graph containing number of chat message views and shares. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > | [message\_reaction\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a10cafa8eb0a84ee5de90d064fd35017b) |
|  | A graph containing number of reactions on messages. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > | [story\_interaction\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a6d0b785689bdc7c5374a8bbf3261a79c) |
|  | A graph containing number of story views and shares. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > | [story\_reaction\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a57bbc2f62e328c2019a6324bfcf1d338) |
|  | A graph containing number of reactions on stories. |
|  | |
| [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > | [instant\_view\_interaction\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a4377ffc3317f5566895bfc7f6496d9a7) |
|  | A graph containing number of views of associated with the chat instant views. |
|  | |
| [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [chatStatisticsInteractionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_interaction_info.html) > > | [recent\_interactions\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#abc6a1e07e04385cf271f6774ebcc39ac) |
|  | Detailed statistics about number of views and shares of recently sent messages and posted stories. |
|  | |

|  |  |
| --- | --- |
| Public Instance Methods | |
|  | [chatStatisticsChannel](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a19df89221b2b87e54f24cfe0314b5bfb) () |
|  | |
|  | [chatStatisticsChannel](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a1120759d703c4493b9468c902ed667d1) ([object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [dateRange](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1date_range.html) > &&[period\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a77b85a479137349a4e31e717c0ff5865), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > &&[member\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a3fc294fb1c072f9135797c21f7740f2f), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > &&[mean\_message\_view\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a2e8b287d9706aefab34715ea386098b8), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > &&[mean\_message\_share\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#aef79a3d4a16149c36b21d93e1b06b051), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > &&[mean\_message\_reaction\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a0c33f67d79615216b79aea760adfef4c), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > &&[mean\_story\_view\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a11797d36fa07dc5a47438ad87ccab4e8), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > &&[mean\_story\_share\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#ac8b3d006bc9e2c4835f62ba43c2f725b), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > &&[mean\_story\_reaction\_count\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a9cde679c516173da9cf94bd43f2dc571), double [enabled\_notifications\_percentage\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a1e7064957b5a84daf6893a78e8c80dbf), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > &&[member\_count\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a0d51856f0374e6592972e66c48610fe8), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > &&[join\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a8628734e71b6b29fd024215c7ac0addc), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > &&[mute\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#ac49c522800e7ec4aa94f0dbdb6feb165), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > &&[view\_count\_by\_hour\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a5b164108b1c256ce2498662760c15aa3), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > &&[view\_count\_by\_source\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a031c8fe266ff1efe051f4f47551dc853), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > &&[join\_by\_source\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#aef0553b31f6f92498f845fde99555d88), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > &&[language\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a9f699034b73f92699a5ce2f37afb4017), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > &&[message\_interaction\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a6df69eb883cca1024a43bd8f7834c933), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > &&[message\_reaction\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a10cafa8eb0a84ee5de90d064fd35017b), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > &&[story\_interaction\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a6d0b785689bdc7c5374a8bbf3261a79c), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > &&[story\_reaction\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a57bbc2f62e328c2019a6324bfcf1d338), [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > &&[instant\_view\_interaction\_graph\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a4377ffc3317f5566895bfc7f6496d9a7), [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [chatStatisticsInteractionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_interaction_info.html) >> &&[recent\_interactions\_](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#abc6a1e07e04385cf271f6774ebcc39ac)) |
|  | |
| void | [store](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a8044dab2ba3c75066745014259c050c7) (TlStorerToString &s, const char \*field\_name) const final |
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
| static const std::int32\_t | [ID](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#ac8ca971fe7ed0677d67b1507df9bcc5f) = -1375151660 |
|  | Identifier uniquely determining a type of the object. |
|  | |

## Constructor & Destructor Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a19df89221b2b87e54f24cfe0314b5bfb)chatStatisticsChannel() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [chatStatisticsChannel](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html) | ( |  | ) |  |

A detailed statistics about a channel chat.

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a1120759d703c4493b9468c902ed667d1)chatStatisticsChannel() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| [chatStatisticsChannel](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html) | ( | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [dateRange](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1date_range.html) > && | *period\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > && | *member\_count\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > && | *mean\_message\_view\_count\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > && | *mean\_message\_share\_count\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > && | *mean\_message\_reaction\_count\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > && | *mean\_story\_view\_count\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > && | *mean\_story\_share\_count\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [statisticalValue](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1statistical_value.html) > && | *mean\_story\_reaction\_count\_*, |
|  |  | double | *enabled\_notifications\_percentage\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > && | *member\_count\_graph\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > && | *join\_graph\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > && | *mute\_graph\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > && | *view\_count\_by\_hour\_graph\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > && | *view\_count\_by\_source\_graph\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > && | *join\_by\_source\_graph\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > && | *language\_graph\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > && | *message\_interaction\_graph\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > && | *message\_reaction\_graph\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > && | *story\_interaction\_graph\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > && | *story\_reaction\_graph\_*, |
|  |  | [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [StatisticalGraph](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_statistical_graph.html) > && | *instant\_view\_interaction\_graph\_*, |
|  |  | [array](https://core.telegram.org/tdlib/docs/td__api_8h.html#af1fc9e22ea256af1e507bbaf7885b312)< [object\_ptr](https://core.telegram.org/tdlib/docs/td__api_8h.html#a7b249263de52128c32781ba0e713b556)< [chatStatisticsInteractionInfo](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_interaction_info.html) >> && | *recent\_interactions\_* |
|  | ) |  |  |

A detailed statistics about a channel chat.

Parameters
:   |  |  |  |
    | --- | --- | --- |
    | [in] | period\_ | A period to which the statistics applies. |
    | [in] | member\_count\_ | Number of members in the chat. |
    | [in] | mean\_message\_view\_count\_ | Mean number of times the recently sent messages were viewed. |
    | [in] | mean\_message\_share\_count\_ | Mean number of times the recently sent messages were shared. |
    | [in] | mean\_message\_reaction\_count\_ | Mean number of times reactions were added to the recently sent messages. |
    | [in] | mean\_story\_view\_count\_ | Mean number of times the recently posted stories were viewed. |
    | [in] | mean\_story\_share\_count\_ | Mean number of times the recently posted stories were shared. |
    | [in] | mean\_story\_reaction\_count\_ | Mean number of times reactions were added to the recently posted stories. |
    | [in] | enabled\_notifications\_percentage\_ | A percentage of users with enabled notifications for the chat; 0-100. |
    | [in] | member\_count\_graph\_ | A graph containing number of members in the chat. |
    | [in] | join\_graph\_ | A graph containing number of members joined and left the chat. |
    | [in] | mute\_graph\_ | A graph containing number of members muted and unmuted the chat. |
    | [in] | view\_count\_by\_hour\_graph\_ | A graph containing number of message views in a given hour in the last two weeks. |
    | [in] | view\_count\_by\_source\_graph\_ | A graph containing number of message views per source. |
    | [in] | join\_by\_source\_graph\_ | A graph containing number of new member joins per source. |
    | [in] | language\_graph\_ | A graph containing number of users viewed chat messages per language. |
    | [in] | message\_interaction\_graph\_ | A graph containing number of chat message views and shares. |
    | [in] | message\_reaction\_graph\_ | A graph containing number of reactions on messages. |
    | [in] | story\_interaction\_graph\_ | A graph containing number of story views and shares. |
    | [in] | story\_reaction\_graph\_ | A graph containing number of reactions on stories. |
    | [in] | instant\_view\_interaction\_graph\_ | A graph containing number of views of associated with the chat instant views. |
    | [in] | recent\_interactions\_ | Detailed statistics about number of views and shares of recently sent messages and posted stories. |

## Method Documentation

## [◆](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_statistics_channel.html#a8044dab2ba3c75066745014259c050c7)store()

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