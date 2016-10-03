import unittest
from . import build_tower


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(build_tower.tower_builder(1), ['*', ])

    def test_2(self):
        self.assertEqual(build_tower.tower_builder(1), ['*', ])

    def test_3(self):
        self.assertEqual(build_tower.tower_builder(2), [' * ', '***'])

    def test_4(self):
        self.assertEqual(build_tower.tower_builder(3), ['  *  ', ' *** ', '*****'])

    def test_5(self):
        self.assertEqual(build_tower.tower_builder(6), ['     *     ',
                                                        '    ***    ',
                                                        '   *****   ',
                                                        '  *******  ',
                                                        ' ********* ',
                                                        '***********'
                                                        ])


if __name__ == '__main__':
    unittest.main()
