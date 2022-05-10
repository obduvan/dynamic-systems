from Figure import MyFunction
from export_to_matlab import export_bif


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


        # x0 = x_start
        a0 += 0.0001
        func.set_a0(a0)
    export_bif(res_a_9, res_x0_9, "a_9", folder="bif")

    return res_a0, res_x0

a0_min = 1.4
a0_max = 4
b = 2.9

x0 = 0.3
label_param = "a"