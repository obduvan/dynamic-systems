from collections import defaultdict
from Figure import MyFunction


def check_cycles(list: list) -> int:
    for i in range(1, 16):
        if is_cycle(list, i):
            return i
    return -1


def is_cycle(list: list, cycle_type: int) -> bool:
    if cycle_type < len(list):
        return abs(list[0] - list[cycle_type]) < 0.000001
    return False


def f4(b):
    return b * 1.16583 + 0.078616


def f5(b):
    return b * (117 / 101) - (4691 / 101000)


def f13_down(b):
    return b * 1.15625 - 0.16271875


def f13_up(b):
    return b * (21 / 17) - 517 / 3400


def f9_up(b):
    return b * (435 / 374) + 3167 / 374000


def f9_up_1(b):
    return b * (35479 / 29300) + 3409031 / 29300000


def find_cycles(my_func, a0, b, x0, points):
    for _ in range(iterations):
        x1 = my_func.f_with_param(x0)
        if x1 is None:
            print(x1, a0, b)
            break
        x0 = x1
    x_iter = x0

    a0_b_vals = []
    for _ in range(15 + 1):
        x1 = my_func.f_with_param(x0)

        if x1 is None:
            print(x1, a0, b)
            break

        a0_b_vals.append(x1)
        x0 = x1

    cycle_type = check_cycles(a0_b_vals)
    if cycle_type != -1:
        points[cycle_type].append([a0, b])

    return x0, x_iter


def iter_a0(my_func, b, x_start, points, func_xy):
    a0 = func_xy(b)  # идем по функции
    a0_start = a0
    my_func.set_b(b)
    x0 = x_start

    x_iter_next = x0

    flag = True

    while a0 < 4:
        my_func.set_a0(a0)
        x0, x_iter = find_cycles(my_func, a0, b, x0, points)
        if flag:
            x_iter_next = x_iter
        flag = False
        a0 += 0.001

    a0 = a0_start
    x0 = x_start
    while a0 > 3:
        my_func.set_a0(a0)
        x0, trash = find_cycles(my_func, a0, b, x0, points)
        a0 -= 0.001

    return x_iter_next


def regime_map(my_func, b_start, x_start, func_xy):
    points: dict[int:list] = defaultdict(lambda: [])
    b = b_start
    flag = True
    x_iter_new = x_start
    while b < 3:
        x_iter = iter_a0(my_func=my_func, b=b, x_start=x_iter_new, points=points, func_xy=func_xy)
        b += 0.001
        x_iter_new = x_iter

    b = b_start
    x_iter_new = x_start
    while b > 2.4:
        x_iter1 = iter_a0(my_func=my_func, b=b, x_start=x_iter_new, points=points, func_xy=func_xy)
        x_iter_new = x_iter1
        b -= 0.001

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


# f4
# b_start = 2.55
# func_xy = f4

# f5
# b_start = 2.701
# func_xy = f5

# f13_down
# b_start = 2.801
# func_xy = f13_down

# f13_up

# b_start = 2.593
# func_xy = f13_up

# f9_up
b_start = 2.7
func_xy = f9_up

myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=func_xy(b_start), b=b_start)
p0 = 0.4
iterations = 200

regime_map(myf, b_start, x_start=p0, func_xy=func_xy)
