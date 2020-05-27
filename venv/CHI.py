from math import *
from numpy import arange


class NumericalIntegration:
    def __init__(self, expression, a, b, n):
        self.expression = expression
        self.a = a
        self.b = b
        self.n = n

    def method_of_rectangles(self):
        """
            :param expression: Функция для вычисления под знаком интеграла
            :param a: Верхняя граница интеграла
            :param b: Нижняя граница интеграла
            :param n: Количество отрезков
            :return: Приблеженное значение интеграла
        """
        a = self.a
        b = self.b
        n = self.n
        h = (a - b) / n
        sum = 0
        try:
            while a <= b:
                x = b
                sum += eval(self.expression) * h
                b += h
        except Exception:
            sum = 'Вычислить невозможно'
        return sum

    def method_of_trapezes(self):
        """
            :param expression: Функция для вычисления под знаком интеграла
            :param a: Верхняя граница интеграла
            :param b: Нижняя граница интеграла
            :param n: Количество отрезков
            :return: Приблеженное значение интеграла
        """
        a = self.a
        b = self.b
        n = self.n
        h = (a - b) / n
        try:
            sum = 0
            x = b
            sum += eval(self.expression) / 2
            b += h
            x = a
            sum += eval(self.expression) / 2
            a -= h
            while a <= b:
                x = b
                sum += eval(self.expression)
                b += h
            return sum * h
        except Exception:
            return 'Вычислить невозможно'

    def method_of_simpson(self):
        """
            :param expression: Функция для вычисления под знаком интеграла
            :param a: Верхняя граница интеграла
            :param b: Нижняя граница интеграла
            :param n: Количество отрезков
            :return: Приблеженное значение интеграла
        """
        a = self.a
        b = self.b
        n = self.n
        N = 2 * n
        h = (a - b) / N
        list_of_x = arange(b, a + h, h)
        try:
            sum = 0
            for k in range(1, N, 2):
                x = list_of_x[k-1]
                sum += eval(self.expression)
                x = list_of_x[k]
                sum += eval(self.expression) * 4
                x = list_of_x[k + 1]
                sum += eval(self.expression)
            return sum * h / 3
        except Exception:
            return 'Вычислить невозможно'


# if __name__ == '__main__':
#     integral = 'sqrt(x+4)'
#     chi = NumericalIntegration(integral, 6, 2, 6)
#     print('Интеграл {} методом прямоугольников {}'
#           .format(integral, chi.method_of_rectangles()))
#     print('Интеграл {} методом трапеций {}'
#           .format(integral, chi.method_of_trapezes()))
#     print('Интеграл {} методом Симпсона {}'
#           .format(integral, chi.method_of_simpson()))