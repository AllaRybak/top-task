# import sys
import unittest
from Rybakova_modul_testirov import IntElements


class Testing(unittest.TestCase):
    def setUp(self):
        self.int_elements = IntElements()

    def test_sum_int(self):
        buf = [[5, 3, 8],
               [2, '123', 'Error'],
               [-2, -3, -5],
               [1.6, 3.4, 'Error']]
        for i in buf:
            with self.subTest():
                self.assertEqual(self.int_elements.sum_int(i[0], i[1]), i[2])

    def test_arifm_middle(self):
        buf = [[5, 3, 4],
               [2, '123', 'Error'],
               [-2, -3, -2.5],
               [3, 2, 2.5]]
        for i in buf:
            with self.subTest():
                self.assertEqual(self.int_elements.arifm_middle(i[0], i[1]), i[2])

    def test_max(self):
        buf = [[5, 3, 5],
               [2, 3.5, 'Error'],
               [-2, -3, -2],
               [3, 2, 3]]
        for i in buf:
            with self.subTest():
                self.assertEqual(self.int_elements.maxim(i[0], i[1]), i[2])

    def test_min(self):
        buf = [[5, 3, 3],
               [2, 3.5, 'Error'],
               [-2, -3, -3],
               [3, 2, 2]]
        for i in buf:
            with self.subTest():
                self.assertEqual(self.int_elements.mini(i[0], i[1]), i[2])

    def tearDown(self):
        print('Сделано!')


if __name__ == '__main__':
    unittest.main()
