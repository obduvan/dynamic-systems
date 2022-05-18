from matplotlib import pyplot as plt

from Figure import MyFunction
from export_to_matlab import export_two_arr


def c1(func: MyFunction):
    return func.v - func.ga


def c2(func: MyFunction):
    return func.v - func.el


def c3(f: MyFunction):
    return f.v + f.el


def c4(f: MyFunction):
    return f.v + f.ga


def left_central(f: MyFunction):
    return f.v - f.el + 0.00001


def right_central(f: MyFunction):
    return f.v + f.el - 0.00001


def find_c(func: MyFunction, b, b_max, func_c, label):
    res_b_c, res_p_c = [], []
    res_b_fc, res_p_fc = [], []

    while b < b_max:
        f_c = func_c(func)
        f_c1 = func.f_with_param(f_c)
        res_p_c.append(f_c1)
        res_b_c.append(b)

        p = func.f_with_param(f_c1)
        res_p_fc.append(p)
        res_b_fc.append(b)

        b += 0.001
        func.set_b(b)

    export_two_arr(res_b_c, res_p_c, f"{label}", folder="c_function")
    export_two_arr(res_b_fc, res_p_fc, f"f({label})", folder="c_function")
    plt.scatter(res_b_c, res_p_c, label=f"{label}", color='green', linewidths=0.01, marker=".")
    plt.scatter(res_b_fc, res_p_fc, label=f"f({label})", color='green', linewidths=0.01, marker=".")


b = 1.74
b_max = 3
a0 = 3.35
label_param = "b"

myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=b)


find_c(func_c=right_central, b=b, b_max=b_max, func=myf, label="right_central")

plt.legend()
plt.grid(True)
plt.xlim([b, b_max])
plt.ylim([0, 1])
plt.xlabel(label_param)
plt.ylabel('p')
plt.show()
