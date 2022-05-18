
import matplotlib.pyplot as plt

from Figure import MyFunction
from analys_cycles import check_cycles
from export_to_matlab import export_two_arr


def check_9(func, x0, b):
    x00 = x0

    a0_b_vals = []
    res_b_9, res_x0_9 = [], []
    for _ in range(16):
        x11 = func.f_with_param(x00)
        if x11 is None:
            break

        a0_b_vals.append(x11)
        x00 = x11

    cycle_type = check_cycles(a0_b_vals)
    if cycle_type == 9:
        res_b_9.append(b)
        res_x0_9.append(x0)

    return res_b_9, res_x0_9


def bifurcation_b(func: MyFunction, x0, b_max, b, T1=200, T2=200):
    res_b, res_x0 = [], []
    res_b_9, res_x0_9 = [], []

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

        # b_9, x0_9 = check_9(func, x0, b)
        # res_b_9 += b_9
        # res_x0_9 += x0_9

        x0 = x_start
        b += 0.001
        func.set_b(b)

    # export_bif(res_b_9, res_x0_9, "b_9",  folder="bif")
    return res_b, res_x0


def bifurcation_a(func: MyFunction, x0, a0_max, a0, T1=200, T2=200):
    res_a0, res_x0 = [], []
    res_a_9, res_x0_9 = [], []

    while a0 < a0_max:
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
            res_a0.append(a0)

        # a_9, x0_9 = check_9(func, x0)
        # res_a_9 += b_9
        # res_x0_9 += x0_9

        x0 = x_start
        a0 += 0.001
        func.set_a0(a0)
    # export_bif(res_a_9, res_x0_9, "a_9",  folder="bif")

    return res_a0, res_x0


# для а0
# a0_min = 1.4
# a0_max = 4
# b = 2.9
#
# x0 = 0.3
# label_param = "a"

# для b
b_min = 1.74
b_max = 3
a0 = 3.35
x0 = 0.3
label_param = "b"



"""for a"""
# myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0_min, b=b)
# res_b, res_x0 = bifurcation_a(func=myf, x0=x0, a0_max=a0_max, a0=a0_min)

"""for b"""
myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=b_min)
res_b, res_x0 = bifurcation_b(func=myf, x0=x0, b_max=b_max, b=b_min)

plt.scatter(res_b, res_x0, label=f"x0={x0}", color='green', linewidths=0.01, marker=".")
export_two_arr(res_b, res_x0, file_name=f"bif_by_{label_param}_{x0}", folder="bif")


x0 = 0.7
"""for a"""
# myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0_min, b=b)
# res_b, res_x0 = bifurcation_a(func=myf, x0=x0, a0_max=a0_max, a0=a0_min)

"""for b"""
myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=b_min)
res_b, res_x0 = bifurcation_b(func=myf, x0=x0, b_max=b_max, b=b_min)

plt.scatter(res_b, res_x0, label=f'x0={x0}', color='red', linewidths=0.01, marker=".")
export_two_arr(res_b, res_x0, file_name=f"bif_by_{label_param}_{x0}", folder="bif")


plt.legend()
plt.grid(True)
plt.xlim([b_min, b_max])
plt.ylim([0, 1])
plt.xlabel(label_param)
plt.ylabel('p')
plt.show()
