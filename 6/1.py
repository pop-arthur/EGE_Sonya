from itertools import *

a = "НАСТЯ"
count = 0
for word in product(a, repeat=6):
    word = "".join(word)
    if word.count("А") <= 1 and word.count("Я") <= 1:
        count += 1

print(count)
