def check_num(a, b):
    if a > b:
        print("Larger is", a)
        print("Smaller is", b)
    elif b > a:
        print("Larger is", b)
        print("Smaller is", a)
    else:
        print("Both are equal")


check_num(7, 7)
check_num(7, 5)
check_num(7, 9)