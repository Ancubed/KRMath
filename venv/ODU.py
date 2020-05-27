import numpy as np
import matplotlib.pylab as plt


class OrdinaryDifferentialEquation:
    def __init__(self, equation, y0, a, b, h):
        self.equation = equation
        self.y0 = y0
        self.a = a
        self.b = b
        self.h = h
        self.xlist = list(np.arange(self.a, self.b + self.h, self.h))

    def eulers_method(self):
        """
        :param equation: Уравнение в виде y' = f(x, y)
        :param y0: y(0)
        :param a: Левая граница интервала
        :param b: Правая граница интервала
        :param h: Шаг
        :return: Решение уравнения: xlist, ylist
        """
        try:
            x = 0
            y = self.y0
            f0 = eval(self.equation)
            hf0 = f0 * self.h
            ylist = [self.y0]
            for i in range(1, len(self.xlist), 1):
                x = self.xlist[i - 1]
                y = ylist[i - 1]
                ylist.append(ylist[i - 1] + self.h * eval(self.equation))
            return ylist
        except Exception:
            return None

    def runge_kutta_method(self):
        """
        :param equation: Уравнение в виде y' = f(x, y)
        :param y0: y(0)
        :param a: Левая граница интервала
        :param b: Правая граница интервала
        :param h: Шаг
        :return: Решение уравнения: xlist, ylist
        """
        try:
            x = 0
            y = self.y0
            f0 = eval(self.equation)
            hf0 = f0 * self.h
            ylist = [self.y0]
            for i in range(1, len(self.xlist), 1):
                x = self.xlist[i - 1]
                y = ylist[i - 1]
                k1 = eval(self.equation)
                x = self.xlist[i - 1] + self.h / 2
                y = ylist[i - 1] + self.h * k1 / 2
                k2 = eval(self.equation)
                x = self.xlist[i - 1] + self.h / 2
                y = ylist[i - 1] + self.h * k2 / 2
                k3 = eval(self.equation)
                x = self.xlist[i - 1] + self.h
                y = ylist[i - 1] + self.h * k3
                k4 = eval(self.equation)
                ylist.append(ylist[i - 1] + self.h / 6 * (k1 + k2 + k3 + k4))
            return ylist
        except Exception:
            return None

    def calc(self):
        answer = []
        ylist1 = self.eulers_method()
        answer.append(self.xlist)
        answer.append(ylist1)
        # plt.gcf().canvas.set_window_title('Решения уравнения {}'.format(self.equation))
        # plt.figure(1)
        # plt.plot(xlist, ylist, label='Решение по Эйлеру')
        # plt.legend()
        # plt.grid(True)
        ylist2 = self.runge_kutta_method()
        answer.append(ylist2)
        # plt.figure(1)
        # plt.plot(xlist, ylist, label='Решение по Рунге-Кутта')
        # plt.legend()
        # plt.grid(True)
        # plt.show()
        return answer

# if __name__ == '__main__':
#     odu = OrdinaryDifferentialEquation('x+y*2', 1, 0, 1, 0.1)
#     odu.calc()
