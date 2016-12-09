import unittest


def nb_dig(n, d):
    squares = [x**2 for x in range(0, n+1)]
    return sum([str(i).count(str(d)) for i in squares if str(d) in str(i)])


class DigTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(nb_dig(5750, 0), 4700)

    def test2(self):
        self.assertEqual(nb_dig(11011, 2), 9481)

    def test3(self):
        self.assertEqual(nb_dig(12224, 8), 7733)

    def test4(self):
        self.assertEqual(nb_dig(11549, 1), 11905)
