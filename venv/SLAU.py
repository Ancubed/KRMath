from copy import deepcopy
from math import fabs, sqrt
from datetime import datetime


class SystemsOfLinearAlgebraicEquations:
    def __init__(self, matrix, precision):
        self.ext_matrix = matrix
        self.precision = precision

    def diagonal_prevalence(self):
        for k in range(len(self.ext_matrix), -1, -1):
            for i in range(len(self.ext_matrix)):
                row_max = 0
                for j in range(len(self.ext_matrix[i]) - 1):
                    if fabs(row_max) <= fabs(self.ext_matrix[i][j]):
                        row_max = self.ext_matrix[i][j]
                row_index_max = self.ext_matrix[i].index(row_max)
                tmp = self.ext_matrix[row_index_max]
                self.ext_matrix[row_index_max] = self.ext_matrix[i]
                self.ext_matrix[i] = tmp

    def gaussian_method(self):
        a = deepcopy(self.ext_matrix)
        n = len(a)
        x = [0 for i in range(n)]
        for k in range(1, n):
            for j in range(k, n):
                m = a[j][k - 1] / a[k - 1][k - 1]
                for i in range(0, n + 1):
                    a[j][i] = a[j][i] - m * a[k - 1][i]
        for i in range(n - 1, -1, -1):
            x[i] = a[i][n] / a[i][i]
            for c in range(n - 1, i, -1):
                x[i] = x[i] - a[i][c] * x[c] / a[i][i]
        return x

    def iteration_method(self):
        try:
            A = deepcopy(self.ext_matrix)
            n = len(A)
            B = [A[i].pop() for i in range(n)]
            res = []
            for i in range(len(B)):
                res.append(B[i] / A[i][i])
            Xn = deepcopy(res)
            start = datetime.now()
            while True:
                delta = datetime.now() - start
                if delta.seconds > 3:
                    raise Exception("TimeOut")
                for i in range(n):
                    Xn[i] = B[i] / A[i][i]
                    for j in range(n):
                        if i == j:
                            continue
                        else:
                            Xn[i] -= A[i][j] / A[i][i] * res[j]
                flag = True
                for i in range(n):
                    if fabs(Xn[i] - res[i]) > self.precision:
                        flag = False
                        break
                for i in range(n):
                    res[i] = Xn[i]
                if flag:
                    break
            return res
        except Exception:
            return "Не выполняется условие преобладания главной диагонали."

    def seidels_method(self):
        try:
            A = deepcopy(self.ext_matrix)
            n = len(A)
            B = [A[i].pop() for i in range(n)]
            x = [.0 for i in range(n)]
            converge = False
            while not converge:
                x_new = deepcopy(x)
                for i in range(n):
                    s1 = sum(A[i][j] * x_new[j] for j in range(i))
                    s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
                    x_new[i] = (B[i] - s1 - s2) / A[i][i]
                converge = sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= self.precision
                x = x_new
            return x
        except Exception:
            return "Не выполняется условие преобладания главной диагонали."