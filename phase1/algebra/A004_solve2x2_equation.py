def solve_2x2_eq(a, b, c, d, e, f):
    y = (a*f - d*c) / (a*e - d*b)
    x = (c - b*y) / a
    return (x, y)

print(solve_2x2_eq(1, 1, 10, 1, -1, 4))

