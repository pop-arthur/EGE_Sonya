for n in range(4, 10000):
    a = "1" + "2" * n

    while "12" in a or "3322" in a or "2222" in a:
        if "12" in a:
            a = a.replace("12", "33", 1)
        if "2222" in a:
            a = a.replace("2222", "1", 1)
        if "3322" in a:
            a = a.replace("3322", "21", 1)

    summa_digits = 0
    for digit in a:
        summa_digits += int(digit)

    if summa_digits == 218:
        print(n)
        break
