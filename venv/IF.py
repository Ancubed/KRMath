import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


def lagrange_polynomial(x, y, need_to_calc, var_x = 2.5):
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
                        li += '(x - {}) / ({} - {}) * '\
                            .format(newX[j], newX[i], newX[j])
                li = li[0:len(li) - 3]
                print('Полином l{}({}) = {}'.format(i, newX[i], li))
                polynoms.append(li)
            for i in range(len(newY)):
                L += '{} * {} + '.format(newY[i], polynoms[i])
            L = L[0:len(L)-3]
            print('Многочлен по Лагранжу:', L, sep='\n')
            for value in need_to_calc:
                x = value
                values.append(eval(L))
            x = var_x
            print('Значение F({}) = {}'.format(var_x, eval(L)))
            return np.array(values)
    except Exception as e:
        return None


def cubic_spline(x, y, need_to_calc):
    tck = interpolate.splrep(x, y)
    return interpolate.splev(need_to_calc, tck)


def newton_polynomial(x, y, need_to_calc):
    try:
       newX = x.copy().astype(float)
       newY = y.copy().astype(float)
       n = len(newX)
       a = []
       for i in range(n):
           a.append(newY[i])
       for j in range(1, n):
           for i in range(n-1, j-1, -1):
               a[i] = float(a[i]-a[i-1])/float(newX[i]-newX[i-j])
       #return np.array(a) # return an array of coefficient
       n = len(a) - 1
       temp = a[n]
       for i in range(n - 1, -1, -1):
           temp = temp * (need_to_calc - newX[i]) + a[i]
       return temp
    except Exception as e:
            return None


if __name__ == '__main__':
    x = np.array([2, 3, 4])
    y = np.array([-4, 1, 6])
    cubic_spline_x = np.array([2, 3, 4, 5])
    cubic_spline_y = np.array([4, -1, 4, 3])
    x_axes = list(np.arange(-10, 10, 0.1))
    print('Лагранж'.format(x_axes))
    y_lagrange = lagrange_polynomial(x, y, x_axes)
    y_newton = newton_polynomial(x, y, x_axes)
    y_spline = cubic_spline(cubic_spline_x, cubic_spline_y, x_axes)
    plt.subplot(221)
    plt.plot(x_axes, y_lagrange)
    plt.grid(True)
    plt.title('Лагранж')
    plt.subplot(222)
    plt.plot(x_axes, y_newton)
    plt.grid(True)
    plt.title('Ньютон')
    plt.subplot(223)
    plt.plot(x_axes, y_spline)
    plt.grid(True)
    plt.title('Кубический сплайн')
    #plt.savefig('demo.png', bbox_inches='tight')
    plt.show()



