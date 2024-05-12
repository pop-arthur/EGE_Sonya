from itertools import *

count = 0
a = "КОНФЕТА"
for word in product(a, repeat=5):
    word = "".join(word)
    if word.count("Е") == 2 and word[1] != "Ф":
        count += 1

print(count)