def check_cycles(list: list) -> int:
    for i in range(1, 16):
        if is_cycle(list, i):
            return i
    return -1


def is_cycle(list: list, cycle_type: int) -> bool:
    if cycle_type < len(list):
        return abs(list[0] - list[cycle_type]) < 0.000001
    return False