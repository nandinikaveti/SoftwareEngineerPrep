import math
def quadratic(a, b, c):
    discriminant = b*b - 4*a*c

    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)

    return (root1, root2)

print(quadratic(3, -5, -2))