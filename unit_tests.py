import unittest
from main import algorithm


class TestHamsters(unittest.TestCase):

    def test_algorithm(self):
        """Тест який порівнює результат алгоритму на основі вхідних і вихідних файлів in/hamstr.in та in/hamstr.out"""
        current = algorithm('in/hamstr.in', 'out/hamstr.out')
        self.assertEqual(current, 2)

    def test1_algorithm(self):
        """Тест який порівнює результат алгоритму на основі вхідних і вихідних файлів in/hamstr.in1 та in/hamstr.out1"""
        current = algorithm('in/hamstr.in1', 'out/hamstr.out1')
        self.assertEqual(current, 3)

    def test2_algorithm(self):
        """Тест який порівнює результат алгоритму на основі вхідних і вихідних файлів in/hamstr.in2 та in/hamstr.out2"""
        current = algorithm('in/hamstr.in2', 'out/hamstr.out2')
        self.assertEqual(current, 1)


if __name__ == '__main__':
    unittest.main()
