a = [1, 2, 3, 4, 5, 6]

# пары
for i in range(len(a) - 1):
    x = a[i]
    y = a[i + 1]
    print(x, y)

# тройки
for i in range(len(a) - 2):
    x = a[i]
    y = a[i + 1]
    z = a[i + 2]
    print(x, y, z)
