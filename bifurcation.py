import matplotlib.pyplot as plt

from Figure import MyFunction


def bifurcation(func: MyFunction, x0, a0_max, a0, b, T1=400, T2=200):
    res_a0, res_x0 = [], []
    while a0 < a0_max:
        x_start = x0

        def foo(x0, func):
            for _ in range(T1):
                x1 = func.f_with_param(x0)
                if x1 is None:
                    break
                x0 = x1
            return x0

        x0 = foo(x0, func)

        for _ in range(T2):
            x1 = func.f_with_param(x0)
            if x1 is None:
                break
            x0 = x1
            res_x0.append(x0)
            res_a0.append(a0)

        # x0 = x_start
        a0 += 0.001
        func.set_a0(a0)
    return res_a0, res_x0


# a0_max = 3.25
a0_min = 3
b = 3.25

x0 = 0.3
myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0_min, b=b)

"""Построение с двух точек"""
res_a0, res_x0 = bifurcation(func=myf, x0=x0, a0_max=4, a0=a0_min, b=b)

plt.scatter(res_a0, res_x0, label=f"x0={x0}", color='green', linewidths=0.01, marker=".")
res_a0, res_x0 = bifurcation(func=myf, x0=0.7, a0_max=4, a0=a0_min, b=b)

plt.scatter(res_a0, res_x0, label=f'x0={0.7}', color='red', linewidths=0.01, marker=".")

plt.legend()
plt.grid(True)
plt.xlim([3, 4])
plt.ylim([0, 1])
plt.xlabel('a0')
plt.ylabel('p')
plt.show()
