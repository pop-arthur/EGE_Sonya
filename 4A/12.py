a = []
for n in range(4, 1000):
    s = "8" * n

    while "8888" in s:
        s = s.replace("8888", "44", 1)
        s = s.replace("4444", "848", 1)

    summa = 0
    for x in s:
        summa = summa + int(x)

    if summa >= 52:
        a.append(s.count("8"))

print(min(a))