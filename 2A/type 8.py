from itertools import product

letters = "ЕГЭ"

count = 0
for word in product(letters, repeat=5):
    if word[0] == "Е" or word[0] == "Э":
        count += 1

print(count)
