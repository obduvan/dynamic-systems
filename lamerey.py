from matplotlib import pyplot as plt

from Figure import MyFunction


def draw_lamerey(func: MyFunction, x0, show=False, label=""):
    res_x, res_y = [], []
    f = True
    if f:
        for _ in range(100):
            x1 = func.f_with_param(x0)
            if x1 is None:
                print(f"Параметр {x0} вышел за область функции.a0={func.a0}, b={func.b}")
                break
            x0 = x1

    for _ in range(1, 51):
        x1 = func.f_with_param(x0)
        if x1 is None:
            print(f"Параметр {x0} вышел за область функции.a0={func.a0}, b={func.b}")
            break

        res_x += [x0, x0, x0, x1]
        res_y += [x0, x1, x1, x1]
        x0 = x1

    plt.plot(res_x, res_y, color='green')

    func.draw_function(title=label)
    func.draw_xy()
    if show:
        plt.show()


"""Построение с конкретными параметрами: """

myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=3.35, b=2.8)
# myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=1.4, b=2.9)
draw_lamerey(myf, show=True, x0=0.3)
myf.draw_function()

# x0=0.25
# x0=0.2
