import unittest
from ayum import translit

cases_cyr_lat = {
    'авдотья': 'avdothya',
    'авдотьи': 'avdothi',
    'авдотьe': 'avdothe',
    'отъявленный': 'othyavlennyy',
    'бактерицидные': 'baktericidnye',
    'вьюга': 'vhyuga',
    'конъюктивит': 'konhyuktivit',
    'каньон': 'kanhyon',
    'гэй': 'gqy',
    'гей': 'gey',
    'юг': 'yug',
    'эра': 'qra',
    'эон': 'qon',
    'мэон': 'mqon',
    'цирк': 'cirk',
    'жюри': 'juri',
    'щебетать': 'whebetath',
    'парашют': 'parawut',
    'аллофон': 'allofon',
    'съезд': 'shezd',
    'бельё': 'belhyo',
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
    'ща': 'wha',
    'щьа': 'whya',
    'щья': 'whya',
    'щьу': 'whyu',
    'щу': 'whu',
    'щё': 'who',
    'щьё': 'whyo',
    'жё': 'jo',
    'жьё': 'jyo',
    'жьо': 'jyo',
    'цью': 'cyu',
    'цю': 'cu',
    'цу': 'cu',
    'цьу': 'cyu',
    'лье': 'lhe',
    'льё': 'lhyo',
    'лью': 'lhyu',
    'льо': 'lhyo',
    'шъо': 'wyo',
    'цъу': 'cyu',
    'щъё': 'whyo',
    'жъю': 'jyu',
    'чъи': 'chyi',
    'шъе': 'wye',
    'удушье': 'uduwye',
    'ружьё': 'rujyo',
    'ыфкуиль': 'yyfkuilh',
    'подыграть': 'podygrath',
    'вожжи': 'vojji',
    'жужжать': 'jujjath',
    'объём': 'obhyom',
    'выемка': 'vyemka',
    'каньон': 'kanhyon',
    'гальюн': 'galhyun',
    'веет': 'veet',
    'веешь': 'veew',
    'вьётся': 'vhyotsha',
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
    'дйон' : 'dhyon',
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
    'Объёмом 5 литров': 'obhyomom-5-litrov',
}

class TestSlugify(unittest.TestCase):

    def test_all(self):
        for cyr, slug in cases_cyr_slug.items():
            self.assertEqual(translit.slugify(cyr), slug)


if __name__ == '__main__':
    unittest.main()
