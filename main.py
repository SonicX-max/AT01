import unittest


# Функции для базовых операций
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль недопустимо.")
    return a / b


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


# Тесты
class TestMathOperations(unittest.TestCase):

    # Тесты для функции сложения
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-3, 5), 2)
        self.assertEqual(add(0, 0), 0)

    # Тесты для функции вычитания
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-5, -5), 0)
        self.assertEqual(subtract(0, 5), -5)

    # Тесты для функции умножения
    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-3, 5), -15)
        self.assertEqual(multiply(0, 5), 0)

    # Тесты для функции деления
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        with self.assertRaises(ValueError):  # Проверка деления на ноль
            divide(10, 0)

    # Тесты для функции остатка от деления
    def test_remainder(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(-10, 3), -1)  # Остаток со знаком делимого
        self.assertEqual(remainder(10, -3), 1)
        self.assertEqual(remainder(-10, -3), -1)
        with self.assertRaises(ValueError):  # Проверка деления на ноль
            remainder(10, 0)


if __name__ == "__main__":
    unittest.main()