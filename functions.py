import numpy as np
from sympy import Eq, symbols


class Equation:
    def __init__(self, string_view, calculate, d1=None, fi=None, dfi=None):
        self.string_view = string_view
        self.calculate = calculate
        self.d1 = d1
        self.fi = fi
        self.dfi = dfi


class SystemOfEquations:
    def __init__(self, array_of_equations, sympy_eq):
        self.array_of_equations = array_of_equations
        self.sympy_eq = sympy_eq

    def get_string_view(self):
        ret = "—————\n"
        for eq in self.array_of_equations:
            ret += "| " + eq.string_view + "\n"
        return ret + "—————"


f_1 = Equation("0.5x^3 - 6x^2 + 5x + 8 = 0",
               lambda x: 0.5 * x ** 3 - 6 * x ** 2 + 5 * x + 8,
               d1=lambda x: 1.5 * x ** 2 - 12 * x + 5,
               fi=lambda x: 0.5 * x ** 3 - 6 * x ** 2 + 6 * x + 8,
               dfi=lambda x: 1.5 * x ** 2 - 12 * x + 6
               )

f_2 = Equation("-4x^2 + 15x - 7 = 0",
               lambda x: - 4 * x ** 2 + 15 * x - 7,
               d1=lambda x: -8 * x + 15,
               fi=lambda x: - 4 * x ** 2 + 16 * x - 7,
               dfi=lambda x: -8 * x + 16
               )

f_3 = Equation("(x - 3)^2 + sin(x^2) = 0",
               lambda x: (x - 3) * (x - 3) + np.sin(x * x) - 1,
               d1=lambda x: 2 * (x * np.cos(x * x) + x - 3),
               fi=lambda x: (x - 3) ** 2 + np.sin(x * x) + x,
               dfi=lambda x: 2 * (x * np.cos(x * x) + x - 2.5)
               )

f_4 = Equation("sin(x^2) + cos(x) + x - 2 = 0",
               lambda x: np.sin(x ** 2) + np.cos(x) + x - 2,
               d1=lambda x: 2 * x * np.cos(x * x) - np.sin(x) + 1,
               fi=lambda x: np.sin(x ** 2) + np.cos(x) + 2 * x - 2,
               dfi=lambda x: 2 * x * np.cos(x * x) - np.sin(x) + 2
               )

x = symbols('x')
y = symbols('y')

ffs_1_1 = Equation("x^2 + y^2 = 4",
                   lambda x, y: x * x + y * y - 4,
                   fi=lambda x, y: x * x + y * y - 4 + x
                   )
ffs_1_2 = Equation("x^2 - y^2 = 1",
                   lambda x, y: x * x - y * y - 1,
                   fi=lambda x, y: x * x - y * y - 1 + y
                   )

ffs_2_1 = Equation("x^2 + y^2 = 9",
                   lambda x, y: x * x + y * y - 9,
                   fi=lambda x, y:  x * x + y * y - 9 + x,
                   )
ffs_2_2 = Equation("x^3 - y^3 = 1",
                   lambda x, y: x * x * x - y * y * y - 1,
                   fi=lambda x, y: x * x * x - y * y * y - 1 + y,
                   )

ffs_3_1 = Equation("x^3 - y^2 = 2",
                   lambda x, y: x * x * x - y * y - 2,
                   fi=lambda x, y: x * x * x - y * y - 2 + x
                   )
ffs_3_2 = Equation("x^2 + y^3 = 1",
                   lambda x, y: x * x + y * y * y - 1,
                   fi=lambda x, y: x * x + y * y * y - 1 + y
                   )

s_1 = SystemOfEquations([ffs_1_1, ffs_1_2], [Eq(x ** 2 + y ** 2, 4), Eq(x ** 2 - y ** 2, 1)])
s_2 = SystemOfEquations([ffs_2_1, ffs_2_2], [Eq(x ** 2 + y ** 2, 9), Eq(x ** 3 - y ** 3, 1)])
s_3 = SystemOfEquations([ffs_3_1, ffs_3_2], [Eq(x ** 3 - y ** 2, 2), Eq(x ** 2 + y ** 3, 1)])
