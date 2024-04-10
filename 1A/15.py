# ((x < 6) → (x2 < A)) ∧ ((y2 ≤ A) → (y ≤ 6))
def f(x, y, A):
    return ((x < 6) <= (x ** 2 < A)) and ((y ** 2 <= A) <= (y <= 6))


count = 0
for A in range(-1000, 1000):
    all_true = True

    for x in range(100):
        for y in range(100):
            if not f(x, y, A):
                all_true = False

    if all_true:
        count += 1
        print(A)

print(count)

#
# ЧТО ДЕЛАТЬ ДЛЯ РЕШЕНИЯ 15 ЗАДАНИЯ
#
# 1. НАПИСАТЬ ФУНКЦИЮ
# 2. НАПИСАТЬ ЦИКЛ ДЛЯ А
# 3. СОЗДАТЬ ПЕРЕМЕННУЮ ALL_TRUE
# 4. ПРОВЕРИТЬ ЧТО ФУНКЦИЯ ИСТИННА ДЛЯ ВСЕХ X, Y, ....
# 5. ЕСЛИ ФУНКЦИЯ ИСТИННА, ЧТО-ТО СДЕЛАТЬ
#










