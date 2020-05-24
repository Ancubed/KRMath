from math import cos, sin, tan, fabs
from matplotlib import pylab
from numpy import linalg, array


class SystemsOfNonlinearEquations:
    def __init__(self, f1, f2, x0, y0, precision, df1x=None,
                 df1y=None, df2x=None, df2y=None):
        self.f1 = f1
        self.f2 = f2
        self.x0 = x0
        self.y0 = y0
        self.precision = precision
        self.df1x = df1x
        self.df1y = df1y
        self.df2x = df2x
        self.df2y = df2y
        if df1x is None or df1y is None or df2x is None or df2y is None:
            self.full_construct_flag = False
        else:
            self.full_construct_flag = True

    def first_method_function_x(self, y, x=0):
        return eval(self.f2)

    def first_method_function_y(self, x, y=0):
        return eval(self.f1)

    def second_method_function_x(self, x, y):
        return eval(self.f2)

    def second_method_dx_x(self, x, y):
        return eval(self.df2x)

    def second_method_dx_y(self, x, y):
        return eval(self.df2y)

    def second_method_function_y(self, x, y):
        return eval(self.f1)

    def second_method_dy_x(self, x, y):
        return eval(self.df1x)

    def second_method_dy_y(self, x, y):
        return eval(self.df1y)

    def method_of_simple_iteration(self, x_start, y_start, precision=0.001):
        x_finish = self.first_method_function_x(y_start)
        y_finish = self.first_method_function_y(x_start)
        while fabs(y_finish - y_start) <= precision and fabs(x_finish - x_start) <= precision:
            y_start = y_finish
            x_start = x_finish
            x_finish = self.first_method_function_x(y_start)
            y_finish = self.first_method_function_y(x_finish)
        return [x_finish, y_finish]

    def newton_method(self, x_start, y_start, precision=0.001):
        x = x_start
        y = y_start
        x_tmp = x+1
        y_tmp = y+1
        while fabs(x - x_tmp) >= precision and fabs(y - y_tmp) >= precision:
            x_tmp = x
            y_tmp = y
            J = array([[self.second_method_dx_x(x, y), self.second_method_dx_y(x, y)],
                            [self.second_method_dy_x(x, y), self.second_method_dy_y(x, y)]])
            A1 = array([[self.second_method_function_x(x, y), self.second_method_dx_y(x, y)],
                              [self.second_method_function_y(x, y), self.second_method_dy_y(x, y)]])
            A2 = array([[self.second_method_dx_x(x, y), self.second_method_function_x(x, y)],
                              [self.second_method_dy_x(x, y), self.second_method_function_y(x, y)]])
            x = x - linalg.det(A1)/linalg.det(J)
            y = y - linalg.det(A2)/linalg.det(J)
        return [x, y]

    def calc(self):
        if not self.full_construct_flag:
            return self.method_of_simple_iteration(self.x0, self.y0, self.precision)
        else:
            return self.newton_method(self.x0, self.y0, self.precision)
