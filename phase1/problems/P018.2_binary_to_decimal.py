def binary_to_dec(n, base):
    element = 0
    number = 0
    #n = n[::-1]
    for i in range(len(n)):
        element = n[i]*base ** (len(n) - 1 - i)
        number+= element
        print(number)

n = [1, 0, 0]
print(binary_to_dec(n, 2))