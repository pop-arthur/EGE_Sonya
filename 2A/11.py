# from sys import setrecursionlimit
#
# setrecursionlimit(10 ** 9)
from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return f(n-1) + 1
    if n > 0 and n % 2 == 0:
        return f(n / 2)


count = 0
# for n in range(10 ** 9):
#     print(n)
#     if bin(n).count("1") == 3:
#         count += 1
    # if f(n) == 3:
    #     print(bin(n), ":", f(n))
    # if f(n) == 3:
    #     count = count + 1
        # count += 1

print(len(bin(10 ** 9)[2:]))
print()
print(28 * 29 * 5)
