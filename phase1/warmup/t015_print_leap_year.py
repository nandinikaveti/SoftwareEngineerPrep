def leap_year(x:int):
    if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
        print(x, "is a leap year")
    else:
        print(x, "is not a leap year")
print(leap_year(2020))
print(leap_year(1900))
print(leap_year(23445004))