from matplotlib import pyplot as plt

from Figure import MyFunction


def bifurcation(func: MyFunction, x0, a0, b, b_max, T1=400, T2=200):
    res_a0, res_x0 = [], []
    while b < b_max:
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
            res_a0.append(b)

        x0 = x_start
        b += 0.001
        func.set_b(b)
    return res_a0, res_x0


# a0_max = 3.25
a0 = 3.5
b = 2.9
myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=b)

"""Построение с двух точек"""
res_a0, res_x0 = bifurcation(func=myf, x0=0.3, a0=a0, b=b, b_max=3)

plt.scatter(res_a0, res_x0, label=f"x0={0.3}", color='green', linewidths=0.01, marker=".")
# res_a0, res_x0 = bifurcation(func=myf, x0=0.7, a0_max=4, a0=0.2, b=b)

# plt.scatter(res_a0, res_x0, label=f'x0={0.7}', color='red', linewidths=0.01, marker=".")

plt.legend()
plt.grid(True)
plt.xlim([0, 3])
plt.ylim([0, 1])
plt.xlabel('b')
plt.ylabel('p')
plt.show()
