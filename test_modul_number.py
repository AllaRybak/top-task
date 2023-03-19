# import sys
import unittest
from Rybakova_modul_testirov2 import Number


class Testing(unittest.TestCase):
    def setUp(self):
        self.number = Number()

    def test_num22(self):
        buf = [[26, '11010'],
               ['a', 'Error'],
               [-90, '-1011010'],
               ['', 'Error']]
        for i in buf:
            with self.subTest():
                self.assertEqual(self.number.num22(i[0]), i[1])

    def test_num28(self):
        buf = [[26, '32'],
               ['a', 'Error'],
               [-90, '-132'],
               ['', 'Error']]
        for i in buf:
            with self.subTest():
                self.assertEqual(self.number.num28(i[0]), i[1])

    def test_num216(self):
        buf = [[26, '1a'],
               ['a', 'Error'],
               [-90, '-5a'],
               ['', 'Error']]
        for i in buf:
            with self.subTest():
                self.assertEqual(self.number.num216(i[0]), i[1])

    def tearDown(self):
        print('Сделано!')


if __name__ == '__main__':
    unittest.main()
