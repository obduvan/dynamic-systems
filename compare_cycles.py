from collections import defaultdict

import numpy as np
from matplotlib import pyplot as plt

from Figure import MyFunction



def compare(x_range, iterations, a0, b, func):
    points: dict[int:list] = defaultdict(lambda: [])
    for x in x_range:
        x0 = x

        for _ in range(iterations):
            x1 = func.f_with_param(x0)
            if x1 is None:
                print(x1, a0, b)
                break
            x0 = x1

        a0_b_vals = []

        for _ in range(16):
            x1 = func.f_with_param(x0)
            if x1 is None:
                print(x1, a0, b)
                break

            a0_b_vals.append(x1)
            x0 = x1

        cycle_type = check_cycles(a0_b_vals)
        if cycle_type != -1:
            vals = set()
            for val in a0_b_vals:
                vals.add(round(val, 5))

            if vals not in points[cycle_type]:
                points[cycle_type].append(vals)


def check_cycles(list: list) -> int:
    for i in range(1, 16):
        if is_cycle(list, i):
            return i
    return -1


def is_cycle(list: list, cycle_type: int) -> bool:
    if cycle_type < len(list):
        return abs(list[0] - list[cycle_type]) < 0.000001
    return False


x_values_9 = {0.68471, 0.59511, 0.44839, 0.27354, 0.39977, 0.62288, 0.56327, 0.34934, 0.42243}
x_values_9_1 = {0.72646, 0.60023, 0.37712, 0.55161, 0.43673, 0.65066, 0.57757, 0.31529, 0.40489}
x_values_4 = {0.26377, 0.40079, 0.73623, 0.59921}
x_values_eq = {0.5}

x_9 = [[], []]
x_9_1 = [[], []]
x_4 = [[], []]
x_eq = [[], []]


def write_file(points: list[list], file):
    line = ""
    for x, y in zip(points[0], points[1]):
        line += f"{x} {y}\n"

    file.write(line)


def load_txt(fync: MyFunction):
    main_path = "D:\\DEVELOP PROJECTS\\В рамках предмета в универе\\dynamic-systems\\compare_cycles\\"
    txt_func = open(f'{main_path}fync.txt', 'w')
    txt_9 = open(f'{main_path}x_9.txt', 'w')
    txt_9_1 = open(f'{main_path}x_9_1.txt', 'w')
    txt_4 = open(f'{main_path}x_4.txt', 'w')
    txt_eq = open(f'{main_path}x_eq.txt', 'w')

    p_vals, f_vals = fync.get_points()
    write_file([p_vals, f_vals], txt_func)

    write_file(x_9, txt_9)
    write_file(x_9_1, txt_9_1)
    write_file(x_4, txt_4)
    write_file(x_eq, txt_eq)

    txt_func.close()
    txt_9.close()
    txt_9_1.close()
    txt_4.close()
    txt_eq.close()


def draw_cycle_types(func: MyFunction, title):
    plt.scatter(x_9[0], x_9[1], label=f"9", color='red', linewidths=0.01, marker=".")
    plt.scatter(x_9_1[0], x_9_1[1], label=f"9_1", color='blue', linewidths=0.01, marker=".")
    plt.scatter(x_4[0], x_4[1], label=f"4", color='green', linewidths=0.01, marker=".")
    plt.scatter(x_eq[0], x_eq[1], label=f"eq", color='black', linewidths=0.01, marker=".")

    func.draw_function(show=True, title=title)
    # plt.legend()
    # plt.grid(True)
    # plt.xlim([0, 1])
    # plt.ylim([0, 1])
    # plt.xlabel('p')
    # plt.ylabel('f(p)')
    # plt.show()


def compare_cycles(x_range, iterations, a0, b, func):
    for x in x_range:
        x0 = x
        x_start = x

        for _ in range(iterations):
            x1 = func.f_with_param(x0)
            if x1 is None:
                print(x1, a0, b)
                break
            x0 = x1
        x0 = round(x0, 5)
        s = x_start
        if x0 in x_values_9:
            x_9[0].append(x_start)
            x_9[1].append(x_start)

        elif x0 in x_values_9_1:
            x_9_1[0].append(x_start)
            x_9_1[1].append(x_start)

        elif x0 in x_values_4:
            x_4[0].append(x_start)
            x_4[1].append(x_start)

        elif x0 in x_values_eq:
            x_eq[0].append(x_start)
            x_eq[1].append(x_start)
        else:
            print(x0, "  ??")


step = 0.0001
a0 = 3.3811
b = 2.896
iterations = 100
x_range = np.arange(0, 1 + step, step)
myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=b)

compare_cycles(x_range, iterations, a0=a0, b=b, func=myf)
draw_cycle_types(myf, f"a0={a0}  b={b}, step={step}")
load_txt(myf)
