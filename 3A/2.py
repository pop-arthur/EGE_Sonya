file = open("17 (4).txt")
a = file.readlines()
print(a)

# смотрит элементы и преобразует в целые числа
a = [int(elem) for elem in a]

count = 0
max_summa = 0
# перебираем пары
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        x = a[i]
        y = a[j]

        if abs(x - y) % 2 == 0:
            if (x % 19 == 0) or (y % 19 == 0):
                count += 1
                max_summa = max(x + y, max_summa)

print(count, max_summa)
