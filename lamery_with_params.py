import numpy as np
from matplotlib import pyplot as plt

from Figure import MyFunction


def draw_lamerey(func: MyFunction, x0):
    res_x, res_y = [], []
    f = True
    if f:
        for _ in range(100):
            x1 = func.f_with_param(x0)
            if x1 is None:
                print(f"Параметр {x0} вышел за область функции.a0={func.a0}, b={func.b}")
                break
            x0 = x1

    for _ in range(1, 100):
        x1 = func.f_with_param(x0)
        if x1 is None:
            print(f"Параметр {x0} вышел за область функции.a0={func.a0}, b={func.b}")
            break
        res_x += [x0, x0, x0, x1]
        res_y += [x0, x1, x1, x1]
        x0 = x1

    plt.plot(res_x, res_y, color='green', label="lamerey")
    plt.title(f"a0={func.a0}")
    func.draw_xy()

    # plt.show()


def lamerey_with_params():
    a = 4
    v = 0.5
    el = 0.1
    ga = 0.2
    b = 2.95
    a0_start = 3

    step_a0 = 0.1
    x0 = 0.3

    a0_range = np.arange(a0_start, 4 + step_a0 / 10, step_a0)
    for a0 in a0_range:
        myf = MyFunction(a=a, v=v, ga=ga, el=el, a0=a0, b=b)
        draw_lamerey(myf, x0=x0)
        myf.draw_function(show=True)


lamerey_with_params()
