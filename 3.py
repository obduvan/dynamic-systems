import random

import matplotlib.pyplot as plt
import numpy as np


class MyFunction:
    def __init__(self, a, b, v, ga, el, a0, al=None, ar=None, bl=None, br=None):
        self.a = a
        self.b = b
        self.v = v
        self.ga = ga
        self.a0 = a0
        self.el = el
        self.al = self.ar = a
        self.bl = self.br = b
        self.step = 0.0001
        self.range_p1 = np.arange(0, self.v - self.ga, self.step)
        self.range_p2 = np.arange(self.v - self.ga, self.v - self.el, self.step)
        self.range_p3 = np.arange(self.v - self.el, self.v + self.el, self.step)
        self.range_p4 = np.arange(self.v + self.el, self.v + self.ga, self.step)
        self.range_p5 = np.arange(self.v + self.ga, 1, self.step)

    def f1(self, p):
        return (1 - self.al + self.bl) * p + (self.a0 * self.ga) + (self.al * self.v) - (self.al * self.ga) - (
                self.bl * self.v)

    def f2(self, p):
        return (1 - self.a0 + self.bl) * p + self.a0 * self.v - self.bl * self.v

    def f3(self, p):
        return (1 - self.a0) * p + self.a0 * self.v

    def f4(self, p):
        return (1 - self.a0 + self.br) * p + self.a0 * self.v - self.br * self.v

    def f5(self, p):
        return (1 - self.ar + self.br) * p - self.a0 * self.ga + self.ar * self.v + self.ar * self.ga - self.br * self.v

    def draw_f1(self, show=False):
        p = self.range_p1
        f = [self.f1(i) for i in p]
        plt.plot(p, f, label="f1", color='red')

        if show:
            self.draw()

    def draw_f2(self, show=False):
        p = self.range_p2
        f = [self.f2(i) for i in p]
        plt.plot(p, f, label="f2", color='blue')

        if show:
            self.draw()

    def draw_f3(self, show=False):
        p = self.range_p3
        f = [self.f3(i) for i in p]
        plt.plot(p, f, label="f3", color='purple')

        if show:
            self.draw()

    def draw_f4(self, show=False):
        p = self.range_p4
        f = [self.f4(i) for i in p]
        plt.plot(p, f, label="f4", color='black')

        if show:
            self.draw()

    def draw_f5(self, show=False):
        p = self.range_p5
        f = [self.f5(i) for i in p]
        plt.plot(p, f, label="f5", color='yellow')

        if show:
            self.draw()

    def draw_function(self, show=False, label=""):
        # plt.figure(figsize=(8,4))
        self.draw_f1()
        self.draw_f2()
        self.draw_f3()
        self.draw_f4()
        self.draw_f5()
        self.draw(show, label)

    def draw_xy(self, show=False):
        plt.plot(np.arange(0, 1, self.step), np.arange(0, 1, self.step), color='grey')
        if show:
            plt.show()

    def f_with_param(self, p):
        # print(self.range_p1[0], self.range_p1[-1], p)
        if self.range_p1[0] <= p <= self.range_p1[-1]:
            return self.f1(p)
        elif self.range_p2[0] <= p <= self.range_p2[-1]:
            return self.f2(p)
        elif self.range_p3[0] <= p <= self.range_p3[-1]:
            return self.f3(p)
        elif self.range_p4[0] <= p <= self.range_p4[-1]:
            return self.f4(p)
        elif self.range_p5[0] <= p <= self.range_p5[-1]:
            return self.f5(p)

    def draw(self, show=False, label=""):
        plt.legend()
        plt.grid(True)
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.title(label)
        plt.xlabel('p')
        plt.ylabel('f(p)')
        if show:
            plt.show()


def draw_lamerey(func: MyFunction, x0=0.35, show=False, label=""):
    res_x, res_y = [], []
    res = []
    for _ in range(1, 51):
        x1 = func.f_with_param(x0)
        if x1 is None:
            print(f"Параметр {x0} вышел за область функции.a0={func.a0}, b={func.b}")
            exit(0)
        res_x += [x0, x0, x0, x1]
        res_y += [x0, x1, x1, x1]
        # res.append((x0, x0, x0, x1))
        # res.append((x0, x1, x1, x1))
        x0 = x1

    plt.plot(res_x, res_y, label='Lamerey', color='green')
    # for i in res:
    #     plt.plot([i[0], i[2]], [i[1], i[3]], color='green')

    func.draw_function(label=label)
    func.draw_xy()
    if show:
        plt.show()


def random_a0_b(iter_count=5, show_lamerey=True):
    a0_range = np.arange(0, 4, 0.2)
    b_range = np.arange(0, 3, 0.2)

    for i in range(iter_count):
        a0_i = random.randint(0, len(a0_range) - 1)
        b_i = random.randint(0, len(b_range) - 1)
        a0 = a0_range[a0_i]
        b = b_range[b_i]
        myf = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=b)
        if show_lamerey:
            draw_lamerey(myf, show=True, x0=0.3, label=f"a0={round(a0, 6)}, b={round(b, 6)}")
        else:
            myf.draw_function(show=True, label=f"a0={round(a0, 6)}, b={round(b, 6)}")


""" Построение лестницы со случайными a0, b из диапазона (2x2) рис 1.8:"""
# random_a0_b(show_lamerey=False)

"""Построение с конкретными параметрами: """

myf = MyFunction(a=5, v=0.5, ga=0.2, el=0.1, a0=4.5, b=3.8)
draw_lamerey(myf, show=True, x0=0.25)
# myf.draw_function()


# x0=0.25
# x0=0.2
