def distribution(a, b, c, d):
    if a >0:
        print("The equation is a(bx + c) = d")
        print("After expanding: abx + ac = d")
        
        numerator = d - (a * c)
        denominator = a * b
        
        print("Numerator:", numerator)
        print("Denominator:", denominator)
        
        x = numerator / denominator
        print("x =", x)

distribution(2, 1, 3, 5)
