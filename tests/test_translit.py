import unittest
from ayum import translit

cases_cyr_lat = {
    'авдотья': 'avdotya',
    'авдотьи': 'avdothi',
    'авдотьe': 'avdothe',
    'отъявленный': 'otqavlennyy',
    'бактерицидные': 'baktericidnye',
    'вьюга': 'vyuga',
    'конъюктивит': 'konquktivit',
    'каньон': 'kanyon',
    'гэй': 'gqy',
    'юг': 'yug',
    'эра': 'qra',
    'эон': 'qon',
    'мэон': 'mqhon',
    'цирк': 'cirk',
    'жюри': 'juri',
    'щебетать': 'whebetath',
    'парашют': 'parawut',
    'аллофон': 'allofon',
    'съезд': 'sqezd',
    'бельё': 'belyo',
    'отребье': 'otrebhe',
    'красивые': 'krasivye',
    'метр': 'metr',
    'мэтр': 'mqtr',
    'лук': 'luk',
    'люк': 'lhuk',
    'клык': 'klyk',
    'клик': 'klik',
    'клён': 'klhon',
    'клон': 'klon',
    'раса': 'rasa',
    'ряса': 'rhasa',
    'пот': 'pot',
    'под': 'pod',
    'топ': 'top',
    'топь': 'toph',
    'йод': 'yod',
    'яд': 'yad',
    'чьи': 'chyi',
    'чья': 'chya',
    'чёрт': 'chort',
    'чьорт': 'chyort',
    'чьёрт': 'chyort',
    'шью': 'wyu',
    'шьу': 'wyu',
    'щя': 'wha',
    'щьа': 'whya',
    'щьа': 'whya',
    'ыфкуиль': 'yyfkuilh',
    'подыграть': 'podygrath',
    'вожжи': 'vojji',
    'жужжать': 'jujjath',
    'объём': 'obqom',
    'выемка': 'vyemka',
    'каньон': 'kanyon',
    'гальюн': 'galyun',
    'веет': 'veet',
    'веешь': 'veew',
    'вьётся': 'vyotsha',
    'выёживаться': 'vyyojivathsha',
    'выиграть': 'vyigrath',
    'епархия': 'eparxiya',
    'ералаш': 'eralaw',
    'красивые': 'krasivye',
    'коммерсантъ': 'kommersant',
    'мэи': 'mqi',
    'ыкать': 'yykath',
    'ЙЦУКЕНГШЩЗХЪ' : 'YCUKENGWWHZX',
    'Ёж': 'Yoj',
    'ЁЖ': 'YOJ',
    'ФЫВАПРОЛД': 'FYVAPROLD',
    'ЯЧСМИТЬ': 'YACHSMITH',
}


class TestToLatin(unittest.TestCase):

    def test_all(self):
        for cyr, lat in cases_cyr_lat.items():
            self.assertEqual(translit.to_latin(cyr), lat)


cases_cyr_slug = {
    'лучше — не хуже': 'luchwe-ne-xuje',
    'ḟ...aÅ—ß': 'f-aa-ss',
}

class TestSlugify(unittest.TestCase):

    def test_all(self):
        for cyr, slug in cases_cyr_slug.items():
            self.assertEqual(translit.slugify(cyr), slug)


if __name__ == '__main__':
    unittest.main()
