import unittest
from ayum import translit

cases_cyr_lat = {
    'авдотья': 'avdothya',
    'отъявленный': 'otyavlennqiy',
    'бактерицидный': 'baktericidnqiy',
    'вьюга': 'vhyuga',
    'юг': 'yug',
    'эра': 'era',
    'цирк': 'cirk',
    'жюри': 'juri',
    'щебетать': 'whebetath',
    'парашют': 'parawut',
    'аллофон': 'allofon',
    'съезд': 'syezd',
    'метр': 'metr',
    'мэтр': 'mqetr',
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
    'объём': 'obyom',
    'выемка': 'vqiemka',
    'каньон': 'kanyon',
    'гальюн': 'galyun',
    'веет': 'veet',
    'веешь': 'veew',
    'епархия': 'yeparxiya',
    'ералаш': 'yeralaw',
    'красивые': 'krasivqie',
}


class TestToLatin(unittest.TestCase):

    def test_all(self):
        for cyr, lat in cases_cyr_lat.items():
            self.assertEqual(translit.to_latin(cyr), lat)


if __name__ == '__main__':
    unittest.main()
