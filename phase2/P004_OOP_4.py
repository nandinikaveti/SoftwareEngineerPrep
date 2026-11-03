def analyze_list(n):
    dictionary = {}
    count_digits = 0
    even_num = []

    for c in n:
        count_digits += 1

        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1

        if c % 2 == 0:
            even_num.append(c)

    if n:
        maximum = max(n)
        minimum = min(n)
    else:
        maximum = None
        minimum = None

    return dictionary, count_digits, maximum, minimum, even_num

n = [1, 2, 3, 4, 5]
print(analyze_list(n))
