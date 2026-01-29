from icu import UnicodeString, Normalizer2, Transliterator
import re

def to_latin(string):
    ustring = UnicodeString(string)
    nfc = Normalizer2.getNFCInstance()
    ustring = nfc.normalize(ustring)

    trans = Transliterator.createFromRules("",
                                           "$wb = [^[:Letter:]] ;"
                                           "$vow = [аАоОуУэЭыЫяЯёЁюЮеЕиИaAoOuUqQyYeEiI] ;"
                                           "$con = [цкнгшщзхфвпрлджчсмтбЦКНГШЩЗХФВПРЛДЖЧСМТБ] ;"
                                           "$cwj = [цЦчЧшШщЩжЖйЙ] ;"
                                           "$hh = [ьЬъЪ] ;"
                                           ";"
                                           # Искуственное добавление ъ в некоторых местах (ср. МИРДАЛЬС^ЙЕКЮДЛЬ)
                                           "$con { й > ъ | й ;"
                                           "$con { Й > Ъ | Й ;"
                                           # Удаление нетраслитерируемых ь и ъ
                                           "$wb { ($hh+) } $wb > $1 | ;"
                                           "[ъЪ] $hh* } $wb > ;"
                                           "[ъЪ] $hh* } $con > ;"
                                           "$cwj { [ьЬ] $hh* } $wb > ;"
                                           "$cwj { [ьЬ] $hh* } $con > ;"
                                           # Проход сначала
                                           ":: Any-Null ;"
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
                                           # ё
                                           "$wb { ё } $wb > yo ;"
                                           "$wb { Ё } $wb > YO ;"
                                           "$wb { ё > yo ;"
                                           "$wb { Ё } [[:Ll:]] > Yo ;"
                                           "$wb { Ё > YO ;"
                                           "$cwj { ё > o ;"
                                           "$cwj { Ё > O ;"
                                           "$vow { ё > yo ;"
                                           "$vow { Ё > YO ;"
                                           "$hh { ё > yo ;"
                                           "$hh { Ё > YO ;"
                                           "ё > ho ;"
                                           "Ё > HO ;"
                                           # ю
                                           "$wb { ю > yu ;"
                                           "$wb { Ю } [[:Ll:]] > Yu ;"
                                           "$wb { Ю > YU ;"
                                           "$cwj { ю > u ;"
                                           "$cwj { Ю > U ;"
                                           "$vow { ю > yu ;"
                                           "$vow { Ю > YU ;"
                                           "$hh { ю > yu ;"
                                           "$hh { Ю > YU ;"
                                           "ю > hu ;"
                                           "Ю > HU ;"
                                           # я
                                           "$wb { я > ya ;"
                                           "$wb { Я } [[:Ll:]] > Ya ;"
                                           "$wb { Я > YA ;"
                                           "$cwj { я > a ;"
                                           "$cwj { Я > A ;"
                                           "$vow { я > ya ;"
                                           "$vow { Я > YA ;"
                                           "$hh { я > ya ;"
                                           "$hh { Я > YA ;"
                                           "я > ha ;"
                                           "Я > HA ;"
                                           # Буква и
                                           "и > i ; И > I ;"
                                           # Буква а
                                           "$hh { а > ya ;"
                                           "$hh { А > YA ;"
                                           "а > a ; А > A ;"
                                           # Буква о
                                           "$hh { о > yo ;"
                                           "$hh { О > YO ;"
                                           "о > o ; О > O ;"
                                           # Буква у
                                           "$hh { у > yu ;"
                                           "$hh { У > YU ;"
                                           "у > u ; У > U ;"
                                           # Проход с начала, в строке незаменены остались согласные и ь и ъ
                                           ":: Any-Null ;"
                                           # Буквы ь и ъ
                                           "$cwj { [ьъ] } [yY] > ;"
                                           "$cwj { [ЬЪ] } [yY] > ;"
                                           "$cwj { [ьъ] > y ;"
                                           "$cwj { [ЬЪ] > Y ;"
                                           "[ьъ] > h ;"
                                           "[ЬЪ] > H ;"
                                           # Проход с начала, в строке незаменены остались согласные
                                           ":: Any-Null ;"
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
