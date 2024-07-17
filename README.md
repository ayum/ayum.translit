Латинизация русской кириллицы
=============================

Используется следующее соответствие:
- *а* —  *a*;
- *б* —  *b*;
- *в* —  *v*;
- *г* —  *g*;
- *д* —  *d*;
- *е* —  *e*;
- *ё* — *yo*, если стоит в начале слов, после гласных, *ь*;
- *ё* —  *o*, если стоит после непарных твердых согласных, *ъ*;
- *ё* — *ho*, во всех остальных случаях;
- *ж* —  *j*;
- *з* —  *z*;
- *и* —  *i*;
- *й* —  *y*;
- *к* —  *k*;
- *л* —  *l*;
- *м* —  *m*;
- *н* —  *n*;
- *о* —  *o*;
- *п* —  *p*;
- *р* —  *r*;
- *с* —  *s*;
- *т* —  *t*;
- *у* —  *u*;
- *ф* —  *f*;
- *х* —  *x*;
- *ц* —  *c*;
- *ч* — *ch*;
- *ш* —  *w*;
- *щ* — *wh*;
- *ъ* —  *q*, не может использоваться для имитации старой орфографии;
- *ы* —  *y*;
- *ь* —  *h*, а также как разделитель (редко встречается): между *э* и *а*, *о*, *у*, *е*, между *ы* и *а*, *о*, *у*, между гласными и *ы*, в начале слова перед *ы*;
- *э* —  *q*;
- *ю* — *yu*, если стоит в начале слов, после гласных, *ь*;
- *ю* —  *u*, если стоит после непарных твердых согласных, *ъ*;
- *ю* — *hu*, во всех остальных случаях;
- *я* — *ya*, если стоит в начале слов, после гласных, *ь*;
- *я* — *a*, если стоит после непарных твердых согласных, *ъ*;
- *я* — *ha*, во всех остальных случаях.

Соответствие интуитивное, но несколько пояснений сделаю нужно: 
- Буквосочетание *ьо* после *л* или *н*, встречающееся в заимствованных словах, которое произносится с йотирование передается как *yo*, иначе было бы *лё*, *нё*.
- Если на письме в заимствованных словах предполагается смягчение согласной, которое не происходит, это можно отражать отходом при латинизации от кириллического написания. Но, в основном, рекомендуется сохранять буквенное соответствие с кириллическим написанием, так как часто одной из норм является смягченное произношение. Например, допускаются два варианта произношения: со смягченной согласной перед *е* и с несмягчённой в слове *бактерицидный*.
- В словах *веешь*, *смеешь*, *вошь* и подобных, там где мягкий знак не несёт орфоэпической функции он не транслитерируется, иначе проставление *h* меняло бы букву, например, с *ш* (*w*) на *щ* (*wh*).
- В словах с *ъ* на конце, имитирующих старую орфографию, твёрдый знак опускается.
- Разделительные знаки перед йотированными гласными обозначаются твердый — *q*, мягкий — *h*, если требуется. Мягкий знак не требуется, если йотированность уже показана латинской *y*, обозначающей *й*, которая смягчает согласную.
- Латинские буквы *y*, *q* обозначают кроме *й* и *ъ*, также *ы*, *э*, что путаницы почти не вносит, потому что эти буквы в некоторых сочетаниях (*эи*, *аы*) в русском языке почти не встречаются, гласные после *э* редкость, а после *ы* доставляет сложность только относительно часто встречающаяся *у*, как в слове *выучить*.
- Буква *q* используется как разделительный *ъ*. Так как *q* используется ещё как *э*, то если после *э* идёт *а*, *о*, *у*, *е*, она отделяется *h*, чтобы различать *э* и *ъ*. Если слово начиначется с *э*, то разделительная *h* не требуется, так как *q*  в начале слова всегда обозначает *э*.
- Латинская *y* всегда обозначает *й* в начале слова и после латинской *h*. 

Примеры:

- авдотья - avdotya;
- отъявленный - otqavlennyy;
- бактерицидные - baktericidnye;
- вьюга - vyuga;
- юг - yug;
- эра - qra;
- эон - qon;
- мэон - mqhon;
- цирк - cirk;
- жюри - juri;
- щебетать - whebetath;
- парашют - parawut;
- аллофон - allofon;
- съезд - sqezd;
- метр - metr;
- мэтр - mqtr;
- лук - luk;
- люк - lhuk;
- клык - klyk;
- клик - klik;
- клён - klhon;
- клон - klon;
- раса - rasa;
- ряса - rhasa;
- пот - pot;
- под - pod;
- топ - top;
- топь - toph;
- йод - yod;
- яд - yad;
- ыфкуиль - yyfkuilh
- подыграть - podygrath;
- вожжи - vojji;
- жужжать - jujjath;
- объём - obqom;
- бельё - belyo;
- подъезд - podqezd;
- отребье - otrebye;
- выемка - vyemka;
- гальюн - galyun;
- веет - veet;
- веешь - veew;
- епархия - yeparxiya;
- ералаш - eralaw;
- красивые - krasivye;
- коммерсантъ - kommersant;
- тэер - tqher;
- гэй - gqy;
- гей - gey;
- МЭИ - MQI.
- чей - chey;
- чьи - chyi;
- каньон - kanyon;

Примеры использования кода:
===========================

При латинизации выполняется нормализация юникода, делать её вручную не нужно. См. пример 2.


```python3
from ayum.translit import to_latin

# 1
print(to_latin('Объёмом 5 литров')) # prints 'Оbqomom 5 litrov'

# 2
print(to_latin('\u0435\u0308')) # prints 'yo'
print(to_latin('\u0451'))       # prints 'yo'

```
