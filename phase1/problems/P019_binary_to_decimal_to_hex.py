def num_conversion(n):
    if n.startswith("0b"):
        binary_digit = n[2:]
        number = 0
        for i in range(len(binary_digit)):
            digit = int(binary_digit[i])
            element = digit * 2 ** (len(binary_digit) - 1 - i)
            number+= element
        print(number)
n = "0b1010"
num_conversion(n)
a = 0b1010
print(a)