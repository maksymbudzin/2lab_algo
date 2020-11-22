import unittest
from hamster_manager import algorithm


class HamsterTestCase(unittest.TestCase):
    """Тести для hamster_manager.py"""

    def test_hamstr1_out(self):
        """Тест який порівнює результат алгоритму і вихідний файл hamstr.in1"""
        current = algorithm('in_put/hamstr.in1', 'out_put/hamstr.in1')

        self.assertEqual(current, 2)

    def test_hamstr2_out(self):
        """Тест який порівнює результат алгоритму і вихідний файл hamstr.in2"""
        current = algorithm('in_put/hamstr.in2', 'out_put/hamstr.in2')

        self.assertEqual(current, 3)

    def test_hamstr3_out(self):
        """Тест який порівнює результат алгоритму і вихідний файл hamstr.in3"""
        current = algorithm('in_put/hamstr.in3', 'out_put/hamstr.in3')

        self.assertEqual(current, 1)


if __name__ == '__name__':
    unittest.main()
