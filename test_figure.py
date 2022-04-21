from Figure import MyFunction


def incorrect_xi(x1, x0) -> bool:
    if x1 is None:
        return True
    return False


def check_cycles(list: list) -> int:
    for i in range(1, 16):
        if is_cycle(list, i):
            return i
    return -1


def is_cycle(list: list, cycle_type: int) -> bool:
    if cycle_type < len(list):
        return abs(list[0] - list[cycle_type]) < 0.000001
    return False



a0 = 3.254
b = 2.888
my_func = MyFunction(a=4, v=0.5, ga=0.2, el=0.1, a0=a0, b=b)
x0 = 0.8
iterations = 200


def check_point():
    global x0
    for _ in range(iterations):
        x1 = my_func.f_with_param(x0)
        if x1 is None:
            print(x1, x0)
            exit()
        x0 = x1
    a0_b_vals = []

    for _ in range(15 + 1):
        x1 = my_func.f_with_param(x0)
        if incorrect_xi(x1, x0):
            print(x1, a0, b)
            exit()
        a0_b_vals.append(x1)
        x0 = x1

    cycle_type = check_cycles(a0_b_vals)
    print(a0, b)
    print(cycle_type)
    print(a0_b_vals)


check_point()
