from icu import UnicodeString, Normalizer2, Transliterator
import re

def to_latin(string):
    ustring = UnicodeString(string)
    nfc = Normalizer2.getNFCInstance()
    ustring = nfc.normalize(ustring)

    trans = Transliterator.createFromRules("",
                                           "$wb = [^[:Letter:]] ;"
                                           ";"
                                           # е
                                           "е > e ;"
                                           "Е > E ;"
                                           # э
                                           "э > q ;"
                                           "Э > Q ;"
                                           # ы
                                           "$wb { ы } $wb > y ;"
                                           "$wb { Ы } $wb > Y ;"
                                           "$wb { ы > yy ;"
                                           "$wb { Ы } [[:Ll:]] > Yy ;"
                                           "$wb { Ы > YY ;"
                                           "ы > y ;"
                                           "Ы > Y ;"
                                           # ё (ы транслитерирована, но не й)
                                           "$wb { ё } $wb > yo ;"
                                           "$wb { Ё } $wb > YO ;"
                                           "$wb { ё > yo ;"
                                           "$wb { Ё } [[:Ll:]] > Yo ;"
                                           "$wb { Ё > YO ;"
                                           "[жЖшШщЩцЦчЧйЙjJwWcC] { ё > o ;"
                                           "[жЖшШщЩцЦчЧйЙjJwWcC] { Ё > O ;"
                                           "[jJwWcC][hH] { ё > o ;"
                                           "[jJwWcC][hH] { Ё > O ;"
                                           "[уУеЕёЁыЫаАоОэЭяЯиИюЮьЬiIuUoOeEaAqQyY] { ё > yo ;"
                                           "[уУеЕёЁыЫаАоОэЭяЯиИюЮьЬiIuUoOeEaAqQyY] { Ё > YO ;"
                                           "[ъЪ] { ё > o ;"
                                           "[ъЪ] { Ё > O ;"
                                           "ё > ho ;"
                                           "Ё > HO ;"
                                           # ю (ы транслитерирована, но не й)
                                           "$wb { ю > yu ;"
                                           "$wb { Ю } [[:Ll:]] > Yu ;"
                                           "$wb { Ю > YU ;"
                                           "[жЖшШщЩцЦчЧйЙjJwWcC] { ю > u ;"
                                           "[жЖшШщЩцЦчЧйЙjJwWcC] { Ю > U ;"
                                           "[jJwWcC][hH] { ю > u ;"
                                           "[jJwWcC][hH] { Ю > U ;"
                                           "[уУеЕёЁыЫаАоОэЭяЯиИюЮьЬiIuUoOeEaAqQyY] { ю > yu ;"
                                           "[уУеЕёЁыЫаАоОэЭяЯиИюЮьЬiIuUoOeEaAqQyY] { Ю > YU ;"
                                           "[ъЪ] { ю > u ;"
                                           "[ъЪ] { Ю > U ;"
                                           "ю > hu ;"
                                           "Ю > HU ;"
                                           # я (ы транслитерирована, но не й)
                                           "$wb { я > ya ;"
                                           "$wb { Я } [[:Ll:]] > Ya ;"
                                           "$wb { Я > YA ;"
                                           "[жЖшШщЩцЦчЧйЙjJwWcC] { я > a ;"
                                           "[жЖшШщЩцЦчЧйЙjJwWcC] { Я > A ;"
                                           "[jJwWcC][hH] { я > a ;"
                                           "[jJwWcC][hH] { Я > A ;"
                                           "[уУеЕёЁыЫаАоОэЭяЯиИюЮьЬiIuUoOeEaAqQyY] { я > ya ;"
                                           "[уУеЕёЁыЫаАоОэЭяЯиИюЮьЬiIuUoOeEaAqQyY] { Я > YA ;"
                                           "[ъЪ] { я > a ;"
                                           "[ъЪ] { Я > A ;"
                                           "я > ha ;"
                                           "Я > HA ;"
                                           # Буква и
                                           "и > i ; И > I ;"
                                           # Буква а (э, ы уже транслитерированы)
                                           "$wb [qQyYэЭыЫ] { а > a ;"
                                           "$wb [qQyYэЭыЫ] { А > A ;"
                                           "[qQyYэЭыЫ] { а > ha ;"
                                           "[qQyYэЭыЫ] { А > HA ;"
                                           "[ьъ] { а > ya ;"
                                           "[ЬЪ] { а > Ya ;"
                                           "[ьъ] { А > yA ;"
                                           "[ЬЪ] { А > YA ;"
                                           "а > a ; А > A ;"
                                           # Буква о (э, ы уже транслитерирована)
                                           "$wb [qQyYэЭыЫ] { о > o ;"
                                           "$wb [qQyYэЭыЫ] { О > O ;"
                                           "[qQyYэЭыЫ] { о > ho ;"
                                           "[qQyYэЭыЫ] { О > HO ;"
                                           "[ьъ] { о > yo ;"
                                           "[ЬЪ] { о > Yo ;"
                                           "[ьъ] { О > yO ;"
                                           "[ЬЪ] { О > YO ;"
                                           "о > o ; О > O ;"
                                           # Буква у (э, ы уже транслитерирована)
                                           "$wb [qQyYэЭыЫ] { у > u ;"
                                           "$wb [qQyYэЭыЫ] { У > U ;"
                                           "[qQyYэЭыЫ] { у > hu ;"
                                           "[qQyYэЭыЫ] { У > HU ;"
                                           "[ьъ] { у > yu ;"
                                           "[ЬЪ] { у > Yu ;"
                                           "[ьъ] { У > yU ;"
                                           "[ЬЪ] { У > YU ;"
                                           "у > u ; У > U ;"
                                           # Согласные буквы
                                           "б > b ; Б > B ;"
                                           "в > v ; В > V ;"
                                           "г > g ; Г > G ;"
                                           "д > d ; Д > D ;"
                                           "ж > j ; Ж > J ;"
                                           "з > z ; З > Z ;"
                                           "й > y ; Й > Y ;"
                                           "к > k ; К > K ;"
                                           "л > l ; Л > L ;"
                                           "м > m ; М > M ;"
                                           "н > n ; Н > N ;"
                                           "п > p ; П > P ;"
                                           "р > r ; Р > R ;"
                                           "с > s ; С > S ;"
                                           "т > t ; Т > T ;"
                                           "ф > f ; Ф > F ;"
                                           "х > x ; Х > X ;"
                                           "ц > c ; Ц > C ;"
                                           "ч > ch ;"
                                           "$wb { Ч } [[:Ll:]] > Ch ;"
                                           "Ч > CH ;"
                                           "ш > w ; Ш > W ;"
                                           "щ > wh ;"
                                           "$wb { Щ } [[:Ll:]] > Wh ;"
                                           "Щ > WH ;"
                                           # Проход с начала, в строке незаменены остались только буквы ь и ъ
                                           ":: Any-Null ;"
                                           "ь } [yYйЙ] > ;"
                                           "ъ } [yYйЙ] > ;"
                                           "Ь } [yYйЙ] > ;"
                                           "Ъ } [yYйЙ] > ;"
                                           "[cCwWцЦшШ] { ь > ;"
                                           "[cCwWцЦшШ] { Ь > ;"
                                           "[ъЪ] } $wb > ;"
                                           "ъ > q ;"
                                           "Ъ > Q ;"
                                           "[hH] { ь } [iI] > y ;"
                                           "[hH] { Ь } [iI] > Y ;"
                                           "[hH] { ь > ;"
                                           "[hH] { Ь >;"
                                           "ь > h ;"
                                           "Ь > H ;"
                                           )
    ustring = trans.transliterate(ustring)
    return ustring

def slugify(string):
    latin = string if string.isascii() else to_latin(string)
    slug = latin.lower()
    slug = slug.replace("ß", "ss")
    slug = slug.replace("œ", "oe")
    slug = slug.replace("æ", "ae")
    slug = slug.replace("—", "-")
    slug = slug.replace("–", "-")
    nfkd = Normalizer2.getNFKDInstance()
    slug = nfkd.normalize(slug)
    slug = ''.join(['' if ord(c) > 127 else c if ord('0') <= ord(c) <= ord('9') or ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') else '-' for c in slug]).strip('-')
    print(slug)
    slug = re.sub(r'[-]+', '-', slug)
    return slug
