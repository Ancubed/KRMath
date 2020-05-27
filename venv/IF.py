import numpy as np
from scipy import interpolate


class InterpolatingFunctions:
    def __init__(self, x, y, need_to_calc):
        self.x_list = np.array(x)
        self.y_list = np.array(y)
        self.need_to_calc = need_to_calc

    def lagrange_polynomial(self):
        try:
            newX = self.x_list.copy()
            newY = self.y_list.copy()
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
                for value in self.need_to_calc:
                    x = value
                    values.append(eval(L))
                return np.array(values)
        except Exception as e:
            return "Ошибка"

    def newton_polynomial(self):
        try:
            newX = self.x_list.copy()
            newY = self.y_list.copy()
            n = len(newX)
            a = []
            for i in range(n):
                a.append(newY[i])
            for j in range(1, n):
                for i in range(n - 1, j - 1, -1):
                    a[i] = float(a[i] - a[i - 1]) / float(newX[i] - newX[i - j])
            # return np.array(a) # return an array of coefficient
            n = len(a) - 1
            temp = a[n]
            for i in range(n - 1, -1, -1):
                temp = temp * (self.need_to_calc - newX[i]) + a[i]
            return temp
        except Exception as e:
            return "Ошибка"

    def cubic_spline(self):
        try:
            newX = self.x_list.copy()
            newY = self.y_list.copy()
            tck = interpolate.splrep(newX, newY)
            return interpolate.splev(self.need_to_calc, tck)
        except Exception as e:
            return "Ошибка"


if __name__ == '__main__':
    x = np.array([2, 3, 4])
    y = np.array([-4, 1, 6])
    if_obj = InterpolatingFunctions([1, 2, 3], [1, 4, 9], [4, 5, 6, 10, 7])
    print(if_obj.newton_polynomial(), if_obj.lagrange_polynomial(), if_obj.cubic_spline(), sep='\n')



