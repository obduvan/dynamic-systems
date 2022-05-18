
from matplotlib import pyplot as plt
from Figure import MyFunction

def plt_show():
    plt.legend()
    plt.grid(True)
    plt.xlim([b_min, 2.9])
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


def find_9_b(func: MyFunction, x0, b_max,b_min, b_start=2.83, T1=100, T2=100):
    res_b, res_x0 = [], []
    x_first = x0
    b = b_start

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

        for _ in range(T2):
            x1 = func.f_with_param(x0)
            if x1 is None or x1 > 1 or x1 < 0:
                break
            x0 = x1
            res_x0.append(x0)
            res_b.append(b)

        # x0 = x_start
        b += 0.0001
        func.set_b(b)

    x0 = x_first
    b = b_start
    func.set_b(b)
    #
    # plt.scatter(res_b, res_x0, label=f"x0={x0}", color='green', linewidths=0.01, marker=".")
    # plt_show()
    while b > b_min:
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

        # x0 = x_start
        b -= 0.0001
        func.set_b(b)

    plt.scatter(res_b, res_x0, label=f"x0={x_first}", color='black', linewidths=0.01, marker=".")
    plt_show()

    return res_b, res_x0


"""отрезок где пересекается 9 и 4"""
b_min = 2.8
b_start = 2.83

a0 = 3.35
x0 = 0.3
label_param = "b"

"4 only"
# b_max = 2.872
# myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=b_start)
# res_b, res_x = find_9_b(func=myf, x0=x0, b_max=b_max, b_start=2.83, b_min=2.8)
# export_two_arr(res_b, res_x, "4_only", "find_9")

"9"
# x0 = 0.3
# myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=2.874)
# res_b, res_x = find_9_b(func=myf, x0=x0, b_max=2.8758, b_start=2.874, b_min=2.855)
# export_two_arr(res_b, res_x, "9_only", "find_9")

"9_1"
# x0 = 0.72646
# # x_values_9_1 = {0.72646, 0.60023, 0.37712, 0.55161, 0.43673, 0.65066, 0.57757, 0.31529, 0.40489}
# myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=2.874)
# res_b, res_x = find_9_b(func=myf, x0=x0, b_max=2.8758, b_start=2.874, b_min=2.855)
# export_two_arr(res_b, res_x, "9_1_only", "find_9")

"14"
# x0 = 0.3
# myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=2.874)
# res_b, res_x = find_9_b(func=myf, x0=x0, b_max=2.9, b_start=2.889, b_min=2.8769)
# export_two_arr(res_b, res_x, "14_only", "find_9")


# 2.877?

