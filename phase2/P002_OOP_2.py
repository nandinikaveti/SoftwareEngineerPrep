def classify_num(a):
    if a > 0 and a % 2 == 0:
        print("a is positive even number")
    elif a > 0 and a % 2 != 0:
        print("a is positive odd number")
    elif a < 0 and a % 2 == 0:
        print("a is negative even number")
    elif a < 0 and a % 2 != 0:
        print("a is negative odd number")
    else:
        print("a is zero")

classify_num(3)
classify_num(-87765)
classify_num(-989897654)
classify_num(7655432321)
classify_num(0)



