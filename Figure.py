import numpy as np
from matplotlib import pyplot as plt


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
        self.step = 0.001
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
        plt.plot(p, f, color='red')

        if show:
            self.draw()

    def draw_f2(self, show=False):
        p = self.range_p2
        f = [self.f2(i) for i in p]
        plt.plot(p, f, color='red')

        if show:
            self.draw()

    def draw_f3(self, show=False):
        p = self.range_p3
        f = [self.f3(i) for i in p]
        plt.plot(p, f, color='red')

        if show:
            self.draw()

    def draw_f4(self, show=False):
        p = self.range_p4
        f = [self.f4(i) for i in p]
        plt.plot(p, f, color='red')

        if show:
            self.draw()

    def draw_f5(self, show=False):
        p = self.range_p5
        f = [self.f5(i) for i in p]
        plt.plot(p, f, color='red')

        if show:
            self.draw()

    def draw_function(self, show=False, title=""):
        self.draw_f1()
        self.draw_f2()
        self.draw_f3()
        self.draw_f4()
        self.draw_f5()
        self.draw(show, title)

    def draw_xy(self, show=False):
        plt.plot(np.arange(0, 1, self.step), np.arange(0, 1, self.step), color='grey')
        if show:
            plt.show()

    def f_with_param(self, p):
        if 0 <= p < self.v - self.ga:
            return self.f1(p)
        elif self.v - self.ga <= p <= self.v - self.el:
            return self.f2(p)
        elif self.v - self.el < p < self.v + self.el:
            return self.f3(p)
        elif self.v + self.el <= p <= self.v + self.ga:
            return self.f4(p)
        elif self.v + self.ga < p <= 1:
            return self.f5(p)

    def draw(self, show=False, title=""):
        plt.legend()
        plt.grid(True)
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        # plt.title(title)
        plt.xlabel('p')
        plt.ylabel('f(p)')
        if show:
            plt.show()

    def set_a0(self, a0):
        self.a0 = a0

    def set_b(self, b):
        self.b = b
        self.bl = b
        self.br = b
