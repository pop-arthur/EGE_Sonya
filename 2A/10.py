from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)


for i in range(1, 6):
    print(i, "=", f(i))

# print(f(2023) / f(2020))
print(2021 * 2022 * 2023)