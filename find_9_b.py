from collections import defaultdict

from matplotlib import pyplot as plt

from Figure import MyFunction
from utils import check_cycles


def plt_show():
    plt.legend()
    plt.grid(True)
    plt.xlim([b_min, b_max])
    plt.ylim([0, 1])
    plt.xlabel(label_param)
    plt.ylabel('p')
    plt.show()



def export_points(points):
    main_path = f"D:\\DEVELOP PROJECTS\\В рамках предмета в универе\\dynamic-systems\\find_9\\"

    cycle_4 = open(f'{main_path}cycle4.txt', 'w')
    cycle_9 = open(f'{main_path}cycle9.txt', 'w')
    cycle_14 = open(f'{main_path}cycle14.txt', 'w')

    for type in points:
        line = ""
        for x, y in zip(points[type][0], points[type][1]):
            line += f"{x} {y}\n"

        if type == 4:
            cycle_4.write(line)
        elif type == 9:
            cycle_9.write(line)
        elif type == 14:
            cycle_14.write(line)

    cycle_4.close()
    cycle_9.close()
    cycle_14.close()


def find_9_b(func: MyFunction, x0, b_max, b, T1=200, T2=200):
    res_b, res_x0 = [], []
    x_first = x0
    points: dict[int: list] = defaultdict(lambda: [[], []])

    while b < b_max:
        x_start = x0

        def foo(x0, func):
            for _ in range(T1):
                x1 = func.f_with_param(x0)
                if x1 is None or x1 > 1 or x1 < 0:
                    break

                x0 = x1
            return x0

        x0 = foo(x0, func)

        res_b, res_x0 = [], []

        for _ in range(T2):
            x1 = func.f_with_param(x0)
            if x1 is None or x1 > 1 or x1 < 0:
                break

            x0 = x1
            res_x0.append(x0)
            res_b.append(b)

        vals = []
        _x0 = x0

        for _ in range(16):
            _x1 = func.f_with_param(_x0)
            if _x1 is None:
                break

            vals.append(_x1)
            _x0 = _x1

        cycle_type = check_cycles(vals)
        if cycle_type != -1:
            points[cycle_type][0] += res_b
            points[cycle_type][1] += res_x0

        # x0 = x_start
        b += 0.001
        func.set_b(b)

    x0 = x_first
    b = 2.88
    func.set_b(b)
    #
    # plt.scatter(res_b, res_x0, label=f"x0={x0}", color='black', linewidths=0.01, marker=".")
    # export_bif(res_b, res_x0, file_name=f"from_right{x0}", folder="find_9")
    # plt_show()

    res_b, res_x0 = [], []

    while b > 2.8:
        x_start = x0

        def foo(x0, func):
            for _ in range(T1):
                x1 = func.f_with_param(x0)
                if x1 is None or x1 > 1 or x1 < 0:
                    break

                x0 = x1
            return x0

        x0 = foo(x0, func)

        for _ in range(T2):
            x1 = func.f_with_param(x0)
            if x1 is None or x1 > 1 or x1 < 0:
                break

            x0 = x1
            res_x0.append(x0)
            res_b.append(b)

        vals = []
        _x0 = x0
        for _ in range(16):
            _x1 = func.f_with_param(_x0)
            if _x1 is None:
                break

            vals.append(_x1)
            _x0 = _x1

        cycle_type = check_cycles(vals)
        if cycle_type != -1:
            points[cycle_type][0] += res_b
            points[cycle_type][1] += res_x0

        # x0 = x_start
        b -= 0.001
        func.set_b(b)

    print(points.keys())

    # return res_b, res_x0

    return points


"""отрезок где пересекается 9 и 4"""
b_min = 2.8
b_max = 2.88
a0 = 3.35
x0 = 0.3
label_param = "b"

myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=b_min)
points = find_9_b(func=myf, x0=x0, b_max=b_max, b=b_min)
export_points(points)
# plt.scatter(res_b, res_x0, label=f"x0={x0}", color='green', linewidths=0.01, marker=".")

# export_bif(res_b, res_x0, file_name=f"from_left{x0}", folder="find_9")

# plt_show()
