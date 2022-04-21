import numpy as np
from collections import defaultdict

from matplotlib import pyplot as plt

from Figure import MyFunction


def incorrect_xi(x1, x0) -> bool:
    if x1 is None:
        # print(f"xi = {x1} вышел за границы")
        # print(f"xi-1 = {x0}")
        return True
    return False


def check_cycles(list: list) -> int:
    for i in range(1, 16):
        if is_cycle(list, i):
            return i
    return -1


def is_cycle(list: list, cycle_type: int) -> bool:
    if cycle_type < len(list):
        return abs(list[0] - list[cycle_type]) < 0.000001
    return False


def regime_map(my_func, a0_range, b_range, iterations, x_start):
    points: dict[int:list] = defaultdict(lambda: [])

    zero_values = ""

    for a0 in a0_range:
        my_func.set_a0(a0)
        flag = False
        for b in b_range:
            x0 = x_start

            my_func.set_b(b)
            for _ in range(iterations):  # итерационный процессы
                x1 = my_func.f_with_param(x0)
                if incorrect_xi(x1, x0):
                    flag = True
                    print(x1, a0, b)
                    break
                x0 = x1
            # if flag:
            #     continue

            a0_b_vals = []
            for _ in range(15 + 1):
                x1 = my_func.f_with_param(x0)
                if incorrect_xi(x1, x0):
                    print(x1, a0, b)
                    break
                a0_b_vals.append (x1)

                x0 = x1

            cycle_type = check_cycles(a0_b_vals)
            if abs(a0 - 3.5) < 0.001 and abs(b - 2.9) < 0.001:
                print(cycle_type, a0, b)
                print(a0_b_vals)
            if cycle_type != -1:
                if a0_b_vals[0] == 0.0:
                    zero_values += f"{b} {a0}\n"
                else:
                    points[cycle_type].append([a0, b])

    equilibrium = open("D:\\eqX2Gt2X1.txt", 'w')
    equilibrium0 = open("D:\\eqX2Lt2X1.txt", 'w')
    cycle_2 = open('D:\\cycle2.txt', 'w')
    cycle_3 = open('D:\\cycle3.txt', 'w')
    cycle_4 = open('D:\\cycle4.txt', 'w')
    cycle_5 = open('D:\\cycle5.txt', 'w')
    cycle_6 = open('D:\\cycle6.txt', 'w')
    cycle_7 = open('D:\\cycle7.txt', 'w')
    cycle_8 = open('D:\\cycle8.txt', 'w')
    cycle_9 = open('D:\\cycle9.txt', 'w')
    cycle_10 = open('D:\\cycle11.txt', 'w')
    cycle_11 = open('D:\\cycle10.txt', 'w')
    cycle_12 = open('D:\\cycle12.txt', 'w')
    cycle_13 = open('D:\\cycle13.txt', 'w')
    cycle_14 = open('D:\\cycle14.txt', 'w')
    cycle_15 = open('D:\\cycle15.txt', 'w')

    equilibrium0.write(zero_values)
    # print(points[4])
    a0_v = []
    b_v = []

    for point in points[4]:
        a0_v.append(point[0])
        b_v.append(point[1])

    plt.scatter(b_v, a0_v, label=f'x0={0.3}', color='red', linewidths=0.01, marker=".")

    plt.legend()
    plt.grid(True)
    plt.xlim([0, 3])
    plt.ylim([0, 4])
    plt.xlabel('b')
    plt.ylabel('a0')
    plt.show()

    for cycle_type in range(1, 16):
        line = ""

        for point in points[cycle_type]:
            a0, b = point[0], point[1]
            line += f"{b} {a0}\n"

        if cycle_type == 1:
            equilibrium.write(line)
        if cycle_type == 2:
            cycle_2.write(line)
        if cycle_type == 3:
            cycle_3.write(line)
        if cycle_type == 4:
            cycle_4.write(line)
        if cycle_type == 5:
            cycle_5.write(line)
        if cycle_type == 6:
            cycle_6.write(line)
        if cycle_type == 7:
            cycle_7.write(line)
        if cycle_type == 8:
            cycle_8.write(line)
        if cycle_type == 9:
            cycle_9.write(line)
        if cycle_type == 10:
            cycle_10.write(line)
        if cycle_type == 11:
            cycle_11.write(line)
        if cycle_type == 12:
            cycle_12.write(line)
        if cycle_type == 13:
            cycle_13.write(line)
        if cycle_type == 14:
            cycle_14.write(line)
        if cycle_type == 15:
            cycle_15.write(line)

    equilibrium.close()
    equilibrium0.close()
    cycle_2.close()
    cycle_3.close()
    cycle_4.close()
    cycle_5.close()
    cycle_6.close()
    cycle_7.close()
    cycle_8.close()
    cycle_9.close()
    cycle_10.close()
    cycle_11.close()
    cycle_12.close()
    cycle_13.close()
    cycle_14.close()
    cycle_15.close()


a0 = 3.4
b = 2.8
myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=b)
step = 0.001
a0_range = np.arange(a0, 4 + step, step)
b_range = np.arange(b, 3 + step, step)

x00 = 0.3
iterations = 100

# x_start = 0.2
# x0 = x_start
# a_range = np.arange(0.01, 2, 0.01)
# b_range = np.arange(0.01, 0.6, 0.01)
# time_range = range(1, 10000 + 1)

regime_map(myf, a0_range, b_range, iterations, x_start=x00)

# a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=b)
# 0 <= p<= 0.3
# 0.3 <= p <= 0.4
# 0.4 <= p <= 0.6
# 0.6 <= p <= 0.7
# 0.7 <= p <= 1
