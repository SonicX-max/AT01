import unittest

def remainder(a, b):
    """
    Функция для вычисления остатка от деления с корректным знаком.
    """
    if b == 0:
        raise ValueError("Деление на ноль недопустимо.")
    remainder_result = a % b
    if remainder_result != 0 and (a < 0) != (b < 0):
        remainder_result -= b
    return remainder_result

# Тесты для функции remainder
class TestRemainderFunction(unittest.TestCase):
    def test_positive_numbers(self):
        """Проверка работы функции с положительными числами"""
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(20, 4), 0)

    def test_negative_numbers(self):
        """Проверка работы функции с отрицательными числами"""
        self.assertEqual(remainder(-10, 3), -1)
        self.assertEqual(remainder(10, -3), 1)
        self.assertEqual(remainder(-10, -3), -1)

    def test_zero_dividend(self):
        """Проверка случая, когда делимое равно нулю"""
        self.assertEqual(remainder(0, 5), 0)

    def test_division_by_zero(self):
        """Проверка обработки деления на ноль"""
        with self.assertRaises(ValueError):
            remainder(10, 0)

    def test_large_numbers(self):
        """Проверка работы функции с большими числами"""
        self.assertEqual(remainder(1000000001, 1000000000), 1)

if __name__ == "__main__":
    unittest.main()