def f(n):
    sonya = bin(n)[2:]
    sonya = "0" * (8 - len(sonya)) + sonya

    arthur = ""
    for i in range(len(sonya)):
        if sonya[i] == "0":
            arthur = arthur + '1'
        if sonya[i] == "1":
            arthur = arthur + '0'

    return int(arthur, 2) - n


for i in range(1000):
    if f(i) == 111:
        print(i)
