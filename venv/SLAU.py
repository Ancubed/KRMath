import copy
import math


def diagonal_prevalence(matrix):
    for k in range(len(matrix), -1, -1):
        for i in range(len(matrix)):
            row_max = 0
            for j in range(len(matrix[i]) - 1):
                if math.fabs(row_max) <= math.fabs(matrix[i][j]):
                    row_max = matrix[i][j]
            row_index_max = matrix[i].index(row_max)
            tmp = matrix[row_index_max]
            matrix[row_index_max] = matrix[i]
            matrix[i] = tmp
    #print("МАТРИЦА ИЗМЕНЕННАЯ", matrix, sep="\n")


def gaussian_method(extended_matrix):
    a = copy.deepcopy(extended_matrix)
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


def iteration_method(extended_matrix, precision=0.0001):
    try:
        A = copy.deepcopy(extended_matrix)
        n = len(A)
        B = [A[i].pop() for i in range(n)]
        res = []
        for i in range(len(B)):
            res.append(B[i] / A[i][i])
        Xn = copy.deepcopy(res)
        while True:
            for i in range(n):
                Xn[i] = B[i] / A[i][i]
                for j in range(n):
                    if i == j:
                        continue
                    else:
                        Xn[i] -= A[i][j] / A[i][i] * res[j]
            flag = True
            for i in range(n):
                if math.fabs(Xn[i] - res[i]) > precision:
                    flag = False
                    break
            for i in range(n):
                res[i] = Xn[i]
            if flag:
                break
        return res
    except Exception:
        return "Ошибка выполнения метода. Скорее всего, не возможно выполнить условие главной диагонали."


def seidels_method(extended_matrix, precision=0.0001):
    try:
        A = copy.deepcopy(ext_matrix)
        n = len(A)
        B = [A[i].pop() for i in range(n)]
        x = [.0 for i in range(n)]
        converge = False
        while not converge:
            x_new = copy.deepcopy(x)
            for i in range(n):
                s1 = sum(A[i][j] * x_new[j] for j in range(i))
                s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
                x_new[i] = (B[i] - s1 - s2) / A[i][i]
            converge = math.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= precision
            x = x_new
        return x
    except Exception:
        return "Ошибка выполнения метода. Скорее всего, не возможно выполнить условие главной диагонали."


if __name__ == '__main__':
    variable = ['x1', 'x2', 'x3', 'b']
    ext_matrix = [[7.6, 0.5, 2.4, 1.9],
                  [2.2, 9.1, 4.4, 9.7], # 3 var DONE
                  [-1.3, 0.2, 5.8, -1.4]]
    # ext_matrix = [[1, 1, 2, -1],
    #               [2, -1, 2, -4], # 1 var NOT ITERATION
    #               [4, 1, 4, -2]]
    # ext_matrix = [[1.14, -2.15, -5.11, 2.05],
    #               [-0.71, 0.81, -0.02, -1.07],  # 8 var NOT
    #               [0.42, -1.13, 7.05, 0.8]]
    # ext_matrix = [[2, -1, -1, 1],
    #               [3, -4, 1, 2],  # 12 var DONE
    #               [1, -1, -1, 3]]
    # ext_matrix = [[11, 3, -1, 15],
    #               [2, 5, -5, -11],  # 7 var DONE
    #               [1, 1, 4, 1]]
    # ext_matrix = [[0.3, 1.2, -0.2, -0.6], # 20 var  DONE
    #               [-0.1, -0.2, 1.6, 0.3],
    #               [-0.05, 0.34, 0.1, 0.32]]
    # ext_matrix = [[3, 1, -1, 2], # 16 var  DONE
    #               [1, 4, -2, 3],
    #               [2, -1, 5, 15]]
    # ext_matrix = [[0.63, -0.37, 1.76, -9], # 17 var  DONE
    #               [0.9, 1, 0.05, 0.12],
    #               [0.13, -0.95, 0.69, 0.7]]
    # ext_matrix = [[6.4, 11.75, 10, -41.4],  # 18 var  NOT
    #               [7.42, 19, 11.8, -49.7],
    #               [5.8, 7.5, 6.4, -27.7]]
    # ext_matrix = [[2, 2, 10, 14],
    #               [10, 1, 1, 12],
    #               [2, 10, 1, 13]]
    # for k in range(3):
    #     print("Введите коэффициенты " + str(k+1) + " уравнения: ")
    #     matrix_row = []
    #     for x_name in variable:
    #         x = float(input("При {}: ".format(x_name)))
    #         matrix_row.append(x)
    #     extended_matrix.append(matrix_row)
    print("Расширенная матрица системы: ", ext_matrix, sep="\n")
    print("Решение методом Гаусса: ", gaussian_method(ext_matrix), sep='\n')
    diagonal_prevalence(ext_matrix)
    # precision = float(input("Введите точность для выполнения метода итераций и Зейделя: "))
    print("Решение методом Итераций: ", iteration_method(ext_matrix), sep='\n')
    print("Решение методом Зейделя: ", seidels_method(ext_matrix), sep='\n')