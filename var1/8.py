from itertools import *

a = "АВИОРТФ"
count = 0
k = 0
for word in product(a, repeat=6):
    word = "".join(word)
    count += 1

    if count % 2 == 0 and word[0] != "О" and word.count("Р") == 2:
        k += 1

print(k)

# product(repeat=) - сочетания с повторениями
# permutations(r=) - перестановки без повторений