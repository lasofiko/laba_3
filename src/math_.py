def fact(a):  # +
    k = 1
    for i in range(1, a + 1):
        k *= i
    return k


def fact_recurs(a):  # +
    if a == 1:
        return 1
    return fact_recurs(a - 1) * a


def fibb(a):  # +
    f0 = 1
    f1 = 1
    f2 = 0
    for i in range(2, a):
        f2 = f1 + f0
        f0 = f1
        f1 = f2
    return f1


def fibb_recurs(a):  # +
    if a == 1 or a == 2:
        return 1
    return fibb_recurs(a - 1) + fibb_recurs(a - 2)
