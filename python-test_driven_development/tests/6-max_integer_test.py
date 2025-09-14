#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_UniqueElems(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_MultipleMaxs(self):
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)

    def test_NoUnique(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_Negatives(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_MaxInMiddle(self):
        self.assertEqual(max_integer([-1, -2, 3, 2, 0]), 3)

    def test_Mixed(self):
        self.assertEqual(max_integer([1, 4, -1, 7, 0, 3, -15, 12]), 12)

    def test_OneElem(self):
        self.assertEqual(max_integer([0]), 0)

    def test_EmptyArray(self):
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()
