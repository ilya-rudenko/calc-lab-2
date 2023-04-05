import numpy as np
from mpl_toolkits.axisartist.axislines import AxesZero
import matplotlib.pyplot as plt

from sympy import plot_implicit


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def print_error(s):
    print(bcolors.FAIL + s + bcolors.ENDC)


def ask(question, answers=None, is_numeric=False, is_positive=False):
    if answers is None:
        answers = []
    print(question)

    if is_numeric:
        print(">>", end=" ")
        answ = input()

        while (not is_number(answ)) or (is_positive and float(answ) < 0):
            print_error("Ошибка ввода")
            print(">>", end=" ")
            answ = input()

        return float(answ)

    else:
        print(">>", end=" ")
        answ = input()

        while answ not in answers:
            print_error("Ошибка ввода")
            print(">>", end=" ")
            answ = input()

        return answ


def get_function_linspace():
    return np.linspace(0, 8, 100)


def draw_function_graph(func):
    fig = plt.figure()
    ax = fig.add_subplot(axes_class=AxesZero)

    for direction in ["xzero", "yzero"]:
        # adds arrows at the ends of each axis
        ax.axis[direction].set_axisline_style("-|>")

        # adds X and Y-axis from the origin
        ax.axis[direction].set_visible(True)

    for direction in ["left", "right", "bottom", "top"]:
        # hides borders
        ax.axis[direction].set_visible(False)

    x = get_function_linspace()
    ax.plot(x, func.calculate(x))
    ax.set_xlabel(func.string_view[:-3])

    plt.show()


def draw_system_graph(system):
    p1 = plot_implicit(system.sympy_eq[0], aspect_ratio=(1, 1), line_color='g', show=False)

    p2 = plot_implicit(system.sympy_eq[1], aspect_ratio=(1, 1), line_color='r', show=False)

    p1.append(p2[0])

    p1.show()
