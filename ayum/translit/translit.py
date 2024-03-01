from icu import UnicodeString, Locale, Normalizer2, Transliterator

locale = Locale('ru_RU')


def to_latin(string, locale=locale):
    ustring = UnicodeString(string)
    nfc = Normalizer2.getNFCInstance()
    ustring = nfc.normalize(ustring)

    trans = Transliterator.createFromRules("",
                                           "$wb = [^[:Letter:]] ;"
                                           # е
                                           "$wb { е > ye ;"
                                           "[ыq] { е } $wb > e ;"
                                           "[уеёыаоэяиюьъiuoeaq] { е > ye ;"
                                           "е > e ;"
                                           # э
                                           "$wb { э > e ;"
                                           "[жшцйjwcy] { э > е ;"
                                           "э > qe ;"
                                           # ы
                                           "[жшцйjwcy] { ы > i ;"
                                           "ы > q ;"
                                           # ё
                                           "$wb { ё > yo ;"
                                           "[жшцйjwcy] { ё > o ;"
                                           "[уеёыаоэяиюьъiuoeaq] { ё > yo ;"
                                           "ё > ho ;"
                                           # ю
                                           "$wb { ю > yu ;"
                                           "[жшцйjwcy] { ю > u ;"
                                           "[уеёыаоэяиюьъiuoeaq] { ю > yu ;"
                                           "ю > hu ;"
                                           # я
                                           "$wb { я > ya ;"
                                           "[жшцйjwcy] { я > a ;"
                                           "[уеёыаоэяиюьъiuoeaq] { я > ya ;"
                                           "я > ha ;"
                                           # Остальные буквы
                                           "а > a ;"
                                           "б > b ;"
                                           "в > v ;"
                                           "г > g ;"
                                           "д > d ;"
                                           "ж > j ;"
                                           "з > z ;"
                                           "и > i ;"
                                           "й > y ;"
                                           "к > k ;"
                                           "л > l ;"
                                           "м > m ;"
                                           "н > n ;"
                                           "о > o ;"
                                           "п > p ;"
                                           "р > r ;"
                                           "с > s ;"
                                           "т > t ;"
                                           "у > u ;"
                                           "ф > f ;"
                                           "х > x ;"
                                           "ц > c ;"
                                           "ч > ch ;"
                                           "ш > w ;"
                                           "щ > wh ;"
                                           # Проход с начала
                                           ":: Any-Null ;"
                                           "ь > h ;"
                                           "ъ > ;"
                                           # Проход с начала
                                           ":: Any-Null ;"
                                           "h+ > h ;"
                                           )
    ustring = trans.transliterate(ustring)
    return ustring
