import numpy as np
from matplotlib import pyplot as plt


class Eq:
    def __init__(self, a=4, v=0.5, g=0.2, el=0.1):
        self.a = a
        self.v = v
        self.g = g
        self.el = el
        self.ar = a
        self.al = a

    def is_valid_a0(self, b, a0):
        c1 = ((self.v - 1) / self.g) + 1 + b < a0
        c2 = a0 > (b + 1) - (self.v / self.g)
        c3 = a0 < 1 + self.v / self.el
        c4 = a0 < 1 + (1 - self.v) / self.el
        return c1 and c2 and c3 and c4

    def p(self, b, a0):
        f = False
        res_p = (0.5 * b - 0.2 * a0 - 1.2) / 2
        if 2 < b < 4:
            f = True
        return 0 <= res_p < 0.3, f

    def p3(self, b, a0):
        res_p = 0.5

    def p5(self, b, a0):
        f = False

        if 2 < b < 4:
            f = True
        p = (0.2 * a0 + 0.5 * b - 2.8) / (b - 4)
        return 0.7 < p <= 1, f

    def is_eq(self, b, a0):
        if not self.is_valid_a0(b, a0):
            return False, False
        eq, ust = self.p(b, a0)
        if eq:
            return True, ust
        eq, ust = self.p5(b, a0)
        if eq:
            return True, ust
        return False, False


def draw_eq(a0_range, b_range):
    values_b = [
    ]
    values_a0 = []
    values_b_u = []
    values_a0_u = []
    eq = Eq()
    for a0 in a0_range:
        for b in b_range:
            eq1, ust = eq.is_eq(b, a0)
            if eq1:
                if ust:
                    values_b_u.append(b)
                    values_a0_u.append(a0)

                values_b.append(b)
                values_a0.append(a0)

    plt.scatter(values_b, values_a0, label="eq", color='green', linewidths=0.01, marker=".")
    plt.scatter(values_b_u, values_a0_u, label="e1q", color='blue', linewidths=0.01, marker=".")

    plt.legend()
    plt.grid(True)
    plt.xlim([0, 3])
    plt.ylim([0, 4])
    plt.xlabel('b')
    plt.ylabel('a0')
    plt.show()


a0_range = np.arange(0, 4 + 0.001, 0.01)
b_range = np.arange(0, 3 + 0.001, 0.01)
draw_eq(a0_range, b_range)
