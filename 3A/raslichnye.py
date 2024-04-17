a = [1, 2, 3, 4, 5, 6]

# пары
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        x = a[i]
        y = a[j]
        print(x, y)

# тройки
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
            x = a[i]
            y = a[j]
            z = a[k]
            print(x, y, z)