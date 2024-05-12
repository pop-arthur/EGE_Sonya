def chetv(n):
    a = ""
    while n > 0:
        a = str(n % 4) + a
        n //= 4
    return a


def f(n):
    n_chetv = chetv(n)
    if n % 4 == 0:
        n_chetv = n_chetv + n_chetv[-2:]
    else:
        n_chetv = n_chetv + chetv(n % 4 * 2)

    return int(n_chetv, 4)


for n in range(1, 1000):
    if f(n) < 261:
        print(n)
