import unittest
from math import sqrt
from itertools import count, islice


class Pernicious(object):
    """
    get the range of the number from 3 to the number, converting each to binary
    for
    """
    def __init__(self, number):
        self.number = number

    # long method
    def is_pernicious(self):
        primes = []
        if self.number <= 2:
            return "No pernicious numbers"
        for x in range(3, int(self.number) + 1):
            if Pernicious.is_prime(sum([int(i) for i in '{0:b}'.format(x)])):
                primes.append(x)
        return primes

    # using ternary and lambda
    def is_pernicious_v2(self):
        m = lambda i: '{0:b}'.format(i)
        if self.number <= 1:
            return "No pernicious numbers"
        return [x for x in range(3, int(self.number) + 1) if Pernicious.is_prime(sum([int(y) for y in m(x)]))]

    def is_pernicious_v3(self):
        return [x for x in range(int(self.number) + 1) if
                bin(x).count("1") in [2, 3, 5, 7, 11, 13]] or "No pernicious numbers"


    @staticmethod
    def is_prime(num):
        return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num) - 1)))


class PerniciousTests(unittest.TestCase):
    def test_1(self):
        pern = Pernicious(4)
        self.assertEqual(pern.is_pernicious(), [3])

    def test_2(self):
        pern = Pernicious(5)
        self.assertEqual(pern.is_pernicious(), [3, 5])

    def test_3(self):
        pern = Pernicious(232)
        self.assertEqual(pern.is_pernicious(),
                         [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 24, 25, 26, 28, 31, 33, 34, 35, 36,
                          37, 38, 40, 41, 42, 44, 47, 48, 49, 50, 52, 55, 56, 59, 61, 62, 65, 66, 67, 68, 69, 70, 72,
                          73, 74, 76, 79, 80, 81, 82, 84, 87, 88, 91, 93, 94, 96, 97, 98, 100, 103, 104, 107, 109, 110,
                          112, 115, 117, 118, 121, 122, 124, 127, 129, 130, 131, 132, 133, 134, 136, 137, 138, 140, 143,
                          144, 145, 146, 148, 151, 152, 155, 157, 158, 160, 161, 162, 164, 167, 168, 171, 173, 174, 176,
                          179, 181, 182, 185, 186, 188, 191, 192, 193, 194, 196, 199, 200, 203, 205, 206, 208, 211, 213,
                          214, 217, 218, 220, 223, 224, 227, 229, 230])

    def test_4(self):
        pern = Pernicious(0)
        self.assertEqual(pern.is_pernicious(), "No pernicious numbers")

    def test_5(self):
        pern = Pernicious(1)
        self.assertEqual(pern.is_pernicious(), "No pernicious numbers")

    def test_6(self):
        pern = Pernicious(-54)
        self.assertEqual(pern.is_pernicious(), "No pernicious numbers")

    def test_7(self):
        pern = Pernicious(6.99)
        self.assertEqual(pern.is_pernicious(), [3, 5, 6])

    def test_8(self):
        pern = Pernicious(-6.99)
        self.assertEqual(pern.is_pernicious(), "No pernicious numbers")

    def test_9(self):
        pern = Pernicious(42.42424242)
        self.assertEqual(pern.is_pernicious(),
                         [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 24, 25, 26, 28, 31, 33, 34, 35, 36,
                          37, 38, 40, 41, 42])

    def test_10(self):
        pern = Pernicious(2)
        self.assertEqual(pern.is_pernicious(), "No pernicious numbers")