def roman_int(roman_number:str):
    values = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500, "M": 1000
    }
    
    total = 0
    length = len(roman_number)
    for i in range(length):
        current = values[roman_number[i]]
        if i+1 < length:
            next_letter = values[roman_number[i+1]]
        else:
            next_letter = 0

        if next_letter < current or next_letter == current :
            total += current

        else:
            total -= current

    return total



print(roman_int(""))
print(roman_int("I"))
print(roman_int("V"))
print(roman_int("IV"))
print(roman_int("VI"))
print(roman_int("XIV"))
print(roman_int("XVII"))
print(roman_int("XL"))
print(roman_int("LX"))
print(roman_int("M"))
print(roman_int("MCMLXXXIV"))