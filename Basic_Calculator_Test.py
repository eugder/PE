import unittest
from Basic_Calculator import calculator


class MyTestCase(unittest.TestCase):
    def test_calculator_1(self):
        self.assertEqual(calculator(1, "+", 2), 3)
    def test_calculator_2(self):
        self.assertEqual(calculator(2, "*", 2), 4)
    def test_calculator_3(self):
        self.assertEqual(calculator(2, "/", 2), 1)
    def test_calculator_4(self):
        self.assertEqual(calculator(2, "-", 2), 0)
    def test_calculator_5(self):
        self.assertEqual(calculator(2, "/", 0), "Can't divide by 0!")


if __name__ == '__main__':
    unittest.main()
