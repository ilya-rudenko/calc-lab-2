from utils import draw_function_graph, ask, print_error, draw_system_graph
import numpy as np


def horde_method(func):
    draw_function_graph(func)

    left = ask("Введите левую границу корня:", is_numeric=True)
    right = ask("Введите правую границу корня:", is_numeric=True)

    while func.calculate(left) * func.calculate(right) > 0:
        print_error("Ошибка. Значения функции в точках должны быть разных знаков")
        left = ask("Введите левую границу корня:", is_numeric=True)
        right = ask("Введите правую границу корня:", is_numeric=True)

    accuracy = ask("Введите точность корня:", is_numeric=True, is_positive=True)

    iter_count = 0
    x = left
    while abs(func.calculate(x)) > accuracy:
        x = x - (right - x) * func.calculate(x) / (func.calculate(right) - func.calculate(x))
        iter_count += 1

    print(
        f"Найденный корень: {round(x, len(str(accuracy)))}.\nЗначение функции в корне: {round(func.calculate(x), len(str(accuracy)))}\nКоличество итераций: {iter_count}")


def newton_method(func):
    draw_function_graph(func)

    left = ask("Введите левую границу корня:", is_numeric=True)
    right = ask("Введите правую границу корня:", is_numeric=True)

    while func.calculate(left) * func.calculate(right) > 0:
        print_error("Ошибка. Значения функции в точках должны быть разных знаков")
        left = ask("Введите левую границу корня:", is_numeric=True)
        right = ask("Введите правую границу корня:", is_numeric=True)

    accuracy = ask("Введите точность корня:", is_numeric=True, is_positive=True)

    iter_count = 0
    x = (left + right) / 2

    while abs(func.calculate(x)) > accuracy:
        x = x - func.calculate(x) / func.d1(x)
        iter_count += 1

    print(
        f"Найденный корень: {round(x, len(str(accuracy)))}.\nЗначение функции в корне: {round(func.calculate(x), len(str(accuracy)))}\nКоличество итераций: {iter_count}")


def simple_iterations(func):
    draw_function_graph(func)

    left = ask("Введите левую границу корня:", is_numeric=True)
    right = ask("Введите правую границу корня:", is_numeric=True)

    flag_convergence = check_simple_convergence(func, left, right) is None

    while flag_convergence:

        if flag_convergence:
            print_error("Ошибка. На промежутке нет значения, удовлетворяющего сходимости функции")

        left = ask("Введите левую границу корня:", is_numeric=True)
        right = ask("Введите правую границу корня:", is_numeric=True)

        flag_convergence = check_simple_convergence(func, left, right) is None

    accuracy = ask("Введите точность корня:", is_numeric=True, is_positive=True)

    func.fi = lambda x: x - func.calculate(x) / get_max(func, left, right)

    iter_count = 0
    x = check_simple_convergence(func, left, right)
    x_next = func.fi(x)

    while abs(x_next - x) > accuracy:

        if abs(x) > 1e+10 or iter_count > 100:
            print("Не сходится :(")
            return

        x = x_next
        x_next = func.fi(x)
        iter_count += 1

    print(
        f"Найденный корень: {round(x, len(str(accuracy)))}.\nЗначение функции в корне: {round(func.calculate(x), len(str(accuracy)))}\nКоличество итераций: {iter_count}")


def check_simple_convergence(func, left, right):
    x = np.linspace(left, right, 100)

    for i in x:
        if abs(func.dfi(i)) < 1:
            return i
    return None


def get_max(func, left, right):
    x = np.linspace(left, right, 100)

    max = 0.01

    for i in x:
        if abs(func.d1(i)) > max:
            max = abs(func.d1(i))

    return max


def system_simple_iterations(system, x=None, y=None, accuracy=None, test_mode=False):

    if not test_mode:
        draw_system_graph(system)
        x = ask("Введите начальное приближение X:", is_numeric=True)
        y = ask("Введите начальное приближение Y:", is_numeric=True)

        accuracy = ask("Введите точность корня:", is_numeric=True, is_positive=True)

    iter_count = 0

    max_iter = 1000
    max_val = 1e+10

    while abs(system.array_of_equations[0].calculate(x, y)) > accuracy:
        x = system.array_of_equations[0].fi(x, y)
        y = system.array_of_equations[1].fi(x, y)

        iter_count += 1

        if iter_count > max_iter or x > max_val or y > max_val:
            if not test_mode:
                print("Не сходится :(")
            return False

    if not test_mode:
        print(
            f"Найденный корень: (x = {round(x, len(str(accuracy)))} , y = {round(y, len(str(accuracy)))}) .\nЗначение "
            f"функции в корне: {round(system.array_of_equations[0].calculate(x, y), len(str(accuracy)))}\nКоличество "
            f"итераций: {iter_count}")
    return True


