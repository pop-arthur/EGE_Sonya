file = open("1_17.txt")
a = file.readlines()

a = [int(elem) for elem in a]

max17 = max([elem for elem in a if abs(elem) % 100 == 17])

count = 0
for i in range(len(a) - 2):
    x = a[i]
    y = a[i + 1]
    z = a[i + 2]

    count3 = 0
    if 100 <= abs(x) <= 999:
        count3 += 1
    if 100 <= abs(y) <= 999:
        count3 += 1
    if 100 <= abs(z) <= 999:
        count3 += 1

    if count3 == 1:
        if x + y + z < max17:
            count += 1

print(count)
