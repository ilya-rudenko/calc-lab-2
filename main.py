import numpy as np

from utils import ask, draw_system_graph
from functions import f_1, f_2, f_3, f_4, s_1, s_2, s_3
from methods import horde_method, newton_method, simple_iterations, system_simple_iterations

test_mode = False

if test_mode:

    x = np.linspace(-5, 5, 1000)
    y = np.linspace(-5, 5, 1000)

    system = s_3

    draw_system_graph(system)

    for i in x:
        for j in y:
            if system_simple_iterations(system, x=i, y=j, accuracy=0.001, test_mode=True):
                print(f"x: {i}, y:{j}")


if ask("Что хотите решать, уравнения или системы?\n    1. Нелинейные уравнения\n    2. Системы нелинейных уравнений",
       answers=["1", "2"]) == "1":

    answ = ask(
        "Выберите уравнение:\n    1. " + f_1.string_view + "\n    2. " + f_2.string_view + "\n    3. " + f_3.string_view + "\n    4. " + f_4.string_view,
        answers=["1", "2", "3", "4"]
    )

    if answ == "1":
        func = f_1
    elif answ == "2":
        func = f_2
    elif answ == "3":
        func = f_3
    else:
        func = f_4

    answ = ask(
        "Выберите метод:\n    1. Метод хорд\n    2. Метод Ньютона\n    3. Метод простых итераций",
        answers=["1", "2", "3"]
    )

    if answ == "1":
        horde_method(func)
    elif answ == "2":
        newton_method(func)
    else:
        simple_iterations(func)

else:
    answ = ask(
        "Выберите систему нелинейных уравнений:\n    1. \n" + s_1.get_string_view() + "\n    2. \n" + s_2.get_string_view() + "\n    3. \n" + s_3.get_string_view(),
        answers=["1", "2", "3"]
    )

    if answ == "1":
        system = s_1
    elif answ == "2":
        system = s_2
    else:
        system = s_3

    system_simple_iterations(system)
