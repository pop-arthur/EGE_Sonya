s = "МАТВЕЙ"
k = 0

for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        if word.count("М") == 1 and word.count("А") == 1 and word.count("Т") == 1 and word.count("В") == 1 and word.count("Е") == 1 and word.count("Й") == 1:
                            if word[0] != "Й" in word:
                                if "АЕ" not in word:
                                    print(word)
                                    k += 1

print(k)
