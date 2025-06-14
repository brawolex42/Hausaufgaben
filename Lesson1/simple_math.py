import math

class SimpleMath:
    """Класс с простыми математическими операциями."""

    def square(self, x):
        """Возвращает квадрат числа."""
        return x * x

    def cube(self, x):
        """Возвращает куб числа."""
        return x * x * x

    def sqrt(self, x):
        """Возвращает квадратный корень из числа."""
        if x < 0:
            raise ValueError("Нельзя извлечь корень из отрицательного числа.")
        return math.sqrt(x)

    def divide(self, a, b):
        """Делит a на b."""
        if b == 0:
            raise ZeroDivisionError("Деление на ноль недопустимо.")
        return a / b

    def add(self, a, b):
        """Сложение двух чисел."""
        return a + b

    def subtract(self, a, b):
        """Вычитание двух чисел."""
        return a - b

    def multiply(self, a, b):
        """Умножение двух чисел."""
        return a * b
