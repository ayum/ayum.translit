import unittest
from ayum import translit

cases_cyr_lat = {
    'авдотья': 'avdotya',
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
    'епархия': 'eparxiya',
    'ералаш': 'eralaw',
    'красивые': 'krasivye',
    'коммерсантъ': 'kommersant',
    'мэи': 'mqi',
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


if __name__ == '__main__':
    unittest.main()
