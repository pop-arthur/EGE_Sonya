from itertools import *

a = "ЕНОС"
count = 0
for word in product(a, repeat=4):
    word = "".join(word)
    count += 1
    if word[0] == "С":
        print(count)
