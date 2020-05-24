import math
import numpy as np
import sympy


def method_of_rectangles(expression, a, b, n):
    """
        :param expression: Функция для вычисления под знаком интеграла
        :param a: Верхняя граница интеграла
        :param b: Нижняя граница интеграла
        :param n: Количество отрезков
        :return: Приблеженное значение интеграла
    """
    h = (a - b) / n
    sum = 0
    try:
        while b <= a:
            x = b
            sum += eval(expression) * h
            b += h
    except Exception as e:
        sum = 'Вычислить невозможно'
    return sum


def method_of_trapezes(expression, a, b, n):
    """
        :param expression: Функция для вычисления под знаком интеграла
        :param a: Верхняя граница интеграла
        :param b: Нижняя граница интеграла
        :param n: Количество отрезков
        :return: Приблеженное значение интеграла
    """
    h = (a - b) / n
    try:
        sum = 0
        x = b
        sum += eval(expression) / 2
        b += h
        x = a
        sum += eval(expression) / 2
        a -= h
        while b <= a:
            x = b
            sum += eval(expression)
            b += h
        return sum * h
    except Exception as e:
        return 'Вычислить невозможно'


def method_of_simpson(expression, a, b, n):
    """
        :param expression: Функция для вычисления под знаком интеграла
        :param a: Верхняя граница интеграла
        :param b: Нижняя граница интеграла
        :param n: Количество отрезков
        :return: Приблеженное значение интеграла
    """
    N = 2 * n
    h = (a - b) / N
    list_of_x = np.arange(b, a + h, h)
    try:
        sum = 0
        for k in range(1, N, 2):
            x = list_of_x[k-1]
            sum += eval(expression)
            x = list_of_x[k]
            sum += eval(expression) * 4
            x = list_of_x[k + 1]
            sum += eval(expression)
        return sum * h / 3
    except Exception as e:
        return 'Вычислить невозможно'


def diff(x, y, need_to_calc=[2.5]):
    """
    :param x: Массив х
    :param y: Массив У
    :param need_to_calc: Массив значений, которые нужно вычислить
    :return:
    """
    try:
        newX = x.copy()
        newY = y.copy()
        if len(newX) == len(newY):
            polynoms = []
            values = []
            L = ''
            for i in range(len(newX)):
                li = ''
                for j in range(len(newX)):
                    if i != j:
                        li += '(x - {}) / ({} - {}) * ' \
                            .format(newX[j], newX[i], newX[j])
                li = li[0:len(li) - 3]
                polynoms.append(li)
            for i in range(len(newY)):
                L += '{} * {} + '.format(newY[i], polynoms[i])
            L = L[0:len(L) - 3]
            diff_arr = []
            expr = sympy.diff(L)
            for value in need_to_calc:
                diff_arr.append(expr.evalf(subs={'x': value}))
            return diff_arr
    except Exception as e:
        return e

if __name__ == '__main__':
    integral = 'math.sqrt(x+4)'
    print('Интеграл {} методом прямоугольников {}'
          .format(integral, method_of_rectangles(integral, 6, 2, 6)))
    print('Интеграл {} методом трапеций {}'
          .format(integral, method_of_trapezes(integral, 6, 2, 6)))
    print('Интеграл {} методом Симпсона {}'
          .format('math.cos(x*x)', method_of_simpson('math.cos(x*x)', 3, 1, 6)))
    print('Диффериенциал в точках {} = {}'
          .format(3.8, diff([2, 3, 4], [-4, 1, 6])))