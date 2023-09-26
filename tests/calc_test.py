from unittest import TestCase, main
from calc import calc


class calcTest(TestCase):
    def test_add(self):
        self.assertEqual(calc('2+2'), 4)
        self.assertEqual(calc('-2+2'), 0)

    def test_sub(self):
        self.assertEqual(calc('0-2'), -2)

    def test_mul(self):
        self.assertEqual(calc('10*5'), 50)

    def test_div(self):
        self.assertEqual(calc('10/5'), 2.0)
        with self.assertRaises(ZeroDivisionError) as e:
            calc('2/0')
        self.assertEqual('Ошибка деления на ноль!', e.exception.args[0])

    def test_pow(self):
        self.assertEqual(calc('2^4'), 16)
        with self.assertRaises(ValueError) as e:
            calc('2^')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак!', e.exception.args[0])

    def test_fac(self):
        self.assertEqual(calc('5!1'), 120)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('abc')
        self.assertEqual('Выражение должно содержать хотя бы один знак (+-*/^!|)!', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('1+2+3')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак!', e.exception.args[0])

    def test_dnum(self):
        with self.assertRaises(ValueError) as e:
            calc('1.1+2.2')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак!', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calc('abc+def')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак!', e.exception.args[0])

    def test_empty(self):
        with self.assertRaises(TypeError) as e:
            calc('')
        self.assertEqual('Пустая строка, выражение должно содержать 2 целых числа и 1 знак!', e.exception.args[0])

    def test_sqrt(self):
        self.assertEqual(calc('25|1'), 5)

if __name__ == '__main__':
    main()
