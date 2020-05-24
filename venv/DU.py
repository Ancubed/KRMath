import numpy as np
import matplotlib.pylab as plt


def eulers_method(equation, y0, a, b, h):
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
        y = y0
        f0 = eval(equation)
        hf0 = f0 * h
        xlist = list(np.arange(a, b+h, h))
        ylist = [y0]
        for i in range(1, len(xlist), 1):
            x = xlist[i - 1]
            y = ylist[i - 1]
            ylist.append(ylist[i - 1] + h * eval(equation))
        return xlist, ylist
    except Exception:
        return None, None


def runge_kutta_method(equation, y0, a, b, h):
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
        y = y0
        f0 = eval(equation)
        hf0 = f0 * h
        xlist = list(np.arange(a, b + h, h))
        ylist = [y0]
        for i in range(1, len(xlist), 1):
            x = xlist[i - 1]
            y = ylist[i - 1]
            k1 = eval(equation)
            x = xlist[i - 1] + h / 2
            y = ylist[i - 1] + h * k1 / 2
            k2 = eval(equation)
            x = xlist[i - 1] + h / 2
            y = ylist[i - 1] + h * k2 / 2
            k3 = eval(equation)
            x = xlist[i - 1] + h
            y = ylist[i - 1] + h * k3
            k4 = eval(equation)
            ylist.append(ylist[i - 1] + h / 6 * (k1 + k2 + k3 + k4))
        return xlist, ylist
    except Exception:
        return None, None


if __name__ == '__main__':
    xlist, ylist = eulers_method('x+2*y', 1, 0, 1, 0.1)
    plt.gcf().canvas.set_window_title('Решения уравнения x+2*y')
    print('По Эйлеру', xlist, ylist, sep='\n')
    plt.figure(1)
    plt.plot(xlist, ylist, label = 'Решение по Эйлеру')
    plt.legend()
    plt.grid(True)
    xlist, ylist = runge_kutta_method('x+2*y', 1, 0, 1, 0.1)
    print('По Рунге-Кутта', xlist, ylist, sep='\n')
    plt.figure(1)
    plt.plot(xlist, ylist, label = 'Решение по Рунге-Кутта')
    plt.legend()
    plt.grid(True)
    plt.show()

