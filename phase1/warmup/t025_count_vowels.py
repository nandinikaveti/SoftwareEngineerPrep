def count_vowels(x:str):
    count = { }
    total = 0
    for c in x.lower():
            total +=1
            if c in "aeiou":
                if c in count:
                    count[c] +=1
                else:
                    count[c] = 1

    print(count)
    print(total)

count_vowels("Sanjeeth")
count_vowels("Nandu")
