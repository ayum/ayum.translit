import unittest
from ayum import translit

cases_cyr_lat = {
    'авдотья': 'avdotya',
    'отъявленный': 'otqavlennqiy',
    'бактерицидный': 'baktericidnqiy',
    'вьюга': 'vyuga',
    'конъюктивит': 'konquktivit',
    'каньон': 'kanyon',
    'гэй': 'gqy',
    'юг': 'yug',
    'эра': 'qra',
    'эон': 'qhon',
    'цирк': 'cirk',
    'жюри': 'juri',
    'щебетать': 'whebetath',
    'парашют': 'parawut',
    'аллофон': 'allofon',
    'съезд': 'sqezd',
    'бельё': 'belyo',
    'отребье': 'otrebye',
    'метр': 'metr',
    'мэтр': 'mqtr',
    'лук': 'luk',
    'люк': 'lhuk',
    'клык': 'klqik',
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
    'подыграть': 'podqigrath',
    'вожжи': 'vojji',
    'жужжать': 'jujjath',
    'объём': 'obqom',
    'выемка': 'vqiemka',
    'каньон': 'kanyon',
    'гальюн': 'galyun',
    'веет': 'veet',
    'веешь': 'veew',
    'епархия': 'eparxiya',
    'ералаш': 'eralaw',
    'красивые': 'krasivqie',
    'коммерсантъ': 'kommersant',
    'мэи': 'mqhi',
    'ЙЦУКЕНГШЩЗХЪ' : 'YCUKENGWWHZX',
    'Ёж': 'Yoj',
    'ЁЖ': 'YOJ',
    'ФЫВАПРОЛД': 'FQIVAPROLD',
    'ЯЧСМИТЬ': 'YACHSMITH',
}


class TestToLatin(unittest.TestCase):

    def test_all(self):
        for cyr, lat in cases_cyr_lat.items():
            self.assertEqual(translit.to_latin(cyr), lat)


if __name__ == '__main__':
    unittest.main()
