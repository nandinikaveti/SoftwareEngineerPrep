def discriminant(a, b, c):
    d = b** 2 - 4 *a*c
    return d

def roots(a, b, c):
    if discriminant(a, b, c) > 0:
        print("The roots are real")
    elif discriminant(a, b, c) == 0:
        print("One root is real")
    else:
        print("No root is real")

discriminant(2, 3, -2)
roots(2, 3, -2)