file = open("17 (3).txt")
a = file.readlines()
print(a)

a = [int(elem) for elem in a]
print(a)

min6 = min([elem for elem in a if abs(elem) % 10 == 6]) ** 2
# min6 = []
# for elem in a:
#     if abs(elem) % 10 == 6:
#         min6.append(elem)

count = 0
max_summa = 0
for i in range(len(a) - 1):
    x = a[i]
    y = a[i + 1]

    count6 = 0
    if abs(x) % 10 == 6:
        count6 += 1
    if abs(y) % 10 == 6:
        count6 += 1

    if count6 != 1:
        continue

    if x ** 2 + y ** 2 < min6:
        # пара подходит
        count += 1
        max_summa = max(x ** 2 + y ** 2, max_summa)

print(count, max_summa)
