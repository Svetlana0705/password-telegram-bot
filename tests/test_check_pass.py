import unittest
from helper import check_pass


class TestStringMethods(unittest.TestCase):

    def test(self):
        result = check_pass('1F1h*158')
        self.assertEqual(result, 'Пароль идеален')

    def test1(self):
        self.assertEqual(check_pass('1F1h*15'), 'Пароль ненадежный')

    def test2(self):
        self.assertEqual(check_pass('1F1h*158gfk4'), 'Пароль трудно запомнить')

    def test3(self):
        self.assertEqual(check_pass('Fh*gfkWS'), 'Пароль должен содержать числа')

    def test4(self):
        self.assertEqual(check_pass('3L1hg158'), 'Пароль должен содержать специальный символы *-#')

    def test5(self):
        self.assertEqual(check_pass('3Ы1ол1*8'),
                         'Пароль может содержать только латинские буквы, цифры или специальные символы *-#')

    def test6(self):
        self.assertEqual(check_pass('1f1h*158'), 'Пароль должен содержать заглавные буквы')

    def test7(self):
        self.assertEqual(check_pass('ВВ1S*158'), 'Пароль должен содержать строчные буквы')

    def test8(self):
        self.assertEqual(check_pass('!L1hg15@'), 'Пароль должен содержать специальный символы *-#')

    def test9(self):
        self.assertEqual(check_pass('11AAaa**'), 'Пароль должен содержать более 6 уникальных символов')


if __name__ == '__main__':
    unittest.main()
