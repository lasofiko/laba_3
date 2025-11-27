# для вещественных чисел
def help_sort(a):
    for i in range(1, len(a)):
        k = a[i]
        j = i - 1
        while j >= 0 and a[j] > k:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = k


def bucket_s(a, n):

    m = [[] for _ in range(n)]

    for num in a:
        b = int(n * num)
        m[b].append(num)

    for i in m:
        help_sort(i)

    k = 0
    for i in m:
        for num in i:
            a[k] = num
            k += 1
    return a


def bobble(a, n):  # +
    for j in range(0, n):
        f = 1
        for i in range(n - 1, j, -1):
            if a[i] < a[i - 1]:
                t = a[i]
                a[i] = a[i - 1]
                a[i - 1] = t
                f = 0
        if f == 1:
            break
    return a


def count(a, n):  # +
    amin = a[0]
    amax = a[0]
    cnt = [" " for i in range(1000)]
    for i in range(n):
        amin = min(amin, a[i])
        amax = max(amax, a[i])
    t = amax - amin + 1
    for i in range(t):
        cnt[i] = 0
    for i in range(n):
        cnt[a[i] - amin] += 1
    k = 0
    for i in range(t):
        for m in range(cnt[i]):
            a[k] = i + amin
            k += 1
    return a


def qsort(a, st, ed):  # +
    if st >= ed:
        return
    L = st
    R = ed
    x = a[L + (R - L) // 2]
    while L <= R:
        while a[L] < x:
            L += 1
        while a[R] > x:
            R -= 1
        if L <= R:
            t = a[L]
            a[L] = a[R]
            a[R] = t
            L += 1
            R -= 1
    qsort(a, st, R)
    qsort(a, L, ed)


def radix(a, n):  # ?
    l = max([len(str(i)) for i in a])
    m = [[] for _ in range(n)]
    for i in range(0, l):
        for j in a:
            d = (j // n**i) % n
            m[d].append(j)
        a = [j for k in m for j in k]
        m = [[] for _ in range(n)]
    return a


def hp(a, n, i):
    l = i
    left = 2 * i + 1
    rg = 2 * i + 2

    if left < n and a[left] > a[l]:
        l = left
    if rg < n and a[rg] > rg[l]:
        l = rg
    if l != i:
        a[i], a[l] = a[l], a[i]

        hp(a, n, l)
    return a


def heapy(a, n):
    for i in range(n // 2 - 1, -1, -1):
        hp(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        hp(a, i, 0)
    return a
