def f(x, A_min, A_max):
    return ((5 <= x <= 30) == (14 <= x <= 23)) <= (not (A_min <= x <= A_max))

max_length = 0
for A_min in range(-100, 100):
    for A_max in range(A_min + 1, 200):
        all_true = True

        for x in range(-100, 100):
            if not f(x, A_min, A_max):
                all_true = False

        if all_true:
            max_length = max(A_max - A_min + 1, max_length)

print(max_length)